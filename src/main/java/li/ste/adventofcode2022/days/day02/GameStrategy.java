package li.ste.adventofcode2022.days.day02;

import li.ste.adventofcode2022.utils.RegexResultRecipient;

public class GameStrategy implements RegexResultRecipient {

    public static final int SHAPE_ROCK = 1;
    public static final int SHAPE_PAPER = 2;
    public static final int SHAPE_SCISSORS = 3;
    public static final int RESULT_I_SHOULD_LOSE = 1;
    public static final int RESULT_I_SHOULD_DRAW = 2;
    public static final int RESULT_I_SHOULD_WIN = 3;
    private int shapeOtherPlayer;
    private int attribute2;

    @Override
    public void setRegexResult(String[] listEntry) {
        shapeOtherPlayer = listEntry[0].charAt(0) - 64;
        attribute2 = listEntry[1].charAt(0) - 87;
    }

    public int getAttribute2() {
        return attribute2;
    }

    public int getShapeToWin() {
        if (shapeOtherPlayer < SHAPE_SCISSORS) {
            return shapeOtherPlayer + 1;
        }
        return shapeOtherPlayer - 2;
    }

    public int getShapeToLose() {
        if (shapeOtherPlayer > SHAPE_ROCK) {
            return shapeOtherPlayer - 1;
        }
        return shapeOtherPlayer + 2;
    }

    public int getShapeToDraw() {
        return shapeOtherPlayer;
    }

    public boolean isDraw() {
        return shapeOtherPlayer == attribute2;
    }

    public boolean isDefeat() {
        return shapeOtherPlayer -1 == attribute2 || shapeOtherPlayer + 2 == attribute2;
    }
}
