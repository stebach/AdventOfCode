package li.ste.adventofcode.year2022;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Day01 extends Day {
    public static void main(String[] args) {
        Day day = new Day01(new InputProvider());
        day.solvePuzzles();
    }

    public Day01(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        List<String> data = getData();

        List<Integer> numbers = new ArrayList<>();
        int currentNumber = 0;
        for (String row : data) {
            if (row.length() > 0) {
                currentNumber += Integer.parseInt(row);
            } else {
                numbers.add(currentNumber);
                currentNumber = 0;
            }
        }
        numbers.add(currentNumber);

        Collections.sort(numbers);
        Collections.reverse(numbers);

        setSolution1(numbers.get(0));
        setSolution2(numbers.get(0) + numbers.get(1) + numbers.get(2));
    }
}
