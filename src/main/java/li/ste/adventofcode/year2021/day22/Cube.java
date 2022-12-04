package li.ste.adventofcode.year2021.day22;

import li.ste.adventofcode.utils.AdventOfCodeException;

import java.util.ArrayList;
import java.util.List;

public class Cube {
    private final int fromX;
    private final int fromY;
    private final int fromZ;
    private final int toX;
    private final int toY;
    private final int toZ;
    private final boolean on;

    public Cube(ReactorRebootCommand command) {
        on = command.isOn();
        fromX = command.getFromX();
        fromY = command.getFromY();
        fromZ = command.getFromZ();
        toX = command.getToX();
        toY = command.getToY();
        toZ = command.getToZ();
    }

    public Cube(int fromX, int toX, int fromY, int toY, int fromZ, int toZ, boolean on) {
        this.fromX = fromX;
        this.toX = toX;
        this.fromY = fromY;
        this.toY = toY;
        this.fromZ = fromZ;
        this.toZ = toZ;
        this.on = on;
    }

    public boolean intersects(Cube cube) {
        return (cube.toX >= fromX && toX >= cube.fromX)
                && (cube.toY >= fromY && toY >= cube.fromY)
                && (cube.toZ >= fromZ && toZ >= cube.fromZ);
    }

    public boolean isOn() {
        return on;
    }

    public List<Cube> removeIntersecting(Cube cubeToAdd) {
        List<Cube> newCubes = new ArrayList<>();
        newCubes.add(this);

        if (cubeToAdd.toX <= toX) {
            // cut X
            cutIntersectingAtX(cubeToAdd.toX, newCubes);
        }
        if (cubeToAdd.fromX >= fromX) {
            // cut X
            cutIntersectingAtX(cubeToAdd.fromX -1, newCubes);
        }
        if (cubeToAdd.toY <= toY) {
            // cut Y
            cutIntersectingAtY(cubeToAdd.toY, newCubes);
        }
        if (cubeToAdd.fromY >= fromY) {
            // cut Y
            cutIntersectingAtY(cubeToAdd.fromY -1, newCubes);
        }
        if (cubeToAdd.toZ <= toZ) {
            // cut Z
            cutIntersectingAtZ(cubeToAdd.toZ, newCubes);
        }
        if (cubeToAdd.fromZ >= fromZ) {
            // cut Z
            cutIntersectingAtZ(cubeToAdd.fromZ -1, newCubes);
        }


        int interSectingIndex = -1;
        for (int i=0; i<newCubes.size(); i++) {
            if (newCubes.get(i).intersects(cubeToAdd)) {
                if (interSectingIndex == -1) {
                    interSectingIndex = i;
                } else {
                    throw new AdventOfCodeException("MORE INTERSECTING THAN ALLOWED");
                }
            }
        }


        if (interSectingIndex == -1) {
            throw new AdventOfCodeException("NO INTERSECTS?");
        }

        newCubes.remove(interSectingIndex);

        return newCubes;
    }

    private void cutIntersectingAtZ(int z, List<Cube> newCubes) {
        List<Cube> tmp = new ArrayList<>();
        while (!newCubes.isEmpty()) {
            Cube currentCube = newCubes.remove(0);
            if (currentCube.fromZ<=z && currentCube.toZ >= z) {
                tmp.add(new Cube(currentCube.fromX, currentCube.toX, currentCube.fromY, currentCube.toY, currentCube.fromZ, z, currentCube.on));
                tmp.add(new Cube(currentCube.fromX, currentCube.toX, currentCube.fromY, currentCube.toY, z+1, currentCube.toZ, currentCube.on));
            } else {
                tmp.add(currentCube);
            }
        }
        newCubes.addAll(tmp);
    }

    private void cutIntersectingAtY(int y, List<Cube> newCubes) {
        List<Cube> tmp = new ArrayList<>();
        while (!newCubes.isEmpty()) {
            Cube currentCube = newCubes.remove(0);
            if (currentCube.fromY<=y && currentCube.toY >= y) {
                tmp.add(new Cube(currentCube.fromX, currentCube.toX, currentCube.fromY, y, currentCube.fromZ, currentCube.toZ, currentCube.on));
                tmp.add(new Cube(currentCube.fromX, currentCube.toX, y+1, currentCube.toY, currentCube.fromZ, currentCube.toZ, currentCube.on));
            } else {
                tmp.add(currentCube);
            }
        }
        newCubes.addAll(tmp);
    }

    private void cutIntersectingAtX(int x, List<Cube> newCubes) {
        List<Cube> tmp = new ArrayList<>();
        while (!newCubes.isEmpty()) {
            Cube currentCube = newCubes.remove(0);
            if (currentCube.fromX<=x && currentCube.toX >= x) {
                tmp.add(new Cube(currentCube.fromX, x, currentCube.fromY, currentCube.toY, currentCube.fromZ, currentCube.toZ, currentCube.on));
                tmp.add(new Cube(x+1, currentCube.toX, currentCube.fromY, currentCube.toY, currentCube.fromZ, currentCube.toZ, currentCube.on));
            } else {
                tmp.add(currentCube);
            }
        }
        newCubes.addAll(tmp);
    }


    public long getSize() {
        return (long)(toX - fromX + 1) * (long)(toY - fromY + 1) * (toZ - fromZ +1);
    }
}
