package li.ste.adventofcode.year2019.intcode;

import li.ste.adventofcode.utils.AdventOfCodeException;

public class IntCode {
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

