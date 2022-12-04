package li.ste.adventofcode.year2021.day04;

import li.ste.adventofcode.utils.AdventOfCodeException;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Card {
    List<CardNumbers> rows = new ArrayList<>();
    List<CardNumbers> columns = new ArrayList<>();
    private boolean hasWon = false;
    private int lastNumber = 0;

    public int addLine(String string) {
        if (string.length() > 0) {
            int[] numbers = Arrays.stream(string.replace("  ", " ").split(" ")).mapToInt(Integer::parseInt).toArray();
            if (numbers.length != 5) {
                throw new AdventOfCodeException("wrong number count: " + string);
            }
            CardNumbers newCardNumbers = new CardNumbers();
            newCardNumbers.add(numbers[0]);
            newCardNumbers.add(numbers[1]);
            newCardNumbers.add(numbers[2]);
            newCardNumbers.add(numbers[3]);
            newCardNumbers.add(numbers[4]);
            rows.add(newCardNumbers);
            if (rows.size() == 1) {
                columns.add(new CardNumbers());
                columns.add(new CardNumbers());
                columns.add(new CardNumbers());
                columns.add(new CardNumbers());
                columns.add(new CardNumbers());
            }
            for (int i=0; i<5; i++) {
                columns.get(i).add(numbers[i]);
            }
        }
        return rows.size();
    }

    public void playNumber(int number) {
        if (hasWon) {
            return;
        }
        lastNumber = number;
        for (CardNumbers row : rows) {
            if (row.playNumber(number)) {
                hasWon = true;
            }
        }
        for (CardNumbers col : columns) {
            if (col.playNumber(number)) {
                hasWon = true;
            }
        }
    }

    public int getScore() {
        int sum = 0;
        for (CardNumbers row : rows) {
            sum += row.getScore();
        }
        return sum * lastNumber;
    }

    public boolean didWinWithNumber(int number) {
        return (number == lastNumber && hasWon);
    }
}
