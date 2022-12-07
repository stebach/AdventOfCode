package li.ste.adventofcode.year2020;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.year2020.day07.LuggageRule;

import java.util.List;

public class Day07 extends Day {
    public static void main(String[] args) {
        Day day = new Day07(new InputProvider());
        day.solvePuzzles();
    }

    public Day07(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        List<LuggageRule> data = getRegexData("^(.*?) bags contain (.*)\\.$", LuggageRule.class);
        String checkFor = "shiny gold";
        int solution1 = 0;
        for (LuggageRule luggageRule : data) {
            if (luggageRule.canHold(checkFor, data)) {
                solution1++;
            }
        }
        setSolution1(solution1);
        setSolution2(data.stream().filter(r -> r.getColor().equals(checkFor)).findFirst().get().getContentCount(data));
    }
}
