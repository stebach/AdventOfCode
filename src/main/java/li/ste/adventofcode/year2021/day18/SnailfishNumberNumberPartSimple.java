package li.ste.adventofcode.year2021.day18;

public class SnailfishNumberNumberPartSimple extends SnailfishNumberNumberPart {
    private int value;

    public SnailfishNumberNumberPartSimple(int value) {
        super();
        this.value = value;
    }

    @Override
    public String toString() {
        return String.valueOf(value);
    }

    @Override
    public boolean shouldExplode() {
        return false;
    }

    @Override
    public boolean shouldSplit() {
        return value > 9;
    }

    @Override
    public int getMagnitude() {
        return getValue();
    }

    public int getValue() {
        return value;
    }

    public void increaseValue(int addedValue) {
        value += addedValue;
    }
}
