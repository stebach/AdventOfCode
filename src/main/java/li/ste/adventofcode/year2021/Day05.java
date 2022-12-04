package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.year2021.day05.Day05Entry;
import li.ste.adventofcode.year2021.day05.Grid;

import java.util.List;

public class Day05 extends Day {
    public static void main(String[] args) {
        Day day = new Day05(new InputProvider());
        day.solvePuzzles();
    }

    public Day05(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        List<Day05Entry> data = getRegexData("^([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)$", Day05Entry.class);

        Grid grid = new Grid();
        for (Day05Entry entry : data) {
            grid.addIfHorizontalOrVertical(entry);
        }

        setSolution1(grid.getReachedTwoCount());
        for (Day05Entry entry : data) {
            grid.addIfNotHorizontalOrVertical(entry);
        }

        setSolution2(grid.getReachedTwoCount());
    }
}
