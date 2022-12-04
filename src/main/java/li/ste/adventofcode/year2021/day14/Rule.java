package li.ste.adventofcode.year2021.day14;

import java.util.Map;

public class Rule {
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
