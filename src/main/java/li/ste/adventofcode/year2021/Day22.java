package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.year2021.day22.Cube;
import li.ste.adventofcode.year2021.day22.ReactorRebootCommand;

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
}
