package li.ste.adventofcode.year2019;

import li.ste.adventofcode.utils.AdventOfCodeException;
import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

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

        IntCode intCode = new IntCode();

        int[] result = intCode.run(values, 12, 2);

        setSolution1(result[0]);

        int result2 = 0;
        loop:
        for (int noun = 1; noun < 100; noun += 1) {
            for (int verb = 1; verb < 100; verb += 1) {
                result = intCode.run(values, noun, verb);
                if (result[0] == 19690720) {
                    result2 = noun * 100 + verb;
                    break loop;
                }
            }
        }

        setSolution2(result2);
    }

    private static class IntCode {
        public int[] run(int[] memory, int noun, int verb) {
            int[] localMemory = memory.clone();
            localMemory[1] = noun;
            localMemory[2] = verb;
            int instructionPointer = 0;
            while (localMemory[instructionPointer] != 99) {
                switch (localMemory[instructionPointer]) {
                    case 1 -> {
                        localMemory[localMemory[instructionPointer + 3]] = localMemory[localMemory[instructionPointer + 1]] + localMemory[localMemory[instructionPointer + 2]];
                        instructionPointer += 4;
                    }
                    case 2 -> {
                        localMemory[localMemory[instructionPointer + 3]] = localMemory[localMemory[instructionPointer + 1]] * localMemory[localMemory[instructionPointer + 2]];
                        instructionPointer += 4;
                    }
                    default ->
                            throw new AdventOfCodeException("invalid operation: " + localMemory[instructionPointer] + " at " + instructionPointer);
                }
            }
            return localMemory;
        }
    }
}
