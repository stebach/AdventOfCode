package li.ste.adventofcode.year2021.day17;

import li.ste.adventofcode.utils.RegexResultRecipient;

public class TargetArea implements RegexResultRecipient {
    private int minX;
    private int maxX;
    private int minY;
    private int maxY;

    @Override
    public void setRegexResult(String[] listEntry) {
        minX = Integer.parseInt(listEntry[0]);
        maxX = Integer.parseInt(listEntry[1]);
        minY = Integer.parseInt(listEntry[2]);
        maxY = Integer.parseInt(listEntry[3]);
    }

    public int getMinY() {
        return minY;
    }

    public int getMaxY() {
        return maxY;
    }

    public int getMaxX() {
        return maxX;
    }
    public int getMinX() {
        return minX;
    }
}
