package li.ste.adventofcode.year2022;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.year2022.day04.SectionRangePair;

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

}