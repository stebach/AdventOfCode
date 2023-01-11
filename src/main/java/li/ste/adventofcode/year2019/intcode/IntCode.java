package li.ste.adventofcode.year2019.intcode;

import li.ste.adventofcode.utils.AdventOfCodeException;

import java.util.ArrayList;
import java.util.List;

public class IntCode {
    public int[] run(int[] memory, int noun, int verb) {
        return run(memory, noun, verb, new ArrayList<>(), new ArrayList<>());
    }

    public int[] run(int[] memory, List<Integer> input, List<Integer> output) {
        return run(memory, memory[1], memory[2], input, output);
    }

    private int[] run(int[] memory, int noun, int verb, List<Integer> input, List<Integer> output) {
        int[] localMemory = memory.clone();
        localMemory[1] = noun;
        localMemory[2] = verb;
        int instructionPointer = 0;
        while (localMemory[instructionPointer] != 99) {
            int operation = localMemory[instructionPointer] % 100;
            int modeMask = Integer.parseInt(String.valueOf(localMemory[instructionPointer] / 100), 2);
            switch (operation) {
                case 1 -> { // add
                    localMemory[localMemory[instructionPointer + 3]] = getParam(1, modeMask, localMemory, instructionPointer)
                            + getParam(2, modeMask, localMemory, instructionPointer);
                    instructionPointer += 4;
                }
                case 2 -> { // multiply
                    localMemory[localMemory[instructionPointer + 3]] =
                            getParam(1, modeMask, localMemory, instructionPointer) *
                                    getParam(2, modeMask, localMemory, instructionPointer);
                    instructionPointer += 4;
                }
                case 3 -> { // input
                    if (input.isEmpty()) {
                        throw new AdventOfCodeException("IntCode: no input available");
                    }
                    localMemory[localMemory[instructionPointer + 1]] = input.remove(0);
                    instructionPointer += 2;
                }
                case 4 -> { // output
                    output.add(getParam(1, modeMask, localMemory, instructionPointer));
                    instructionPointer += 2;
                }
                case 5 -> { // jump if true
                    if (getParam(1, modeMask, localMemory, instructionPointer) == 0) {
                        instructionPointer += 3;
                    } else {
                        instructionPointer = getParam(2, modeMask, localMemory, instructionPointer);
                    }
                }
                case 6 -> { // jump if true
                    if (getParam(1, modeMask, localMemory, instructionPointer) == 0) {
                        instructionPointer = getParam(2, modeMask, localMemory, instructionPointer);
                    } else {
                        instructionPointer += 3;
                    }
                }
                case 7 -> { // less than
                    if (getParam(1, modeMask, localMemory, instructionPointer) < getParam(2, modeMask, localMemory, instructionPointer)) {
                        localMemory[localMemory[instructionPointer + 3]] = 1;
                    } else {
                        localMemory[localMemory[instructionPointer + 3]] = 0;
                    }
                    instructionPointer += 4;
                }
                case 8 -> { // equals
                    if (getParam(1, modeMask, localMemory, instructionPointer) == getParam(2, modeMask, localMemory, instructionPointer)) {
                        localMemory[localMemory[instructionPointer + 3]] = 1;
                    } else {
                        localMemory[localMemory[instructionPointer + 3]] = 0;
                    }
                    instructionPointer += 4;
                }
                default ->
                        throw new AdventOfCodeException("IntCode: invalid operation: " + operation + " at " + instructionPointer);
            }
        }
        return localMemory;
    }

    private int getParam(int paramNum, int modeMask, int[] localMemory, int instructionPointer) {
        int localMemoryVal = localMemory[instructionPointer + paramNum];
        return (((modeMask & (int)Math.pow(2, paramNum - 1)) > 0) ? localMemoryVal :  localMemory[localMemoryVal]);
    }
}

