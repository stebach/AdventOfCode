package li.ste.adventofcode.year2022;

import li.ste.adventofcode.utils.TestInputProvider;
import org.junit.jupiter.api.DisplayNameGeneration;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

@DisplayNameGeneration(li.ste.adventofcode.DisplayNameGenerator.class)

public class TestDay25 {
    private static Day25 day;

    @BeforeAll
    public static void prepareTest() {
        day = new Day25(new TestInputProvider());
        day.run();
    }

    @Test
    void testSnafu2Dec() {
        assertEquals(4890, Day25.snafu2dec("2=-1=0"));
        assertEquals(1747, Day25.snafu2dec("1=-0-2"));
        assertEquals(31, Day25.snafu2dec("111"));
    }

    @Test
    void testDec2Snafu() {
        assertEquals("2=-1=0", Day25.dec2snafu(4890));
        assertEquals("1=-0-2", Day25.dec2snafu(1747));
        assertEquals("111", Day25.dec2snafu(31));
    }
    @Test
    void testSolution1() {
        assertEquals("2=-1=0", day.getSolution1());
    }

    @Test
    void testSolution2() {
        assertEquals("", day.getSolution2());
    }
}
