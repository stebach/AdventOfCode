package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.ArrayList;
import java.util.List;

public class Day03 extends Day {
    public static void main(String[] args) {
        Day day = new Day03(new InputProvider());
        day.solvePuzzles();
    }

    public Day03(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        int charLen = getData().get(0).length();

        int[][] data = new int[charLen][2];
        for (String line : getData()) {
            for (int pos=0; pos<charLen; pos++) {
                data[pos][line.charAt(pos) - 48] += 1;
            }
        }
        StringBuilder gammaStringBuilder = new StringBuilder();
        for (int pos=0; pos<charLen; pos++) {
            if (data[pos][0] > data[pos][1]) {
                gammaStringBuilder.append("0");
            } else {
                gammaStringBuilder.append("1");
            }
        }

        String gammaStr = gammaStringBuilder.toString();

        int gamma = Integer.parseInt(gammaStr, 2);
        int epsilon = Integer.parseInt("1".repeat(charLen), 2) ^ gamma;

        setSolution1(gamma * epsilon);

        List<Integer> oxygenList = getBinaryData();
        List<Integer> co2List = getBinaryData();

        String filter = "1" + "0".repeat(charLen-1);
        for (int pos=0; pos<charLen; pos++) {
            int filterNumber = Integer.parseInt(filter.substring(0,charLen-pos), 2);
            oxygenList = cleanOxygenList(oxygenList, filterNumber);
            co2List = cleanCo2List(co2List, filterNumber);
        }

        setSolution2(oxygenList.get(0) * co2List.get(0));
    }

    private List<Integer> cleanCo2List(List<Integer> co2List, int filterNumber) {
        if (co2List.size() > 1) {
            List<Integer> co2One = new ArrayList<>();
            List<Integer> co2Zero = new ArrayList<>();
            for (Integer co2Number : co2List) {
                if ((co2Number & filterNumber) > 0) {
                    co2One.add(co2Number);
                } else {
                    co2Zero.add(co2Number);
                }
            }
            if (co2One.size() < co2Zero.size()) {
                co2List = co2One;
            } else {
                co2List = co2Zero;
            }
        }
        return co2List;
    }

    private List<Integer> cleanOxygenList(List<Integer> oxygenList, int filterNumber) {
        if (oxygenList.size() > 1) {
            List<Integer> oxyOne = new ArrayList<>();
            List<Integer> oxyZero = new ArrayList<>();
            for (Integer oxygenNumber : oxygenList) {
                if ((oxygenNumber & filterNumber) > 0) {
                    oxyOne.add(oxygenNumber);
                } else {
                    oxyZero.add(oxygenNumber);
                }
            }
            if (oxyOne.size() >= oxyZero.size()) {
                oxygenList = oxyOne;
            } else {
                oxygenList = oxyZero;
            }
        }
        return oxygenList;
    }
}
