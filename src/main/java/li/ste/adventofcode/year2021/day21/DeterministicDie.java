package li.ste.adventofcode.year2021.day21;

public class DeterministicDie extends Die {
    int next = 0;
    int rollCount = 0;
    @Override
    public DieResult throwDie() {
        int roll = getNext() + getNext() + getNext();
        return new DieResult(roll);
    }

    @Override
    public int getRollCount() {
        return rollCount;
    }

    private int getNext() {
        next ++;
        if (next > 100) {
            next = 1;
        }
        rollCount ++;
        return next;
    }
}
