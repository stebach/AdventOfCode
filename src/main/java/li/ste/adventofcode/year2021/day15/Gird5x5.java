package li.ste.adventofcode.year2021.day15;

public class Gird5x5 extends Grid {

    @Override
    public void addRow(String row) {
        width = row.length() * 5;
        height += 1;
        int[] newRow = new int[width];
        for (int i=0; i<width / 5; i++) {
            for (int j=0; j<5; j++) {
                newRow[i + j*(width / 5)] = max9(row.charAt(i) - 48 + j);
            }
        }
        rows.add(newRow);
    }

    @Override
    public int solve() {
        for (int j=1; j<5; j++) {
            for (int i=0; i<height; i++) {
                int[] newRow = new int[width];
                for (int k=0;k<width; k++) {
                    newRow[k] = max9(rows.get(i)[k] + j);
                }
                rows.add(newRow);
            }
        }
        height *= 5;
        return super.solve();
    }

    private int max9(int nr) {
        if (nr > 9) {
            return nr - 9;
        }
        return nr;
    }
}
