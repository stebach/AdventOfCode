package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.AdventOfCodeException;
import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.utils.RegexResultRecipient;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Day22 extends Day {
    public static void main(String[] args) {
        Day day = new Day22(new InputProvider());
        day.solvePuzzles();
    }

    public Day22(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        List<ReactorRebootCommand> data = getRegexData("^(on|off) x=([-0-9]+)\\.\\.([-0-9]+),y=([-0-9]+)\\.\\.([-0-9]+),z=([-0-9]+)\\.\\.([-0-9]+)$", ReactorRebootCommand.class);

        Set<String> on = new HashSet<>();
        for (ReactorRebootCommand command : data) {
            for (int x = command.getFromX(); x<=command.getToX(); x++) {
                for (int y = command.getFromY(); y<=command.getToY(); y++) {
                    for (int z = command.getFromZ(); z<=command.getToZ(); z++) {
                        String key = x + "_" + y + "_" + z;
                        if (command.isOn()) {
                            on.add(key);
                        } else {
                            on.remove(key);
                        }
                    }
                }
            }
        }

        setSolution1(on.size());
        ReactorRebootCommand.setLimit(false);
        List<Cube> cubes = new ArrayList<>();

        for (ReactorRebootCommand command : data) {
            List<Cube> cubesToAdd = new ArrayList<>();
            cubesToAdd.add(new Cube(command));

            while (!cubesToAdd.isEmpty()) {
                Cube cubeToAdd = cubesToAdd.remove(0);
                List<Cube> intersectingCubes = new ArrayList<>();
                for (Cube cube : cubes) {
                    if (cubeToAdd.intersects(cube)) {
                        intersectingCubes.add(cube);
                    }
                }
                while (!intersectingCubes.isEmpty()) {
                    Cube currentIntersectingCube = intersectingCubes.remove(0);
                    cubes.remove(currentIntersectingCube);

                    List<Cube> parts = currentIntersectingCube.removeIntersecting(cubeToAdd);
                    cubes.addAll(parts);
                }

                if (cubeToAdd.isOn()) {
                    cubes.add(cubeToAdd);
                }
            }
        }

        long size = 0;
        for (Cube cube : cubes) {
            size += cube.getSize();
        }

        setSolution2(size);
    }

    private class Cube {
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

    private class ReactorRebootCommand  implements RegexResultRecipient {
        private boolean on;
        private int fromX;
        private int toX;
        private int fromY;
        private int toY;
        private int fromZ;
        private int toZ;
        private static boolean doLimit = true;

        public static void setLimit(boolean b) {
            doLimit = b;
        }

        @Override
        public void setRegexResult(String[] listEntry) {
            on = listEntry[0].equals("on");
            int x1 = Integer.parseInt(listEntry[1]);
            int x2 = Integer.parseInt(listEntry[2]);
            int y1 = Integer.parseInt(listEntry[3]);
            int y2 = Integer.parseInt(listEntry[4]);
            int z1 = Integer.parseInt(listEntry[5]);
            int z2 = Integer.parseInt(listEntry[6]);

            fromX = Math.min(x1, x2);
            toX = Math.max(x1, x2);
            fromY = Math.min(y1, y2);
            toY = Math.max(y1, y2);
            fromZ = Math.min(z1, z2);
            toZ = Math.max(z1, z2);
        }

        public int getFromX() {
            if (doLimit) {
                return Math.max(-50,fromX);
            }
            return fromX;
        }

        public int getToX() {
            if (doLimit) {
                return Math.min(50,toX);
            }
            return toX;
        }

        public int getFromY() {
            if (doLimit) {
                return Math.max(-50,fromY);
            }
            return fromY;
        }

        public int getToY() {
            if (doLimit) {
                return Math.min(50,toY);
            }
            return toY;
        }

        public int getFromZ() {
            if (doLimit) {
                return Math.max(-50,fromZ);
            }
            return fromZ;
        }

        public int getToZ() {
            if (doLimit) {
                return Math.min(50,toZ);
            }
            return toZ;
        }

        public boolean isOn() {
            return on;
        }
    }
}
