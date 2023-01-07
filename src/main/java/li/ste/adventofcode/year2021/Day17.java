package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.utils.RegexResultRecipient;

import java.util.*;

public class Day17 extends Day {
    public static void main(String[] args) {
        Day day = new Day17(new InputProvider());
        day.solvePuzzles();
    }

    public Day17(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        List<TargetArea> data = getRegexData("target area: x=([-0-9]+)..([-0-9]+), y=([-0-9]+)..([-0-9]+)", TargetArea.class);

        int maxHeight = calcMaxHeight(data.get(0));
        Map<Integer, List<Integer>> yPossibilities = calcYPossibilities(data.get(0));
        Map<Integer, List<Integer>> xPossibilities = calcXPossibilities(data.get(0),
                Collections.max(yPossibilities.keySet()));

        Set<String> finalResult = new HashSet<>();
        for (Map.Entry<Integer, List<Integer>> yPossibility : yPossibilities.entrySet()) {
            if (xPossibilities.containsKey(yPossibility.getKey())) {
                for (Integer yVal : yPossibility.getValue()) {
                    for (Integer xVal : xPossibilities.get(yPossibility.getKey())) {
                        finalResult.add(xVal + "," + yVal);
                    }
                }
            }
        }

        setSolution1(maxHeight);
        setSolution2(finalResult.size());
    }


    private Map<Integer, List<Integer>> calcXPossibilities(TargetArea targetArea, int max) {
        Map<Integer, List<Integer>> retVal = new HashMap<>();
        for (int x=1; x <= targetArea.getMaxX(); x++) {
            int currX = 0;
            int currVelocityX = x;
            int steps = 0;

            while (currX <= targetArea.getMaxX() && steps <= max) {
                currX += currVelocityX;
                if (currVelocityX > 0) {
                    currVelocityX -= 1;
                }
                steps ++;
                if (currX >= targetArea.getMinX() && currX <= targetArea.getMaxX()) {
                    retVal.putIfAbsent(steps, new ArrayList<>());
                    retVal.get(steps).add(x);
                }
            }

        }
        return retVal;
    }

    private Map<Integer, List<Integer>> calcYPossibilities(TargetArea targetArea) {
        Map<Integer, List<Integer>> retVal = new HashMap<>();
        for (int y=Math.abs(targetArea.getMinY())-1; y>=targetArea.getMinY(); y--) {
            int currY = 0;
            int currVelocityY = y;
            int steps = 0;

            while (currY >= targetArea.getMinY()) {
                currY += currVelocityY;
                currVelocityY -= 1;
                steps ++;
                if (currY <= targetArea.getMaxY() && currY >= targetArea.getMinY()) {
                    retVal.putIfAbsent(steps, new ArrayList<>());
                    retVal.get(steps).add(y);
                }
            }
        }
        return retVal;
    }

    private int calcMaxHeight(TargetArea targetArea) {
        for (int y=Math.abs(targetArea.getMinY())-1; y>0; y--) {
            int runMaxHeight = 0;
            int currY = 0;
            int currVelocityY = y;
            boolean hitTarget = false;
            while (currY >= targetArea.getMinY()) {
                currY += currVelocityY;
                currVelocityY -= 1;
                if (currY > runMaxHeight) {
                    runMaxHeight = currY;
                }
                if (currY <= targetArea.getMaxY() && currY >= targetArea.getMinY()) {
                    hitTarget = true;
                }
            }
            if (hitTarget) {
                return runMaxHeight;
            }
        }
        return 0;
    }

    private class TargetArea implements RegexResultRecipient {
        private int minX;
        private int maxX;
        private int minY;
        private int maxY;

        @Override
        public void setRegexResult(String[] listEntry) {
            minX = Integer.parseInt(listEntry[0]);
            maxX = Integer.parseInt(listEntry[1]);
            minY = Integer.parseInt(listEntry[2]);
            maxY = Integer.parseInt(listEntry[3]);
        }

        public int getMinY() {
            return minY;
        }

        public int getMaxY() {
            return maxY;
        }

        public int getMaxX() {
            return maxX;
        }
        public int getMinX() {
            return minX;
        }
    }
}
