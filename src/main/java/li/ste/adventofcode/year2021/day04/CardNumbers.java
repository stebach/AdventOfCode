package li.ste.adventofcode.year2021.day04;

import java.util.ArrayList;
import java.util.List;

public class CardNumbers {
    private final List<CardNumber> numbers = new ArrayList<>();
    private int hits = 0;

    public void add(int number) {
        numbers.add(new CardNumber(number));
    }

    public boolean playNumber(int number) {
        for (CardNumber cardNumber : numbers) {
            if (cardNumber.isNumber(number)) {
                hits += 1;
            }
        }
        return hits == 5;
    }

    public int getScore() {
        int retVal = 0;
        for (CardNumber cardNumber : numbers) {
            retVal += cardNumber.getScore();
        }
        return retVal;
    }
}
