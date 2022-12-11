package li.ste.adventofcode.year2022;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.*;
import java.util.HashMap;

public class Day10 extends Day {
    public static void main(String[] args) {
        Day day = new Day10(new InputProvider());
        day.solvePuzzles();
    }

    public Day10(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        Scanner scanner = getScanner();
        int x = 1;
        int instructionDuration = 1;
        int signalStrength = 0;
        List<Integer> cyclesToCheck = Arrays.asList(20, 60, 100, 140, 180, 220);
        String instruction="";
        StringBuilder display = new StringBuilder();

        Map<String, Integer> instructionDurations = new HashMap<>();
        instructionDurations.put("noop",1);
        instructionDurations.put("addx",2);

        for (int cycle = 1; cycle <= 240; cycle++) {
            //start of cycle
            instructionDuration--;
            if (instructionDuration == 0) { // get next instruction
                instruction = scanner.next();
                instructionDuration = instructionDurations.get(instruction);
            }

            //mid of cycle
            if (cyclesToCheck.contains(cycle)) {
                signalStrength += cycle * x;
            }

            if ((cycle -1) % 40 <= x+1 && (cycle -1) % 40 >= x-1) {
                display.append("#");
            } else {
                display.append(".");
            }

            if (cycle % 40 == 0) {
                display.append("\n");
            }

            //end of cycle
            if ("addx".equals(instruction) && instructionDuration == 1) {
                x += scanner.nextInt();
            }
        }

        setSolution1(signalStrength);
        setSolution2("\n" + display);
    }
}
