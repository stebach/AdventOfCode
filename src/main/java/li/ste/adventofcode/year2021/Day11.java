package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.year2021.day11.Grid;

public class Day11 extends Day {
    public static void main(String[] args) {
        Day day = new Day11(new InputProvider());
        day.solvePuzzles();
    }

    public Day11(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        Grid grid = new Grid();
        for (String line : getData()) {
            grid.addLine(line);
        }
        grid.doSteps(100);
        setSolution1(grid.getFlashes());
        setSolution2(grid.getFirstCompleteFlashStep());
    }
}
