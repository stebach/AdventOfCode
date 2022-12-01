package li.ste.adventofcode2022.days;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
public class TestDay01 {
    private static Day01 day;

    @BeforeAll
    public static void prepareTest() {
        day = new Day01(new TestInputProvider());
        day.run();
    }

    @Test
    void testSolution1() {
        assertEquals("24000", day.getSolution1());
    }

    @Test
    void testSolution2() {
        assertEquals("45000", day.getSolution2());
    }
}
