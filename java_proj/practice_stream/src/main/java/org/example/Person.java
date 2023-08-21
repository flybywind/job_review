package org.example;

import java.util.Comparator;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

class Person {
    private String name;
    private int age;
    private String nationality;

    public Person(String name, int age, String nationality) {
        this.name = name;
        this.age = age;
        this.nationality = nationality;
    }

    public Person(String name, int age) {
        this(name, age, "");
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public String getNationality() {
        return nationality;
    }

    public static Person getOldestPerson(List<Person> people) {
        return people.stream().max(Comparator.comparingInt(Person::getAge)).get();
    }

    public static Set<String> getKidNames(List<Person> people) {
        return people.stream().filter(p -> p.getAge() < 18).map(Person::getName).collect(Collectors.toSet());
    }
}
