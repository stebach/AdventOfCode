package li.ste.adventofcode.year2020;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Day20 extends Day {
    public static void main(String[] args) {
        Day day = new Day20(new InputProvider());
        day.solvePuzzles();
    }

    public Day20(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        List<Tile> tiles = new ArrayList<>();
        Scanner scanner = getScanner();
        while (scanner.hasNextLine()) {
            int tileNum = Integer.parseInt(scanner.nextLine().substring(5, 9));
            Tile tile = new Tile(tileNum, 10);
            for (int i = 0; i < 10; i++) {
                tile.addLine(scanner.nextLine());
            }
            tiles.add(tile);
            if (scanner.hasNextLine()) {
                scanner.nextLine();
            }
        }

        List<Tile> positionedTiles = new ArrayList<>();
        tiles.get(0).setPosition(0,0);
        positionedTiles.add(tiles.remove(0));

        int max = 1000;
        while (!tiles.isEmpty()) {
            Tile next = tiles.remove(0);

            boolean found = false;

            positionedTileLoop:
            for (Tile positionedTile : positionedTiles) {
                for (int flipped = 0; flipped < 2; flipped ++) {
                    if (flipped == 1) {
                        next.flip();
                    }
                    for (int rotation = 0; rotation < 4; rotation ++) {
                        //check
                        if (positionedTile.top.equals(next.bottom)) {
                            next.setPosition(positionedTile.x, positionedTile.y - 1);
                            found = true;
                        } else if (positionedTile.bottom.equals(next.top)) {
                            next.setPosition(positionedTile.x, positionedTile.y + 1);
                            found = true;
                        } else if (positionedTile.left.equals(next.right)) {
                            next.setPosition(positionedTile.x - 1, positionedTile.y);
                            found = true;
                        } else if (positionedTile.right.equals(next.left)) {
                            next.setPosition(positionedTile.x + 1, positionedTile.y);
                            found = true;
                        }
                        if (found) {
                            break positionedTileLoop;
                        }

                        next.rotate();
                    }
                }
            }


            if (found) {
                positionedTiles.add(next);
            } else {
                tiles.add(next);
            }

            if (max -- < 1) {
                break;
            }
        }

        int minX = positionedTiles.stream().mapToInt(r->r.x).min().getAsInt();
        int maxX = positionedTiles.stream().mapToInt(r->r.x).max().getAsInt();
        int minY = positionedTiles.stream().mapToInt(r->r.y).min().getAsInt();
        int maxY = positionedTiles.stream().mapToInt(r->r.y).max().getAsInt();


        long[] tileNums = positionedTiles.stream().filter(r -> (r.x == minX || r.x == maxX) && (r.y == minY || r.y == maxY)).mapToLong(r -> r.tileNum).toArray();
        long result1 = 1L;
        for (long tileNum : tileNums) {
            result1 *= tileNum;
        }

        setSolution1(result1);

        // 96 * 96
        int size = 8*(int)Math.sqrt(positionedTiles.size());
        char[][] map = new char[size][size];
        for (int y = minY; y <= maxY; y++) {
            for (int x = minX; x <= maxX; x++) {
                int searchX = x;
                int searchY = y;
                Tile tile = positionedTiles.stream().filter(r -> r.x == searchX && r.y == searchY).findFirst().get();
                for (int y2 = 1; y2 < 9; y2 ++) {
                    for (int x2 = 1; x2 < 9; x2 ++) {
                        map[(y - minY) * 8 + y2-1][(x - minX) * 8 + x2-1] = tile.lines[y2][x2];
                    }
                }
            }
        }

        Tile mapTile = new Tile(1, map.length);
        for (char[] chars : map) {
            mapTile.addLine(new String(chars));
        }

        int[][] monster = new int[][]{
                { 18,0 },
                { 0,1 },
                { 5,1 },
                { 6,1 },
                { 11,1 },
                { 12,1 },
                { 17,1 },
                { 18,1 },
                { 19,1 },
                { 1,2 },
                { 4,2 },
                { 7,2 },
                { 10,2 },
                { 13,2 },
                { 16,2 },
        };

        boolean matchFound = false;

        monsterSearch:
        for (int flip = 0; flip < 2; flip ++) {
            for (int rotate = 0; rotate < 4; rotate ++) {

                for (int y = 0; y < size - 2; y ++) {
                    for (int x = 0; x < size - 19; x++) {
                        boolean match = true;
                        for (int[] ints : monster) {
                            if (mapTile.lines[y + ints[1]][x + ints[0]] == '.') {
                                match = false;
                                break;
                            }
                        }
                        if (match) {
                            matchFound = true;
                            for (int[] ints : monster) {
                                mapTile.lines[y + ints[1]][x + ints[0]] = 'O';
                            }
                        }
                    }
                }


                if (matchFound) {
                    break monsterSearch;
                }

                mapTile.rotate();
            }
            mapTile.flip();
        }

        int solution2 = Arrays.stream(mapTile.lines).mapToInt(r-> {
            int count = 0;
            for (char c : r) {
                if (c == '#') {
                    count += 1;
                }
            }
            return count;
        }).sum();

        setSolution2(solution2);
    }

    private static class Tile {
        private final int tileNum;
        private final int size;
        private char[][] lines;
        private int x;
        private int y;
        private String top;
        private String bottom;
        private String left;
        private String right;
        private int lineIndex = 0;

        public Tile(int tileNum, int size) {
            this.tileNum = tileNum;
            this.lines = new char[size][size];
            this.size = size;
        }

        public void addLine(String line) {

            lines[lineIndex] = line.toCharArray();
            lineIndex += 1;

            if (lineIndex == size) {
                top = new String(lines[0]);
                bottom = new String(lines[size-1]);
                StringBuilder sb = new StringBuilder();
                StringBuilder sb2 = new StringBuilder();
                for (char[] chars : lines) {
                    sb.append(chars[0]);
                    sb2.append(chars[size-1]);
                }
                left = sb.toString();
                right = sb2.toString();
            }
        }

        public void setPosition(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public void flip() {
            String tmp = left;
            left = right;
            right = tmp;
            top = reversed(top);
            bottom = reversed(bottom);
            for (int i = 0; i < lines.length; i++) {
                lines[i] = reversed(new String(lines[i])).toCharArray();
            }

        }

        private String reversed(String str) {
            StringBuilder sb = new StringBuilder();
            sb.append(str);
            sb.reverse();
            return sb.toString();
        }

        public void rotate() {
            String tmp = top;
            top = reversed(left);
            left = bottom;
            bottom = reversed(right);
            right = tmp;

            char[][] newLines = new char[size][size];

            for (int y = 0; y < size; y++) {
                for (int x = 0; x < size; x++) {
                    int y2 = x;
                    int x2 = (int)(((y-(size-1)/2.0) * -1) + (size-1)/2.0);
                    newLines[y2][x2] = lines[y][x];
                }
            }

            lines = newLines;
        }
    }
}
