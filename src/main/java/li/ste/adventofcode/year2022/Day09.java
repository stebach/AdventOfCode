package li.ste.adventofcode.year2022;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.*;

public class Day09 extends Day {
    public static void main(String[] args) {
        Day day = new Day09(new InputProvider());
        day.solvePuzzles();
    }

    public Day09(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        Scanner scanner = getScanner();
        List<int[]> positions = Arrays.asList(
                new int[] { 0,0 },
                new int[] { 0,0 },
                new int[] { 0,0 },
                new int[] { 0,0 },
                new int[] { 0,0 },
                new int[] { 0,0 },
                new int[] { 0,0 },
                new int[] { 0,0 },
                new int[] { 0,0 },
                new int[] { 0,0 }
        );
        Set<String> visitedP1 = new HashSet<>();
        Set<String> visitedP9 = new HashSet<>();

        Map<String, int[]> directions = new HashMap<>();
        directions.put("R", new int[] { 1,0 });
        directions.put("L", new int[] { -1,0 });
        directions.put("D", new int[] { 0,1 });
        directions.put("U", new int[] { 0,-1 });

        while (scanner.hasNext()) {
            String direction = scanner.next();
            int steps = scanner.nextInt();

            for (int step=0; step<steps; step++) {
                int[] currentDirection = directions.get(direction);
                positions.get(0)[0] += currentDirection[0];
                positions.get(0)[1] += currentDirection[1];

                for (int i=1;i<positions.size(); i++) {
                    Set<String> visited = null;
                    if (i==1) {
                        visited = visitedP1;
                    } else if (i==9) {
                        visited = visitedP9;
                    }
                    positions.set(i, updateRelativePosition(positions.get(i), positions.get(i-1), visited));
                }
            }
        }
        setSolution1(visitedP1.size());
        setSolution2(visitedP9.size());
    }

    private int[] updateRelativePosition(int[] me, int[] other, Set<String> visited) {
        if (Math.abs(other[0] - me[0]) > 1) {
            me[0] += (other[0] - me[0]) / 2;
            if (other[1] != me[1]) {
                me[1] += (other[1] - me[1]) / Math.abs(other[1] - me[1]);
            }
        }
        if (Math.abs(other[1] - me[1]) > 1) {
            me[1] += (other[1] - me[1]) / 2;
            if (other[0] != me[0]) {
                me[0] += (other[0] - me[0]) / Math.abs(other[0] - me[0]);
            }
        }
        if (visited != null) {
            visited.add(me[0] +"|"+me[1]);
        }
        return me;
    }

}
