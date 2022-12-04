package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.AdventOfCodeException;
import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.year2021.day23.Position;

import java.util.*;

public class Day23 extends Day {
    public static void main(String[] args) {
        Day day = new Day23(new InputProvider());
        day.solvePuzzles();
    }

    public Day23(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        setSolution1(runTask());
        setSolution2(runTask(true));
    }

    private int runTask() {
        return runTask(false);
    }

    private int runTask(boolean addTask2Lines) {
        List<String> data = new ArrayList<>(getData());

        if (addTask2Lines) {
            data.add(3,"  #D#B#A#C#");
            data.add(3,"  #D#C#B#A#");
        }

        int y=0;
        List<Position> initialList = new ArrayList<>();
        List<Integer> figures = new ArrayList<>();

        for (String line : data) {
            char goalFor = 1;
            for (int x=0; x<line.length(); x++) {
                Position position;
                switch (line.charAt(x)) {
                    case '.':
                        position = new Position(x,y);
                        initialList.add(position);
                        figures.add(0);
                        break;
                    case 'A', 'B', 'C', 'D':
                        position = new Position(x,y);
                        position.setIsGoalFor(goalFor);
                        figures.add(line.charAt(x) - 64);
                        initialList.add(position);
                        for (Position updateGoalNrPosition : initialList) {
                            if (updateGoalNrPosition.isGoalFor(goalFor)) {
                                updateGoalNrPosition.increaseGoalNr();
                            }
                        }

                        goalFor ++;
                        break;
                    case '#', ' ':
                        break;
                    default:
                        throw new AdventOfCodeException("unknown char: " + line.charAt(x));
                }
            }
            y++;
        }
        Map<String, Position> connectedList = new HashMap<>();
        int goalCount = 0;
        int corridorCount = 0;
        List<String> allValidFields = new ArrayList<>();
        while (!initialList.isEmpty()) {
            Position pos = initialList.remove(0);
            for (Position otherPos : initialList) {
                if (
                        ((pos.getX() == otherPos.getX()+1 || pos.getX() == otherPos.getX()-1) && pos.getY() == otherPos.getY())
                                || ((pos.getY() == otherPos.getY()+1 || pos.getY() == otherPos.getY()-1) && pos.getX() == otherPos.getX())
                ) {
                    if (pos.isGoal() && !otherPos.isGoal()) {
                        otherPos.setInvalidStop(true);
                        figures.remove(0);
                    }
                    if (otherPos.isGoal() && !pos.isGoal()) {
                        pos.setInvalidStop(true);
                        figures.remove(0);
                    }
                }
            }

            String key = pos.getX() + "_" + pos.getY();
            if (pos.isGoal()) {
                goalCount++;
            } else if (!pos.isInvalidStop()) {
                corridorCount++;
            }
            if (!pos.isInvalidStop()) {
                allValidFields.add(key);
            }

            connectedList.put(key, pos);
        }

        // define goal positions for a simple check if the puzzle was solved
        Map<Integer, Map<Integer, Integer>> goalMap = new HashMap<>() ;
        for (int i=1; i<=4; i++) {
            goalMap.put(i, new HashMap<>());
        }



        for (int i=0; i<allValidFields.size(); i++) {
            Position checkPos = connectedList.get(allValidFields.get(i));
            checkPos.setFigureIndex(i);
            if (checkPos.isGoal()) {
                goalMap.get(checkPos.getGoalFor()).put(checkPos.getGoalNr(), i);
            }
        }

        int costIndex = figures.size();
        figures.add(0); // last spot for movement cost

        int minSolveCost = Integer.MAX_VALUE;

        // now solve it!
        int validPositionCount = goalCount + corridorCount;
        Set<List<Integer>> figurePositions = new HashSet<>();
        figurePositions.add(figures);

        int totalRuns = 0;

        while (!figurePositions.isEmpty()) {
            List<Integer> currentFigurePositions = figurePositions.iterator().next();
            figurePositions.remove(currentFigurePositions);

            if (currentFigurePositions.get(costIndex) >= minSolveCost) {
                continue;
            }

            for (int figure=0; figure<validPositionCount; figure ++) {
                if (currentFigurePositions.get(figure) == 0) {
                    continue; //no figure there
                }
                // check if it is a solved one
                Position positionToCheck = connectedList.get(allValidFields.get(figure));
                if (checkSolved(positionToCheck, currentFigurePositions, connectedList, goalMap, allValidFields)) {
                    continue;
                }

                int from = 0;
                int to = validPositionCount;

                if (positionToCheck.isGoal()) {
                    to = corridorCount;
                } else {
                    from = corridorCount;
                }


                for (int target=from; target<to; target++) {
                    //check if target is valid
                    int moves = 0;
                    if (currentFigurePositions.get(figure) < 3 || (target > 2 || target < 7)) {
                        moves = calcMoves(figure, target ,allValidFields, connectedList, currentFigurePositions, goalMap);
                    }

                    if (moves > 0) {

                        List<Integer> newFigurePositions = new ArrayList<>(currentFigurePositions);

                        int currentCost = newFigurePositions.get(costIndex);
                        int newCost = currentCost + moves * (int)Math.pow(10,newFigurePositions.get(figure)-1);
                        newFigurePositions.set(costIndex, newCost);

                        newFigurePositions.set(target, newFigurePositions.get(figure));
                        newFigurePositions.set(figure, 0);

                        Position targetField = connectedList.get(allValidFields.get(target));
                        boolean completed = false;
                        if (targetField.isGoal()) {
                            // check completed
                            completed = true;
                            for (Map.Entry<Integer, Map<Integer,Integer>> goalMapEntry : goalMap.entrySet()) {
                                for (Map.Entry<Integer, Integer> goalIndexEntry : goalMapEntry.getValue().entrySet()) {
                                    if (!newFigurePositions.get(goalIndexEntry.getValue()).equals(goalMapEntry.getKey())) {
                                        completed = false;
                                        break;
                                    }
                                }
                                if (!completed) {
                                    break;
                                }
                            }
                        }

                        if (completed) {
                            if (minSolveCost > newFigurePositions.get(costIndex)) {
                                minSolveCost = newFigurePositions.get(costIndex);
                                out("new best found: " + minSolveCost);
                            }
                        } else  {
                            if (newFigurePositions.get(costIndex) <= minSolveCost) {
                                figurePositions.add(newFigurePositions);
                            }
                        }
                        totalRuns ++;
                        if (totalRuns % 100000 == 0) {
                            out(totalRuns + " " + figurePositions.size());
                        }
                    }
                }
            }
        }
        return minSolveCost;
    }

