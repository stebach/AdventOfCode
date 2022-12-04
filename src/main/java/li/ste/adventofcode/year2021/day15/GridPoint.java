package li.ste.adventofcode.year2021.day15;

import java.util.List;

public class GridPoint {
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
