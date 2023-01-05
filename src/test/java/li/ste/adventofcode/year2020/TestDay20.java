package li.ste.adventofcode.year2020;

import li.ste.adventofcode.utils.TestInputProvider;
import org.junit.jupiter.api.DisplayNameGeneration;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

@DisplayNameGeneration(li.ste.adventofcode.DisplayNameGenerator.class)

public class TestDay20 {
    private static Day20 day;

    @BeforeAll
    public static void prepareTest() {
        day = new Day20(new TestInputProvider());
        day.run();
    }

    @Test
    void testSolution1() {
        assertEquals("20899048083289", day.getSolution1());
    }

    @Test
    void testSolution2() {
        assertEquals("273", day.getSolution2());
    }
}
