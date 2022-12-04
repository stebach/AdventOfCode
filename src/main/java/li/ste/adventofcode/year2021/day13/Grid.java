package li.ste.adventofcode.year2021.day13;

import li.ste.adventofcode.utils.Letter4x6grid;

import java.util.ArrayList;
import java.util.List;

public class Grid implements Letter4x6grid {
    List<List<Boolean>> lines = new ArrayList<>();
    private int width;

    public void addDot(int x, int y) {
        while (lines.size() <= y) {
            lines.add(new ArrayList<>());
        }
        while (lines.get(y).size() <= x) {
            lines.get(y).add(false);
        }
        lines.get(y).set(x,true);
        if (x >= width) {
            width = x + 1;
        }
    }

    public void foldX(int pos) {
        for (List<Boolean> line : lines) {
            for (int x = pos; x < width; x++) {
                if (line.get(x).booleanValue()) {
                    line.set(width - 1 - x, true);
                }
            }
            while (line.size() > pos) {
                line.remove(line.size() - 1);
            }
        }
        width = pos;
    }

    public void foldY(int pos) {
        for (int y = pos; y < lines.size(); y++) {
            for (int x = 0; x<width; x++) {
                if (lines.get(y).get(x).booleanValue()) {
                    lines.get(lines.size()-1-y).set(x, true);
                }
            }
        }
        for (int y = lines.size(); y > pos; y--) {
            lines.remove(y-1);
        }
    }

    public void fillEmpty() {
        for (List<Boolean> yLine : lines) {
            while (yLine.size() < width) {
                yLine.add(false);
            }
        }
    }

    public int countDots() {
        int retVal = 0;
        for (List<Boolean> line : lines) {
            for (int x = 0; x < width; x++) {
                if (line.get(x).booleanValue()) {
                    retVal += 1;
                }
            }
        }
        return retVal;
    }

    public String draw() {
        StringBuilder sb = new StringBuilder();
        for (List<Boolean> line : lines) {
            for (Boolean aBoolean : line) {
                if (aBoolean.booleanValue()) {
                    sb.append("#");
                } else {
                    sb.append(".");
                }
            }
            sb.append("\n");
        }
        return sb.toString();
    }


    @Override
    public boolean getLetterPixel(int x, int y) {
        return lines.get(y).get(x);
    }

    @Override
    public boolean hasLetter(int letterIndex) {
        return width >= 5 * (letterIndex + 1) - 1;
    }
}
