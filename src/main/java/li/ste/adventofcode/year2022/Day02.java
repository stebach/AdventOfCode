package li.ste.adventofcode.year2022;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.utils.RegexResultRecipient;

import java.util.List;

public class Day02 extends Day {
    private static final int SCORE_DRAW = 3;
    private static final int SCORE_WIN = 6;

    public static void main(String[] args) {
        Day day = new Day02(new InputProvider());
        day.solvePuzzles();
    }

    public Day02(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        List<GameStrategy> data = getRegexData("^([A-C]) ([X-Z])$", GameStrategy.class);

        int score = 0;
        for (GameStrategy game : data) {
            if (game.isDraw()) {
                score += SCORE_DRAW + game.getAttribute2();
            } else if (game.isDefeat()) {
                score += game.getAttribute2();
            } else {
                score += SCORE_WIN + game.getAttribute2();
            }
        }
        setSolution1(score);

        score = 0;
        for (GameStrategy game : data) {
            if (game.getAttribute2() == GameStrategy.RESULT_I_SHOULD_WIN) {
                score += SCORE_WIN + game.getShapeToWin();
            } else if (game.getAttribute2() == GameStrategy.RESULT_I_SHOULD_LOSE) {
                score += game.getShapeToLose();
            } else { //game.getExpectedResult() == GameStrategy.RESULT_I_SHOULD_DRAW
                score += SCORE_DRAW + game.getShapeToDraw();
            }
        }
        setSolution2(score);
    }

    private class GameStrategy implements RegexResultRecipient {

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
}
