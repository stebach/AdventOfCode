package li.ste.adventofcode.year2019;

import li.ste.adventofcode.utils.TestInputProvider;
import li.ste.adventofcode.year2019.intcode.IntCode;
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
    void testPart1() {
        //1002,4,3,4,33
        IntCode intCode = new IntCode();

        List<Integer> output = new ArrayList<>();
        int[] result = intCode.run(new int[] { 1002, 4, 3, 4, 33 }, new ArrayList<>(), output);
        assertEquals(99,result[4]);
    }

    @Test
    void testPart2() {
        int[] memory = new int[] { 3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99 };
        IntCode intCode = new IntCode();
        List<Integer> output = new ArrayList<>();
        List<Integer> input = new ArrayList<>();
        input.add(3);
        intCode.run(memory, input, output);
        assertEquals(999, output.get(output.size() - 1));

        output.clear();
        input.add(5);
        intCode.run(memory, input, output);
        assertEquals(999, output.get(output.size() - 1));

        output.clear();
        input.add(7);
        intCode.run(memory, input, output);
        assertEquals(999, output.get(output.size() - 1));

        output.clear();
        input.add(8);
        intCode.run(memory, input, output);
        assertEquals(1000, output.get(output.size() - 1));

        output.clear();
        input.add(10);
        intCode.run(memory, input, output);
        assertEquals(1001, output.get(output.size() - 1));

        output.clear();
        input.add(1000);
        intCode.run(memory, input, output);
        assertEquals(1001, output.get(output.size() - 1));
    }
}
