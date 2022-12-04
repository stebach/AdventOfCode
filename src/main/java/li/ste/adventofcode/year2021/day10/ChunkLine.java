package li.ste.adventofcode.year2021.day10;

import java.util.ArrayList;
import java.util.List;

public class ChunkLine {
    private int score;
    private long missingScore;

    public ChunkLine(String line) {
        List<Character> charList = new ArrayList<>();
        char[] arr = line.toCharArray();
        for (char c : arr) {
            charList.add(c);
        }
        char next = charList.remove(0);
        try {
            while (!charList.isEmpty()) {
                new Chunk(charList, Chunk.getType(next), this);
            }
        } catch (Day10MismatchedTypeException e) {
            switch (e.getRecieved()) {
                case Chunk.TYPE_PARENTHESES -> score += 3;
                case Chunk.TYPE_SQUARE_BRACKETS -> score += 57;
                case Chunk.TYPE_CURLY_BRACKETS -> score += 1197;
                case Chunk.TYPE_ANGLE_BRACKETS -> score += 25137;
                default -> {
                    // ignore
                }
            }
        }
    }

    public int getScore() {
        return score;
    }

    public long getMissingScore() {
        return missingScore;
    }

    public void addMissing(int type) {
        missingScore *= 5;
        switch (type) {
            case Chunk.TYPE_PARENTHESES -> missingScore += 1;
            case Chunk.TYPE_SQUARE_BRACKETS -> missingScore += 2;
            case Chunk.TYPE_CURLY_BRACKETS -> missingScore += 3;
            case Chunk.TYPE_ANGLE_BRACKETS -> missingScore += 4;
            default -> {
                // ignore
            }
        }
    }
}
