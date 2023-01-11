package li.ste.adventofcode.year2019;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.year2019.intcode.IntCode;

import java.util.*;

public class Day02 extends Day {
    public static void main(String[] args) {
        Day day = new Day02(new InputProvider());
        day.solvePuzzles();
    }

    public Day02(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        Scanner scanner = getScanner();
        int[] values = Arrays.stream(scanner.nextLine().split(",")).mapToInt(Integer::parseInt).toArray();

        IntCode intCode = new IntCode(values, 12, 2);


        int[] result = intCode.run();

        setSolution1(result[0]);

        int result2 = 0;
        loop:
        for (int noun = 1; noun < 100; noun += 1) {
            for (int verb = 1; verb < 100; verb += 1) {
                intCode = new IntCode(values, noun, verb);
                result = intCode.run();
                if (result[0] == 19690720) {
                    result2 = noun * 100 + verb;
                    break loop;
                }
            }
        }

        setSolution2(result2);
    }
}
