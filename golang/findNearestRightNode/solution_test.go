package findnearestrightnode

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

var nilNode *TreeNode

func TestCreateTreeCase1(t *testing.T) {
	tree := createTree([]int{1, 2, 3, 0, 4, 5, 6})
	assert.Equal(t, 1, tree.Val)
	assert.Equal(t, 2, tree.Left.Val)
	assert.Equal(t, 3, tree.Right.Val)
	assert.Equal(t, nilNode, tree.Left.Left)
	assert.Equal(t, 4, tree.Left.Right.Val)
	assert.Equal(t, 3, tree.Right.Val)
	assert.Equal(t, 5, tree.Right.Left.Val)
	assert.Equal(t, 6, tree.Right.Right.Val)
}

func TestCreateTreeCase2(t *testing.T) {
	tree := createTree([]int{3, 0, 4, 2})
	assert.Equal(t, 3, tree.Val)
	assert.Equal(t, nilNode, tree.Left)
	assert.Equal(t, 4, tree.Right.Val)
	assert.Equal(t, 2, tree.Right.Left.Val)
	assert.Equal(t, nilNode, tree.Right.Right)
}

func TestCase1(t *testing.T) {
	tree := createTree([]int{1, 2, 3, 0, 4, 5, 6})
	assert.Equal(t, 5, findNearestRightNode(tree, tree.Left.Right).Val)
}

func TestCase2(t *testing.T) {
	tree := createTree([]int{3, 0, 4, 2})
	assert.Equal(t, nilNode, findNearestRightNode(tree, tree.Right.Left))
	tree = createTree([]int{1})
	assert.Equal(t, nilNode, findNearestRightNode(tree, tree))
}

func TestCase3(t *testing.T) {
	tree := createTree([]int{3, 4, 2, 0, 0, 0, 1})
	assert.Equal(t, 2, findNearestRightNode(tree, tree.Left).Val)
}
