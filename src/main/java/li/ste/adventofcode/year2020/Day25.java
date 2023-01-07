package li.ste.adventofcode.year2020;

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

    @Override
    public void run() {
        Scanner scanner = getScanner();
        int publicKeyCard = scanner.nextInt();
        int publicKeyDoor = scanner.nextInt();

        int loopSizeCard = -1;
        int loopSizeDoor = -1;

        long subject = 7;
        long val = 1;
        int loopSize = 0;
        while (loopSizeCard < 0 || loopSizeDoor < 0) {
            loopSize += 1;
            val = (val * subject) % 20201227;
            if (val == publicKeyCard && loopSizeCard < 0) {
                loopSizeCard = loopSize;
            }
            if (val == publicKeyDoor && loopSizeDoor < 0) {
                loopSizeDoor = loopSize;
            }
        }

        val = 1;
        subject = publicKeyDoor;

        for (int i = 0; i < loopSizeCard; i++) {
            val = (val * subject) % 20201227;
        }

        setSolution1(val);
        setSolution2("@todo");
    }
}
