package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.year2021.day20.LightPixelImage;

import java.util.List;

public class Day20 extends Day {
    public static void main(String[] args) {
        Day day = new Day20(new InputProvider());
        day.solvePuzzles();
    }

    public Day20(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        List<String> data = getData();

        boolean[] bytes = new boolean[512];

        for (int i=0; i<512; i++) {
            bytes[i] = (data.get(0).charAt(i) == '#');
        }

        LightPixelImage img = new LightPixelImage(bytes);

        for (int row = 2; row < data.size(); row++) {
            img.addRow(data.get(row), row-2);
        }

        img.enhanceTwice();


        setSolution1(img.getLightPixelCount());

        for (int i=0; i<24; i++) {
            img.enhanceTwice();
        }
        setSolution2(img.getLightPixelCount());
    }
}
