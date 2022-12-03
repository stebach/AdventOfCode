package li.ste.adventofcode2022.days;

import li.ste.adventofcode2022.utils.AdventOfCodeException;
import li.ste.adventofcode2022.utils.Day;
import li.ste.adventofcode2022.utils.InputProvider;

import java.util.List;

public class Day03 extends Day {
    public Day03(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        List<String> data = getData();

        int solution1 = 0;
        int solution2 = 0;

        for (int i=0; i<data.size(); i++) {
            String rucksackContents = data.get(i);
            String compartment1 = rucksackContents.substring(0, rucksackContents.length() / 2);
            String compartment2 = rucksackContents.substring(rucksackContents.length() / 2);

            char item = searchCommonItem(compartment1, new String[] { compartment2 });
            solution1 += priorityForItem(item);

            if (i % 3 == 0) {
                char badgeItm = searchCommonItem(rucksackContents, new String[] {
                        data.get(i + 1),
                        data.get(i + 2)
                });
                solution2 += priorityForItem(badgeItm);
            }
        }
        setSolution1(solution1);
        setSolution2(solution2);
    }

    private char searchCommonItem(String first, String[] others) {
        for (char item : first.toCharArray()) {
            boolean wrongItem = false;
            for (String other : others) {
                if (!other.contains(item+"")) {
                    wrongItem = true;
                    break;
                }
            }
            if (!wrongItem) {
                return item;
            }
        }
        throw new AdventOfCodeException("no matching item found");
    }

    private int priorityForItem(char item) {
        if (item < 'a') {
            return item - 'A' + 27;
        } else {
            return item - 'a' + 1;
        }
    }
}
