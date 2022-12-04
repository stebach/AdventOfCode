package li.ste.adventofcode.year2021.day20;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class LightPixelImage {
    private final boolean[] bytes;
    Set<String> pixelList = new HashSet<>();
    Map<String, Boolean> preEnhance = new HashMap<>();
    private int startX;
    private int startY;
    private int height;
    private int width;

    public LightPixelImage(boolean[] bytes) {
        this.bytes = bytes;
    }


    public void addRow(String row, int rowNum) {
        height += 1;
        width = row.length();


        for (int col = 0; col<row.length(); col++) {
            if (row.charAt(col) == '#') {
                pixelList.add(col + "_"  + rowNum);
            }
        }
    }

    public int getLightPixelCount() {
        return pixelList.size();
    }


    public void enhanceTwice() {
        startX -= 2;
        startY -= 2;
        width += 4;
        height += 4;

        Set<String> newList = new HashSet<>();
        preEnhance = new HashMap<>();

        for (int y=startY; y<startY + height; y++) {
            for (int x=startX; x<startX + width; x++) {
                // crate num
                if (bytes[Integer.parseInt(getRelativeRangeString(x, y),2)]) {
                    newList.add(x + "_" + y);
                }
            }
        }

        pixelList = newList;
    }

    private String getRelativeRangeString(int x, int y) {
        StringBuilder sb = new StringBuilder();
        for (int relativeY = y-1; relativeY <= y+1; relativeY++) {
            for (int relativeX = x-1; relativeX <= x+1; relativeX++) {
                if (getEnhanced(relativeX, relativeY)) {
                    sb.append("1");
                } else {
                    sb.append("0");
                }
            }
        }
        return sb.toString();
    }

    private boolean getEnhanced(int x, int y) {
        String key = x + "_" + y;
        if (!preEnhance.containsKey(key)) {
            StringBuilder sb = new StringBuilder();
            for (int relativeY = y-1; relativeY <= y+1; relativeY++) {
                for (int relativeX = x-1; relativeX <= x+1; relativeX++) {
                    if (pixelList.contains(relativeX + "_" + relativeY)) {
                        sb.append("1");
                    } else {
                        sb.append("0");
                    }
                }
            }
            preEnhance.put(key, bytes[Integer.parseInt(sb.toString(),2)]);
        }
        return preEnhance.get(key);
    }
}
