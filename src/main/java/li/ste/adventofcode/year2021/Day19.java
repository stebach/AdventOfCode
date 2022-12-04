package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.year2021.day19.Beacon;
import li.ste.adventofcode.year2021.day19.Scanner;

import java.util.*;

public class Day19 extends Day {
    private final List<Scanner> scanners = new ArrayList<>();
    public static void main(String[] args) {
        Day day = new Day19(new InputProvider());
        day.solvePuzzles();
    }

    public Day19(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        Scanner currentScanner = null;
        for (String line: getData()) {
            if (line.length() > 0) {
                if (line.startsWith("---")) {
                    // new scanner
                    currentScanner = new Scanner(scanners.size());
                    scanners.add(currentScanner);
                } else if (currentScanner != null) {
                    String[] parts = line.split(",");
                    currentScanner.addBeacon(Integer.parseInt(parts[0]), Integer.parseInt(parts[1]), Integer.parseInt(parts[2]));
                }
            }
        }

        scanners.get(0).setPositionAndRotation(0,0,0,0,0,0);

        boolean repeat = true;
        while (repeat) {
            repeat = false;
            for (Scanner scanner : scanners) {
                if (scanner.toScanFrom()) {
                    repeat = true;
                    scanner.findNext(scanners);
                }
            }
        }

        Set<Beacon> allBeacons = new HashSet<>();

        for (Scanner scanner : scanners) {
            allBeacons.addAll(scanner.getBeacons());
        }

        setSolution1(allBeacons.size());

        List<Integer> distances = new ArrayList<>();
        for (Scanner scanner : scanners) {
            distances.add(scanner.getMaxManhattanDistance(scanners));
        }

        setSolution2(Collections.max(distances));
    }
}
