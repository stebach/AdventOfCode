package li.ste.adventofcode.year2022;

import li.ste.adventofcode.utils.TestInputProvider;
import org.junit.jupiter.api.DisplayNameGeneration;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

@DisplayNameGeneration(li.ste.adventofcode.DisplayNameGenerator.class)

public class TestDay22 {
    private static Day22 day;

    @BeforeAll
    public static void prepareTest() {
        day = new Day22(new TestInputProvider());
        day.run();
    }

    @Test
    void testSolution1() {
        assertEquals("6032", day.getSolution1());
    }

    @Test
    void testSolution2() {
        assertEquals("@todo", day.getSolution2()); // TODO: check solution 2 of day 22
    }
}
