package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.ArrayList;
import java.util.List;

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

    private class DijkstraSovler {
        private List<int[]> distances;
        private final List<GridPoint> activePoints = new ArrayList<>();
        private Grid grid;

        public int solve(Grid grid) {
            this.grid = grid;
            distances = new ArrayList<>();
            while (distances.size() < grid.getHeight()) {
                distances.add(new int[grid.getWidth()]);
            }
            activePoints.add(new GridPoint(0,0));

            while (!activePoints.isEmpty()) {
                run();
            }

            return distances.get(grid.getHeight()-1)[grid.getWidth() -1];
        }

        private void run() {
            GridPoint currentPoint = activePoints.remove(0);
            currentPoint.run(grid, distances, activePoints);
        }
    }

    private class Gird5x5 extends Grid {

        @Override
        public void addRow(String row) {
            width = row.length() * 5;
            height += 1;
            int[] newRow = new int[width];
            for (int i=0; i<width / 5; i++) {
                for (int j=0; j<5; j++) {
                    newRow[i + j*(width / 5)] = max9(row.charAt(i) - 48 + j);
                }
            }
            rows.add(newRow);
        }

        @Override
        public int solve() {
            for (int j=1; j<5; j++) {
                for (int i=0; i<height; i++) {
                    int[] newRow = new int[width];
                    for (int k=0;k<width; k++) {
                        newRow[k] = max9(rows.get(i)[k] + j);
                    }
                    rows.add(newRow);
                }
            }
            height *= 5;
            return super.solve();
        }

        private int max9(int nr) {
            if (nr > 9) {
                return nr - 9;
            }
            return nr;
        }
    }

    private class Grid {

        List<int[]> rows = new ArrayList<>();
        protected int width;
        protected int height;

        public void addRow(String row) {
            width = row.length();
            height += 1;
            int[] newRow = new int[width];
            for (int i=0; i<width; i++) {
                newRow[i] = row.charAt(i) - 48;
            }
            rows.add(newRow);
        }

        public int solve() {
            //get baseline
            DijkstraSovler dijkstraSovler = new DijkstraSovler();

            return dijkstraSovler.solve(this);
        }

        public int getWidth() {
            return width;
        }
        public int getHeight() {
            return height;
        }

        public int getNumber(int x, int y) {
            return rows.get(y)[x];
        }
    }

    private class GridPoint {
        private final int x;
        private final int y;

        public GridPoint(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public void run(Grid grid, List<int[]> distances, List<GridPoint> activePoints) {
            // north
            tryPoint(x, y-1, grid, distances, activePoints);

            // east
            tryPoint(x+1, y, grid, distances, activePoints);

            // south
            tryPoint(x, y+1, grid, distances, activePoints);

            // west
            tryPoint(x-1, y, grid, distances, activePoints);
        }

        private void tryPoint(int localX, int localY, Grid grid, List<int[]> distances, List<GridPoint> activePoints) {
            if (
                    (localX >= 0 && localX < grid.getWidth() && localY >= 0 && localY < grid.getHeight())
                            && (distances.get(localY)[localX] == 0 || distances.get(localY)[localX] > distances.get(y)[x] + grid.getNumber(localX, localY))
            ) {
                distances.get(localY)[localX] = distances.get(y)[x] + grid.getNumber(localX, localY);
                activePoints.add(new GridPoint(localX, localY));
            }
        }
    }
}
