package li.ste.adventofcode.year2020;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.*;

public class Day22 extends Day {
    public static void main(String[] args) {
        Day day = new Day22(new InputProvider());
        day.solvePuzzles();
    }

    public Day22(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        Scanner scanner = getScanner();
        scanner.nextLine();
        List<Integer> originalDeck1 = new ArrayList<>();
        List<Integer> originalDeck2 = new ArrayList<>();
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            if (line.length() == 0) {
                originalDeck1.addAll(originalDeck2);
                originalDeck2.clear();
                scanner.nextLine();
            } else {
                originalDeck2.add(Integer.parseInt(line));
            }
        }

        List<Integer> deck1 = new ArrayList<>(originalDeck1);
        List<Integer> deck2 = new ArrayList<>(originalDeck2);

        while (!deck1.isEmpty() && !deck2.isEmpty()) {
            int card1 = deck1.remove(0);
            int card2 = deck2.remove(0);
            if (card1 > card2) {
                deck1.add(card1);
                deck1.add(card2);
            } else {
                deck2.add(card2);
                deck2.add(card1);
            }
        }

        int solution1 = 0;
        List<Integer> deck = new ArrayList<>(deck1);
        if (deck.isEmpty()) {
            deck.addAll(deck2);
        }
        for (int i = 0; i < deck.size(); i++) {
            solution1 += (deck.size() - i) * deck.get(i);
        }

        setSolution1(solution1);


        deck1 = new ArrayList<>(originalDeck1);
        deck2 = new ArrayList<>(originalDeck2);

        playGame(deck1, deck2);

        int solution2 = 0;
        deck = new ArrayList<>(deck1);
        if (deck.isEmpty()) {
            deck.addAll(deck2);
        }
        for (int i = 0; i < deck.size(); i++) {
            solution2 += (deck.size() - i) * deck.get(i);
        }

        setSolution2(solution2);
    }

    private void playGame(List<Integer> deck1, List<Integer> deck2) {
        Set<String> playedGames = new HashSet<>();
        while (!deck1.isEmpty() && !deck2.isEmpty()) {
            String key = String.join(",", deck1.stream().map(Object::toString).toList()) + "|" + String.join(",", deck2.stream().map(Object::toString).toList());
            if (!playedGames.add(key)) {
                return;
            }

            int card1 = deck1.remove(0);
            int card2 = deck2.remove(0);

            boolean player1won = false;
            if (deck1.size() >= card1 && deck2.size() >= card2) {
                List<Integer> subDeck1 = new ArrayList<>(deck1.subList(0,card1));
                List<Integer> subDeck2 = new ArrayList<>(deck2.subList(0,card2));
                playGame(subDeck1, subDeck2);
                if (!subDeck1.isEmpty()) {
                    player1won = true;
                }
            } else if (card1 > card2) {
                player1won = true;
            }

            if (player1won) {
                deck1.add(card1);
                deck1.add(card2);
            } else {
                deck2.add(card2);
                deck2.add(card1);
            }

        }
    }
}
