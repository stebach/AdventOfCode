package li.ste.adventofcode.year2021.day15;

import java.util.ArrayList;
import java.util.List;

public class DijkstraSovler {
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
