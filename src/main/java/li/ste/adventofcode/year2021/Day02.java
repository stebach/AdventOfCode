package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.AdventOfCodeException;
import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.year2021.day02.Command;

import java.util.ArrayList;
import java.util.List;


public class Day02 extends Day {
    public static void main(String[] args) {
        Day day = new Day02(new InputProvider());
        day.solvePuzzles();
    }

    public Day02(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        // prepare data
        List<Command> commands = new ArrayList<>();
        for (String line : getData()) {
            String[] parts = line.split(" ");
            commands.add(new Command(parts[0], Integer.parseInt(parts[1])));
        }

        int forward = 0;
        int depth = 0;
        int depth2 = 0;
        int aim = 0;
        for (Command command : commands) {
            switch (command.getType()) {
                case Command.TYPE_FORWARD -> {
                    forward += command.getAmount();
                    depth2 += aim * command.getAmount();
                }
                case Command.TYPE_DOWN -> {
                    depth += command.getAmount();
                    aim += command.getAmount();
                }
                case Command.TYPE_UP -> {
                    depth -= command.getAmount();
                    aim -= command.getAmount();
                }
                default -> throw new AdventOfCodeException("Unexpected value: " + command.getType());
            }
        }

        setSolution1(forward * depth);
        setSolution2(forward * depth2);
    }
}
