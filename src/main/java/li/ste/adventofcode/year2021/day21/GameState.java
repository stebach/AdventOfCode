package li.ste.adventofcode.year2021.day21;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class GameState {
    int player1pos;
    int player1score = 0;
    int player2pos;
    int player2score = 0;
    long count = 1;
    int playerTurn = 1;

    static int[][] diceThrows =  {
            { 3,1 },
            { 4,3 },
            { 5,6 },
            { 6,7 },
            { 7,6 },
            { 8,3 },
            { 9,1 },
    };

    public GameState(int pos1, int pos2) {
        player1pos = pos1;
        player2pos = pos2;
    }

    public boolean player1won() {
        return player1score >= 21;
    }

    public boolean player2won() {
        return player2score >= 21;
    }

    public long getCount() {
        return count;
    }

    public List<GameState> play() {
        List<GameState> retVal = new ArrayList<>();
        for (int[] diceThrow : diceThrows) {
            GameState state = this.copy().move(diceThrow[0], diceThrow[1]);
            retVal.add(state);
        }
        return retVal;
    }

    private GameState move(int fields, int increaseCount) {
        if (playerTurn == 1) {
            player1pos += fields;
            if (player1pos > 10) {
                player1pos -= 10;
            }
            player1score += player1pos;
            playerTurn = 2;
        } else  {
            player2pos += fields;
            if (player2pos > 10) {
                player2pos -= 10;
            }
            player2score += player2pos;
            playerTurn = 1;
        }
        count *= increaseCount;
        return this;
    }

    private GameState copy() {
        GameState retVal = new GameState(player1pos, player2pos);
        retVal.player1score = player1score;
        retVal.player2score = player2score;
        retVal.count = count;
        retVal.playerTurn = playerTurn;
        return retVal;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        GameState gameState = (GameState) o;
        return player1pos == gameState.player1pos && player1score == gameState.player1score && player2pos == gameState.player2pos && player2score == gameState.player2score && playerTurn == gameState.playerTurn;
    }

    @Override
    public int hashCode() {
        return Objects.hash(player1pos, player1score, player2pos, player2score, playerTurn);
    }

    public void increaseCount(long count) {
        this.count += count;
    }
}
