package li.ste.adventofcode.year2020;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.utils.RegexResultRecipient;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

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

    private class LuggageRule implements RegexResultRecipient {
        private String color;
        private final Map<String, Integer> otherBags = new HashMap<>();

        @Override
        public void setRegexResult(String[] listEntry) {
            color = listEntry[0];
            if (!"no other bags".equals(listEntry[1])) {
                String[] otherBagsArray = listEntry[1].split(", ");
                for (String otherBag : otherBagsArray) {
                    String[] parts = otherBag.split(" ");
                    this.otherBags.put(String.join(" ", Arrays.copyOfRange(parts,1,parts.length-1)), Integer.parseInt(parts[0]));
                }
            }
        }

        public boolean canHold(String checkFor, List<LuggageRule> data) {
            if (otherBags.containsKey(checkFor)) {
                return true;
            }
            for (String otherBagColor : otherBags.keySet()) {
                if (data.stream().filter(r -> r.getColor().equals(otherBagColor)).findFirst().get().canHold(checkFor, data)) {
                    return true;
                }
            }
            return false;
        }

        public Object getColor() {
            return color;
        }

        public int getContentCount(List<LuggageRule> data) {
            if (otherBags.size() == 0) {
                return 0;
            }
            int retVal = 0;
            for (Map.Entry<String, Integer> entry : otherBags.entrySet()) {
                retVal += entry.getValue()  + entry.getValue() * data.stream().filter(r -> r.getColor().equals(entry.getKey())).findFirst().get().getContentCount(data);
            }
            return retVal;
        }
    }
}
