package li.ste.adventofcode.year2019.intcode;

import li.ste.adventofcode.utils.AdventOfCodeException;

import java.util.ArrayList;
import java.util.List;

public class IntCode {
    private final int[] localMemory;
    private final List<Integer> input;
    private final List<Integer> output;
    private int instructionPointer;

    public IntCode(int[] memory, List<Integer> input, List<Integer> output) {
        this.localMemory = memory.clone();
        this.input = input;
        this.output = output;
    }

    public IntCode(int[] memory, int noun, int verb) {
        this.localMemory = memory.clone();
        this.localMemory[1] = noun;
        this.localMemory[2] = verb;
        this.input = new ArrayList<>();
        this.output = new ArrayList<>();
    }


    public int[] run() {
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
                        throw new IntCodeNoInputException("IntCode: no input available");
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

    public List<Integer> getOutput() {
        return output;
    }

    public List<Integer> getInput() {
        return input;
    }

    public class IntCodeNoInputException extends AdventOfCodeException {
        public IntCodeNoInputException(String message) {
            super(message);
        }
    }
}

