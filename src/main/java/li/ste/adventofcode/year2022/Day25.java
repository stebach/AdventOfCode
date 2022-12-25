package li.ste.adventofcode.year2022;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.Scanner;

public class Day25 extends Day {
    public static void main(String[] args) {
        Day day = new Day25(new InputProvider());
        day.solvePuzzles();
    }

    public Day25(InputProvider provider) {
        super(provider);
    }

    public static long snafu2dec(String snafu) {
        long retVal = 0;
        for (char c : snafu.toCharArray()) {
            retVal *= 5;
            if (c == '-') {
                retVal -= 1;
            } else if (c == '=') {
                retVal -= 2;
            } else {
                retVal += c - 48;
            }
        }
        return retVal;
    }

    public static String dec2snafu(long dec) {
        char[] data = Long.toString(dec, 5).toCharArray();
        StringBuilder sb = new StringBuilder();

        boolean incrementNext = false;
        for (int i = data.length - 1; i >= 0; i --) {
            char c = (char)(data[i] + (incrementNext ? 1 : 0));
            incrementNext = false;
            switch (c) {
                case '5' -> {
                    sb.append("0");
                    incrementNext = true;
                }
                case '3' -> {
                    sb.append("=");
                    incrementNext = true;
                }
                case '4' -> {
                    sb.append("-");
                    incrementNext = true;
                }
                default -> sb.append(c);
            }
        }
        if (incrementNext) {
            sb.append('1');
        }

        sb.reverse();
        return sb.toString();
    }

    @Override
    public void run() {
        Scanner scanner = getScanner();

        long sum = 0;
        while (scanner.hasNextLine()) {
            sum += snafu2dec(scanner.nextLine());
        }

        setSolution1(dec2snafu(sum));
        setSolution2("");
    }
}
