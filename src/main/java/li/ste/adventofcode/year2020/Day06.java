package li.ste.adventofcode.year2020;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.*;
import java.util.concurrent.atomic.AtomicInteger;

public class Day06 extends Day {
    public static void main(String[] args) {
        Day day = new Day06(new InputProvider());
        day.solvePuzzles();
    }

    public Day06(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        List<String> data = getData();
        data.add("");
        Map<Character, Integer> groupAnswers = new HashMap<>();

        int solution1 = 0;
        int solution2 = 0;
        AtomicInteger personCount = new AtomicInteger();
        for (String row : data) {
            if (row.length() > 0) {
                personCount.incrementAndGet();
                char[] groupChars = row.toCharArray();
                for (char groupChar : groupChars) {
                    groupAnswers.putIfAbsent(groupChar, 0);
                    groupAnswers.compute(groupChar, (k,v) -> v += 1);
                }
            } else {
                solution2 += groupAnswers.entrySet().stream().filter(entry -> entry.getValue() == personCount.intValue()).count();
                solution1 += groupAnswers.size();
                groupAnswers.clear();
                personCount.set(0);
            }
        }

        setSolution1(solution1);
        setSolution2(solution2);
    }
}
