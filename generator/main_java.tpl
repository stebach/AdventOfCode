package li.ste.adventofcode.year{{YEAR}};

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.*;

public class Day{{DAY}} extends Day {
    public static void main(String[] args) {
        Day day = new Day{{DAY}}(new InputProvider());
        day.solvePuzzles();
    }

    public Day{{DAY}}(InputProvider provider) {
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
