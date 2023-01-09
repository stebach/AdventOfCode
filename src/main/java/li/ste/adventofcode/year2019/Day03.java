package li.ste.adventofcode.year2019;

import li.ste.adventofcode.utils.AdventOfCodeException;
import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.*;

public class Day03 extends Day {

    private record Coord(int x, int y) {}

    public static void main(String[] args) {
        Day day = new Day03(new InputProvider());
        day.solvePuzzles();
    }

    public Day03(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        Scanner scanner = getScanner();

        String[] wireDirections1 = scanner.nextLine().split(",");
        String[] wireDirections2 = scanner.nextLine().split(",");

        Map<Coord, Integer> firstVisits1 = new HashMap<>();
        Map<Coord, Integer> firstVisits2 = new HashMap<>();
        Set<Coord> wire1Coords = getCoords(wireDirections1, firstVisits1);
        Set<Coord> wire2Coords = getCoords(wireDirections2, firstVisits2);

        Set<Coord> wireCoords = new HashSet<>(wire1Coords);
        wireCoords.retainAll(wire2Coords);

        int minDistance = Integer.MAX_VALUE;
        int minDistance2 = Integer.MAX_VALUE;
        for (Coord wireCoord : wireCoords) {
            int distance = Math.abs(wireCoord.x) + Math.abs(wireCoord.y);
            if (distance < minDistance) {
                minDistance = distance;
            }
            int distance2 = firstVisits1.get(wireCoord) + firstVisits2.get(wireCoord);
            if (distance2 < minDistance2) {
                minDistance2 = distance2;
            }
        }

        setSolution1(minDistance);
        setSolution2(minDistance2);
    }

    private Set<Coord> getCoords(String[] wireDirections, Map<Coord, Integer> firstVisits) {
        Set<Coord> retVal = new HashSet<>();

        int x = 0;
        int y = 0;
        int xMod = 0;
        int yMod = 0;
        int index = 1;
        Coord nextCoord = null;
        for (String direction : wireDirections) {
            switch (direction.charAt(0)) {
                case 'R' -> {
                    xMod = 1;
                    yMod = 0;
                }
                case 'L' -> {
                    xMod = -1;
                    yMod = 0;
                }
                case 'U' -> {
                    xMod = 0;
                    yMod = -1;
                }
                case 'D' -> {
                    xMod = 0;
                    yMod = 1;
                }
                default -> throw new AdventOfCodeException("unknown direction: " + direction.charAt(0));
            }
            for (int i = 0; i < Integer.parseInt(direction.substring(1)); i++) {
                x += xMod;
                y += yMod;
                nextCoord = new Coord(x, y);
                if (retVal.add(nextCoord)) {
                    firstVisits.put(nextCoord, index);
                }
                index += 1;
            }
        }

        return retVal;
    }

}
