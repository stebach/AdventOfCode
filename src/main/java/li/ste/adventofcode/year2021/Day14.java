package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Day14 extends Day {
    private Map<String, Long> bonds;
    private Map<String, Long> elements;
    private Map<String, Rule> rules;

    public static void main(String[] args) {
        Day day = new Day14(new InputProvider());
        day.solvePuzzles();
    }

    public Day14(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        List<String> data = getData();

        char[] polymer = data.get(0).toCharArray();
        bonds = new HashMap<>();
        elements = new HashMap<>();
        for (int i=0; i< polymer.length; i++) {
            elements.computeIfPresent("" + polymer[i], (k, v) -> v + 1);
            elements.putIfAbsent("" + polymer[i], 1L);
            if (i > 0) {
                String key = "" + polymer[i-1] + polymer[i];
                bonds.computeIfPresent(key, (k, v) -> v + 1);
                bonds.putIfAbsent(key, 1L);
            }
        }

        rules = new HashMap<>();
        for (int i=2; i<data.size(); i++) {
            String[] parts = data.get(i).split(" -> ");

            rules.put(parts[0], new Rule(parts[0], parts[1].toCharArray()[0]));
        }

        doRuns(10);

        setSolution1(getMaximumElements() - getMinimumElements());

        doRuns(30);

        setSolution2(getMaximumElements() - getMinimumElements());

    }

    private long getMinimumElements() {
        long retVal = Long.MAX_VALUE;
        for (Map.Entry<String, Long> entry : elements.entrySet()) {
            if (entry.getValue() < retVal) {
                retVal = entry.getValue();
            }
        }
        return retVal;
    }

    private long getMaximumElements() {
        long retVal = Long.MIN_VALUE;
        for (Map.Entry<String, Long> entry : elements.entrySet()) {
            if (entry.getValue() > retVal) {
                retVal = entry.getValue();
            }
        }
        return retVal;
    }

    private void doRuns(int runs) {
        for (int i=0; i<runs; i++) {
            Map<String, Long> newBonds = new HashMap<>(bonds);
            for(Map.Entry <String, Rule> rule : rules.entrySet()) {
                rule.getValue().work(bonds, newBonds, elements);
            }
            bonds = newBonds;
        }
    }

    private class Rule {
        private final String[] newKeys;
        private final char newElement;
        private final String oldKey;

        public Rule(String oldBond, char newElement) {
            newKeys = new String[] {
                    "" + oldBond.charAt(0) + newElement,
                    "" + newElement + oldBond.charAt(1)
            };
            this.newElement = newElement;
            this.oldKey = oldBond;
        }

        public void work(Map<String, Long> bonds, Map<String, Long> newBonds, Map<String, Long> elements) {
            newBonds.putIfAbsent(newKeys[0], 0L);
            newBonds.putIfAbsent(newKeys[1], 0L);
            newBonds.putIfAbsent(oldKey, 0L);
            bonds.putIfAbsent(oldKey, 0L);
            elements.putIfAbsent("" + newElement, 0L);

            Long count = bonds.get(oldKey);

            newBonds.compute(newKeys[0], (k, v) -> v + count);
            newBonds.compute(newKeys[1], (k, v) -> v + count);
            newBonds.compute(oldKey, (k, v) -> v - count);
            elements.compute("" + newElement, (k, v) -> v + count);
        }
    }
}
