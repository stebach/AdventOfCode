package li.ste.adventofcode.year2020;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Day23 extends Day {
    public static void main(String[] args) {
        Day day = new Day23(new InputProvider());
        day.solvePuzzles();
    }

    public Day23(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        Scanner scanner = getScanner();
        String line = scanner.nextLine();


        List<Integer> cups = line.chars().mapToObj(r->Integer.valueOf(r-'0')).toList();
        int[] nextCup = new int[cups.size() + 1];
        for (int i = 0; i < cups.size(); i++) {
            nextCup[cups.get(i)] = i + 1 == cups.size() ? 0 : i + 1;
        }

        moveCups(cups, nextCup, 100);
        setSolution1(formatResult(cups, nextCup));

        cups = new ArrayList<>(line.chars().mapToObj(r->Integer.valueOf(r-'0')).toList());
        for (int i = 10; i <= 1_000_000 ; i++) {
            cups.add(i);
        }
        nextCup = new int[cups.size() + 1];
        for (int i = 0; i < cups.size(); i++) {
            nextCup[cups.get(i)] = i + 1 == cups.size() ? 0 : i + 1;
        }

        moveCups(cups, nextCup, 10_000_000);

        int num1 = cups.get(nextCup[1]);
        int num2 = cups.get(nextCup[num1]);

        long solution2 = (long)num1 * num2;

        setSolution2(solution2);
    }

    public void moveCups(List<Integer> cups, int[] nextCup, int moves) {
        int idx = 0;
        for (int i = 0; i < moves; i++) {
            int number = cups.get(idx);
            int[] move = new int[3];
            for (int j = 0; j < 3; j++) {
                move[j] = nextCup[number];
                number = cups.get(move[j]);
            }
            // remove 3
            nextCup[cups.get(idx)] = nextCup[number];

            int destinationNumber = cups.get(idx) - 1;
            while (destinationNumber < 1 || destinationNumber > cups.size() || cups.get(move[0]) == destinationNumber || cups.get(move[1]) == destinationNumber || cups.get(move[2]) == destinationNumber) {
                destinationNumber -= 1;

                if (destinationNumber < 1) {
                    destinationNumber = cups.size();
                }
            }

            nextCup[cups.get(move[2])] = nextCup[destinationNumber];
            nextCup[destinationNumber] = move[0];

            idx = nextCup[cups.get(idx)];
        }
    }

    public String formatResult(List<Integer> cups, int[] nextCup) {
        int start = nextCup[1];
        StringBuilder sb = new StringBuilder();
        sb.append(cups.get(start));
        int next = nextCup[cups.get(start)];
        while (cups.get(next) != 1) {
            sb.append(cups.get(next));
            next = nextCup[cups.get(next)];
        }
        return sb.toString();
    }

    public String cupsToString(List<Integer> cups, int[] nextCupClone) {
        StringBuilder sb = new StringBuilder();
        int first = 0;
        sb.append(cups.get(first));
        int next = nextCupClone[cups.get(first)];
        while (next != first) {
            sb.append(cups.get(next));
            next = nextCupClone[cups.get(next)];
        }
        return sb.toString();
    }
}
