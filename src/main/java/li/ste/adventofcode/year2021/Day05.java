package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.utils.RegexResultRecipient;

import java.util.ArrayList;
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

    private class Day05Entry implements RegexResultRecipient {
        private int x1;
        private int y1;
        private int x2;
        private int y2;

        @Override
        public void setRegexResult(String[] listEntry) {
            this.x1 = Integer.parseInt(listEntry[0]);
            this.y1 = Integer.parseInt(listEntry[1]);
            this.x2 = Integer.parseInt(listEntry[2]);
            this.y2 = Integer.parseInt(listEntry[3]);
        }

        public boolean isHorizontalOrVertical() {
            return x1 == x2 || y1 == y2;
        }

        public List<int[]> getCoordinates() {
            List<int[]> retVal = new ArrayList<>();

            int numbers = Math.max(Math.abs(x1-x2)+1, Math.abs(y1-y2)+1);

            int[] xNumbers = generateCoordinateNumbers(x1, x2, numbers);
            int[] yNumbers = generateCoordinateNumbers(y1, y2, numbers);

            for (int i = 0; i< numbers; i++) {
                retVal.add(new int[] { xNumbers[i], yNumbers[i] });
            }

            return retVal;
        }

        private int[] generateCoordinateNumbers(int n1, int n2, int numbers) {
            int[] nNumbers = new int[numbers];
            if (n1 == n2) {
                for (int i=0; i<numbers; i++) {
                    nNumbers[i] = n1;
                }
            } else if (n1 < n2) {
                for (int i = 0; i< numbers; i++) {
                    nNumbers[i] = n1 + i;
                }
            } else {
                for (int i = 0; i< numbers; i++) {
                    nNumbers[i] = n1 - i;
                }
            }

            return nNumbers;
        }
    }

    private class Grid {
        private final List<GridRow> gridRows = new ArrayList<>();

        public void addIfHorizontalOrVertical(Day05Entry entry) {
            if (entry.isHorizontalOrVertical()) {
                this.add(entry);
            }
        }

        private void add(Day05Entry entry) {
            List<int[]> coordinates = entry.getCoordinates();
            for (int[] coordinate : coordinates) {
                while (gridRows.size() <= coordinate[0]) {
                    gridRows.add(new GridRow());
                }
                gridRows.get(coordinate[0]).add(coordinate[1]);
            }
        }

        public int getReachedTwoCount() {
            int retVal = 0;
            for (GridRow gridRow : gridRows) {
                retVal += gridRow.getReachedTwo();
            }
            return retVal;
        }

        public void addIfNotHorizontalOrVertical(Day05Entry entry) {
            if (!entry.isHorizontalOrVertical()) {
                this.add(entry);
            }
        }

        private class GridRow {
            private final List<Integer> columns = new ArrayList<>();
            private int reachedTwo;

            public void add(int column) {
                while (columns.size() <= column) {
                    columns.add(0);
                }
                int newVal = columns.get(column) + 1;
                columns.set(column, newVal);
                if (newVal == 2) {
                    reachedTwo += 1;
                }
            }

            public int getReachedTwo() {
                return reachedTwo;
            }
        }
    }
}
