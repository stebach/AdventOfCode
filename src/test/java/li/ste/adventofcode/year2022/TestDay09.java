package li.ste.adventofcode.year2022;

import li.ste.adventofcode.utils.TestInputProvider;
import org.junit.jupiter.api.DisplayNameGeneration;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

@DisplayNameGeneration(li.ste.adventofcode.DisplayNameGenerator.class)

public class TestDay09 {
    private static Day09 day;

    @BeforeAll
    public static void prepareTest() {
        day = new Day09(new TestInputProvider());
        day.run();
    }

    @Test
    void testSolution1() {
        assertEquals("13", day.getSolution1());
    }

    @Test
    void testSolution2() {
        assertEquals("1", day.getSolution2());
    }
}
