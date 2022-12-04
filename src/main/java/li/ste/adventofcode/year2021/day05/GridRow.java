package li.ste.adventofcode.year2021.day05;

import java.util.ArrayList;
import java.util.List;

public class GridRow {
    private final List<Integer> columns = new ArrayList<>();
    private int reachedTwo;

    public void add(int column) {
        while (columns.size() <= column) {
            columns.add(0);
        }
        int newVal = columns.get(column) + 1;
        columns.set(column, newVal);
        if (newVal == 2) {
            reachedTwo += 1;
        }
    }

    public int getReachedTwo() {
        return reachedTwo;
    }
}
