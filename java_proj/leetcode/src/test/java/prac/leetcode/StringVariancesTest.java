package prac.leetcode;

import static org.junit.jupiter.api.Assertions.*;

class StringVariancesTest {

    @org.junit.jupiter.api.Test
    void parseNum() {
        String input = "123";
        assertEquals(3, StringVariances.parseNum(input));
    }
    @org.junit.jupiter.api.Test
    void parseNumWithZero() {
        String input = "0123";
        assertEquals(0, StringVariances.parseNum(input));
        input = "901";
        assertEquals(0, StringVariances.parseNum(input));
        input = "1030";
        assertEquals(0, StringVariances.parseNum(input));
    }
    @org.junit.jupiter.api.Test
    void parseNumWithZero2() {
        String input = "100221";
        assertEquals(0, StringVariances.parseNum(input));

        input = "102213";
        assertEquals(5, StringVariances.parseNum(input));

        input = "102213123";
        assertEquals(15, StringVariances.parseNum(input));
    }
}