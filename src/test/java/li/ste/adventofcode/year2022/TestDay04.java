package li.ste.adventofcode.year2022;

import li.ste.adventofcode.utils.TestInputProvider;
import org.junit.jupiter.api.DisplayNameGeneration;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

@DisplayNameGeneration(li.ste.adventofcode.DisplayNameGenerator.class)

public class TestDay04 {
    private static Day04 day;

    @BeforeAll
    public static void prepareTest() {
        day = new Day04(new TestInputProvider());
        day.run();
    }

    @Test
    void testSolution1() {
        assertEquals("2", day.getSolution1());
    }

    @Test
    void testSolution2() {
        assertEquals("4", day.getSolution2());
    }
}