    private int calcMoves(int source, int target, List<String> allValidFields, Map<String, Position> connectedList, List<Integer> currentFigurePositions, Map<Integer, Map<Integer, Integer>> goalMap) {
        if (currentFigurePositions.get(target) != 0) {
            return 0; // field has to be empty
        }
        Position sourceField = connectedList.get(allValidFields.get(source));
        Position targetField = connectedList.get(allValidFields.get(target));
        if (sourceField.isGoal() == targetField.isGoal()) {
            return 0; // type has to change
        }
        if (targetField.isGoal() && !targetField.isGoalFor(currentFigurePositions.get(source))) {
            return 0; // wrong goal area
        }
        if (targetField.isGoal() && targetField.getGoalNr() > 1) {
            Position nextToCheck = connectedList.get(allValidFields.get(goalMap.get(targetField.getGoalFor()).get(targetField.getGoalNr() - 1)));
            if (!checkSolved(nextToCheck, currentFigurePositions, connectedList, goalMap, allValidFields)) {
                return 0; //lower field in goal have to be filled first
            }
        }
        int moves = 0;
        // try to move to goal
        int currentX = sourceField.getX();
        int currentY = sourceField.getY();

        if (sourceField.isGoal()) {
            // first up
            while (currentY != targetField.getY()) {
                currentY--;
                Position check = connectedList.get(currentX + "_" + currentY);
                if (!check.isInvalidStop() && currentFigurePositions.get(check.getFigureIndex()) != 0) {
                    return 0;
                }
                moves ++;
            }
        }

        int moveDirection = 1;
        if (currentX > targetField.getX()) {
            moveDirection = -1;
        }
        while (currentX != targetField.getX()) {
            currentX += moveDirection;
            Position check = connectedList.get(currentX + "_" + currentY);
            if (!check.isInvalidStop() && currentFigurePositions.get(check.getFigureIndex()) != 0) {
                return 0;
            }
            moves ++;
        }

        if (!sourceField.isGoal()) {
            // move down
            while (currentY != targetField.getY()) {
                currentY++;
                Position check = connectedList.get(currentX + "_" + currentY);
                if (!check.isInvalidStop() && currentFigurePositions.get(check.getFigureIndex()) != 0) {
                    return 0;
                }
                moves ++;
            }
        }

        return moves;
    }

    private boolean checkSolved(Position positionToCheck, List<Integer> currentFigurePositions, Map<String, Position> connectedList, Map<Integer, Map<Integer, Integer>> goalMap, List<String> allValidFields) {
        if (positionToCheck.isGoalFor(currentFigurePositions.get(positionToCheck.getFigureIndex()))) {
            if (positionToCheck.getGoalNr() == 1) {
                return true;
            } else {
                Position nextToCheck = connectedList.get(allValidFields.get(goalMap.get(positionToCheck.getGoalFor()).get(positionToCheck.getGoalNr() - 1)));
                return checkSolved(nextToCheck, currentFigurePositions, connectedList, goalMap, allValidFields);
            }
        }
        return false;
    }
}
