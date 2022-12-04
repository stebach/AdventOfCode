package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.TestInputProvider;
import li.ste.adventofcode.year2021.day16.Message;
import org.junit.jupiter.api.DisplayNameGeneration;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

@DisplayNameGeneration(li.ste.adventofcode.DisplayNameGenerator.class)

public class TestDay16 {
    private static Day16 day;

    @BeforeAll
    public static void prepareTest() {
        day = new Day16(new TestInputProvider());
        day.run();
    }

    @Test
    void string2bin() {
        String string = "38006F45291200";
        String bin = "00111000000000000110111101000101001010010001001000000000";
        short[] shorts = Message.stringToBin(string);

        StringBuilder sb = new StringBuilder();
        for (short s : shorts) {
            sb.append(String.valueOf(s));
        }
        assertEquals(bin, sb.toString());
    }

    @Test
    void testSolution1() {
        assertEquals("31", day.getSolution1());
    }

    @Test
    void testSolution2() {
        assertEquals("54", day.getSolution2());
    }
}
