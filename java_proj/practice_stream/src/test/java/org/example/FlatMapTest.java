package org.example;

import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class FlatMapTest {

    @Test
    void transform() {
        List<String> ret = FlatMap.transform(List.of(
                List.of("ab", "cd"),
                List.of("12", "34")
        ));
        assertEquals(4, ret.size());
        assertEquals("ab", ret.get(0));
        assertEquals("cd", ret.get(1));
        assertEquals("12", ret.get(2));
        assertEquals("34", ret.get(3));
    }
}