package li.ste.adventofcode.year2022;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import org.json.simple.JSONArray;
import org.json.simple.JSONValue;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Day13 extends Day {
    public static void main(String[] args) {
        Day day = new Day13(new InputProvider());
        day.solvePuzzles();
    }

    public Day13(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        List<String> data = getData();
        List<List<JSONArray>> packetPairs = new ArrayList<>();
        List<JSONArray> allPackets = new ArrayList<>();
        for (int i=0; i<data.size(); i++) {
            String leftPacketData = data.get(i);
            if (leftPacketData.length() == 0) {
                continue;
            }
            i++;
            String rightPacketData = data.get(i);

            packetPairs.add(Arrays.asList(
                    (JSONArray) JSONValue.parse(leftPacketData),
                    (JSONArray) JSONValue.parse(rightPacketData)
            ));
        }

        int sum = 0;
        for (int i=0; i<packetPairs.size(); i++) {
            allPackets.add(packetPairs.get(i).get(0));
            allPackets.add(packetPairs.get(i).get(1));
            if (Day13.packetSorter(packetPairs.get(i).get(0), packetPairs.get(i).get(1)) == -1) {
                sum += i+1;
            }
        }

        setSolution1(sum);

        JSONArray additionalPacket1 = (JSONArray) JSONValue.parse("[[2]]");
        JSONArray additionalPacket2 = (JSONArray) JSONValue.parse("[[6]]");
        allPackets.add(additionalPacket1);
        allPackets.add(additionalPacket2);

        allPackets.sort(Day13::packetSorter);

        setSolution2(
                (allPackets.indexOf(additionalPacket1) + 1) *
                (allPackets.indexOf(additionalPacket2) + 1)
        );
    }

    private static int packetSorter(List<JSONArray> left, List<JSONArray> right) {
        int positions = Math.max(left.size(), right.size());
        for (int i=0; i<positions; i++) {
            if (left.size()-1 < i) {
                return -1;
            }
            if (right.size()-1 < i) {
                return 1;
            }
            Object leftValue = left.get(i);
            Object rightValue = right.get(i);
            if (leftValue.getClass() == Long.class && rightValue.getClass() == Long.class) {
                if (((Long) rightValue).longValue() != ((Long) leftValue).longValue()) {
                    return ((Long) leftValue).longValue() < ((Long) rightValue).longValue() ? -1 : 1;
                }
            } else {
                JSONArray newLeftValue = null;
                JSONArray newRightValue = null;
                if (leftValue.getClass() == Long.class) {
                    newLeftValue = new JSONArray();
                    newLeftValue.add(leftValue);
                } else {
                    newLeftValue = (JSONArray)leftValue;
                }
                if (rightValue.getClass() == Long.class) {
                    newRightValue = new JSONArray();
                    newRightValue.add(rightValue);
                } else {
                    newRightValue = (JSONArray)rightValue;
                }
                int check = packetSorter(newLeftValue, newRightValue);
                if (check != 0) {
                    return check;
                }
            }
        }
        return 0;
    }
}
