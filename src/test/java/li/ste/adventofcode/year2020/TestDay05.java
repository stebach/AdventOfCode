package li.ste.adventofcode.year2020;

import li.ste.adventofcode.utils.TestInputProvider;
import org.junit.jupiter.api.DisplayNameGeneration;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

@DisplayNameGeneration(li.ste.adventofcode.DisplayNameGenerator.class)

public class TestDay05 {
    private static Day05 day;

    @BeforeAll
    public static void prepareTest() {
        day = new Day05(new TestInputProvider());
        day.run();
    }

    @Test
    void testSeatRows() {
        assertEquals(70, day.getRowForSeat("BFFFBBFRRR"));
        assertEquals(14, day.getRowForSeat("FFFBBBFRRR"));
        assertEquals(102, day.getRowForSeat("BBFFBBFRLL"));
    }

    @Test
    void testSeatColumns() {
        assertEquals(7, day.getColumnForSeat("BFFFBBFRRR"));
        assertEquals(7, day.getColumnForSeat("FFFBBBFRRR"));
        assertEquals(4, day.getColumnForSeat("BBFFBBFRLL"));
    }

    @Test
    void testSeatIDs() {
        assertEquals(567, day.getIDForSeat("BFFFBBFRRR"));
        assertEquals(119, day.getIDForSeat("FFFBBBFRRR"));
        assertEquals(820, day.getIDForSeat("BBFFBBFRLL"));
    }

    @Test
    void testSolution1() {
        assertEquals("820", day.getSolution1());
    }

    @Test
    void testSolution2() {
        assertEquals("120", day.getSolution2());
    }
}
