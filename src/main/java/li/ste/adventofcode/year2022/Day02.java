package li.ste.adventofcode.year2022;

import li.ste.adventofcode.year2022.day02.GameStrategy;
import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

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
}
