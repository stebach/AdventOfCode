package li.ste.adventofcode.year2022;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.concurrent.atomic.AtomicInteger;

public class Day06 extends Day {
    public static void main(String[] args) {
        Day day = new Day06(new InputProvider());
        day.solvePuzzles();
    }

    public Day06(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        char[] data = getData().get(0).toCharArray();

        setSolution1(getStartOfFirstAllUniqueString_Baalrukh(data, 4));
        setSolution2(getStartOfFirstAllUniqueString_Baalrukh(data, 14));
    }

    /**
     * Very fast solution by https://github.com/Baalrukh/AdventOfCode2022/
     */
    private int getStartOfFirstAllUniqueString_Baalrukh(char[] line, int patternLength) {
        RepetitionFinder repetitionFinder = new RepetitionFinder();
        int i = 0;
        AtomicInteger advance = new AtomicInteger();
        while (i < line.length - patternLength)
        {
            if (repetitionFinder.HasRepetition(line, i, patternLength, advance))
            {
                return i + patternLength;
            }

            i += advance.intValue();
        }

        return -1;
    }

    private int getStartOfFirstAllUniqueString(char[] data, int length) {
        for (int i=0; i<data.length-(length-1); i++) {
            if (allCharactersUnique(Arrays.copyOfRange(data,i,i+length))) {
                return i;
            }
        }
        return -1;
    }

    private boolean allCharactersUnique(char[] characters) {
        Set<Character> check = new HashSet<>();
        for (char character : characters) {
            if (!check.add(character)) {
                return false;
            }
        }
        return true;
    }

    private class RepetitionFinder {
        private static final int NotFound = -1;
        private final int[] _foundCharacterCache = new int[] { NotFound, NotFound, NotFound, NotFound, NotFound, NotFound, NotFound, NotFound, NotFound, NotFound, NotFound, NotFound, NotFound, NotFound, NotFound, NotFound, NotFound, NotFound, NotFound, NotFound, NotFound, NotFound, NotFound, NotFound, NotFound, NotFound };

        public boolean HasRepetition(char[] line, int startIndex, int patternLength, AtomicInteger advance) {
            for (int i = 0; i < patternLength; i++)
            {
                int c = line[startIndex + i] - 'a';
                if (_foundCharacterCache[c] != NotFound)
                {
                    advance.set(_foundCharacterCache[c] + 1);
                    CleanupCache(line, startIndex, i);
                    return false;
                }

                _foundCharacterCache[c] = i;
            }

            advance.set(0);
            return true;
        }

        private void CleanupCache(char[] line, int startIndex, int length) {
            for (int i = 0; i < length; i++)
            {
                int c = line[startIndex + i] - 'a';
                _foundCharacterCache[c] = NotFound;
            }
        }
    }
}
