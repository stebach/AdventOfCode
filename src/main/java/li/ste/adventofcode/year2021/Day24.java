package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.AdventOfCodeException;
import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Day24 extends Day {
    private int[] div;
    private int[] add;
    private int[] add2;

    public static void main(String[] args) {
        Day day = new Day24(new InputProvider());
        day.solvePuzzles();
    }

    public Day24(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {

        long nr = 99999999999999L;

        long start = System.currentTimeMillis();

        // index            0   1   2    3   4   5   6   7   8   9  10  11  12  13
        // group            0   1   2    2   3   3   1   4   4   5   6   6   5   0
        div = new int[] {   1,  1,  1,  26,  1, 26, 26,  1, 26,  1,  1, 26, 26, 26 };
        add = new int[] {  11, 11, 15, -14, 10,  0, -6, 13, -3, 13, 15, -2, -9, -2 };
        add2 = new int[] {  6, 14, 13,   1,  6, 13,  6,  3,  8, 14,  4,  7, 15,  1 };
        // 0 -> 13:  +6 +  -2 -> +4
        // 1 -> 6:  +14 +  -6 -> +8
        // 2 -> 3 : +13 + -14 -> -1
        // 4 -> 5:   +6 +   0 -> +6
        // 7 -> 8:   +3 +  -3 -> +0
        // 9 -> 12: +14 +  -9 -> +5
        // 10 -> 11: +4 +  -2 -> +2

        List<Long> results = new ArrayList<>();

        for (int group0 = 1; group0 <= 5; group0++) {
            int group1 = 1;
            for (int group2 = 2; group2 <= 9; group2++) {
                for (int group3 = 1; group3 <= 3; group3++) {
                    for (int group4 = 1; group4 <= 9; group4++) {
                        for (int group5 = 1; group5 <= 4; group5++) {
                            for (int group6 = 1; group6 <= 7; group6++) {
                                char[] nrToCheck = new char[] {
                                        (char)group0,
                                        (char)group1,
                                        (char)group2,
                                        (char)(group2 - 1),
                                        (char)group3,
                                        (char)(group3 + 6),
                                        (char)(group1 + 8),
                                        (char)group4,
                                        (char)group4,
                                        (char)group5,
                                        (char)group6,
                                        (char)(group6 + 2),
                                        (char)(group5 + 5),
                                        (char)(group0 + 4)
                                };
                                if (checkNr(nrToCheck)) {
                                    results.add(toReadableNr(nrToCheck));
                                }
                            }
                        }
                    }
                }
            }
        }

        Collections.sort(results);

        setSolution1(results.get(results.size()-1));
        setSolution2(results.get(0));
    }

    private long toReadableNr(char[] charArr) {
        long retVal = 0;
        for (char c : charArr) {
            retVal *= 10;
            retVal += c;
        }
        return retVal;
    }

    private boolean checkNr(char[] nr) {
        int z=0;
        for (int i=0; i<14;i++) {

            if (((z % 26) + add[i]) != nr[i]) {
                z /= div[i];
                z *= 26;
                z += (nr[i] + add2[i]);

                if (div[i] == 26) {
                    throw new AdventOfCodeException("nope!");
                }
            } else {
                z /= div[i];
            }
        }


        return z == 0;
    }
}
