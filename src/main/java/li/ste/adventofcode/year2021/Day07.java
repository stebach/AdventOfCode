package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
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
        List<Integer> positions = Arrays.stream(getData().get(0).split(",")).map(Integer::valueOf).toList();
        int minPosition = Collections.min(positions);
        int maxPosition = Collections.max(positions);
        List<Integer> posArray = new ArrayList<>();

        while(posArray.size() <= maxPosition) {
            posArray.add(0);
        }

        for (int pos : positions) {
            posArray.set(pos, posArray.get(pos) + 1);
        }

        int minValue = Integer.MAX_VALUE;
        int minValue2 = Integer.MAX_VALUE;
        for (int i=minPosition; i<=maxPosition; i++) {
            int checkValue = 0;
            int checkValue2 = 0;
            for (int j=minPosition; j<=maxPosition; j++) {
                checkValue += Math.abs(i-j) * posArray.get(j);
                checkValue2 += getTriangularNumber(Math.abs(i-j)) * posArray.get(j);
            }
            if (checkValue < minValue) {
                minValue = checkValue;
            }
            if (checkValue2 < minValue2) {
                minValue2 = checkValue2;
            }
        }

        setSolution1(minValue);
        setSolution2(minValue2);
    }

    protected int getTriangularNumber(int nr) {
        return (nr * (nr + 1)) / 2;
    }
}
