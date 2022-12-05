package li.ste.adventofcode.year2020.day03;

import java.util.ArrayList;
import java.util.List;

public class Grid {
    List<char[]> rows = new ArrayList<>();
    public void addRow(String row) {
        rows.add(row.toCharArray());
    }

    public int getHeight() {
        return rows.size();
    }

    public boolean hasTreeAt(int x, int y) {
        if (y >= rows.size()) {
            return false;
        }
        char[] row = rows.get(y);
        char check = row[x % row.length];
        return check == '#';
    }
}
