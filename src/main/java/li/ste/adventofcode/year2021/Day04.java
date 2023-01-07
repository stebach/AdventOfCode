package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.AdventOfCodeException;
import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Day04 extends Day {
    public static void main(String[] args) {
        Day day = new Day04(new InputProvider());
        day.solvePuzzles();
    }

    public Day04(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        List<String> data = getData();
        int[] numbers = Arrays.stream(data.get(0).split(",")).mapToInt(Integer::parseInt).toArray();

        List<Card> cards = new ArrayList<>();

        prepareCards(cards, data);

        List<Card> winners = playNumbers(cards, numbers);

        setSolution1(winners.get(0).getScore());
        setSolution2(winners.get(winners.size()-1).getScore());
    }

    private List<Card> playNumbers(List<Card> cards, int[] numbers) {
        List<Card> winner = new ArrayList<>();
        for (int number : numbers) {
            for (Card card : cards) {
                card.playNumber(number);
                if (card.didWinWithNumber(number)) {
                    winner.add(card);
                }
            }
        }

        return winner;
    }

    private void prepareCards(List<Card> cards, List<String> data) {
        Card currentCard = new Card();

        for (int i=2; i<data.size(); i++) {
            if (currentCard.addLine(data.get(i).trim()) == 5) {
                cards.add(currentCard);
                currentCard = new Card();
            }
        }
    }

    private class Card {
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

    private class CardNumber {
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
}
