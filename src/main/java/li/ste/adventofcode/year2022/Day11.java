package li.ste.adventofcode.year2022;

import li.ste.adventofcode.utils.AdventOfCodeException;
import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.year2022.day11.Monkey;

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day11 extends Day {
    public static void main(String[] args) {
        Day day = new Day11(new InputProvider());
        day.solvePuzzles();
    }

    public Day11(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        List<Monkey> monkeys = new ArrayList<>();
        List<Monkey> monkeysNoRelief = new ArrayList<>();
        Scanner scanner = getScanner();
        String line = "";
        Pattern operationPattern = Pattern.compile("^  Operation: new = old ([+\\-*]) ([0-9]+|old)$");
        Pattern testPattern = Pattern.compile("^  Test: divisible by ([0-9]+)$");
        Pattern targetPattern = Pattern.compile("^    If (true|false): throw to monkey ([0-9]+)$");

        Matcher matcher;

        int commonMultiple = 1;

        while (scanner.hasNext()) {
            Monkey monkey = new Monkey();
            line = scanner.nextLine(); // monkey no
            if (line.length() == 0) {
                continue;
            }

            monkey.setStartingItems(Arrays.stream(scanner.nextLine().split(":")[1].trim().split(",")). mapToLong(r -> Long.parseLong(r.trim())).toArray());

            matcher = operationPattern.matcher(scanner.nextLine());
            if (matcher.find()) {
                if ("old".equals(matcher.group(2))) {
                    monkey.setOperation(matcher.group(1).charAt(0));
                } else {
                    monkey.setOperation(matcher.group(1).charAt(0), Integer.parseInt(matcher.group(2)));
                }
            } else {
                throw new AdventOfCodeException("operation not found");
            }

            matcher = testPattern.matcher(scanner.nextLine());
            if (matcher.find()) {
                monkey.setTest(Integer.parseInt(matcher.group(1)));
                commonMultiple *= Integer.parseInt(matcher.group(1));
            } else {
                throw new AdventOfCodeException("test not found");
            }

            matcher = targetPattern.matcher(scanner.nextLine());
            if (matcher.find()) {
                monkey.setTrueTarget(Integer.parseInt(matcher.group(2)));
            } else {
                throw new AdventOfCodeException("target (true) not found");
            }

            matcher = targetPattern.matcher(scanner.nextLine());
            if (matcher.find()) {
                monkey.setFalseTarget(Integer.parseInt(matcher.group(2)));
            } else {
                throw new AdventOfCodeException("target (false) not found");
            }

            monkeys.add(monkey);
            monkeysNoRelief.add(monkey.withoutRelief());
        }

        for (Monkey monkey : monkeys) {
            monkey.setCommonMultiple(commonMultiple);
        }
        for (Monkey monkey : monkeysNoRelief) {
            monkey.setCommonMultiple(commonMultiple);
        }



        for (int round = 0; round < 20; round++) {
            for (Monkey monkey : monkeys) {
                monkey.throwItems(monkeys);
            }
        }

        Collections.sort(monkeys, (m1, m2) -> {
            if (m1.getInspections() > m2.getInspections()) {
                return -1;
            }
            if (m1.getInspections() < m2.getInspections()) {
                return 1;
            }
            return 0;
        });


        setSolution1(monkeys.get(0).getInspections() * monkeys.get(1).getInspections());

        for (int round = 0; round < 10000; round++) {
            for (Monkey monkey : monkeysNoRelief) {
                monkey.throwItems(monkeysNoRelief);
            }
        }

        Collections.sort(monkeysNoRelief, (m1, m2) -> {
            if (m1.getInspections() > m2.getInspections()) {
                return -1;
            }
            if (m1.getInspections() < m2.getInspections()) {
                return 1;
            }
            return 0;
        });

        setSolution2((long)monkeysNoRelief.get(0).getInspections() * (long)monkeysNoRelief.get(1).getInspections());
    }

}
