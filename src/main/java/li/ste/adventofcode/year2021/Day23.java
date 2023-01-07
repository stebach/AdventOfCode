package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.AdventOfCodeException;
import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

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

        // now solve it!
        int validPositionCount = goalCount + corridorCount;

        SortedSet<FigurePosition> positionList = new TreeSet<>((o1, o2) -> {
            if (o1.equals(o2)) {
                return 0;
            }
            if (o1.getCost() < o2.getCost()) {
                return -1;
            }
            if (o1.getCost() > o2.getCost()) {
                return 1;
            }
            if (o1.hashCode() < o2.hashCode()) {
                return -1;
            }
            return 1;
        });
        Set<FigurePosition> completedPositions = new HashSet<>();
        positionList.add(new FigurePosition(figures));

        int minSolveCost = Integer.MAX_VALUE;
        int totalRuns = 0;

        while (!positionList.isEmpty()) {
            FigurePosition currentFigurePositions = positionList.first();
            positionList.remove(currentFigurePositions);

            for (int figure=0; figure<validPositionCount; figure ++) {
                if (currentFigurePositions.figureAtPosition(figure) == 0) {
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
                    int moves = calcMoves(figure, target ,allValidFields, connectedList, currentFigurePositions, goalMap);

                    if (moves > 0) {
                        FigurePosition newFigurePositions = currentFigurePositions.clone();
                        newFigurePositions.addCost(currentFigurePositions, moves * (int)Math.pow(10,newFigurePositions.figureAtPosition(figure)-1));
                        newFigurePositions.setFigureAtPosition(target, newFigurePositions.figureAtPosition(figure));
                        newFigurePositions.setFigureAtPosition(figure, 0);

                        // check if its not a solved one

                        Position targetField = connectedList.get(allValidFields.get(target));
                        boolean completed = false;
                        if (targetField.isGoal()) {
                            // check completed
                            completed = true;
                            for (Map.Entry<Integer, Map<Integer,Integer>> goalMapEntry : goalMap.entrySet()) {
                                for (Map.Entry<Integer, Integer> goalIndexEntry : goalMapEntry.getValue().entrySet()) {
                                    if (newFigurePositions.figureAtPosition(goalIndexEntry.getValue()) != goalMapEntry.getKey().intValue()) {
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
                            if (minSolveCost > newFigurePositions.getCost()) {
                                minSolveCost = newFigurePositions.getCost();
                                out("new best found: " + minSolveCost);

                                //remove all that cost more!
                                while (positionList.size() > 0 && positionList.last().getCost() >= minSolveCost) {
                                    positionList.remove(positionList.last());
                                }

                            }
                        } else  {
                            if (newFigurePositions.getCost() <= minSolveCost) {
                                if (positionList.contains(newFigurePositions)) {
                                    if (positionList.stream().filter(r -> r.equals(newFigurePositions)).findFirst().get().getCost() > newFigurePositions.getCost()) {
                                        positionList.remove(newFigurePositions);
                                        positionList.add(newFigurePositions);
                                    }
                                } else if (!completedPositions.contains(newFigurePositions)) {
                                    positionList.add(newFigurePositions);
                                }
                            }
                        }
                        totalRuns ++;
                        if (totalRuns % 100000 == 0) {
                            out(totalRuns + " " + positionList.size());
                        }
                    }
                }
            }

            completedPositions.add(currentFigurePositions);
        }
        return minSolveCost;
    }

    private int calcMoves(int source, int target, List<String> allValidFields, Map<String, Position> connectedList, FigurePosition currentFigurePositions, Map<Integer, Map<Integer, Integer>> goalMap) {
        if (currentFigurePositions.figureAtPosition(target) != 0) {
            return 0; // field has to be empty
        }
        Position sourceField = connectedList.get(allValidFields.get(source));
        Position targetField = connectedList.get(allValidFields.get(target));
        if (sourceField.isGoal() == targetField.isGoal()) {
            return 0; // type has to change
        }
        if (targetField.isGoal() && !targetField.isGoalFor(currentFigurePositions.figureAtPosition(source))) {
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
                if (!check.isInvalidStop() && currentFigurePositions.figureAtPosition(check.getFigureIndex()) != 0) {
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
            if (!check.isInvalidStop() && currentFigurePositions.figureAtPosition(check.getFigureIndex()) != 0) {
                return 0;
            }
            moves ++;
        }

        if (!sourceField.isGoal()) {
            // move down
            while (currentY != targetField.getY()) {
                currentY++;
                Position check = connectedList.get(currentX + "_" + currentY);
                if (!check.isInvalidStop() && currentFigurePositions.figureAtPosition(check.getFigureIndex()) != 0) {
                    return 0;
                }
                moves ++;
            }
        }

        return moves;
    }

    private boolean checkSolved(Position positionToCheck, FigurePosition currentFigurePositions, Map<String, Position> connectedList, Map<Integer, Map<Integer, Integer>> goalMap, List<String> allValidFields) {
        if (positionToCheck.isGoalFor(currentFigurePositions.figureAtPosition(positionToCheck.getFigureIndex()))) {
            if (positionToCheck.getGoalNr() == 1) {
                return true;
            } else {
                Position nextToCheck = connectedList.get(allValidFields.get(goalMap.get(positionToCheck.getGoalFor()).get(positionToCheck.getGoalNr() - 1)));
                return checkSolved(nextToCheck, currentFigurePositions, connectedList, goalMap, allValidFields);
            }
        }
        return false;
    }

    private class FigurePosition {
        private final List<Integer> positions;
        private int cost;
        private FigurePosition parent;

        public FigurePosition(List<Integer> positions) {
            this.positions = positions;
        }

        public int figureAtPosition(int position) {
            return positions.get(position);
        }

        public FigurePosition clone() {
            return new FigurePosition(new ArrayList<>(positions));
        }

        public void addCost(FigurePosition newParent, int costToAdd) {
            if (parent == null || newParent.getCost() + costToAdd < parent.getCost() + cost) {
                parent = newParent;
                cost += costToAdd;
            }
        }

        public void setFigureAtPosition(int target, int figure) {
            positions.set(target, figure);
        }

        public int getCost() {
            if (parent == null) {
                return 0;
            }
            return cost + parent.getCost();
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            FigurePosition that = (FigurePosition) o;
            return positions.equals(that.positions);
        }

        @Override
        public int hashCode() {
            return Objects.hash(positions);
        }
    }

    private class Position {
        private final int x;
        private final int y;
        private boolean isGoal;
        private int goalFor;
        private boolean invalidStop;
        private int goalNr;
        private int figureIndex;


        public Position(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public void setIsGoalFor(int goalFor) {
            isGoal = true;
            this.goalFor = goalFor;
        }

        public int getX() {
            return x;
        }

        public int getY() {
            return y;
        }

        public boolean isGoal() {
            return isGoal;
        }

        public void setInvalidStop(boolean b) {
            invalidStop = b;
        }


        public boolean isInvalidStop() {
            return invalidStop;
        }

        public boolean isGoalFor(int goalFor) {
            return this.goalFor == goalFor;
        }

        public void increaseGoalNr() {
            goalNr += 1;
        }

        public int getGoalFor() {
            return goalFor;
        }

        public int getGoalNr() {
            return goalNr;
        }

        public void setFigureIndex(int i) {
            figureIndex = i;
        }

        public int getFigureIndex() {
            return figureIndex;
        }
    }
}
