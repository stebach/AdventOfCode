package li.ste.adventofcode.year2019;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.*;

public class Day06 extends Day {
    public static void main(String[] args) {
        Day day = new Day06(new InputProvider());
        day.solvePuzzles();
    }

    public Day06(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        Scanner scanner = getScanner();
        Map<String, List<String>> directOrbits = new HashMap<>();
        while (scanner.hasNextLine()) {
            String[] orbit = scanner.nextLine().split("\\)");
            directOrbits.putIfAbsent(orbit[0], new ArrayList<>());
            directOrbits.get(orbit[0]).add(orbit[1]);
        }

        Map<String, Integer> numberOfOrbits = new HashMap<>();
        Map<String, String> orbitPaths = new HashMap<>();
        calcNumberOfOrbits(directOrbits, "COM", numberOfOrbits, 0, orbitPaths, "");



        setSolution1(numberOfOrbits.values().stream().mapToInt(Integer::intValue).sum());

        List<String> myPath = new ArrayList<>(Arrays.stream(orbitPaths.get("YOU").substring(1).split("-")).toList());
        List<String> santaPath = new ArrayList<>(Arrays.stream(orbitPaths.get("SAN").substring(1).split("-")).toList());

        while (!myPath.isEmpty() && !santaPath.isEmpty() && myPath.get(0).equals(santaPath.get(0))) {
            myPath.remove(0);
            santaPath.remove(0);
        }

        setSolution2(myPath.size() + santaPath.size());
    }

    private void calcNumberOfOrbits(Map<String, List<String>> directOrbits, String currentMass, Map<String, Integer> numberOfOrbits, int previousOrbits, Map<String, String> orbitPaths, String prevPath) {
        numberOfOrbits.put(currentMass, previousOrbits);
        orbitPaths.put(currentMass, prevPath);
        if (directOrbits.containsKey(currentMass)) {
            for (String nextMass : directOrbits.get(currentMass)) {
                calcNumberOfOrbits(directOrbits, nextMass, numberOfOrbits, previousOrbits + 1, orbitPaths, prevPath + "-" + currentMass);
            }
        }
    }
}
