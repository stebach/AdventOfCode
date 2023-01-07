package li.ste.adventofcode.year2020;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.utils.RegexResultRecipient;

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

    private class PasswordEntry implements RegexResultRecipient {
        private String password;
        private int minCount;
        private int maxCount;
        private char character;

        @Override
        public void setRegexResult(String[] listEntry) {
            minCount = Integer.parseInt(listEntry[0]);
            maxCount = Integer.parseInt(listEntry[1]);
            character = listEntry[2].charAt(0);
            password = listEntry[3];
        }

        public boolean isValid() {
            long count = password.chars().filter(c -> c == character).count();
            return count >= minCount && count <= maxCount;
        }

        public boolean isValid2() {
            return (password.charAt(minCount-1) == character ? 1 : 0) + (password.charAt(maxCount-1) == character ? 1 : 0) == 1;
        }
    }
}
