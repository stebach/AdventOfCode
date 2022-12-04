package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.TestInputProvider;
import org.junit.jupiter.api.DisplayNameGeneration;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

@DisplayNameGeneration(li.ste.adventofcode.DisplayNameGenerator.class)

public class TestDay23 {
    private static Day23 day;

    @BeforeAll
    public static void prepareTest() {
        day = new Day23(new TestInputProvider());
        day.run();
    }

    @Test
    void testSolution1() {
        assertEquals("12521", day.getSolution1());
    }

    @Test
    void testSolution2() {
        assertEquals("44169", day.getSolution2());
    }
}
