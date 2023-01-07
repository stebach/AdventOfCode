package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.*;

public class Day19 extends Day {
    private final List<Scanner> scanners = new ArrayList<>();
    public static void main(String[] args) {
        Day day = new Day19(new InputProvider());
        day.solvePuzzles();
    }

    public Day19(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        Scanner currentScanner = null;
        for (String line: getData()) {
            if (line.length() > 0) {
                if (line.startsWith("---")) {
                    // new scanner
                    currentScanner = new Scanner(scanners.size());
                    scanners.add(currentScanner);
                } else if (currentScanner != null) {
                    String[] parts = line.split(",");
                    currentScanner.addBeacon(Integer.parseInt(parts[0]), Integer.parseInt(parts[1]), Integer.parseInt(parts[2]));
                }
            }
        }

        scanners.get(0).setPositionAndRotation(0,0,0,0,0,0);

        boolean repeat = true;
        while (repeat) {
            repeat = false;
            for (Scanner scanner : scanners) {
                if (scanner.toScanFrom()) {
                    repeat = true;
                    scanner.findNext(scanners);
                }
            }
        }

        Set<Beacon> allBeacons = new HashSet<>();

        for (Scanner scanner : scanners) {
            allBeacons.addAll(scanner.getBeacons());
        }

        setSolution1(allBeacons.size());

        List<Integer> distances = new ArrayList<>();
        for (Scanner scanner : scanners) {
            distances.add(scanner.getMaxManhattanDistance(scanners));
        }

        setSolution2(Collections.max(distances));
    }

    private class Beacon {
        private final int x;
        private final int y;
        private final int z;

        public Beacon(int x, int y, int z) {
            this.x = x;
            this.y = y;
            this.z = z;
        }

        public Beacon modify(int shiftX, int shiftY, int shiftZ, int rotateX, int rotateY, int rotateZ) {
            int localX = x;
            int localY = y;
            int localZ = z;

            if (rotateX > 0) {
                int preRotateY = localY;
                int preRotateZ = localZ;
                localY = (int)Math.round(Math.cos(Math.toRadians(rotateX)) * preRotateY - Math.sin(Math.toRadians(rotateX)) * preRotateZ);
                localZ = (int)Math.round(Math.sin(Math.toRadians(rotateX)) * preRotateY + Math.cos(Math.toRadians(rotateX)) * preRotateZ);
            }
            if (rotateY > 0) {
                int preRotateX = localX;
                int preRotateZ = localZ;
                localX = (int)Math.round(Math.cos(Math.toRadians(rotateY)) * preRotateX + Math.sin(Math.toRadians(rotateY)) * preRotateZ);
                localZ = (int)Math.round(-Math.sin(Math.toRadians(rotateY)) * preRotateX + Math.cos(Math.toRadians(rotateY)) * preRotateZ);
            }
            if (rotateZ > 0) {
                int preRotateX = localX;
                int preRotateY = localY;
                localX = (int)Math.round(Math.cos(Math.toRadians(rotateZ)) * preRotateX - Math.sin(Math.toRadians(rotateZ)) * preRotateY);
                localY = (int)Math.round(Math.sin(Math.toRadians(rotateZ)) * preRotateX + Math.cos(Math.toRadians(rotateZ)) * preRotateY);
            }

            localX += shiftX;
            localY += shiftY;
            localZ += shiftZ;

            return new Beacon(localX, localY, localZ);
        }

        public int getX() {
            return x;
        }

        public int getY() {
            return y;
        }

        public int getZ() {
            return z;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Beacon beacon = (Beacon) o;
            return x == beacon.x && y == beacon.y && z == beacon.z;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y, z);
        }

