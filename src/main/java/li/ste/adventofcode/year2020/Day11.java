package li.ste.adventofcode.year2020;

import li.ste.adventofcode.utils.AdventOfCodeException;
import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Day11 extends Day {
    public static void main(String[] args) {
        Day day = new Day11(new InputProvider());
        day.solvePuzzles();
    }

    public Day11(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        List<int[]> grid = new ArrayList<>();
        List<int[]> grid2 = new ArrayList<>();

        Scanner scanner = getScanner();

        while (scanner.hasNextLine()) {
            int[] newLine = scanner.nextLine().chars().map(this::toInt).toArray();
            grid.add(newLine);
            grid2.add(newLine.clone());

        }

        boolean running = true;
        while (running) {
            running = runRound(grid);
        }

        running = true;
        while (running) {
            running = runRoundPart2(grid2);
        }

        int occupied = 0;
        for (int[] row : grid) {
            for (int seat : row) {
                if (seat == 2) {
                    occupied += 1;
                }
            }
        }

        int occupied2 = 0;
        for (int[] row : grid2) {
            for (int seat : row) {
                if (seat == 2) {
                    occupied2 += 1;
                }
            }
        }

        setSolution1(occupied);
        setSolution2(occupied2);
    }

    private boolean runRoundPart2(List<int[]> grid) {
        boolean changed = false;
        List<int[]> newGrid = new ArrayList<>();
        for (int row = 0; row < grid.size(); row ++) {
            int[] newRow = new int[grid.get(row).length];
            for (int col = 0; col < grid.get(row).length; col++) {
                newRow[col] = grid.get(row)[col];
                if (toggleSeatPart2(row, col, grid)) {
                    newRow[col] = (grid.get(row)[col] == 1 ? 2 : 1);
                    changed = true;
                }
            }
            newGrid.add(newRow);
        }

        grid.clear();
        grid.addAll(newGrid);

        return changed;
    }

    private boolean toggleSeatPart2(int row, int col, List<int[]> grid) {
        if (grid.get(row)[col] == 0) {
            return false;
        }
        int[][] directions = new int[][]{
                { -1,-1 }, { 0,-1 }, { 1,-1 }, { -1,0 }, { 1,0 }, { -1,1 }, { 0,1 }, { 1,1 }
        };
        int occupied = 0;
        for (int[] direction : directions) {
            int checkX = col;
            int checkY = row;
            while (true) {
                checkX += direction[0];
                checkY += direction[1];

                if (
                        checkY >= 0 && checkY < grid.size()
                                && checkX >= 0 && checkX < grid.get(checkY).length
                ) {
                    if (grid.get(checkY)[checkX] == 2) {
                        occupied += 1;
                        break;
                    } else if (grid.get(checkY)[checkX] == 1) {
                        break;
                    }
                } else {
                    break;
                }
            }
        }
        return (grid.get(row)[col] == 1 && occupied == 0)
                || (grid.get(row)[col] == 2 && occupied > 4);
    }

    private boolean runRound(List<int[]> grid) {
        boolean changed = false;
        List<int[]> newGrid = new ArrayList<>();
        for (int row = 0; row < grid.size(); row ++) {
            int[] newRow = new int[grid.get(row).length];
            for (int col = 0; col < grid.get(row).length; col++) {
                newRow[col] = grid.get(row)[col];
                if (toggleSeat(row, col, grid)) {
                    newRow[col] = (grid.get(row)[col] == 1 ? 2 : 1);
                    changed = true;
                }
            }
            newGrid.add(newRow);
        }

        grid.clear();
        grid.addAll(newGrid);

        return changed;
    }

    private boolean toggleSeat(int row, int col, List<int[]> grid) {
        if (grid.get(row)[col] == 0) {
            return false;
        }
        int[][] positions = new int[][]{
                { -1,-1 }, { 0,-1 }, { 1,-1 }, { -1,0 }, { 1,0 }, { -1,1 }, { 0,1 }, { 1,1 }
        };
        int occupied = 0;
        for (int[] position : positions) {
            if (
                    position[1] + row >= 0 && position[1] + row < grid.size()
                            && position[0] + col >= 0 && position[0] + col < grid.get(position[1] + row).length
                            && grid.get(position[1] + row)[position[0] + col] == 2
            ) {
                occupied += 1;
            }
        }
        return (grid.get(row)[col] == 1 && occupied == 0)
                || (grid.get(row)[col] == 2 && occupied > 3);
    }

    private int toInt(int inputChar) {
        return switch ((char) inputChar) {
            case '.' -> 0;
            case 'L' -> 1;
            default -> throw new AdventOfCodeException("unknown char");
        };
    }
}
