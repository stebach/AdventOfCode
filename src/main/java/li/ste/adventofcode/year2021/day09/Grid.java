package li.ste.adventofcode.year2021.day09;

import java.util.*;

public class Grid {
    private int width;
    private int height;
    private final List<int[]> lines = new ArrayList<>();
    private final List<int[]> basinMap = new ArrayList<>();

    public void addLine(String line) {
        width = line.length();
        int[] newLine = new int[width];
        char[] chars = line.toCharArray();
        for (int i=0; i<width; i++) {
            newLine[i] = chars[i] - 48;
        }
        lines.add(newLine);
        height += 1;
    }

    public List<int[]> getLowPointCoords() {
        List<int[]> retVal = new ArrayList<>();
        for (int x=0; x<width; x++) {
            for (int y=0; y<height; y++) {
                if (
                        (x == 0 || lines.get(y)[x-1] > lines.get(y)[x]) // left is bigger
                        && (x == width -1 || lines.get(y)[x+1] > lines.get(y)[x]) // right is bigger
                        && (y == 0 || lines.get(y-1)[x] > lines.get(y)[x]) // top is bigger
                        && (y == height -1 || lines.get(y+1)[x] > lines.get(y)[x]) //bottom is bigger
                ) {
                    retVal.add(new int[] { x, y});
                }
            }
        }
        return retVal;
    }

    public int getSumOfCoords(List<int[]> lowPoints) {
        int retVal = 0;
        for (int[] coord : lowPoints) {
            retVal += lines.get(coord[1])[coord[0]];
        }
        return retVal;
    }

    public int calcBasins() {
        drawBasinMap();

        Map<Integer, Integer> sizes = new HashMap<>();
        for (int y=0; y<height; y++) {
            for (int x = 0; x < width; x++) {
                int key = basinMap.get(y)[x];
                if (key != 0) {
                    sizes.computeIfPresent(key, (k, v) -> v + 1);
                    sizes.putIfAbsent(key, 1);
                }
            }
        }
        List<Integer> sizeList = new ArrayList<>(sizes.values());
        Collections.sort(sizeList);
        Collections.reverse(sizeList);

        return sizeList.get(0) * sizeList.get(1) * sizeList.get(2);
    }

    private void drawBasinMap() {
        int idx = 1;
        for (int y=0; y<height; y++) {
            int[] newLine = new int[width];
            for (int x=0; x<width; x++) {
                if (lines.get(y)[x] == 9) {
                    idx++;
                } else {
                    newLine[x] = idx;
                    checkNewLineAndBasinIndexConnection(newLine, x, y, idx);
                }
            }
            idx ++;
            basinMap.add(newLine);
        }
    }

    private void checkNewLineAndBasinIndexConnection(int[] newLine, int x, int y, int idx) {
        if (y > 0 && basinMap.get(y-1)[x] > 0) {
            for (int x2=0; x2<x; x2++) {
                if (newLine[x2] == basinMap.get(y-1)[x]) {
                    newLine[x2] = idx;
                }
            }
            replaceBasinIdx(basinMap.get(y-1)[x], idx);
        }
    }

    private void replaceBasinIdx(int oldIdx, int newIdx) {
        for (int[] row : basinMap) {
            for (int i=0; i<row.length; i++) {
                if (row[i] == oldIdx) {
                    row[i] = newIdx;
                }
            }
        }
    }
}