        @Override
        public String toString() {
            return "Beacon{" +
                    "x=" + x +
                    ", y=" + y +
                    ", z=" + z +
                    '}';
        }
    }

    private static class Rotation {
        private final int x;
        private final int y;
        private final int z;

        public Rotation(int x, int y, int z) {
            this.x = x;
            this.y = y;
            this.z = z;
        }

        public int getX() {
            return x;
        }
        public int getY() {
            return y;
        }
        public int getZ() {
            return z;
        }
    }

    private class Scanner {
        private final int id;
        private final List<Beacon> beacons = new ArrayList<>();
        private int posX = 0;
        private int posY = 0;
        private int posZ = 0;
        private int rotX = 0;
        private int rotY = 0;
        private int rotZ = 0;
        private boolean done = false;
        private boolean scanDone = false;
        private static final List<Rotation> rotations = new ArrayList<>(Arrays.asList(

                new Rotation(270,0,180),

                new Rotation(0,0,0),
                new Rotation(0,0,90),
                new Rotation(0,0,180),
                new Rotation(0,0,270),

                new Rotation(0,90,0),
                new Rotation(0,90,90),
                new Rotation(0,90,180),
                new Rotation(0,90,270),

                new Rotation(0,180,0),
                new Rotation(0,180,90),
                new Rotation(0,180,180),
                new Rotation(0,180,270),

                new Rotation(0,270,0),
                new Rotation(0,270,90),
                new Rotation(0,270,180),
                new Rotation(0,270,270),

                new Rotation(90,0,0),
                new Rotation(90,0,90),
                new Rotation(90,0,180),
                new Rotation(90,0,270),

                new Rotation(270,0,0),
                new Rotation(270,0,90),
                new Rotation(270,0,270)
        ));

        public Scanner(int id) {
            this.id = id;
        }

        public void addBeacon(int x, int y, int z) {
            beacons.add(new Beacon(x, y, z));
        }

        public void setPositionAndRotation(int posX, int posY, int posZ, int rotX, int rotY, int rotZ) {
            this.posX = posX;
            this.posY = posY;
            this.posZ = posZ;
            this.rotX = rotX;
            this.rotY = rotY;
            this.rotZ = rotZ;
            this.done = true;
        }

        public boolean toScanFrom() {
            return done && !scanDone;
        }

        public void findNext(List<Scanner> scanners) {
            for (Scanner scanner : scanners) {
                if (scanner.done || scanner.id == this.id) {
                    continue;
                }
                List<Beacon> theirBeacons = scanner.getBeacons();

                for (Rotation rotation : rotations) {
                    List<Beacon> rotatedBeacons = modifyBeacons(theirBeacons, 0, 0, 0, rotation.getX(), rotation.getY(), rotation.getZ());
                    List<Beacon> myBeacons = getBeacons();

                    for (int myBeacon = 0; myBeacon < myBeacons.size() - 11; myBeacon += 1) {
                        for (int theirBeacon = 0; theirBeacon < theirBeacons.size() - 11; theirBeacon += 1) {

                            checkMatches(myBeacons, myBeacon, rotatedBeacons, theirBeacon, scanner, rotation);

                        }
                    }
                }
            }
            scanDone = true;
        }

        private void checkMatches(List<Beacon> myBeacons, int myBeacon, List<Beacon> rotatedBeacons, int theirBeacon, Scanner scanner, Rotation rotation) {
            int xShift = myBeacons.get(myBeacon).getX() - rotatedBeacons.get(theirBeacon).getX();
            int yShift = myBeacons.get(myBeacon).getY() - rotatedBeacons.get(theirBeacon).getY();
            int zShift = myBeacons.get(myBeacon).getZ() - rotatedBeacons.get(theirBeacon).getZ();

            List<Beacon> modifiedBeacons = modifyBeacons(rotatedBeacons, xShift, yShift, zShift, 0, 0, 0);

            int matchCount = 0;
            for (Beacon modifiedBeacon : modifiedBeacons) {
                if (myBeacons.contains(modifiedBeacon)) {
                    matchCount++;
                }
            }
            if (matchCount > 11) {
                scanner.setPositionAndRotation(xShift, yShift, zShift, rotation.getX(), rotation.getY(), rotation.getZ());
            }

        }

        public List<Beacon> getBeacons() {
            return modifyBeacons(beacons, posX, posY, posZ, rotX, rotY, rotZ);
        }

        private List<Beacon> modifyBeacons(List<Beacon> beacons, int shiftX, int shiftY, int shiftZ, int rotateX, int rotateY, int rotateZ) {
            List<Beacon> retVal = new ArrayList<>();
            for (Beacon beacon : beacons) {
                retVal.add(beacon.modify(shiftX, shiftY, shiftZ, rotateX, rotateY, rotateZ));
            }
            return retVal;
        }

        @Override
        public String toString() {
            return "Scanner{" +
                    "id=" + id +
                    ", posX=" + posX +
                    ", posY=" + posY +
                    ", posZ=" + posZ +
                    ", rotX=" + rotX +
                    ", rotY=" + rotY +
                    ", rotZ=" + rotZ +
                    ", done=" + done +
                    ", scanDone=" + scanDone +
                    '}';
        }

        public Integer getMaxManhattanDistance(List<Scanner> scanners) {
            List<Integer> distances = new ArrayList<>();
            for (Scanner scanner : scanners) {
                distances.add(scanner.getManhattanDistance(this.posX, this.posY, this.posZ));
            }
            return Collections.max(distances);
        }

        private Integer getManhattanDistance(int posX, int posY, int posZ) {
            return Math.abs(this.posX - posX) + Math.abs(this.posY - posY) + Math.abs(this.posZ - posZ);
        }
    }
}
