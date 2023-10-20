package main

import (
	"encoding/json"
	"fmt"
	"unsafe"
)

type MutableStr struct {
	rawptr uintptr
	len    int
}

func NewMutableStr(s string) *MutableStr {
	rawptr := unsafe.Pointer(&s)
	return &MutableStr{
		rawptr: uintptr(rawptr),
		len:    len(s),
	}
}

func (s *MutableStr) Set(i int, b byte) {
	if i < s.len {
		b0 := (*byte)(unsafe.Pointer(s.rawptr + unsafe.Sizeof(b)*uintptr(i)))
		fmt.Printf("got code: %d at %d\n", *b0, i)
		*b0 = b
	}
}

func string2bytes(str string) []byte {
	if str == "" {
		return nil
	}
	return unsafe.Slice(unsafe.StringData(str), len(str))
}

type field struct {
	name string
}

func (p field) print() {
	fmt.Println(p.name)
}

func (p *field) printPtr() {
	fmt.Println("PTR:", p.name)
}

func print(p field) {
	fmt.Println("func:", p.name)
}
func printPtr(p *field) {
	fmt.Println("func PTR:", p.name)
}
func main() {
	// s := "abc"
	// fmt.Println("hello!", s)
	// for _, b := range(s) {
	// 	fmt.Print(b, " ")
	// }
	// fmt.Println("hello!", s)

	// var arr []int = nil;
	// fmt.Printf("slice: %#v, len = %d\n", arr, len(arr))
	// arr = append(arr, 1)
	// fmt.Printf("slice: %#v, len = %d\n", arr, len(arr))
	// // var map0 map[string]int = nil
	// // map0 := map[string]int{}
	// map0 := map[string][]int{}
	// fmt.Printf("map: %#v, len = %d\n", map0, len(map0))
	// map0["a"] = []int{1,22}
	// fmt.Printf("map: %#v, len = %d\n", map0, len(map0))
	// fmt.Printf("non exist value: %d\n", map0["x"])
	// 从一个closed状态的channel读取数据是安全的，可通过返回状态（第二个返回参数）判断是否关闭；而向一个closed状态的channel写数据会导致panic。
	// Json反序列化数字到interface{}类型的值中，默认解析为float64类型，在使用时要注意。
	// ch := make(chan int)
	// go func() {
	// 	for {
	// 		select {
	// 		case i, ok := <-ch:
	// 			fmt.Println("got", i, "status:", ok)
	// 			if !ok {
	// 				fmt.Println("closed, return")
	// 				return
	// 			}
	// 		}
	// 	}

	// }()
	// for i := 0; i < 10; i++ {
	// 	ch <- i
	// }
	// close(ch)
	// time.Sleep(time.Second * 1)
	// json RawMessage其实就是一个[]byte, 可以推后反序列化某些对象
	type Resp struct {
		Status json.RawMessage `json:"status"`
		Tag    string          `json:"tag"`
	}
	// records := [][]byte{
	// 	[]byte(`{"status": 200, "tag":"one"}`),
	// 	[]byte(`{"status":"ok", "tag":"two"}`),
	// }
	// for _, v := range records {
	// 	var resp Resp
	// 	if err := json.NewDecoder(bytes.NewReader(v)).Decode(&resp); err == nil {
	// 		fmt.Printf("got response: %#v, raw = %s\n", resp, string(resp.Status))
	// 	} else {
	// 		fmt.Printf("got err: %#v\n", err)
	// 	}
	// }

	// Slice 超范围覆盖
	// path := []byte("AAAA/BBBBBBBBB")
	// sepIndex := bytes.IndexByte(path, '/')
	// // dir1 := path[:sepIndex]
	// // 解决方法: full slice expression
	// dir1 := path[:sepIndex:sepIndex] //full slice expression
	// dir2 := path[sepIndex+1:]
	// fmt.Println("dir1 =>", string(dir1)) //prints: dir1 => AAAA
	// fmt.Println("dir2 =>", string(dir2)) //prints: dir2 => BBBBBBBBB

	// dir1 = append(dir1, "suffix"...)
	// path = bytes.Join([][]byte{dir1, dir2}, []byte{'/'})

	// fmt.Println("dir1 =>", string(dir1)) //prints: dir1 => AAAAsuffix
	// fmt.Println("dir2 =>", string(dir2)) //prints: dir2 => uffixBBBB (not ok)

	// fmt.Println("new path =>", string(path))

	// 闭包中的变量使用问题
	// data := []field{{"one"}, {"two"}, {"three"}}
	// for _, v := range data {
	// 	fmt.Printf("%p->%p\n", &v, v)
	// 	// 解决办法：添加如下语句
	// 	// v := v
	// 	go v.print()
	// 	go print(v)
	// 	// 这里之所以出现问题，就是因为在执行函数前，编译器需要一个指针，作为参数传入print函数。
	// 	// 默认的话，取的地址是这个临时变量v的地址。而这个地址所指的内容一直在变。最终变成结尾元素
	// 	go v.printPtr()
	// 	go printPtr(&v)
	// }
	// time.Sleep(3 * time.Second) //goroutines print: three, three, three
	// fmt.Printf("===========split========\n")
	// data2 := []*field{{"one"}, {"two"}, {"three"}} // 注意data2是指针数组
	// for _, v := range data2 {
	// 	fmt.Printf("%p->%p\n", &v, v)
	// 	// 这里之所以正常，因为对于需要指针的函数，编译器直接把这个指针给他就行了, 不需要再对v取地址。
	// 	// 而对于需要对象引用的函数，编译器则会复制一份新的传入函数。
	// 	go v.print()
	// 	go v.printPtr()
	// 	go print(*v)
	// 	go printPtr(v)
	// }
	// time.Sleep(3 * time.Second) //goroutines print: one, two, three

	// defer语句调用是在当前函数结束之后调用，而不是变量的作用范围。

	// for _, target := range targets {
	// 	f, err := os.Open(target)
	// 	if err != nil {
	// 		fmt.Println("bad target:", target, "error:", err) //prints error: too many open files
	// 		break
	// 	}
	// 	defer f.Close() //will not be closed at the end of this code block, but closed at end of this function
	// 	// 解决方法1：不用defer
	// 	// f.Close()
	// 	// 解决方法2：将for中的语句添加到匿名函数中执行。
	// 	// func () {
	// 	// }()
	// }

	// ss := "dhello world!"
	// bss := string2bytes(ss)

	// // bss[0] = 'x'
	// // bss := NewMutableStr(ss)
	// // bss.Set(0, 'x')
	// fmt.Println(bss, ss[0])
}
