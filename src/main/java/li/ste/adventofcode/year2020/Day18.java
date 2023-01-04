package li.ste.adventofcode.year2020;

import li.ste.adventofcode.utils.AdventOfCodeException;
import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day18 extends Day {

    static Pattern patternParentheses = Pattern.compile("\\(([^()]+)\\)");
    static Pattern patternAddition = Pattern.compile("([0-9]+) \\+ ([0-9]+)");
    public static void main(String[] args) {
        Day day = new Day18(new InputProvider());
        day.solvePuzzles();
    }

    public Day18(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        Scanner scanner = getScanner();
        List<String> calculations = new ArrayList<>();
        while (scanner.hasNextLine()) {
            calculations.add(scanner.nextLine());
        }

        setSolution1(calculations.stream().mapToLong(this::calc).sum());
        setSolution2(calculations.stream().mapToLong(this::advancedCalc).sum());
    }

    public long calc(String calculation) {
        Matcher matcher = patternParentheses.matcher(calculation);
        while (matcher.find()) {
            calculation = calculation.replace(matcher.group(0), "" + calc(matcher.group(1)));
            matcher = patternParentheses.matcher(calculation);
        }
        List<String> parts = new ArrayList<>(Arrays.stream(calculation.split(" ")).toList());
        long retVal = Long.parseLong(parts.remove(0));
        while (!parts.isEmpty()) {
            String operator = parts.remove(0);
            switch (operator.charAt(0)) {
                case '*' -> retVal *= Long.parseLong(parts.remove(0));
                case '+' -> retVal += Long.parseLong(parts.remove(0));
                default -> throw new AdventOfCodeException("UNKNOWN OPERATOR: " + operator);
            }
        }
        return retVal;
    }

    public long advancedCalc(String calculation) {
        Matcher matcher = patternParentheses.matcher(calculation);
        while (matcher.find()) {
            calculation = calculation.replace(matcher.group(0), "" + advancedCalc(matcher.group(1)));
            matcher = patternParentheses.matcher(calculation);
        }
        matcher = patternAddition.matcher(calculation);
        while (matcher.find()) {
            calculation = calculation.substring(0,matcher.start(0)) + calc(matcher.group(0)) + calculation.substring(matcher.end(0));
            matcher = patternAddition.matcher(calculation);
        }

        return calc(calculation);
    }
}
