package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.year2021.day04.Card;

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
}
