package li.ste.adventofcode.year2022;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

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
        setSolution1(getStartOfFirstAllUniqueString(data, 4)+4);
        setSolution2(getStartOfFirstAllUniqueString(data, 14)+14);
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
            check.add(character);
        }
        return check.size() == characters.length;
    }
}
