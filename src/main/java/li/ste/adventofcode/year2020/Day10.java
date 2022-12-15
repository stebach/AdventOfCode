package li.ste.adventofcode.year2020;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Day10 extends Day {
    public static void main(String[] args) {
        Day day = new Day10(new InputProvider());
        day.solvePuzzles();
    }

    public Day10(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        Scanner scanner = getScanner();
        List<Integer> adapters = new ArrayList<>();

        while (scanner.hasNextInt()) {
            adapters.add(scanner.nextInt());
        }
        adapters.add(0);

        adapters.sort(Integer::compareTo);

        adapters.add(adapters.get(adapters.size() - 1) + 3);

        int[] differences = new int[10];

        int last = -5;
        for (Integer adapter : adapters) {
            int diff = adapter - last;
            differences[diff] += 1;
            last = adapter;
        }

        long[] possibilities = new long[adapters.size()];
        possibilities[adapters.size()-1] = 1;
        for (int i=adapters.size()-2; i>=0; i--) {
            for (int j=i+1; j<adapters.size(); j++) {
                if (adapters.get(j) - adapters.get(i) > 3) {
                    break;
                }
                possibilities[i] += possibilities[j];
            }
        }

        setSolution1(differences[1] * differences[3]);
        setSolution2(possibilities[0]);
    }
}
