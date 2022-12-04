package li.ste.adventofcode.year2021.day05;

import li.ste.adventofcode.utils.RegexResultRecipient;

import java.util.ArrayList;
import java.util.List;

public class Day05Entry implements RegexResultRecipient {
    private int x1;
    private int y1;
    private int x2;
    private int y2;

    @Override
    public void setRegexResult(String[] listEntry) {
        this.x1 = Integer.parseInt(listEntry[0]);
        this.y1 = Integer.parseInt(listEntry[1]);
        this.x2 = Integer.parseInt(listEntry[2]);
        this.y2 = Integer.parseInt(listEntry[3]);
    }

    public boolean isHorizontalOrVertical() {
        return x1 == x2 || y1 == y2;
    }

    public List<int[]> getCoordinates() {
        List<int[]> retVal = new ArrayList<>();

        int numbers = Math.max(Math.abs(x1-x2)+1, Math.abs(y1-y2)+1);

        int[] xNumbers = generateCoordinateNumbers(x1, x2, numbers);
        int[] yNumbers = generateCoordinateNumbers(y1, y2, numbers);

        for (int i = 0; i< numbers; i++) {
            retVal.add(new int[] { xNumbers[i], yNumbers[i] });
        }

        return retVal;
    }

    private int[] generateCoordinateNumbers(int n1, int n2, int numbers) {
        int[] nNumbers = new int[numbers];
        if (n1 == n2) {
            for (int i=0; i<numbers; i++) {
                nNumbers[i] = n1;
            }
        } else if (n1 < n2) {
            for (int i = 0; i< numbers; i++) {
                nNumbers[i] = n1 + i;
            }
        } else {
            for (int i = 0; i< numbers; i++) {
                nNumbers[i] = n1 - i;
            }
        }

        return nNumbers;
    }

}
