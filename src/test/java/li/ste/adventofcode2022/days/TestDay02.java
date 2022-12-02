package li.ste.adventofcode2022.days;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
public class TestDay02 {
    private static Day02 day;

    @BeforeAll
    public static void prepareTest() {
        day = new Day02(new TestInputProvider());
        day.run();
    }

    @Test
    void testSolution1() {
        assertEquals("15", day.getSolution1());
    }

    @Test
    void testSolution2() {
        assertEquals("12", day.getSolution2());
    }
}
