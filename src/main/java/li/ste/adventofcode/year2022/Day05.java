package li.ste.adventofcode.year2022;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Day05 extends Day {
    private final List<List<Character>> stacks = new ArrayList<>();
    private final List<List<Character>> stacks2 = new ArrayList<>();

    public static void main(String[] args) {
        Day day = new Day05(new InputProvider());
        day.solvePuzzles();
    }

    public Day05(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        List<String> data = getData();
        int line;
        for (line=0; line<data.size(); line++) {
            if (!parseInitialPositionLine(data, line)) {
                break;
            }
        }

        for (int instructionLine=line+2; instructionLine<data.size(); instructionLine++) {
            String[] instructionParts = data.get(instructionLine).split(" ");
            moveCrates(stacks, Integer.parseInt(instructionParts[3]), Integer.parseInt(instructionParts[5]), Integer.parseInt(instructionParts[1]), false);
            moveCrates(stacks2, Integer.parseInt(instructionParts[3]), Integer.parseInt(instructionParts[5]), Integer.parseInt(instructionParts[1]), true);
        }

        setSolution1(getTopCrates(stacks));
        setSolution2(getTopCrates(stacks2));
    }

    private boolean parseInitialPositionLine(List<String> data, int line) {
        boolean startingStackFound = false;
        for (int charPos=0; charPos<data.get(line).length(); charPos+=4) {
            if (data.get(line).charAt(charPos) == '[') {
                startingStackFound = true;
                while (stacks.size() < charPos/4+1) {
                    stacks.add(new ArrayList<>());
                }
                while (stacks2.size() < charPos/4+1) {
                    stacks2.add(new ArrayList<>());
                }
                stacks.get(charPos/4).add(0, data.get(line).charAt(charPos+1));
                stacks2.get(charPos/4).add(0, data.get(line).charAt(charPos+1));
            }
        }
        return startingStackFound;
    }

    public String getTopCrates(List<List<Character>> stacks) {
        StringBuilder topCrates = new StringBuilder();
        for (List<Character> stack : stacks) {
            if (!stack.isEmpty()) {
                topCrates.append(stack.get(stack.size()-1));
            }
        }
        return topCrates.toString();
    }

    public void moveCrates(List<List<Character>> stacks, int from, int to, int amount, boolean multipleAtOnce) {
        List<Character> fromStack = stacks.get(from - 1);
        List<Character> toMove = fromStack.subList(fromStack.size() - amount, fromStack.size());
        stacks.set(from-1, fromStack.subList(0, fromStack.size() - amount));
        if (!multipleAtOnce) {
            Collections.reverse(toMove);
        }
        stacks.get(to-1).addAll(toMove);
    }
}
