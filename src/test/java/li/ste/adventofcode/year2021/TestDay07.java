package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.TestInputProvider;
import org.junit.jupiter.api.DisplayNameGeneration;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

@DisplayNameGeneration(li.ste.adventofcode.DisplayNameGenerator.class)

public class TestDay07 {
    private static Day07 day;

    @BeforeAll
    public static void prepareTest() {
        day = new Day07(new TestInputProvider());
        day.run();
    }

    @Test
    void testTriangularNumber() {
        assertEquals(1, day.getTriangularNumber(1));
        assertEquals(3, day.getTriangularNumber(2));
        assertEquals(6, day.getTriangularNumber(3));
        assertEquals(10, day.getTriangularNumber(4));
        assertEquals(55, day.getTriangularNumber(10));
    }

    @Test
    void testSolution1() {
        assertEquals("37", day.getSolution1());
    }

    @Test
    void testSolution2() {
        assertEquals("168", day.getSolution2());
    }
}
