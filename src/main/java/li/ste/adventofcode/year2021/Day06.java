package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Day06 extends Day {
    public static void main(String[] args) {
        Day day = new Day06(new InputProvider());
        day.solvePuzzles();
    }

    public Day06(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        List<Integer> fishList = new ArrayList<>(Arrays.stream(getData().get(0).split(",")).map(Integer::parseInt).toList());

        long[] fishCount = new long[9];

        for (int nr : fishList) {
            fishCount[nr] += 1;
        }

        for (int i=0; i<80; i++) {
            long tmp = fishCount[0];
            for (int j=0; j<8; j++) {
                fishCount[j] = fishCount[j+1];
            }
            fishCount[8] = tmp;
            fishCount[6] += tmp;
        }


        setSolution1(
                fishCount[0] +fishCount[1] +fishCount[2] +fishCount[3] +fishCount[4] +fishCount[5] +fishCount[6] +fishCount[7] +fishCount[8]
        );


        for (int i=0; i<256 - 80; i++) {
            long tmp = fishCount[0];
            for (int j=0; j<8; j++) {
                fishCount[j] = fishCount[j+1];
            }
            fishCount[8] = tmp;
            fishCount[6] += tmp;
        }

        setSolution2(
                fishCount[0] +fishCount[1] +fishCount[2] +fishCount[3] +fishCount[4] +fishCount[5] +fishCount[6] +fishCount[7] +fishCount[8]
        );

    }
}
