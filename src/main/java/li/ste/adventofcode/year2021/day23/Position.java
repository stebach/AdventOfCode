package li.ste.adventofcode.year2021.day23;

public class Position {
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
