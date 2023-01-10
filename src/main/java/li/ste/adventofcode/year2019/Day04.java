package li.ste.adventofcode.year2019;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day04 extends Day {
    Pattern pattern = Pattern.compile("(.)\\1{1,5}");
    public static void main(String[] args) {
        Day day = new Day04(new InputProvider());
        day.solvePuzzles();
    }

    public Day04(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        Scanner scanner = getScanner();
        int[] minMax = Arrays.stream(scanner.nextLine().split("-")).mapToInt(Integer::parseInt).toArray();
        int count = checkNumber(1, 6, "", minMax, false);

        setSolution1(count);

        count = checkNumber(1, 6, "", minMax, true);
        setSolution2(count);
    }

    private int checkNumber(int start, int len, String prefix, int[] minMax, boolean part2) {
        int count = 0;
        Matcher matcher;
        boolean lenReached = (prefix.length() == len -1);
        for (int i=start; i<10; i++) {
            if (lenReached) {
                String toCheck = prefix + i;
                int val = Integer.parseInt(toCheck);
                if (val >= minMax[0] && val <= minMax[1]) {
                    matcher = pattern.matcher(toCheck);
                    while (matcher.find()) {
                        if (!part2 || matcher.group(0).length() == 2) {
                            count += 1;
                            break;
                        }
                    }
                }
            } else {
                count += checkNumber(i, len, prefix + i, minMax, part2);
            }
        }
        return count;
    }
}
