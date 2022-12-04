package li.ste.adventofcode.year2021.day21;

public class Player {
    private int position;
    private Die die;
    private int score;

    public void setPos(int position) {
        this.position = position;
    }

    public void setDie(Die die) {
        this.die = die;
    }

    public void play() {
        DieResult result = die.throwDie();
        position = (position + result.getMovement()) % 10;
        if (position == 0) {
            position = 10;
        }
        score += position;
    }

    public boolean won() {
        int winScore = 1000;
        return score >= winScore;
    }

    public int getScore() {
        return score;
    }
}
