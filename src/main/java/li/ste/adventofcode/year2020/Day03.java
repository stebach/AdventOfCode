package li.ste.adventofcode.year2020;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.year2020.day03.Grid;

import java.util.List;

public class Day03 extends Day {
    public static void main(String[] args) {
        Day day = new Day03(new InputProvider());
        day.solvePuzzles();
    }

    public Day03(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        Grid grid = new Grid();
        List<String> data = getData();
        for (String row : data) {
            grid.addRow(row);
        }

        int[] angles = new int[5];
        for (int x=0; x<grid.getHeight();x++) {
            angles[0] += grid.hasTreeAt(x,x) ? 1 : 0;
            angles[1] += grid.hasTreeAt(x*3,x) ? 1 : 0;
            angles[2] += grid.hasTreeAt(x*5,x) ? 1 : 0;
            angles[3] += grid.hasTreeAt(x*7,x) ? 1 : 0;
            angles[4] += grid.hasTreeAt(x,x*2) ? 1 : 0;
        }

        setSolution1(angles[1]);
        setSolution2(angles[0]*angles[1]*angles[2]*angles[3]*angles[4]);
    }
}
