package org.example;

import static org.junit.jupiter.api.Assertions.*;

class LetterCountTest {
    @org.junit.jupiter.api.Test
    void getTotalNumberOfLettersOfNamesTests() {
        assertEquals(0, LetterCount.getTotalNumberOfLettersOfNamesLongerThanFive(""));
        assertEquals(6, LetterCount.getTotalNumberOfLettersOfNamesLongerThanFive("abcde1", "abc"));
        assertEquals(15, LetterCount.getTotalNumberOfLettersOfNamesLongerThanFive("abcde1234", "abc", "a12345"));

    }
}