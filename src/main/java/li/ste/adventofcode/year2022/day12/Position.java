package li.ste.adventofcode.year2022.day12;

import java.util.ArrayList;
import java.util.List;

public class Position {
    private static int height;
    private static int width;
    private final int x;
    private final int y;
    private final List<List<Integer>> grid;
    private final int cost;
    private final int elevation;

    public Position(int x, int y, List<List<Integer>> grid, int cost) {
        this.x = x;
        this.y = y;
        this.grid = grid;
        this.cost = cost;
        this.elevation = grid.get(y).get(x);
    }

    public static void setHeight(int height) {
        Position.height = height;
    }

    public static void setWidth(int width) {
        Position.width = width;
    }

    public List<Position> getReachablePositions() {
        List<Position> retVal = new ArrayList<>();
        if (x > 0 && grid.get(y).get(x-1) <= elevation + 1) {
            retVal.add(new Position(x-1,y, grid, cost+1));
        }
        if (x < width - 1 && grid.get(y).get(x+1) <= elevation + 1) {
            retVal.add(new Position(x+1,y, grid, cost+1));
        }
        if (y > 0 && grid.get(y-1).get(x) <= elevation + 1) {
            retVal.add(new Position(x,y-1, grid, cost+1));
        }
        if (y < height - 1 && grid.get(y+1).get(x) <= elevation + 1) {
            retVal.add(new Position(x,y+1, grid, cost+1));
        }
        return retVal;
    }

    public int getCost() {
        return cost;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Position position = (Position) o;
        return x == position.x && y == position.y;
    }

    @Override
    public int hashCode() {
        return y * (height * 10) + x;
    }

    @Override
    public String toString() {
        return "Position @ " + x + "/" + y;
    }
}
