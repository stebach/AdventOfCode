package li.ste.adventofcode.year2020;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.*;

public class Day17 extends Day {
    public static void main(String[] args) {
        Day day = new Day17(new InputProvider());
        day.solvePuzzles();
    }

    public Day17(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        Scanner scanner = getScanner();
        int x = 0;
        Map<String, int[]> activeCubes = new HashMap<>();
        Map<String, int[]> activeCubes2 = new HashMap<>();
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            for (int y = 0; y < line.length(); y++) {
                if (line.charAt(y) == '#') {
                    addCube(activeCubes, new int[] { x, y, 0 });
                    addCube(activeCubes2, new int[] { x, y, 0, 0 });
                }
            }
            x += 1;
        }

        Map<String, int[]> newActiveCubes = new HashMap<>();

        for (int i = 0; i < 6; i++) {
            newActiveCubes.clear();

            int minX = activeCubes.values().stream().mapToInt(r->r[0]).min().getAsInt() - 1;
            int maxX = activeCubes.values().stream().mapToInt(r->r[0]).max().getAsInt() + 1;
            int minY = activeCubes.values().stream().mapToInt(r->r[1]).min().getAsInt() - 1;
            int maxY = activeCubes.values().stream().mapToInt(r->r[1]).max().getAsInt() + 1;
            int minZ = activeCubes.values().stream().mapToInt(r->r[2]).min().getAsInt() - 1;
            int maxZ = activeCubes.values().stream().mapToInt(r->r[2]).max().getAsInt() + 1;

            for (x = minX; x <= maxX; x++) {
                for (int y = minY; y <= maxY; y++) {
                    for (int z = minZ; z <= maxZ; z++) {
                        int[] coordToTest = new int[] { x, y , z };
                        int activeNeighbors = getActiveNeighbors(activeCubes, coordToTest);
                        if (activeNeighbors == 3) {
                            addCube(newActiveCubes, coordToTest);
                        } else if (activeNeighbors == 2 && activeCubes.containsKey(coordsToString(coordToTest))) {
                            addCube(newActiveCubes, coordToTest);
                        }
                    }
                }
            }

            activeCubes.clear();
            activeCubes.putAll(newActiveCubes);

            newActiveCubes.clear();
            minX = activeCubes2.values().stream().mapToInt(r->r[0]).min().getAsInt() - 1;
            maxX = activeCubes2.values().stream().mapToInt(r->r[0]).max().getAsInt() + 1;
            minY = activeCubes2.values().stream().mapToInt(r->r[1]).min().getAsInt() - 1;
            maxY = activeCubes2.values().stream().mapToInt(r->r[1]).max().getAsInt() + 1;
            minZ = activeCubes2.values().stream().mapToInt(r->r[2]).min().getAsInt() - 1;
            maxZ = activeCubes2.values().stream().mapToInt(r->r[2]).max().getAsInt() + 1;
            int minW = activeCubes2.values().stream().mapToInt(r->r[3]).min().getAsInt() - 1;
            int maxW = activeCubes2.values().stream().mapToInt(r->r[3]).max().getAsInt() + 1;

            for (x = minX; x <= maxX; x++) {
                for (int y = minY; y <= maxY; y++) {
                    for (int z = minZ; z <= maxZ; z++) {
                        for (int w = minW; w <= maxW; w++) {
                            int[] coordToTest = new int[] { x, y , z, w };
                            int activeNeighbors = getActiveNeighbors2(activeCubes2, coordToTest);
                            if (activeNeighbors == 3) {
                                addCube(newActiveCubes, coordToTest);
                            } else if (activeNeighbors == 2 && activeCubes2.containsKey(coordsToString(coordToTest))) {
                                addCube(newActiveCubes, coordToTest);
                            }
                        }
                    }
                }
            }

            activeCubes2.clear();
            activeCubes2.putAll(newActiveCubes);
        }

        setSolution1(activeCubes.size());
        setSolution2(activeCubes2.size());
    }

    private int getActiveNeighbors(Map<String, int[]> cubes, int[] coord) {
        int retVal = 0;
        for (int x = -1; x < 2; x ++) {
            for (int y = -1; y < 2; y ++) {
                for (int z = -1; z < 2; z ++) {
                    if (!(x == 0 && y == 0 && z == 0) && cubes.containsKey(coordsToString(new int[] { coord[0] + x, coord[1] + y, coord[2] + z }))) {
                        retVal += 1;
                    }
                }
            }
        }
        return retVal;
    }

    private int getActiveNeighbors2(Map<String, int[]> cubes, int[] coord) {
        int retVal = 0;
        for (int x = -1; x < 2; x ++) {
            for (int y = -1; y < 2; y ++) {
                for (int z = -1; z < 2; z ++) {
                    for (int w = -1; w < 2; w ++) {
                        if (!(x == 0 && y == 0 && z == 0 && w == 0) && cubes.containsKey(coordsToString(new int[] { coord[0] + x, coord[1] + y, coord[2] + z, coord[3] + w }))) {
                            retVal += 1;
                        }
                    }
                }
            }
        }
        return retVal;
    }

    private void addCube(Map<String, int[]> cubes, int[] cubePos) {
        cubes.put(coordsToString(cubePos), cubePos);
    }

    private String coordsToString(int[] coords) {
        return String.join(",", Arrays.stream(coords).mapToObj(Integer::toString).toList());
    }
}
