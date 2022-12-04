package li.ste.adventofcode.year2021.day19;

import java.util.Objects;

public class Beacon {
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
