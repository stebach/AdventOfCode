package li.ste.adventofcode.year2020;

import li.ste.adventofcode.utils.AdventOfCodeException;
import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day14 extends Day {
    public static void main(String[] args) {
        Day day = new Day14(new InputProvider());
        day.solvePuzzles();
    }

    public Day14(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        Scanner scanner = getScanner();
        Pattern maskPattern = Pattern.compile("^mask = ([01X]{36})$");
        Pattern memPattern = Pattern.compile("^mem\\[([0-9]+)\\] = ([0-9]+)$");
        Matcher matcher;
        String mask = "X".repeat(36);
        Map<Integer, Long> mem = new HashMap<>();
        Map<Long, Long> mem2 = new HashMap<>();
        List<Long> addresses;
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            matcher = maskPattern.matcher(line);
            if (matcher.find()) {
                mask = matcher.group(1);
                continue;
            }
            matcher = memPattern.matcher(line);
            if (matcher.find()) {
                int key = Integer.parseInt(matcher.group(1));
                String number = Long.toString(Long.parseLong(matcher.group(2)), 2);
                char[] numberArr = ("0".repeat(36 - number.length()) + number).toCharArray();
                for (int i = 0; i < 36; i++) {
                    if (mask.charAt(i) != 'X') {
                        numberArr[i] = mask.charAt(i);
                    }
                }
                mem.put(key, Long.parseLong(new String(numberArr), 2));

                addresses = new ArrayList<>();
                String keyString = Integer.toString(key, 2);
                char[] numberArr2 = ("0".repeat(36 - keyString.length()) + keyString).toCharArray();

                getAddresses(numberArr2, mask, 0, addresses);

                for (Long address : addresses) {
                    mem2.put(address, Long.parseLong(matcher.group(2)));
                }
                continue;
            }
            throw new AdventOfCodeException("no match found (" + line + ")!");
        }
        long sum = mem.values().stream().mapToLong(r->r).sum();
        setSolution1(sum);

        sum = mem2.values().stream().mapToLong(r->r).sum();
        setSolution2(sum);
    }

    private void getAddresses(char[] address, String mask, int index, List<Long> addresses) {
        if (index == 36) {
            addresses.add(Long.parseLong(new String(address), 2));
            return;
        }
        if (mask.charAt(index) == 'X') {
            char[] copy0 = address.clone();
            copy0[index] = '0';
            getAddresses(copy0, mask, index + 1, addresses);
            char[] copy1 = address.clone();
            copy1[index] = '1';
            getAddresses(copy1, mask, index + 1, addresses);
        } else {
            if (mask.charAt(index) == '1') {
                address[index] = '1';
            }
            getAddresses(address, mask, index + 1, addresses);
        }
    }
}
