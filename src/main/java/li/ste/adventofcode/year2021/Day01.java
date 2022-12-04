package li.ste.adventofcode.year2021;

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
        setSolution1(getIncreaseCount(1));
        setSolution2(getIncreaseCount(3));
    }

    private int getIncreaseCount(int numbers) {
        List<Integer> intData = getIntData();

        int lastNr = -1000;
        int increased = 0;

        for (int i=numbers-1; i < intData.size(); i++) {
            int nr = 0;
            for (int n=0; n<numbers; n++) {
                nr += intData.get(i-n);
            }
            if (lastNr > -1000 && lastNr < nr) {
                increased += 1;
            }
            lastNr = nr;
        }


        return increased;
    }
}
