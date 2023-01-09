package li.ste.adventofcode.year2019;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.*;

public class Day01 extends Day {
    public static void main(String[] args) {
        Day day = new Day01(new InputProvider());
        day.solvePuzzles();
    }

    public Day01(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        Scanner scanner = getScanner();

        int fuelNeeded = 0;
        int fuelNeeded2 = 0;

        while (scanner.hasNextInt()) {
            int mass = scanner.nextInt();
            int fuelStep = Math.floorDiv(mass, 3) - 2;
            fuelNeeded += fuelStep;
            int totalFuelForMass = fuelStep;
            while (fuelStep > 8) {
                fuelStep = Math.floorDiv(fuelStep, 3) - 2;
                totalFuelForMass += fuelStep;
            }
            fuelNeeded2 += totalFuelForMass;
        }

        setSolution1(fuelNeeded);
        setSolution2(fuelNeeded2);
    }
}
