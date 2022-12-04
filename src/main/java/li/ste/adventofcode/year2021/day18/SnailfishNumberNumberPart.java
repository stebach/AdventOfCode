package li.ste.adventofcode.year2021.day18;

public abstract class SnailfishNumberNumberPart extends Parentable {
    private int level;

    void setLevel(int level) {
        this.level = level;
    }


    public abstract boolean shouldExplode();

    protected int getLevel() {
        return level;
    }

    public abstract boolean shouldSplit();

    public abstract int getMagnitude();
}
