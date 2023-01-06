package li.ste.adventofcode.year2020;

import li.ste.adventofcode.utils.AdventOfCodeException;
import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Day24 extends Day {
    public static void main(String[] args) {
        Day day = new Day24(new InputProvider());
        day.solvePuzzles();
    }

    public Day24(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        Scanner scanner = getScanner();
        Set<Point> blacks = new HashSet<>();
        while (scanner.hasNextLine()) {
            String line = scanner.next();

            int x = 0;
            int y = 0;

            for (int i = 0; i < line.length(); i++) {
                switch (line.charAt(i)) {
                    case 's' -> {
                        i ++;
                        if (line.charAt(i) == 'e') {
                            x += 1;
                        } else {
                            x -= 1;
                        }
                        y += 1;
                    }
                    case 'n' -> {
                        i ++;
                        if (line.charAt(i) == 'e') {
                            x += 1;
                        } else {
                            x -= 1;
                        }
                        y -= 1;
                    }
                    case 'w' -> x -= 2;
                    case 'e' -> x += 2;
                    default -> throw new AdventOfCodeException("unknown char: " + line.charAt(i));
                }
            }

            Point key = new Point(x, y);

            if (!blacks.add(key)) {
                blacks.remove(key);
            }

        }
        setSolution1(blacks.size());

        int[][] adjacent = new int[][] {
                { -2, 0 }, { -1, -1 }, { 1, -1 }, { 2, 0 }, { 1, 1 }, { -1 ,1 }
        };

        Set<Point> newPoints = new HashSet<>();

        for (int i = 0; i < 100; i++) {
            int minX = blacks.stream().mapToInt(r->r.x).min().getAsInt() - 2;
            int maxX = blacks.stream().mapToInt(r->r.x).max().getAsInt() + 2;
            int minY = blacks.stream().mapToInt(r->r.y).min().getAsInt() - 1;
            int maxY = blacks.stream().mapToInt(r->r.y).max().getAsInt() + 1;


            for (int y = minY; y <= maxY; y++) {
                for (int x = minX; x <= maxX; x++) {
                    int adjacentBlacks = 0;
                    for (int[] ints : adjacent) {
                        if (blacks.contains(new Point(x + ints[0], y + ints[1]))) {
                            adjacentBlacks += 1;
                        }
                    }
                    Point point = new Point(x, y);
                    if (
                            (blacks.contains(point) && (adjacentBlacks == 1 || adjacentBlacks == 2))
                            || (!blacks.contains(point) && adjacentBlacks == 2)
                    ) {
                        newPoints.add(point);
                    }
                }
            }

            blacks.clear();
            blacks.addAll(newPoints);
            newPoints.clear();
        }

        setSolution2(blacks.size());
    }

    private record Point(int x, int y) {
    }

}
