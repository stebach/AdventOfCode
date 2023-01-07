package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.AdventOfCodeException;
import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Day10 extends Day {
    public static void main(String[] args) {
        Day day = new Day10(new InputProvider());
        day.solvePuzzles();
    }

    public Day10(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        int score = 0;
        List<Long> autocompleteScore = new ArrayList<>();
        for(String line: getData()) {
            ChunkLine chunkLine = new ChunkLine(line);
            score += chunkLine.getScore();
            long missingScore = chunkLine.getMissingScore();
            if (missingScore > 0) {
                autocompleteScore.add(missingScore);
            }
        }

        Collections.sort(autocompleteScore);

        setSolution1(score);
        setSolution2(autocompleteScore.get((autocompleteScore.size()-1)/2));
    }

    private class ChunkLine {
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

    private class Chunk {
        public static final int TYPE_SQUARE_BRACKETS = 1;
        public static final int TYPE_CURLY_BRACKETS = 2;
        public static final int TYPE_PARENTHESES = 3;
        public static final int TYPE_ANGLE_BRACKETS = 4;
        List<Chunk> chunks = new ArrayList<>();

        public Chunk(List<Character> charList, int type, ChunkLine chunkLine) throws Day10MismatchedTypeException {
            while (!charList.isEmpty()) {
                char next = charList.remove(0);
                if (Chunk.isOpen(next)) {
                    chunks.add(new Chunk(charList, Chunk.getType(next), chunkLine));
                } else if (Chunk.getType(next) != type) {
                    throw new Day10MismatchedTypeException(Chunk.getType(next));
                } else {
                    return;
                }
            } // else: finished?
            chunkLine.addMissing(type);
        }

        private static boolean isOpen(char c) {
            return (c == '[' || c ==  '{' || c ==  '(' || c ==  '<');
        }

        public static int getType(char c) {
            return switch (c) {
                case '[', ']' -> Chunk.TYPE_SQUARE_BRACKETS;
                case '{', '}' -> Chunk.TYPE_CURLY_BRACKETS;
                case '(', ')' -> Chunk.TYPE_PARENTHESES;
                case '<', '>' -> Chunk.TYPE_ANGLE_BRACKETS;
                default -> throw new AdventOfCodeException("UNKNWON TYPE: " + c);
            };
        }
    }

    private class Day10MismatchedTypeException extends Exception {
        private final int recieved;

        public Day10MismatchedTypeException(int recieved) {
            this.recieved = recieved;
        }

        public int getRecieved() {
            return recieved;
        }
    }
}
