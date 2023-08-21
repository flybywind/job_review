package prac.leetcode;

import org.junit.jupiter.api.Test;

import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.*;

class topologySortTest {

    @Test
    void findTopoOrderNoChildren() {
        topologySort ps = new topologySort(1, new ArrayList<>());
        assertEquals(1, ps.findTopoOrder().size());
        ps = new topologySort(2, new ArrayList<>());
        assertEquals(2, ps.findTopoOrder().size());
        ps = new topologySort(2, new ArrayList<>());
        assertEquals(2, ps.findTopoOrder().size());
    }

    @Test
    void findTopoOrderWithChildren() {
        topologySort ps = new topologySort(1, new ArrayList<>());
        assertEquals(1, ps.findTopoOrder().size());
        ps = new topologySort(2, new ArrayList<>());
        assertEquals(2, ps.findTopoOrder().size());
    }
}