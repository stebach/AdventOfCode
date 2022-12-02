package li.ste.adventofcode2022.days;

import li.ste.adventofcode2022.days.day02.GameStrategy;
import li.ste.adventofcode2022.utils.Day;
import li.ste.adventofcode2022.utils.InputProvider;

import java.util.List;

public class Day02 extends Day {
    private static final int SCORE_DRAW = 3;
    private static final int SCORE_WIN = 6;

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
