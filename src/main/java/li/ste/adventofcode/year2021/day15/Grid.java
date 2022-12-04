package li.ste.adventofcode.year2021.day15;

import java.util.ArrayList;
import java.util.List;

public class Grid {

    List<int[]> rows = new ArrayList<>();
    protected int width;
    protected int height;

    public void addRow(String row) {
        width = row.length();
        height += 1;
        int[] newRow = new int[width];
        for (int i=0; i<width; i++) {
            newRow[i] = row.charAt(i) - 48;
        }
        rows.add(newRow);
    }

    public int solve() {
        //get baseline
        DijkstraSovler dijkstraSovler = new DijkstraSovler();

        return dijkstraSovler.solve(this);
    }

    public int getWidth() {
        return width;
    }
    public int getHeight() {
        return height;
    }

    public int getNumber(int x, int y) {
        return rows.get(y)[x];
    }
}
