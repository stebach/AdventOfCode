package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.utils.Letter4x6recognizer;
import li.ste.adventofcode.year2021.day13.Grid;

public class Day13 extends Day {
    public static void main(String[] args) {
        Day day = new Day13(new InputProvider());
        day.solvePuzzles();
    }

    public Day13(InputProvider provider) {
        super(provider);
    }
    boolean firstFold = true;

    @Override
    public void run() {
        Grid grid = new Grid();
        for (String line : getData()) {
            if (line.length() > 0) {
                if (line.startsWith("fold")) {
                    fold(line, grid);
                } else {
                    String[] parts = line.split(",");
                    grid.addDot(Integer.parseInt(parts[0]), Integer.parseInt(parts[1]));
                }
            } else {
                grid.fillEmpty();
            }
        }

        out(grid.draw());

        setSolution2(Letter4x6recognizer.getText(grid));
    }

    private void fold(String line, Grid grid) {
        if (line.startsWith("fold along x=")) {
            grid.foldX(Integer.parseInt(line.substring(13)));
            if (firstFold) {
                firstFold = false;
                setSolution1(grid.countDots());
            }
        } else if (line.startsWith("fold along y=")) {
            grid.foldY(Integer.parseInt(line.substring(13)));
            if (firstFold) {
                firstFold = false;
                setSolution1(grid.countDots());
            }
        }
    }
}
