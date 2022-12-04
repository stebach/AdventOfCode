package li.ste.adventofcode.year2021.day04;

public class CardNumber {
    private final int number;
    private boolean marked = false;

    public CardNumber(int number) {
        this.number = number;
    }

    public boolean isNumber(int number) {
        if (this.number == number) {
            this.marked = true;
            return true;
        }
        return false;
    }

    public int getScore() {
        if (!this.marked) {
            return number;
        }
        return 0;
    }
}
