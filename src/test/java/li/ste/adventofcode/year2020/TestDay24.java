package li.ste.adventofcode.year2020;

import li.ste.adventofcode.utils.TestInputProvider;
import org.junit.jupiter.api.DisplayNameGeneration;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

@DisplayNameGeneration(li.ste.adventofcode.DisplayNameGenerator.class)

public class TestDay24 {
    private static Day24 day;

    @BeforeAll
    public static void prepareTest() {
        day = new Day24(new TestInputProvider());
        day.run();
    }

    @Test
    void testSolution1() {
        assertEquals("10", day.getSolution1());
    }

    @Test
    void testSolution2() {
        assertEquals("2208", day.getSolution2());
    }
}
