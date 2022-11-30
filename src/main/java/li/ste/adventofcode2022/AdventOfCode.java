package li.ste.adventofcode2022;

import li.ste.adventofcode2022.days.Day01;
import li.ste.adventofcode2022.days.Day02;
import li.ste.adventofcode2022.days.Day03;
import li.ste.adventofcode2022.days.Day04;
import li.ste.adventofcode2022.days.Day05;
import li.ste.adventofcode2022.days.Day06;
import li.ste.adventofcode2022.days.Day07;
import li.ste.adventofcode2022.days.Day08;
import li.ste.adventofcode2022.days.Day09;
import li.ste.adventofcode2022.days.Day10;
import li.ste.adventofcode2022.days.Day11;
import li.ste.adventofcode2022.days.Day12;
import li.ste.adventofcode2022.days.Day13;
import li.ste.adventofcode2022.days.Day14;
import li.ste.adventofcode2022.days.Day15;
import li.ste.adventofcode2022.days.Day16;
import li.ste.adventofcode2022.days.Day17;
import li.ste.adventofcode2022.days.Day18;
import li.ste.adventofcode2022.days.Day19;
import li.ste.adventofcode2022.days.Day20;
import li.ste.adventofcode2022.days.Day21;
import li.ste.adventofcode2022.days.Day22;
import li.ste.adventofcode2022.days.Day23;
import li.ste.adventofcode2022.days.Day24;
import li.ste.adventofcode2022.days.Day25;
import li.ste.adventofcode2022.utils.Day;
import li.ste.adventofcode2022.utils.InputProvider;

public class AdventOfCode {
    public static void main(String[] args) {
        InputProvider inputProvider = new InputProvider();
        Day[] puzzles = new Day[] {
            new Day01(inputProvider),
            new Day02(inputProvider),
            new Day03(inputProvider),
            new Day04(inputProvider),
            new Day05(inputProvider),
            new Day06(inputProvider),
            new Day07(inputProvider),
            new Day08(inputProvider),
            new Day09(inputProvider),
            new Day10(inputProvider),
            new Day11(inputProvider),
            new Day12(inputProvider),
            new Day13(inputProvider),
            new Day14(inputProvider),
            new Day15(inputProvider),
            new Day16(inputProvider),
            new Day17(inputProvider),
            new Day18(inputProvider),
            new Day19(inputProvider),
            new Day20(inputProvider),
            new Day21(inputProvider),
            new Day22(inputProvider),
            new Day23(inputProvider),
            new Day24(inputProvider),
            new Day25(inputProvider),
        };

        int start = 0;
        if (args.length > 0) {
            start = Integer.parseInt(args[0]) - 1;
        }

        for (int i=start; i<puzzles.length; i++) {
            puzzles[i].solvePuzzles();
        }
    }
}
