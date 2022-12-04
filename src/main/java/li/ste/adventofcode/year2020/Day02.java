package li.ste.adventofcode.year2020;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.year2020.day02.PasswordEntry;

import java.util.List;

public class Day02 extends Day {
    public static void main(String[] args) {
        Day day = new Day02(new InputProvider());
        day.solvePuzzles();
    }

    public Day02(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        List<PasswordEntry> data = getRegexData("^([0-9]*)-([0-9]*) ([a-z]): ([a-z]*)$", PasswordEntry.class);
        int solution1 = 0;
        int solution2 = 0;
        for (PasswordEntry entry : data) {
            if (entry.isValid()) {
                solution1++;
            }
            if (entry.isValid2()) {
                solution2++;
            }
        }
        setSolution1(solution1);
        setSolution2(solution2);
    }
}
