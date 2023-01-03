package li.ste.adventofcode.year2020;

import li.ste.adventofcode.utils.AdventOfCodeException;
import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day16 extends Day {
    public static void main(String[] args) {
        Day day = new Day16(new InputProvider());
        day.solvePuzzles();
    }

    public Day16(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        Scanner scanner = getScanner();
        Pattern rangePattern = Pattern.compile("^([^:]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)$");
        Matcher matcher;
        Map<String, int[]> ranges = new HashMap<>();
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            if (line.length() == 0) {
                break;
            }
            matcher = rangePattern.matcher(line);
            if (!matcher.find()) {
                throw new AdventOfCodeException("no match: " + line);
            }
            ranges.put(matcher.group(1), new int[] {
               Integer.parseInt(matcher.group(2)),
               Integer.parseInt(matcher.group(3)),
               Integer.parseInt(matcher.group(4)),
               Integer.parseInt(matcher.group(5))
            });
        }
        scanner.nextLine(); // your ticket:
        int[] myTicket = Arrays.stream(scanner.nextLine().split(",")).mapToInt(Integer::parseInt).toArray();
        scanner.nextLine(); // empty line
        scanner.nextLine(); // nearby tickets:
        List<int[]> nearbyTickets = new ArrayList<>();
        while (scanner.hasNextLine()) {
            nearbyTickets.add(Arrays.stream(scanner.nextLine().split(",")).mapToInt(Integer::parseInt).toArray());
        }

        int solution1 = 0;
        List<int[]> validTickets = new ArrayList<>();
        for (int[] nearbyTicket : nearbyTickets) {
            boolean validTicket = true;
            for (int i : nearbyTicket) {
                boolean found = false;
                for (int[] range : ranges.values()) {
                    if ((i >= range[0] && i <= range[1]) || (i >= range[2] && i <= range[3])) {
                        found = true;
                        break;
                    }
                }
                if (!found) {
                    solution1 += i;
                    validTicket = false;
                }
            }
            if (validTicket) {
                validTickets.add(nearbyTicket);
            }
        }
        setSolution1(solution1);

        List<List<String>> possibleValue = new ArrayList<>();
        for (int i = 0; i < validTickets.get(0).length; i++) {
            possibleValue.add(new ArrayList<>(ranges.keySet().stream().toList()));
        }

        for (int[] validTicket : validTickets) {
            for (int i = 0; i < validTicket.length; i++) {
                for (Map.Entry<String, int[]> entry : ranges.entrySet()) {
                    if (validTicket[i] < entry.getValue()[0] || (validTicket[i] > entry.getValue()[1] && validTicket[i] < entry.getValue()[2]) || validTicket[i] > entry.getValue()[3]) {
                        possibleValue.get(i).remove(entry.getKey());
                    }
                }
            }
        }

        List<String> toRemove = new ArrayList<>();
        for (List<String> singlePossibilities : possibleValue.stream().filter(r -> r.size() == 1).toList()) {
            toRemove.add(singlePossibilities.get(0));
        }

        while (!toRemove.isEmpty()) {
            String toRemoveString = toRemove.remove(0);
            for (List<String> strings : possibleValue) {
                if (strings.size() > 1 && strings.remove(toRemoveString) && strings.size() == 1) {
                    toRemove.add(strings.get(0));
                }
            }
        }

        long solution2 = 1;
        for (int i = 0; i < possibleValue.size(); i++) {
            if (possibleValue.get(i).get(0).startsWith("departure")) {
                solution2 *= myTicket[i];
            }
        }

        setSolution2(solution2);
    }
}
