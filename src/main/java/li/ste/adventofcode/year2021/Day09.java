package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.year2021.day09.Grid;

import java.util.List;

public class Day09 extends Day {
    public static void main(String[] args) {
        Day day = new Day09(new InputProvider());
        day.solvePuzzles();
    }

    public Day09(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        Grid grid = new Grid();
        for (String line : getData()) {
            grid.addLine(line);
        }

        List<int[]> lowPoints = grid.getLowPointCoords();
        int riskLevel = grid.getSumOfCoords(lowPoints) + lowPoints.size();

        int basins = grid.calcBasins();

        setSolution1(riskLevel);
        setSolution2(basins);
    }
}
