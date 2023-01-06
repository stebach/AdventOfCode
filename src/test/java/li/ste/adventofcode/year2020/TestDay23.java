package li.ste.adventofcode.year2020;

import li.ste.adventofcode.utils.TestInputProvider;
import org.junit.jupiter.api.DisplayNameGeneration;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

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
    void testMoves() {
        List<Integer> cups = Arrays.asList(3,8,9,1,2,5,4,6,7);
        int[] nextCup = new int[cups.size() + 1];
        for (int i = 0; i < cups.size(); i++) {
            nextCup[cups.get(i)] = i + 1 == cups.size() ? 0 : i + 1;
        }
        assertEquals("389125467", day.cupsToString(cups, nextCup));

        int[] nextCupClone = nextCup.clone();
        day.moveCups(cups, nextCupClone, 1);
        assertEquals("328915467", day.cupsToString(cups, nextCupClone));
        nextCupClone = nextCup.clone();
        day.moveCups(cups, nextCupClone, 2);
        assertEquals("325467891",  day.cupsToString(cups, nextCupClone));
        nextCupClone = nextCup.clone();
        day.moveCups(cups, nextCupClone, 3);
        assertEquals("346725891",  day.cupsToString(cups, nextCupClone));
        nextCupClone = nextCup.clone();
        day.moveCups(cups, nextCupClone, 4);
        assertEquals("325846791",  day.cupsToString(cups, nextCupClone));
        nextCupClone = nextCup.clone();
        day.moveCups(cups, nextCupClone, 5);
        assertEquals("367925841",  day.cupsToString(cups, nextCupClone));
        nextCupClone = nextCup.clone();
        day.moveCups(cups, nextCupClone, 6);
        assertEquals("367258419",  day.cupsToString(cups, nextCupClone));
        nextCupClone = nextCup.clone();
        day.moveCups(cups, nextCupClone, 7);
        assertEquals("367419258",  day.cupsToString(cups, nextCupClone));
        nextCupClone = nextCup.clone();
        day.moveCups(cups, nextCupClone, 8);
        assertEquals("392674158",  day.cupsToString(cups, nextCupClone));
        nextCupClone = nextCup.clone();
        day.moveCups(cups, nextCupClone, 9);
        assertEquals("392657418",  day.cupsToString(cups, nextCupClone));
        nextCupClone = nextCup.clone();
        day.moveCups(cups, nextCupClone, 10);
        assertEquals("374192658",  day.cupsToString(cups, nextCupClone));
    }


    @Test
    void testFormatResult() {
        List<Integer> cups = Arrays.asList(3,8,9,1,2,5,4,6,7);
        int[] nextCup = new int[cups.size() + 1];
        for (int i = 0; i < cups.size(); i++) {
            nextCup[cups.get(i)] = i + 1 == cups.size() ? 0 : i + 1;
        }

        int[] nextCupClone = nextCup.clone();
        day.moveCups(cups, nextCupClone, 1);
        assertEquals("54673289", day.formatResult(cups, nextCupClone));
        nextCupClone = nextCup.clone();
        day.moveCups(cups, nextCupClone, 2);
        assertEquals("32546789", day.formatResult(cups, nextCupClone));
        nextCupClone = nextCup.clone();
        day.moveCups(cups, nextCupClone, 3);
        assertEquals("34672589", day.formatResult(cups, nextCupClone));
        nextCupClone = nextCup.clone();
        day.moveCups(cups, nextCupClone, 4);
        assertEquals("32584679", day.formatResult(cups, nextCupClone));
        nextCupClone = nextCup.clone();
        day.moveCups(cups, nextCupClone, 5);
        assertEquals("36792584", day.formatResult(cups, nextCupClone));
        nextCupClone = nextCup.clone();
        day.moveCups(cups, nextCupClone, 6);
        assertEquals("93672584", day.formatResult(cups, nextCupClone));
        nextCupClone = nextCup.clone();
        day.moveCups(cups, nextCupClone, 7);
        assertEquals("92583674", day.formatResult(cups, nextCupClone));
        nextCupClone = nextCup.clone();
        day.moveCups(cups, nextCupClone, 8);
        assertEquals("58392674", day.formatResult(cups, nextCupClone));
        nextCupClone = nextCup.clone();
        day.moveCups(cups, nextCupClone, 9);
        assertEquals("83926574", day.formatResult(cups, nextCupClone));
        nextCupClone = nextCup.clone();
        day.moveCups(cups, nextCupClone, 10);
        assertEquals("92658374", day.formatResult(cups, nextCupClone));
    }

    @Test
    void testSolution1() {
        assertEquals("67384529", day.getSolution1());
    }

    @Test
    void testSolution2() {
        assertEquals("149245887792", day.getSolution2());
    }
}
