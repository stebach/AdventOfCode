package li.ste.adventofcode.year2021.day22;

import li.ste.adventofcode.utils.RegexResultRecipient;

public class ReactorRebootCommand implements RegexResultRecipient {
    private boolean on;
    private int fromX;
    private int toX;
    private int fromY;
    private int toY;
    private int fromZ;
    private int toZ;
    private static boolean doLimit = true;

    public static void setLimit(boolean b) {
        doLimit = b;
    }

    @Override
    public void setRegexResult(String[] listEntry) {
        on = listEntry[0].equals("on");
        int x1 = Integer.parseInt(listEntry[1]);
        int x2 = Integer.parseInt(listEntry[2]);
        int y1 = Integer.parseInt(listEntry[3]);
        int y2 = Integer.parseInt(listEntry[4]);
        int z1 = Integer.parseInt(listEntry[5]);
        int z2 = Integer.parseInt(listEntry[6]);

        fromX = Math.min(x1, x2);
        toX = Math.max(x1, x2);
        fromY = Math.min(y1, y2);
        toY = Math.max(y1, y2);
        fromZ = Math.min(z1, z2);
        toZ = Math.max(z1, z2);
    }

    public int getFromX() {
        if (doLimit) {
            return Math.max(-50,fromX);
        }
        return fromX;
    }

    public int getToX() {
        if (doLimit) {
            return Math.min(50,toX);
        }
        return toX;
    }

    public int getFromY() {
        if (doLimit) {
            return Math.max(-50,fromY);
        }
        return fromY;
    }

    public int getToY() {
        if (doLimit) {
            return Math.min(50,toY);
        }
        return toY;
    }

    public int getFromZ() {
        if (doLimit) {
            return Math.max(-50,fromZ);
        }
        return fromZ;
    }

    public int getToZ() {
        if (doLimit) {
            return Math.min(50,toZ);
        }
        return toZ;
    }

    public boolean isOn() {
        return on;
    }
}
