package li.ste.adventofcode.year2019;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.*;

public class Day21 extends Day {
    public static void main(String[] args) {
        Day day = new Day21(new InputProvider());
        day.solvePuzzles();
    }

    public Day21(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        Scanner scanner = getScanner();
        while (scanner.hasNextLine()) {
            System.out.println(scanner.nextLine());
        }

        setSolution1("@todo");
        setSolution2("@todo");
    }
}
