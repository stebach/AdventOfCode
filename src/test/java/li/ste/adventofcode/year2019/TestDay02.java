package li.ste.adventofcode.year2019;

import li.ste.adventofcode.utils.TestInputProvider;
import org.junit.jupiter.api.DisplayNameGeneration;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

@DisplayNameGeneration(li.ste.adventofcode.DisplayNameGenerator.class)

public class TestDay02 {
    private static Day02 day;

    @BeforeAll
    public static void prepareTest() {
        day = new Day02(new TestInputProvider());
        day.run();
    }

    @Test
    void testSolution1() {
        assertEquals("19690720", day.getSolution1());
    }

    @Test
    void testSolution2() {
        assertEquals("111", day.getSolution2());
    }
}
