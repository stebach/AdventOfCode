package li.ste.adventofcode.year2019;

import li.ste.adventofcode.utils.TestInputProvider;
import org.junit.jupiter.api.DisplayNameGeneration;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

@DisplayNameGeneration(li.ste.adventofcode.DisplayNameGenerator.class)

public class TestDay05 {
    private static Day05 day;

    @BeforeAll
    public static void prepareTest() {
        day = new Day05(new TestInputProvider());
        day.run();
    }

    @Test
    void testSolution1() {
        assertEquals("@todo", day.getSolution1()); // TODO: check solution 1 of day 05
    }

    @Test
    void testSolution2() {
        assertEquals("@todo", day.getSolution2()); // TODO: check solution 2 of day 05
    }
}
