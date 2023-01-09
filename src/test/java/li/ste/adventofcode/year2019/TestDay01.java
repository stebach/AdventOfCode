package li.ste.adventofcode.year2019;

import li.ste.adventofcode.utils.TestInputProvider;
import org.junit.jupiter.api.DisplayNameGeneration;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

@DisplayNameGeneration(li.ste.adventofcode.DisplayNameGenerator.class)

public class TestDay01 {
    private static Day01 day;

    @BeforeAll
    public static void prepareTest() {
        day = new Day01(new TestInputProvider());
        day.run();
    }

    @Test
    void testSolution1() {
        assertEquals("34239", day.getSolution1());
    }

    @Test
    void testSolution2() {
        assertEquals("51314", day.getSolution2());
    }
}
