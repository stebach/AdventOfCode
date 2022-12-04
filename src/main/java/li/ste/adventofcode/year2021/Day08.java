package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.year2021.day08.DigitsLine;

import java.util.List;

public class Day08 extends Day {
    public static void main(String[] args) {
        Day day = new Day08(new InputProvider());
        day.solvePuzzles();
    }

    public Day08(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        List<DigitsLine> digitsLines = getRegexData("^([a-g]+) ([a-g]+) ([a-g]+) ([a-g]+) ([a-g]+) ([a-g]+) ([a-g]+) ([a-g]+) ([a-g]+) ([a-g]+) \\| ([a-g]+) ([a-g]+) ([a-g]+) ([a-g]+)$", DigitsLine.class);

        int countOf1478 = 0;
        int totalSum = 0;
        for (DigitsLine digitsLine : digitsLines) {
            digitsLine.solve();

            countOf1478 += digitsLine.getCountOf1478();
            totalSum += digitsLine.getNumber();
        }

        setSolution1(countOf1478);

        setSolution2(totalSum);
    }
}
