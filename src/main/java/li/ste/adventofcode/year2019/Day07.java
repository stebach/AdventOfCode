package li.ste.adventofcode.year2019;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.year2019.intcode.IntCode;

import java.util.*;

public class Day07 extends Day {
    public static void main(String[] args) {
        Day day = new Day07(new InputProvider());
        day.solvePuzzles();
    }

    public Day07(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        Scanner scanner = getScanner();

        int[] program = Arrays.stream(scanner.nextLine().split(",")).mapToInt(Integer::parseInt).toArray();


        setSolution1(getHighestSignal(program));
        setSolution2(getHighestSignal(program, true));
    }

    public int getHighestSignal(int[] program) {
        return getHighestSignal(program, false);
    }

    public int getHighestSignal(int[] program, boolean part2) {
        List<Integer> phases = new ArrayList<>(Arrays.asList(0, 1, 2, 3, 4));
        if (part2) {
            phases = new ArrayList<>(Arrays.asList(5, 6, 7, 8, 9));
        }
        List<Integer> phase = new ArrayList<>();
        return tryPhases(program, phases, phase, part2);
    }

    private int tryPhases(int[] program, List<Integer> phases, List<Integer> phase, boolean part2) {
        if (!phases.isEmpty()) {
            int max = Integer.MIN_VALUE;
            for (Integer integer : phases) {
                List<Integer> newPhase = new ArrayList<>(phase);
                newPhase.add(integer);
                max = Math.max(tryPhases(program, phases.stream().filter(r->!r.equals(integer)).toList(), newPhase, part2), max);
            }
            return max;
        } else {
            int lastOutput = 0;

            if (part2) {
                List<IntCode> intCodes = new ArrayList<>();
                intCodes.add(new IntCode(program.clone(), new ArrayList<>(List.of(phase.get(0))), new ArrayList<>()));
                intCodes.add(new IntCode(program.clone(), new ArrayList<>(List.of(phase.get(1))), new ArrayList<>()));
                intCodes.add(new IntCode(program.clone(), new ArrayList<>(List.of(phase.get(2))), new ArrayList<>()));
                intCodes.add(new IntCode(program.clone(), new ArrayList<>(List.of(phase.get(3))), new ArrayList<>()));
                intCodes.add(new IntCode(program.clone(), new ArrayList<>(List.of(phase.get(4))), new ArrayList<>()));


                List<Integer> output;
                int count = 0;
                while (true) {
                    boolean err = false;
                    try {
                        count ++;
                        intCodes.get(0).getInput().add(lastOutput);
                        intCodes.get(0).run();
                    } catch (IntCode.IntCodeNoInputException e) {
                        err = true;
                    } finally {
                        output = intCodes.get(0).getOutput();
                        lastOutput = output.remove(0);
                        intCodes.add(intCodes.remove(0));
                    }
                    if (err) {
                        continue;
                    }
                    if ((count % 5) == 0) {
                        return lastOutput;
                    }
                }

            } else {
                List<Integer> input = new ArrayList<>();
                List<Integer> output = new ArrayList<>();

                for (Integer integer : phase) {
                    IntCode intCode = new IntCode(program, input, output);
                    input.add(integer);
                    input.add(lastOutput);
                    intCode.run();
                    lastOutput = output.get(output.size() - 1);
                    output.clear();
                }
            }

            return lastOutput;
        }
    }
}
