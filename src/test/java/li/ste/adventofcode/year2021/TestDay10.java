package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.TestInputProvider;
import org.junit.jupiter.api.DisplayNameGeneration;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

@DisplayNameGeneration(li.ste.adventofcode.DisplayNameGenerator.class)

public class TestDay10 {
    private static Day10 day;

    @BeforeAll
    public static void prepareTest() {
        day = new Day10(new TestInputProvider());
        day.run();
    }

    @Test
    void testSolution1() {
        assertEquals("26397", day.getSolution1());
    }

    @Test
    void testSolution2() {
        assertEquals("288957", day.getSolution2());
    }
}
