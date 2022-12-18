package li.ste.adventofcode.year2020;

import li.ste.adventofcode.utils.AdventOfCodeException;
import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Day12 extends Day {
    private int x;
    private int y;
    private int[] direction;
    private int directionIndex;
    private int[][] directions;
    private int waypointX;
    private int waypointY;

    public static void main(String[] args) {
        Day day = new Day12(new InputProvider());
        day.solvePuzzles();
    }

    public Day12(InputProvider provider) {
        super(provider);
    }

    private record Instruction(char action, int value) {}

    @Override
    public void run() {
        Scanner scanner = getScanner();

        List<Instruction> instructionList = new ArrayList<>();
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            instructionList.add(new Instruction(line.charAt(0), Integer.parseInt(line.substring(1))));
        }

        x = 0;
        y = 0;
        directionIndex = 1;
        directions = new int[][] {
                { 0, 1 },
                { 1, 0 },
                { 0, -1 },
                { -1, 0 }
        };
        direction = directions[directionIndex];

        for (Instruction instruction : instructionList) {
            runInstruction(instruction);
        }

        setSolution1(Math.abs(x) + Math.abs(y));

        x = 0;
        y = 0;
        waypointX = 10;
        waypointY = 1;

        for (Instruction instruction : instructionList) {
            runInstruction2(instruction);
        }

        setSolution2(Math.abs(x) + Math.abs(y));
    }

    private void runInstruction(Instruction instruction) {
        switch (instruction.action) {
            case 'N' -> y += instruction.value;
            case 'E' -> x += instruction.value;
            case 'S' -> y -= instruction.value;
            case 'W' -> x -= instruction.value;
            case 'F' -> {
                x += instruction.value * direction[0];
                y += instruction.value * direction[1];
            }
            case 'L' -> {
                directionIndex = (directionIndex + ((360 - instruction.value) / 90)) % 4;
                direction = directions[directionIndex];
            }
            case 'R' -> {
                directionIndex = (directionIndex + (instruction.value / 90)) % 4;
                direction = directions[directionIndex];
            }
            default -> throw new AdventOfCodeException("instruction unknown " + instruction.action);
        }
    }

    private void runInstruction2(Instruction instruction) {
        int cos;
        int sin;
        int newX;
        int newY;
        switch (instruction.action) {
            case 'N' -> waypointY += instruction.value;
            case 'E' -> waypointX += instruction.value;
            case 'S' -> waypointY -= instruction.value;
            case 'W' -> waypointX -= instruction.value;
            case 'F' -> {
                x += instruction.value * waypointX;
                y += instruction.value * waypointY;
            }
            case 'L' -> {
                cos = (int) Math.cos(Math.toRadians(instruction.value));
                sin = (int) Math.sin(Math.toRadians(instruction.value));
                newX = waypointX * cos - waypointY * sin;
                newY = waypointX * sin + waypointY * cos;
                waypointX = newX;
                waypointY = newY;
            }
            case 'R' -> {
                cos = (int) Math.cos(Math.toRadians(-instruction.value));
                sin = (int) Math.sin(Math.toRadians(-instruction.value));
                newX = waypointX * cos - waypointY * sin;
                newY = waypointX * sin + waypointY * cos;
                waypointX = newX;
                waypointY = newY;
            }
            default -> throw new AdventOfCodeException("instruction unknown " + instruction.action);
        }
    }
}
