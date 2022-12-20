package li.ste.adventofcode.year2022;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Day20 extends Day {

    record SequenceNumber ( long number, long number2, int id) {}

    public static void main(String[] args) {
        Day day = new Day20(new InputProvider());
        day.solvePuzzles();
    }

    public Day20(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        List<SequenceNumber> origNumbers = new ArrayList<>();

        Scanner scanner = getScanner();
        int i = 0;
        SequenceNumber zeroNumber = null;
        while (scanner.hasNextInt()) {
            int nextInt = scanner.nextInt();
            SequenceNumber nextNumber = new SequenceNumber(nextInt, nextInt * 811589153L, i);
            if (nextNumber.number == 0) {
                zeroNumber = nextNumber;
            }
            origNumbers.add(nextNumber);
            i++;
        }
        List<SequenceNumber> numbers = new ArrayList<>(origNumbers);


        mix(origNumbers, numbers, false);
        int index = numbers.indexOf(zeroNumber);
        long solution1 = numbers.get((index+1000) % numbers.size()).number
                + numbers.get((index+2000) % numbers.size()).number
                + numbers.get((index+3000) % numbers.size()).number;

        numbers.clear();
        numbers.addAll(origNumbers);
        for (int j = 0; j < 10; j++) {
            mix(origNumbers, numbers, true);
        }

        index = numbers.indexOf(zeroNumber);
        long solution2 = numbers.get((index+1000) % numbers.size()).number2
                + numbers.get((index+2000) % numbers.size()).number2
                + numbers.get((index+3000) % numbers.size()).number2;


        setSolution1(solution1);
        setSolution2(solution2);
    }

    private void mix(List<SequenceNumber> origNumbers, List<SequenceNumber> numbers, boolean part2) {
        for (SequenceNumber origNumber : origNumbers) {
            int idx = numbers.indexOf(origNumber);
            numbers.remove(idx);

            int pos = (int)(((idx + (part2 ? origNumber.number2 : origNumber.number)) % numbers.size()) + numbers.size()) % numbers.size();
            numbers.add(pos, origNumber);
        }
    }

}
