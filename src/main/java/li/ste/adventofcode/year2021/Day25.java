package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.AdventOfCodeException;
import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.stream.Stream;

public class Day25 extends Day {
    private static final Integer CUCUMBER_MOVE_SOUTH = 1;
    private static final Integer CUCUMBER_MOVE_EAST = 2;
    private int width;

    public static void main(String[] args) {
        Day day = new Day25(new InputProvider());
        day.solvePuzzles();
    }

    public Day25(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        Map<String, int[]> cucumberMap = new HashMap<>();
        
        int y = 0;
        List<String> data = getData();
        for (String row : data) {
            width = row.length();
            for (int col=0; col<width; col++) {
                switch (row.charAt(col)) {
                    case 'v':
                        cucumberMap.put(col + "_" + y, new int[] { col, y, CUCUMBER_MOVE_SOUTH} );
                        break;
                    case '.':
                        // ignore
                        break;
                    case '>':
                        cucumberMap.put(col + "_" + y, new int[] { col, y, CUCUMBER_MOVE_EAST} );
                        break;
                    default:
                        throw new AdventOfCodeException("UNKNOWN CHAR: " + row.charAt(col));
                }
            }
            y++;
        }
        int height = y;

        AtomicBoolean didMove = new AtomicBoolean(true);
        int count = 0;
        while (didMove.get()) {
            didMove.set(false);
            Map<String, int[]> newMap = new HashMap<>();
            List<String> keysToRemove = new ArrayList<>();

            Stream<Map.Entry<String, int[]>> stream = cucumberMap.entrySet().stream().filter(entry -> entry.getValue()[2] == CUCUMBER_MOVE_EAST);
            for (Map.Entry<String, int[]> entry : stream.toList()) {
                int[] entryValue = entry.getValue();
                int newX = entryValue[0] + 1;
                if (entryValue[0] + 1 == width) {
                    newX = 0;
                }
                String key = newX + "_" + entryValue[1];
                if (!cucumberMap.containsKey(key)) {
                    entryValue[0] = newX;
                    newMap.put(key, entryValue);
                    didMove.set(true);
                } else {
                    newMap.put(entry.getKey(), entryValue);
                }
                keysToRemove.add(entry.getKey());
            }
            for (String key : keysToRemove) {
                cucumberMap.remove(key);
            }
            for (Map.Entry<String, int[]> newEntry : newMap.entrySet()) {
                cucumberMap.put(newEntry.getKey(), newEntry.getValue());
            }

            newMap.clear();
            keysToRemove.clear();

            stream = cucumberMap.entrySet().stream().filter(entry -> entry.getValue()[2] == CUCUMBER_MOVE_SOUTH);
            for (Map.Entry<String, int[]> entry : stream.toList()) {
                int[] entryValue = entry.getValue();
                int newY = entryValue[1] + 1;
                if (entryValue[1] + 1 == height) {
                    newY = 0;
                }
                String key = entryValue[0] + "_" + newY;
                if (!cucumberMap.containsKey(key)) {
                    entryValue[1] = newY;
                    if (newMap.containsKey(key)) {
                        throw new AdventOfCodeException("ERR");
                    }
                    newMap.put(key, entryValue);
                    didMove.set(true);
                } else {
                    newMap.put(entry.getKey(), entryValue);
                }
                keysToRemove.add(entry.getKey());
            }

            for (String key : keysToRemove) {
                cucumberMap.remove(key);
            }
            for (Map.Entry<String, int[]> newEntry : newMap.entrySet()) {
                cucumberMap.put(newEntry.getKey(), newEntry.getValue());
            }

            newMap.clear();
            keysToRemove.clear();

            count++;
        }


        
        setSolution1(count);
        setSolution2("@todo");
    }
}
