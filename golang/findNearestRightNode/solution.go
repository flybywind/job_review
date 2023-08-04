package findnearestrightnode

/**
 * Definition for a binary tree node.
 *
**/
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func findNearestRightNode(root *TreeNode, u *TreeNode) *TreeNode {
	// iter to find the target u
	height_stack := []int{0}
	iter_stack := []*TreeNode{root}
	for len(iter_stack) > 0 {
		cur := iter_stack[0]
		height := height_stack[0]
		if cur.Val == u.Val {
			if len(height_stack) == 1 {
				return nil
			}
			next_h := height_stack[1]
			if height == next_h {
				return iter_stack[1]
			}
			break
		}
		iter_stack = iter_stack[1:]
		height_stack = height_stack[1:]
		if cur.Left != nil {
			iter_stack = append(iter_stack, cur.Left)
			height_stack = append(height_stack, height+1)
		}
		if cur.Right != nil {
			iter_stack = append(iter_stack, cur.Right)
			height_stack = append(height_stack, height+1)
		}
	}
	return nil
}

func createTree(ary []int) *TreeNode {
	parentStack := []*TreeNode{}
	root := &TreeNode{ary[0], nil, nil}
	parentNode := root
	children := ary[1:]
	for len(children) > 0 {
		var l, r *TreeNode
		if children[0] > 0 {
			l = &TreeNode{children[0], nil, nil}
			parentStack = append(parentStack, l)
		} else {
			l = nil
		}
		children = children[1:]
		if len(children) > 0 {
			if children[0] > 0 {
				r = &TreeNode{children[0], nil, nil}
				parentStack = append(parentStack, r)
			} else {
				r = nil
			}
			children = children[1:]
		}
		parentNode.Left = l
		parentNode.Right = r
		parentNode = parentStack[0]
		parentStack = parentStack[1:]
	}
	return root
}
