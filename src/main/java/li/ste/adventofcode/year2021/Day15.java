package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.year2021.day15.Gird5x5;
import li.ste.adventofcode.year2021.day15.Grid;

public class Day15 extends Day {
    public static void main(String[] args) {
        Day day = new Day15(new InputProvider());
        day.solvePuzzles();
    }

    public Day15(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        Grid grid = new Grid();
        Grid grid2 = new Gird5x5();
        for (String row : getData()) {
            grid.addRow(row);
            grid2.addRow(row);
        }

        setSolution1(grid.solve());
        setSolution2(grid2.solve());
    }
}
