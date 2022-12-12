package li.ste.adventofcode.year2022;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.year2022.day12.Position;

import java.util.*;

public class Day12 extends Day {
    private int endX;
    private int endY;
    private List<List<Integer>> grid;

    public static void main(String[] args) {
        Day day = new Day12(new InputProvider());
        day.solvePuzzles();
    }

    public Day12(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        List<String> data = getData();
        grid = new ArrayList<>();
        int startX = 0;
        int startY = 0;
        endX = 0;
        endY = 0;

        List<int[]> lowestPoints = new ArrayList<>();

        for (int y=0; y<data.size(); y++) {
            List<Integer> newRow = new ArrayList<>();
            char[] chars = data.get(y).toCharArray();
            for (int x=0; x<chars.length; x++) {
                char c = chars[x];
                if (c == 'S') {
                    startX = x;
                    startY = y;
                    c = 'a';
                } else if (c == 'E') {
                    endX = x;
                    endY = y;
                    c = 'z';
                }
                newRow.add(c - 'a');
                if (c == 'a') {
                    lowestPoints.add(new int[] { x, y });
                }
            }
            grid.add(newRow);
        }

        Position.setHeight(grid.size());
        Position.setWidth(grid.get(0).size());

        setSolution1(getDistanceToEnd(startX, startY));

        List<Integer> distances = new ArrayList<>();
        for (int[] lowestPoint : lowestPoints) {
            distances.add(getDistanceToEnd(lowestPoint[0], lowestPoint[1]));
        }
        Collections.sort(distances);

        setSolution2(distances.get(0));
    }

    private int getDistanceToEnd(int startX, int startY) {
        TreeSet<Position> positionsToCheck = new TreeSet<>((o1, o2) -> {
            if (o1.hashCode() == o2.hashCode()) {
                return 0;
            }
            if (o1.getCost() < o2.getCost()) {
                return -1;
            }
            if (o1.getCost() > o2.getCost()) {
                return 1;
            }
            return 1;
        });
        positionsToCheck.add(new Position(startX, startY, grid, 0));
        List<Integer> checkedPositions = new ArrayList<>();

        int minDistance = Integer.MAX_VALUE;

        while (!positionsToCheck.isEmpty()) {
            Position position = positionsToCheck.pollFirst();

            checkedPositions.add(position.hashCode());

            List<Position> newPositions = position.getReachablePositions();
            for (Position newPosition : newPositions) {
                if (!checkedPositions.contains(newPosition.hashCode())) {
                    if (newPosition.getX() == endX && newPosition.getY() == endY) {
                        minDistance = newPosition.getCost();
                        break;
                    } else if (!positionsToCheck.add(newPosition) && positionsToCheck.stream().filter(r -> r.equals(newPosition)).findFirst().get().getCost() > newPosition.getCost()) {
                            positionsToCheck.remove(newPosition);
                            positionsToCheck.add(newPosition);
                    }
                }
            }
            if (minDistance != Integer.MAX_VALUE) {
                break;
            }
        }
        return minDistance;
    }
}
