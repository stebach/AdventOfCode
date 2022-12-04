package li.ste.adventofcode.year2021.day02;

import li.ste.adventofcode.utils.AdventOfCodeException;

public class Command {
    public static final int TYPE_FORWARD = 1;
    public static final int TYPE_DOWN = 2;
    public static final int TYPE_UP = 3;
    private final int type;
    private final int amount;

    public Command(String type, int amount) {
        this.amount = amount;
        switch (type) {
            case "forward" -> this.type = TYPE_FORWARD;
            case "down" -> this.type = TYPE_DOWN;
            case "up" -> this.type = TYPE_UP;
            default -> throw new AdventOfCodeException("unknown type: " + type);
        }
    }

    public int getType() {
        return type;
    }

    public int getAmount() {
        return amount;
    }
}
