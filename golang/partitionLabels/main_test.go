package partitionlabels

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestCase1(t *testing.T) {
	assert.Equal(t, []int{9, 7, 8}, partitionLabels("ababcbacadefegdehijhklij"))
}

func TestCase2(t *testing.T) {
	assert.Equal(t, []int{10}, partitionLabels("eccbbbbdec"))
}

func TestCase3(t *testing.T) {
	assert.Equal(t, []int{13, 1, 1}, partitionLabels("qiejxqfnqceocmy"))
}

func TestCase4(t *testing.T) {
	assert.Equal(t, []int{9, 1}, partitionLabels("aebbedaddc"))
}
