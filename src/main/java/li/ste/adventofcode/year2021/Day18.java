package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.year2021.day18.SnailfishNumber;

import java.util.List;

public class Day18 extends Day {
    public static void main(String[] args) {
        Day day = new Day18(new InputProvider());
        day.solvePuzzles();
    }

    public Day18(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        List<String> data = getData();
        SnailfishNumber number = new SnailfishNumber(data.get(0));
        for (int i=1;i<data.size(); i++) {
            number = number.add(new SnailfishNumber(data.get(i)));
        }
        setSolution1(number.getMagnitude());

        int maxMagnitude = Integer.MIN_VALUE;
        for (int i=0;i<data.size()-1; i++) {
            for (int j=1;j<data.size(); j++) {
                int mag1 = new SnailfishNumber(data.get(i)).add(new SnailfishNumber(data.get(j))).getMagnitude();
                int mag2 = new SnailfishNumber(data.get(j)).add(new SnailfishNumber(data.get(i))).getMagnitude();

                if (mag1 > maxMagnitude) {
                    maxMagnitude = mag1;
                }
                if (mag2 > maxMagnitude) {
                    maxMagnitude = mag2;
                }
            }
        }


        setSolution2(maxMagnitude);
    }
}
