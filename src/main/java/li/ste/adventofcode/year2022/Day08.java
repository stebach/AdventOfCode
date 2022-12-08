package li.ste.adventofcode.year2022;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.ArrayList;
import java.util.List;

public class Day08 extends Day {
    public static void main(String[] args) {
        Day day = new Day08(new InputProvider());
        day.solvePuzzles();
    }

    public Day08(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        List<List<Integer>> trees = new ArrayList<>();
        List<String> data = getData();
        for (String line : data) {
            List<Integer> treeRow = new ArrayList<>();
            for (char tree : line.toCharArray()) {
                treeRow.add(tree-'0');
            }
            trees.add(treeRow);
        }

        int visibleFromOutside = 0;
        int bestScenicScore = 0;
        for (int y=0; y<trees.size(); y++) {
            for (int x=0; x<trees.get(y).size(); x++) {
                if (
                        checkOnlySmallerTrees(x,y,0,-1,trees) // north
                        || checkOnlySmallerTrees(x,y,1,0,trees) // east
                        || checkOnlySmallerTrees(x,y,0,1,trees) // south
                        || checkOnlySmallerTrees(x,y,-1,0,trees) // west
                ) {
                    visibleFromOutside++;
                }

                int scenicScore = checkVisibleTrees(x,y,0,-1,trees)
                        * checkVisibleTrees(x,y,1,0,trees)
                        * checkVisibleTrees(x,y,0,1,trees)
                        * checkVisibleTrees(x,y,-1,0,trees);
                if (scenicScore > bestScenicScore) {
                    bestScenicScore = scenicScore;
                }

            }
        }

        setSolution1(visibleFromOutside);
        setSolution2(bestScenicScore);
    }

    private int checkVisibleTrees(int startX, int startY, int xChange, int yChange, List<List<Integer>> trees) {
        int mySize = trees.get(startY).get(startX);
        int visible = 0;
        for (int y=startY+yChange, x=startX+xChange; y>=0 && y<trees.size() && x>=0 && x<trees.get(y).size(); y += yChange, x += xChange) {
            visible ++;
            if (trees.get(y).get(x) >= mySize) {
                break;
            }
        }
        return visible;
    }

    private boolean checkOnlySmallerTrees(int startX, int startY, int xChange, int yChange, List<List<Integer>> trees) {
        int mySize = trees.get(startY).get(startX);
        for (int y=startY+yChange, x=startX+xChange; y>=0 && y<trees.size() && x>=0 && x<trees.get(y).size(); y += yChange, x += xChange) {
            if (trees.get(y).get(x) >= mySize) {
                return false;
            }
        }
        return true;
    }
}
