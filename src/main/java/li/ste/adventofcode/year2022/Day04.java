package li.ste.adventofcode.year2022;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.utils.RegexResultRecipient;

import java.util.List;

public class Day04 extends Day {
    public static void main(String[] args) {
        Day day = new Day04(new InputProvider());
        day.solvePuzzles();
    }

    public Day04(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        List<SectionRangePair> data = getRegexData("^([0-9]+)-([0-9]+),([0-9]+)-([0-9]+)$", SectionRangePair.class);

        int solution1 = 0;
        int solution2 = 0;
        for (SectionRangePair pair : data) {
            if (pair.firstContainsSecond() || pair.secondContainsFirst()) {
                solution1++;
            }
            if (pair.overlaps()) {
                solution2++;
            }
        }
        setSolution1(solution1);
        setSolution2(solution2);
    }

    private class SectionRangePair implements RegexResultRecipient {
        private int from1;
        private int to1;
        private int from2;
        private int to2;

        @Override
        public void setRegexResult(String[] listEntry) {
            from1 = Integer.parseInt(listEntry[0]);
            to1 = Integer.parseInt(listEntry[1]);
            from2 = Integer.parseInt(listEntry[2]);
            to2 = Integer.parseInt(listEntry[3]);
        }

        public boolean firstContainsSecond() {
            return from1 <= from2 && to1 >= to2;
        }

        public boolean secondContainsFirst() {
            return from2 <= from1 && to2 >= to1;
        }

        public boolean overlaps() {
            return !(to1 < from2 || from1 > to2);
        }
    }
}