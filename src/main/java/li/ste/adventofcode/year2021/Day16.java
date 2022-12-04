package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.year2021.day16.Message;

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
        Message message = new Message(getData().get(0));

        setSolution1(message.getPackageVersionSum());
        setSolution2(message.getPackageSum());
    }
}
