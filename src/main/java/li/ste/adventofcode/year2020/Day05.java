package li.ste.adventofcode.year2020;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Day05 extends Day {
    public static void main(String[] args) {
        Day day = new Day05(new InputProvider());
        day.solvePuzzles();
    }

    public Day05(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        List<String> data = getData();
        int maxID = Integer.MIN_VALUE;
        List<Integer> allIDs = new ArrayList<>();
        for (String seat : data) {
            int seatID = getIDForSeat(seat);
            allIDs.add(seatID);
            if (seatID > maxID) {
                maxID = seatID;
            }
        }
        Collections.sort(allIDs);
        int first = allIDs.get(0);
        int mySeat = -1;
        for (int i=1; i< allIDs.size(); i++) {
            if (allIDs.get(i) != first + i) {
                mySeat = first+i;
                break;
            }
        }
        setSolution1(maxID);
        setSolution2(mySeat);
    }

    public int getRowForSeat(String seat) {
        return Integer.parseInt(seat.substring(0, 7).replace('B', '1').replace('F', '0'),2);
    }

    public int getColumnForSeat(String seat) {
        return Integer.parseInt(seat.substring(7, 10).replace('R', '1').replace('L', '0'),2);
    }

    public int getIDForSeat(String seat) {
        return getRowForSeat(seat) * 8 + getColumnForSeat(seat);
    }
}
