package li.ste.adventofcode.year2020;

import li.ste.adventofcode.utils.TestInputProvider;
import org.junit.jupiter.api.DisplayNameGeneration;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

@DisplayNameGeneration(li.ste.adventofcode.DisplayNameGenerator.class)

public class TestDay18 {
    private static Day18 day;

    @BeforeAll
    public static void prepareTest() {
        day = new Day18(new TestInputProvider());
        day.run();
    }

    @Test
    void testCalc() {
        assertEquals(26, day.calc("2 * 3 + (4 * 5)"));
        assertEquals(437, day.calc("5 + (8 * 3 + 9 + 3 * 4 * 3)"));
        assertEquals(12240, day.calc("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"));
        assertEquals(13632, day.calc("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"));
    }

    @Test
    void testAdvancedCalc() {
        assertEquals(46, day.advancedCalc("2 * 3 + (4 * 5)"));
        assertEquals(1445, day.advancedCalc("5 + (8 * 3 + 9 + 3 * 4 * 3)"));
        assertEquals(669060, day.advancedCalc("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"));
        assertEquals(23340, day.advancedCalc("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"));
        assertEquals(6475593600L, day.advancedCalc("((5 * 6 + 7 + 4 + 3) * 9) * (4 + 8 * 9 + (5 + 2 + 2 + 4 * 7) + (9 * 7 + 4 * 5 + 3) * 2) + 6 * 6 * (7 * 2 + 5) + 7"));
        assertEquals(319L, day.advancedCalc("8 + 3 + 8 + 300"));
        assertEquals(1435392L, day.advancedCalc("(8 + 3 + 8 + (3 * 4 * 3 + 4 + 9 + 9)) + (5 + 3 + (2 + 5) + 6 + (8 + 8)) * 6 * 8 * (4 + 8) * 7"));
    }

    @Test
    void testSolution1() {
        assertEquals("26335", day.getSolution1());
    }

    @Test
    void testSolution2() {
        assertEquals("693891", day.getSolution2());
    }
}
