package li.ste.adventofcode.year2022;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.*;

public class Day15 extends Day {
    private int lineToCheck = 2000000;
    private int maxGridValue = 4000000;

    public static void main(String[] args) {
        Day day = new Day15(new InputProvider());
        day.solvePuzzles();
    }

    public Day15(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        Scanner scanner = getScanner();

        List<int[]> sensors = new ArrayList<>();
        while (scanner.hasNextLine()) {
            String[] line = scanner.nextLine().split(" ");
            int sX = Integer.parseInt(line[2].substring(2, line[2].length()-1));
            int sY = Integer.parseInt(line[3].substring(2, line[3].length()-1));
            int bX = Integer.parseInt(line[8].substring(2, line[8].length()-1));
            int bY= Integer.parseInt(line[9].substring(2));
            sensors.add( new int[] { sX, sY, bX, bY, Math.abs(sX - bX) + Math.abs(sY - bY) });
        }

        Set<Integer> xPosSet = new HashSet<>();
        Set<Integer> beaconsOnLine = new HashSet<>();

        for (int[] sensor : sensors) {
            int distanceToLine = Math.abs(sensor[1] - lineToCheck);

            if (sensor[3] == lineToCheck) {
                beaconsOnLine.add(sensor[2]);
            }


            for (int x = sensor[0] - (sensor[4] - distanceToLine); x <= sensor[0] + (sensor[4] - distanceToLine);  x++) {
                xPosSet.add(x);
            }
        }

        setSolution1(xPosSet.size() - beaconsOnLine.size());

        long solution2 = -1;
        for (int y = 0; y <= maxGridValue; y++) {
            for (int x = 0; x < maxGridValue; x++) {
                boolean found = true;
                for (int[] sensor : sensors) {
                    long distance = (long)Math.abs(sensor[0] - x) + Math.abs(sensor[1] - y);
                    if (distance <= sensor[4]) {
                        x = sensor[0] + (sensor[4] - Math.abs(sensor[1] - y));
                        found = false;
                        break;
                    }
                }
                if (found) {
                    solution2 = x * 4_000_000L + y;
                }
            }
            if (solution2 > -1) {
                break;
            }
        }

        setSolution2(solution2);
    }

    public void setLineToCheck(int line) {
        lineToCheck = line;
    }

    public void setMaxGridValue(int maxValue) {
        maxGridValue = maxValue;
    }
}
