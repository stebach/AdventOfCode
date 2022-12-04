package li.ste.adventofcode.year2021.day10;

import li.ste.adventofcode.utils.AdventOfCodeException;

import java.util.ArrayList;
import java.util.List;

public class Chunk {
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
