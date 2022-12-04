package li.ste.adventofcode.year2020;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.List;

public class Day01 extends Day {
    public static void main(String[] args) {
        Day day = new Day01(new InputProvider());
        day.solvePuzzles();
    }

    public Day01(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        List<Integer> data = getIntData();
        for (Integer number : data) {
            if (data.contains(2020-number)) {
                setSolution1(number * (2020-number));
                break;
            }
        }
        for (int i=0; i<data.size()-2; i++) {
            for (int j=i+1; j<data.size()-1; j++) {
                if (data.contains(2020-data.get(i)-data.get(j))) {
                    setSolution2(data.get(i) * data.get(j) * (2020-data.get(i)-data.get(j)));
                    break;
                }
            }
        }
    }
}
