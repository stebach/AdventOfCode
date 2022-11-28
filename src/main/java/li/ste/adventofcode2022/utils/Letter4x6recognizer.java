package li.ste.adventofcode2022.utils;

public class Letter4x6recognizer {

    private Letter4x6recognizer() {
        throw new IllegalStateException("Utility class");
    }
    public static String getText(Letter4x6grid grid) {
        StringBuilder sb = new StringBuilder();
        int letterIndex = 0;
        while (grid.hasLetter(letterIndex)) {
            switch (getLetterPixels(grid, letterIndex, true)) {
                case "#####...#...#...####...." -> sb.append("C");
                case "#####...###.#...#...####" -> sb.append("E");
                case "#####...###.#...#...#..." -> sb.append("F");
                case ".##.#..##...#.###..#.###" -> sb.append("G");
                case "..##...#...#...##..#.##." -> sb.append("J");
                case "#...#...#...#...#...####" -> sb.append("L");
                case "###.#..##..####.#.#.#..#" -> sb.append("R");
                default ->
                        throw new AdventOfCodeException("letter not found:" + getLetterPixels(grid, letterIndex, true) + "\n" + getLetterPixels(grid, letterIndex, false));
            }
            letterIndex += 1;
        }
        return sb.toString();
    }

    private static String getLetterPixels(Letter4x6grid grid, int letterIndex, boolean noLineBreaks) {
        StringBuilder sb = new StringBuilder();
        for (int y=0; y<6; y++) {
            for (int x=0; x<4; x++) {
                if (grid.getLetterPixel(x + letterIndex * 5,y)) {
                    sb.append("#");
                } else {
                    sb.append(".");
                }
            }
            if (!noLineBreaks) {
                sb.append("\n");
            }
        }
        return sb.toString();
    }
}
