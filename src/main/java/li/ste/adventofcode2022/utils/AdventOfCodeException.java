package li.ste.adventofcode2022.utils;

public class AdventOfCodeException extends RuntimeException {
    public AdventOfCodeException(String message) {
        super(message);
    }

    public AdventOfCodeException(Exception e) {
        super(e);
    }
}
