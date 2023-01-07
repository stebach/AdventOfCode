package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.AdventOfCodeException;
import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.utils.RegexResultRecipient;

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
        List<DigitsLine> digitsLines = getRegexData("^([a-g]+) ([a-g]+) ([a-g]+) ([a-g]+) ([a-g]+) ([a-g]+) ([a-g]+) ([a-g]+) ([a-g]+) ([a-g]+) \\| ([a-g]+) ([a-g]+) ([a-g]+) ([a-g]+)$", DigitsLine.class);

        int countOf1478 = 0;
        int totalSum = 0;
        for (DigitsLine digitsLine : digitsLines) {
            digitsLine.solve();

            countOf1478 += digitsLine.getCountOf1478();
            totalSum += digitsLine.getNumber();
        }

        setSolution1(countOf1478);

        setSolution2(totalSum);
    }

    private class DigitsLine implements RegexResultRecipient {
        private char[] num1;
        private char[] num2;
        private char[] num3;
        private char[] num4;

        private final List<char[]> unknownChars = new ArrayList<>();
        private final Map<Integer, char[]> knownChars = new HashMap<>();
        private final Map<String, Integer> solution = new HashMap<>();
        private final List<String> checkList1478 = new ArrayList<>();

        private final List<char[]> fiveLengthChars = new ArrayList<>();

        @Override
        public void setRegexResult(String[] listEntry) {
            for (int i=0; i<10; i++) {
                unknownChars.add(fixCharsOrder(listEntry[i]));
            }

            num1 = fixCharsOrder(listEntry[10]);
            num2 = fixCharsOrder(listEntry[11]);
            num3 = fixCharsOrder(listEntry[12]);
            num4 = fixCharsOrder(listEntry[13]);
        }

        private char[] fixCharsOrder(String s) {
            char[] charArray = s.toCharArray();
            Arrays.sort(charArray);
            return charArray;
        }

        public void solve() {
            solve1478();
            solve3();

            char segment1 = findExtra(knownChars.get(1), knownChars.get(7));
            char segment2 = findExtra(knownChars.get(4), removeChar(knownChars.get(3), segment1));

            solve25withSegment2(segment2);

            char segment3 = firstSameChar(knownChars.get(1), knownChars.get(2));
            char segment5 = removeAllFrom(knownChars.get(2), knownChars.get(3))[0];

            // solve the rest
            for (int i= unknownChars.size()-1; i>= 0; i--) {
                if (!containsChar(unknownChars.get(i), segment3)) {
                    knownChars.put(6, unknownChars.get(i));
                    unknownChars.remove(i);
                } else if (!containsChar(unknownChars.get(i), segment5)) {
                    knownChars.put(9, unknownChars.get(i));
                    unknownChars.remove(i);
                } else {
                    knownChars.put(0, unknownChars.get(i));
                    unknownChars.remove(i);
                }
            }

            for (Map.Entry<Integer, char[]> entry : knownChars.entrySet()) {
                solution.put(new String(entry.getValue()), entry.getKey());
            }
        }

        private void solve25withSegment2(char segment2) {
            for (int i= unknownChars.size()-1; i>= 0; i--) {
                if (unknownChars.get(i).length == 5) {
                    if (containsChar(unknownChars.get(i), segment2)) {
                        knownChars.put(5, unknownChars.get(i));
                        unknownChars.remove(i);
                    } else {
                        knownChars.put(2, unknownChars.get(i));
                        unknownChars.remove(i);
                    }
                }
            }
        }

        private void solve3() {
            for (int i=0; i<fiveLengthChars.size(); i++) {
                int diffs = 0;
                for (char[] fiveLengthChar : fiveLengthChars) {
                    diffs += charDiffs(fiveLengthChars.get(i), fiveLengthChar);
                }
                if (diffs == 4) {
                    // we found the 3
                    for (int k=0; k<unknownChars.size(); k++) {
                        if (new String(unknownChars.get(k)).equals(new String(fiveLengthChars.get(i)))) {
                            knownChars.put(3, unknownChars.get(k));
                            unknownChars.remove(k);
                            break;
                        }
                    }
                    fiveLengthChars.remove(i);
                    break;
                }
            }
        }

        private void solve1478() {
            // solve 1 / 4 / 7 / 8 first - they are easy
            for (int i= unknownChars.size()-1; i>= 0; i--) {
                switch (unknownChars.get(i).length) {
                    case 2 -> {
                        // it can only be 1
                        knownChars.put(1, unknownChars.get(i));
                        checkList1478.add(new String(unknownChars.get(i)));
                        unknownChars.remove(i);
                    }
                    case 3 -> {
                        // it can only be 7
                        knownChars.put(7, unknownChars.get(i));
                        checkList1478.add(new String(unknownChars.get(i)));
                        unknownChars.remove(i);
                    }
                    case 4 -> {
                        // it can only be 4
                        knownChars.put(4, unknownChars.get(i));
                        checkList1478.add(new String(unknownChars.get(i)));
                        unknownChars.remove(i);
                    }
                    case 7 -> {
                        // it can only be 8
                        knownChars.put(8, unknownChars.get(i));
                        checkList1478.add(new String(unknownChars.get(i)));
                        unknownChars.remove(i);
                    }
                    case 5 -> fiveLengthChars.add(unknownChars.get(i));
                    case 6 -> { /* ignreo */ }
                    default -> throw new AdventOfCodeException("unexpected length!");
                }
            }
        }

        private char[] removeAllFrom(char[] chars, char[] chars2) {
            List<Character> result = new ArrayList<>();
            boolean found;
            for (char c : chars) {
                found = false;
                for (char c2 : chars2) {
                    if (c == c2) {
                        found = true;
                        break;
                    }
                }
                if (!found) {
                    result.add(c);
                }
            }
            char[] retVal = new char[result.size()];
            for (int i=0; i<result.size(); i++) {
                retVal[i] = result.get(i);
            }
            return retVal;
        }

        private char firstSameChar(char[] chars, char[] chars2) {
            for (char c : chars) {
                for (char c2 : chars2) {
                    if (c == c2) {
                        return c;
                    }
                }
            }
            return 0;
        }

        private int charDiffs(char[] chars, char[] chars2) {
            return countCharsThatAreOnlyInFirst(chars, chars2)
                    + countCharsThatAreOnlyInFirst(chars2, chars);
        }

        private int countCharsThatAreOnlyInFirst(char[] needles, char[] haystack) {
            boolean found;
            int diffs = 0;
            for (char c : needles) {
                found = false;
                for (char c2 : haystack) {
                    if (c == c2) {
                        found = true;
                        break;
                    }
                }
                if (!found) {
                    diffs += 1;
                }
            }
            return diffs;
        }

        private char[] removeChar(char[] chars, char segment) {
            char[] retVal = new char[chars.length-1];
            int index = 0;
            for (char c : chars) {
                if (c != segment) {
                    retVal[index] = c;
                    index += 1;
                }
            }
            return retVal;
        }

        private char findExtra(char[] chars, char[] chars2) {
            if (chars2.length > chars.length) {
                for (char c : chars2) {
                    if (!containsChar(chars, c)) {
                        return c;
                    }
                }        } else {
                for (char c : chars) {
                    if (!containsChar(chars2, c)) {
                        return c;
                    }
                }
            }
            return 0;
        }

        private boolean containsChar(char[] chars, char search) {
            for (char c : chars) {
                if (c == search) {
                    return true;
                }
            }
            return false;
        }

        public int getCountOf1478() {
            int retVal = 0;
            if (checkList1478.contains(new String(num1))) {
                retVal += 1;
            }
            if (checkList1478.contains(new String(num2))) {
                retVal += 1;
            }
            if (checkList1478.contains(new String(num3))) {
                retVal += 1;
            }
            if (checkList1478.contains(new String(num4))) {
                retVal += 1;
            }

            return retVal;
        }

        public int getNumber() {
            List<String> numbers = new ArrayList<>();
            numbers.add(new String(num1));
            numbers.add(new String(num2));
            numbers.add(new String(num3));
            numbers.add(new String(num4));

            int retVal = 0;

            for (int i=0; i<numbers.size(); i+=1) {
                retVal += solution.get(numbers.get(i)) * Math.pow(10, (double)3-i);
            }

            return retVal;
        }
    }
}
