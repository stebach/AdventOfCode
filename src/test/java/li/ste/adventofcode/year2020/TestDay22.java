package li.ste.adventofcode.year2020;

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
        assertEquals("@todo", day.getSolution1()); // TODO: check solution 1 of day 22
    }

    @Test
    void testSolution2() {
        assertEquals("@todo", day.getSolution2()); // TODO: check solution 2 of day 22
    }
}
