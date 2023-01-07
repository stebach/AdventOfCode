package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.ArrayList;
import java.util.List;

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

    private class Grid {
        private final List<List<Integer>> lines = new ArrayList<>();
        private int flashes;
        private int currentStep;
        private int allFlashStep;

        public void addLine(String line) {
            List<Integer> newLine = new ArrayList<>();
            char[] chars = line.toCharArray();
            for (char c : chars) {
                newLine.add(c-48);
            }

            lines.add(newLine);
        }

        public void doSteps(int steps) {
            for (int i=0; i<steps; i++) {
                doStep();
            }
        }

        private void doStep() {
            currentStep += 1;
            for (int y=0; y<lines.size(); y++) {
                for (int x=0; x<lines.get(0).size(); x++) {
                    increaseAt(x,y);
                }
            }
            int oldFlashes = flashes;
            for (List<Integer> line : lines) {
                for (int x = 0; x < lines.get(0).size(); x++) {
                    if (line.get(x) > 9) {
                        flashes += 1;
                        line.set(x, 0);
                    }
                }
            }
            if (flashes - oldFlashes == lines.size() * lines.get(0).size()) {
                allFlashStep = currentStep;
            }
        }

        private void increaseAt(int x, int y) {
            int newVal = lines.get(y).get(x)+1;
            lines.get(y).set(x, newVal);
            if (newVal == 10) {
                increaseTopRow(x, y);
                increaseCenterRow(x, y);
                increaseBottomRow(x, y);
            }
        }

        private void increaseBottomRow(int x, int y) {
            if (y + 1 < lines.size()) {
                if (x > 0) {
                    increaseAt(x-1,y+1);
                }
                increaseAt(x,y+1);
                if (x + 1 < lines.get(y).size()) {
                    increaseAt(x+1,y+1);
                }
            }
        }

        private void increaseCenterRow(int x, int y) {
            if (x > 0) {
                increaseAt(x-1,y);
            }
            if (x + 1 < lines.get(y).size()) {
                increaseAt(x+1,y);
            }
        }

        private void increaseTopRow(int x, int y) {
            if (y>0) {
                if (x > 0) {
                    increaseAt(x-1,y-1);
                }
                increaseAt(x,y-1);
                if (x + 1 < lines.get(y).size()) {
                    increaseAt(x+1,y-1);
                }
            }
        }

        public int getFlashes() {
            return flashes;
        }

        public int getFirstCompleteFlashStep() {
            while (allFlashStep == 0) {
                doStep();
                // prevent infiniti loop...
                if (currentStep == 1000000) {
                    break;
                }
            }
            return allFlashStep;
        }
    }
}
