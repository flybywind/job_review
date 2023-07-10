package main

import (
	"fmt"
	"strings"
)

func replaceWords_v0(dictionary []string, sentence string) string {
	dict_map := map[string]struct{}{}
	for _, d := range dictionary {
		dict_map[d] = struct{}{}
	}
	sentence_ary := strings.Split(sentence, " ")
	res := make([]string, len(sentence_ary))
	for j, w := range sentence_ary {
		found := false
		for i := range w[1:] {
			sub_w := w[:i+1]
			if _, ok := dict_map[sub_w]; ok {
				res[j] = sub_w
				found = true
				break
			}
		}
		if !found {
			res[j] = w
		}
	}
	return strings.Join(res, " ")
}

// after some test, 9 is the best param
const LevelWidth = 9

type levelNode struct {
	levlmap     [LevelWidth + 1]map[string]struct{}
	nextLevlmap *levelNode
	depth       int
}

func (l *levelNode) getRoot(word string, word_len int) string {
	for i := l.depth; i < word_len; i++ {
		n := i - l.depth + 1
		if n < LevelWidth {
			if _, exist := l.levlmap[n][word[:i+1]]; exist {
				return word[:i+1]
			}
		}
	}
	if l.nextLevlmap == nil {
		return word
	}
	return l.nextLevlmap.getRoot(word, word_len)
}
func createLevelMap(dictionary []string, depth int) *levelNode {
	lvMap := &levelNode{
		levlmap: [LevelWidth + 1]map[string]struct{}{},
		depth:   depth}
	next_dict := make([]string, 0, 1+int(0.1*float32(len(dictionary))))
	for _, d := range dictionary {
		n := len(d) - depth
		if n < LevelWidth+1 {
			if len(lvMap.levlmap[n]) == 0 {
				lvMap.levlmap[n] = map[string]struct{}{
					d: {},
				}
			} else {
				lvMap.levlmap[n][d] = struct{}{}
			}
		} else {
			next_dict = append(next_dict, d)
		}
	}
	if len(next_dict) > 0 {
		lvMap.nextLevlmap = createLevelMap(next_dict, depth+LevelWidth)
	}
	return lvMap

}
func replaceWords(dictionary []string, sentence string) string {
	sentence_ary := strings.Split(sentence, " ")
	levelMap := createLevelMap(dictionary, 0)
	res := make([]string, len(sentence_ary))
	for j, w := range sentence_ary {
		res[j] = levelMap.getRoot(w, len(w))
	}
	return strings.Join(res, " ")
}
func main() {
	var (
		dictionary = []string{"a", "aa", "aaa", "aaaa"}
		sentence   = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
	)
	fmt.Println(replaceWords(dictionary, sentence))
	dictionary = []string{"cat", "bat", "rat"}
	sentence = "the cattle was rattled by the battery"
	fmt.Println(replaceWords(dictionary, sentence))
}
