package li.ste.adventofcode.year2021.day18;

import li.ste.adventofcode.utils.AdventOfCodeException;

public class SnailfishNumberNumberPartComplex extends SnailfishNumberNumberPart {

    @Override
    public String toString() {
        return "[" + getChild(0).toString() + "," + getChild(1).toString() +
                "]";
    }

    @Override
    public boolean shouldExplode() {
        return this.getLevel() > 3;
    }

    @Override
    public boolean shouldSplit() {
        return false;
    }

    @Override
    public int getMagnitude() {
        return ((SnailfishNumberNumberPart)getChild(0)).getMagnitude() * 3 + ((SnailfishNumberNumberPart)getChild(1)).getMagnitude() * 2;
    }

    public int leftValue() {
        if (getChild(0).getClass() != SnailfishNumberNumberPartSimple.class) {
            throw new AdventOfCodeException("UNEXPECTED CLASS");
        }
        return ((SnailfishNumberNumberPartSimple)getChild(0)).getValue();
    }

    public int rightValue() {
        if (getChild(1).getClass() != SnailfishNumberNumberPartSimple.class) {
            throw new AdventOfCodeException("UNEXPECTED CLASS");
        }
        return ((SnailfishNumberNumberPartSimple)getChild(1)).getValue();
    }
}
