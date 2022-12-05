package li.ste.adventofcode.year2022;

import li.ste.adventofcode.utils.TestInputProvider;
import org.junit.jupiter.api.DisplayNameGeneration;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

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
    void testMove() {
        List<List<Character>> stacks = new ArrayList<>();
        stacks.add(new ArrayList<>());
        stacks.get(0).add('Z');
        stacks.get(0).add('N');
        stacks.add(new ArrayList<>());
        stacks.get(1).add('M');
        stacks.get(1).add('C');
        stacks.get(1).add('D');
        stacks.add(new ArrayList<>());
        stacks.get(2).add('P');

        day.moveCrates(stacks, 2, 1, 1, false);
        assertEquals(3, stacks.get(0).size());
        assertEquals(2, stacks.get(1).size());
        assertEquals("DCP", day.getTopCrates(stacks));

        day.moveCrates(stacks, 1,3,3,false);
        assertEquals(0, stacks.get(0).size());
        assertEquals(4, stacks.get(2).size());
        assertEquals("CZ", day.getTopCrates(stacks));

        day.moveCrates(stacks, 2,1,2,false);
        assertEquals(2, stacks.get(0).size());
        assertEquals(0, stacks.get(1).size());
        assertEquals("MZ", day.getTopCrates(stacks));
    }

    @Test
    void testMoveMultiple() {
        List<List<Character>> stacks = new ArrayList<>();
        stacks.add(new ArrayList<>());
        stacks.get(0).add('Z');
        stacks.get(0).add('N');
        stacks.add(new ArrayList<>());
        stacks.get(1).add('M');
        stacks.get(1).add('C');
        stacks.get(1).add('D');
        stacks.add(new ArrayList<>());
        stacks.get(2).add('P');

        day.moveCrates(stacks, 2, 1, 1, true);
        assertEquals(3, stacks.get(0).size());
        assertEquals(2, stacks.get(1).size());
        assertEquals("DCP", day.getTopCrates(stacks));

        day.moveCrates(stacks, 1,3,3,true);
        assertEquals(0, stacks.get(0).size());
        assertEquals(4, stacks.get(2).size());
        assertEquals("CD", day.getTopCrates(stacks));

        day.moveCrates(stacks, 2,1,2,true);
        assertEquals(2, stacks.get(0).size());
        assertEquals(0, stacks.get(1).size());
        assertEquals("CD", day.getTopCrates(stacks));
    }

    @Test
    void testSolution1() {
        assertEquals("CMZ", day.getSolution1());
    }

    @Test
    void testSolution2() {
        assertEquals("MCD", day.getSolution2());
    }
}
