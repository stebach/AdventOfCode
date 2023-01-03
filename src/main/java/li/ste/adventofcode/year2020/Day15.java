package li.ste.adventofcode.year2020;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Day15 extends Day {
    public static void main(String[] args) {
        Day day = new Day15(new InputProvider());
        day.solvePuzzles();
    }

    public Day15(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        Scanner scanner = getScanner();
        int[] startNumbers = Arrays.stream(scanner.nextLine().split(",")).mapToInt(Integer::parseInt).toArray();
        int round = 1;

        Map<Integer, Integer> lastOccurence = new HashMap<>();

        while (round <= startNumbers.length) {
            lastOccurence.put(startNumbers[round-1], round);
            round++;
        }

        int solution1 = 0;

        int nextNumber = 0;
        int currentNumber = 0;
        while (round < 30000001) {
            currentNumber = nextNumber;
            if (lastOccurence.containsKey(nextNumber)) {
                nextNumber = round - lastOccurence.get(nextNumber);
            } else {
                nextNumber = 0;
            }
            lastOccurence.put(currentNumber, round);

            if (round == 2020) {
                solution1 = currentNumber;
            }

            round++;
        }

        setSolution1(solution1);
        setSolution2(currentNumber);
    }
}
