package li.ste.adventofcode.year2022.day06;

import java.util.concurrent.atomic.AtomicInteger;

public class RepetitionFinder {
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
