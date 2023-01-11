package li.ste.adventofcode.year2019;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.*;

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
        Scanner scanner = getScanner();
        char[] data = scanner.nextLine().toCharArray();
        int width = 25;
        int height = 6;
        int[][] layerdata = new int[data.length/(width*height)][width*height];
        for (int i = 0; i < data.length; i ++) {
            int layer = i / (width * height);
            layerdata[layer][i%(width*height)] = data[i] - '0';
        }

        int layerWithFewestZeroes = -1;
        int fewestZeroes = Integer.MAX_VALUE;
        for (int i = 0; i < layerdata.length; i++) {
            int numberOfZeroes = (int)Arrays.stream(layerdata[i]).filter(r -> r == 0).count();
            if (numberOfZeroes < fewestZeroes) {
                layerWithFewestZeroes = i;
                fewestZeroes = numberOfZeroes;
            }
        }

        long numberOfOnes = Arrays.stream(layerdata[layerWithFewestZeroes]).filter(r -> r == 1).count();
        long numberOfTwos = Arrays.stream(layerdata[layerWithFewestZeroes]).filter(r -> r == 2).count();

        setSolution1(numberOfOnes * numberOfTwos);

        char[] finalImage = new char[width * height];
        for (int i = 0; i < finalImage.length; i++) {
            for (int[] layerdatum : layerdata) {
                if (layerdatum[i] == 0) {
                    finalImage[i] = ' ';
                    break;
                } else if (layerdatum[i] == 1) {
                    finalImage[i] = '█';
                    break;
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < height; i++) {
            sb.append(Arrays.copyOfRange(finalImage, width * i, width * (i + 1)));
            sb.append("\n");
        }

        setSolution2("\n" + sb.toString());

    }
}
