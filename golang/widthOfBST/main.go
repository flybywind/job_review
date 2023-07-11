package main

import (
	"fmt"
)

/**
 * Definition for a binary tree node.
 * Note: hard to validate in loc, as the parser from int[] to TreeNode* is pretty hard
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func widthOfBinaryTree(root *TreeNode) int {
	if root == nil {
		return 0
	}
	stack_ary := []*TreeNode{root}
	end_idx := 1
	max_width := 0
	for end_idx > 0 {
		if end_idx > max_width {
			max_width = end_idx
		}
		left_most_node := true
		for i := 0; i < end_idx; i++ {
			node := stack_ary[i]
			if (node != nil && node.Left != nil) || !left_most_node {
				stack_ary = append(stack_ary, node.Left)
				left_most_node = false
			}
			if node != nil {
				stack_ary = append(stack_ary, node.Right)
			} else {
				stack_ary = append(stack_ary, nil)
			}
		}
		end_idx2 := len(stack_ary)
		for i := end_idx2 - 1; i >= end_idx; i-- {
			if stack_ary[i] == nil {
				end_idx2--
			} else {
				break
			}
		}
		// reset stack_idx and end_idx
		next_len := end_idx2 - end_idx
		stack_ary = stack_ary[end_idx:]
		end_idx = next_len
	}
	return max_width
}

const null = -101

func CreteaTree(ary []int) *TreeNode {
	if len(ary) == 0 {
		return nil
	}
	var rootNode = &TreeNode{Val: ary[0]}
	nodeStack := []*TreeNode{rootNode}
	for i := range ary {
		rootNode = nodeStack[i]
		if 2*i+1 < len(ary) {
			if ary[2*i+1] == null {
				rootNode.Left = nil
			} else {
				rootNode.Left = &TreeNode{Val: ary[2*i+1]}
			}
			if rootNode != nil {
				nodeStack = append(nodeStack, rootNode.Left)
			}
		}
		if 2*i+2 < len(ary) {
			if ary[2*i+2] == null {
				rootNode.Right = nil
			} else {
				rootNode.Right = &TreeNode{Val: ary[2*i+2]}
			}
			if rootNode != nil {
				nodeStack = append(nodeStack, rootNode.Right)
			}
		}

	}
	return nodeStack[0]
}
func main() {
	// var rootNode = CreteaTree([]int{1, 3, 2, 5, 3, null, 9})

	// fmt.Println(widthOfBinaryTree(rootNode))
	var rootNode = CreteaTree([]int{1, 1, 1, 1, 1, 1, 1, null, null, null, 1, null, null, null, null, 2, 2, 2, 2, 2, 2, 2, null, 2, null, null, 2, null, 2})
	fmt.Println(widthOfBinaryTree(rootNode))
}
