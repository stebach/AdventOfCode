package li.ste.adventofcode.year2021.day05;

import java.util.ArrayList;
import java.util.List;

public class Grid {
    private final List<GridRow> gridRows = new ArrayList<>();

    public void addIfHorizontalOrVertical(Day05Entry entry) {
        if (entry.isHorizontalOrVertical()) {
            this.add(entry);
        }
    }

    private void add(Day05Entry entry) {
        List<int[]> coordinates = entry.getCoordinates();
        for (int[] coordinate : coordinates) {
            while (gridRows.size() <= coordinate[0]) {
                gridRows.add(new GridRow());
            }
            gridRows.get(coordinate[0]).add(coordinate[1]);
        }
    }

    public int getReachedTwoCount() {
        int retVal = 0;
        for (GridRow gridRow : gridRows) {
            retVal += gridRow.getReachedTwo();
        }
        return retVal;
    }

    public void addIfNotHorizontalOrVertical(Day05Entry entry) {
        if (!entry.isHorizontalOrVertical()) {
            this.add(entry);
        }
    }
}
