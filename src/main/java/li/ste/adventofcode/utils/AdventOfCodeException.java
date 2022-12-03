package li.ste.adventofcode.utils;

public class AdventOfCodeException extends RuntimeException {
    public AdventOfCodeException(String message) {
        super(message);
    }

    public AdventOfCodeException(Exception e) {
        super(e);
    }
}
