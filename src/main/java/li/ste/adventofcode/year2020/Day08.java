package li.ste.adventofcode.year2020;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.year2020.day08.HandheldConsoleInstruction;

import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;

public class Day08 extends Day {
    public static void main(String[] args) {
        Day day = new Day08(new InputProvider());
        day.solvePuzzles();
    }

    public Day08(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        List<HandheldConsoleInstruction> data = getRegexData("^([a-z]{3}) ([+-][0-9]+)$",HandheldConsoleInstruction.class);
        AtomicInteger pointer = new AtomicInteger();
        AtomicInteger solution1 = new AtomicInteger();
        boolean running = true;
        while (running) {
            running = data.get(pointer.intValue()).execute(solution1, pointer);
        }

        AtomicInteger solution2 = new AtomicInteger();
        boolean solved = false;
        for (int i=0; i<data.size() && !solved; i++) {
            for (HandheldConsoleInstruction instruction : data) {
                instruction.reset();
            }
            if (data.get(i).switchNopJmp()) {
                pointer.set(0);
                solution2.set(0);
                running = true;
                while (running) {
                    if (pointer.intValue() == data.size()) {
                        solved = true;
                        break;
                    }
                    running = data.get(pointer.intValue()).execute(solution2, pointer);
                }
                data.get(i).switchNopJmp();
            }
        }

        setSolution1(solution1);
        setSolution2(solution2);
    }
}
