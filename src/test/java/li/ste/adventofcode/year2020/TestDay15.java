package li.ste.adventofcode.year2020;

import li.ste.adventofcode.utils.TestInputProvider;
import org.junit.jupiter.api.DisplayNameGeneration;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

@DisplayNameGeneration(li.ste.adventofcode.DisplayNameGenerator.class)

public class TestDay15 {
    private static Day15 day;

    @BeforeAll
    public static void prepareTest() {
        day = new Day15(new TestInputProvider());
        day.run();
    }

    @Test
    void testSolution1() {
        assertEquals("1836", day.getSolution1());
    }

    @Test
    void testSolution2() {
        assertEquals("362", day.getSolution2());
    }
}
