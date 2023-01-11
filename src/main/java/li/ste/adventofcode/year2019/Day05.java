package li.ste.adventofcode.year2019;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.year2019.intcode.IntCode;

import java.util.*;

public class Day05 extends Day {
    public static void main(String[] args) {
        Day day = new Day05(new InputProvider());
        day.solvePuzzles();
    }

    public Day05(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        Scanner scanner = getScanner();
        int[] values = Arrays.stream(scanner.nextLine().split(",")).mapToInt(Integer::parseInt).toArray();


        List<Integer> output = new ArrayList<>();
        IntCode intCode = new IntCode(values, new ArrayList<>(List.of(1)), output);
        intCode.run();
        setSolution1(output.get(output.size() - 1));


        output.clear();
        intCode = new IntCode(values, new ArrayList<>(List.of(5)), output);
        intCode.run();
        setSolution2(output.get(output.size() - 1));
    }
}
