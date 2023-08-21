package org.example;


import java.util.Arrays;
import java.util.stream.*;

public class LetterCount {
    public static long getTotalNumberOfLettersOfNamesLongerThanFive(String... names) {
        return Arrays.stream(names)
                .filter(x -> x.length() > 5)
                .mapToLong(s -> (long) (s.length()))
                .sum();
    }
}