package li.ste.adventofcode.year2020;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.Collections;
import java.util.List;

public class Day09 extends Day {
    private int preamble = 25;

    public static void main(String[] args) {
        Day day = new Day09(new InputProvider());
        day.solvePuzzles();
    }

    public Day09(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        List<Long> data = getLongData();
        long solution1 = findFirstInvalid(data);
        List<Long> contiguousSet = findContiguousSetThatAddsUpTo(data, solution1);

        setSolution1(solution1);
        setSolution2(Collections.min(contiguousSet) + Collections.max(contiguousSet));
    }

    private List<Long> findContiguousSetThatAddsUpTo(List<Long> data, long sum) {
        for (int i=0; i<data.size()-1; i++) {
            for (int j=i+1; j<data.size(); j++) {
                if (data.subList(i,j).stream().mapToLong(a -> a).sum() == sum) {
                    return data.subList(i, j);
                }
            }
        }
        return null;
    }

    private long findFirstInvalid(List<Long> data) {
        for (int i=preamble; i<data.size(); i++) {
            List<Long> subList = data.subList(i - preamble, i);
            boolean found = false;
            for (Long toCheck : subList) {
                if (toCheck * 2 != data.get(i) && subList.contains(data.get(i)-toCheck)) {
                    found = true;
                    break;
                }
            }
            if (!found) {
                return data.get(i);
            }

        }
        return -1;
    }

    public void setPreamble(int newPreamble) {
        preamble = newPreamble;
    }
}
