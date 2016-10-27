收集一下自己所有的面试题
==================================

1.  find_max_two.py
---------------------------------
给定一个实数数组，寻找里面和最大的2个数之和：那就寻找最大的前2个数不就行了。

2. string_pattern.py
--------------------------------
所有和字符串相关的都放到这里面吧	
### a) longest_type3.py
给定一个字符串，寻找一个最长连续子串，子串中只有3种字符。比如a、b、c。它们可以多次出现

3. city_route
--------------------------------
给定一批city_paires, 给出从cityA到cityB的所有路径.
如

北京 -- 天津

天津 -- 杭州

杭州 -- 北京

杭州 -- 成都

成都 -- 西安

北京 -- 西安

北京 -- 成都

杭州 -- 福州

4. sortList; problem set from leetcode.com
----------------------------
Sort a linked list in O(n log n) time using constant space complexity.
不用交换节点，交换节点的内容即可！使用快速排序的思路。

5. LRUCache
-----------------------------
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.

set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

6. reorder list; leetcode.com
---------------------------------
Given a singly linked list L: L0→L1→…→Ln-1→Ln, <br/>
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…<br/>

You must do this in-place without altering the nodes' values.

For example,<br/>
Given {1,2,3,4}, reorder it to {1,4,2,3}.

7. Word Break; leetcode.com
----------------------------------
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

8.  candy
-----------------------------------
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

思路：
在ratings里面寻找上升/下降区间，设区间长度n，给区间内每个元素按照从大到小的顺序分别赋值n-1、n-2 …… 0。
上升/下降区间分别扫一次，然后用max merge
