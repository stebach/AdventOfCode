package li.ste.adventofcode.year2021.day19;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Scanner {
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
