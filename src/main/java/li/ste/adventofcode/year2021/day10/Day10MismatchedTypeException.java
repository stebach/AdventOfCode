package li.ste.adventofcode.year2021.day10;

public class Day10MismatchedTypeException extends Exception {
    private final int recieved;

    public Day10MismatchedTypeException(int recieved) {
        this.recieved = recieved;
    }

    public int getRecieved() {
        return recieved;
    }
}
