package li.ste.adventofcode.year2020;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import java.util.*;

public class Day13 extends Day {
    public static void main(String[] args) {
        Day day = new Day13(new InputProvider());
        day.solvePuzzles();
    }

    public Day13(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        Scanner scanner = getScanner();
        int currentTime = Integer.parseInt(scanner.nextLine());
        String[] buslinesStringArray = scanner.nextLine().split(",");
        int[] buslines = Arrays.stream(buslinesStringArray).filter(r->!r.equals("x")).mapToInt(Integer::parseInt).toArray();

        int shortestTime = Integer.MAX_VALUE;
        int shortestTimeBusLine = 0;
        for (int busline : buslines) {
            int timeToWait = busline - (currentTime % busline);
            if (timeToWait < shortestTime) {
                shortestTime = timeToWait;
                shortestTimeBusLine = busline;
            }
        }

        setSolution1(shortestTimeBusLine * shortestTime);

        buslines = Arrays.stream(buslinesStringArray).mapToInt(r -> r.equals("x") ? 1 : Integer.parseInt(r)).toArray();

        List<long[]> buslinesWithPosition = new ArrayList<>();
        long product = 1;
        for (int i = 0; i < buslines.length; i += 1) {
            if (buslines[i] != 1) {
                buslinesWithPosition.add(new long[] { buslines[i], i % buslines[i], 0, 0 });
                product *= buslines[i];
            }
        }

        // Chinese Remainder Theorem
        for (long[] longs : buslinesWithPosition) {
            long number = (product / longs[0]);

            int multiplicator = 0;
            while (((number * multiplicator) % longs[0]) != longs[1]) {
                multiplicator += 1;
            }
            longs[2] = number * multiplicator;
        }

        long sum = buslinesWithPosition.stream().mapToLong(r->r[2]).sum();

        setSolution2(product % (sum % product));
    }
}
