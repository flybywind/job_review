# -*- encoding:utf8 -*-
# 其实关键还是map，但是这个map的大小是固定的，而且是按照LRU弹出旧元素。
# 为了实现LRU，需要构造一个双向链表
class CacheNode:
    def __init__(self):
        self.key = None
        self.val = None
        # must be bidirection list, easy for delete at rear/inter
        self.next = None
        self.prev = None
    def set(self, key, val):
        self.key = key
        self.val = val

    def __str__(self):
        return "("+str(self.key)+", "+str(self.val)+") <-> " + str(self.next)

class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.cap = capacity
        self.__cache_front__ = CacheNode()
        self.__cache_rear__ = CacheNode()
        self.__cache_front__.next = self.__cache_rear__
        self.__cache_rear__.prev = self.__cache_front__
        self.__cache_dict__ = {}
        self.size = 0

    # @return an integer
    def get(self, key):
        n = self.__cache_front__.next
        if n.key != key:
            if key in self.__cache_dict__:
                n = self.__cache_dict__[key]
            else:
                return -1
        prev = n.prev
        next = n.next
        prev.next = next
        next.prev = prev
        n.next = self.__cache_front__.next
        n.next.prev = n
        n.prev = self.__cache_front__
        self.__cache_front__.next = n
        return n.val

    def isful(self):
        return self.size > self.cap
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        n = self.__cache_front__.next
        if n.key != key:
            if key in self.__cache_dict__:
                n = self.__cache_dict__[key]
            else:
                n = None

        if n is None:
        # create:
            n = CacheNode()
            n.key, n.val = (key, value)
            self.size += 1
            self.__cache_dict__[key] = n
            if self.isful():
                # delete:
                last = self.__cache_rear__.prev
                sec_last = last.prev
                sec_last.next = self.__cache_rear__
                self.__cache_rear__.prev = sec_last
                del self.__cache_dict__[last.key]
                del last
                self.size -= 1
        else:
        # delete in old location
            prev = n.prev
            next = n.next
            prev.next = next
            next.prev = prev
            n.val = value

        n.next = self.__cache_front__.next
        n.next.prev = n
        n.prev = self.__cache_front__
        self.__cache_front__.next = n


lru = LRUCache(4)

lru.set("123", 1)
lru.set("abc", 1)
lru.set("a", 1)
lru.set("b", 1)
lru.set("c", 1)
lru.set("123", 2)
lru.set("a", 3)
lru.get("123")
lru.get("c")
lru.get("dd")