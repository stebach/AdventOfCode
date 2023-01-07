package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.utils.RegexResultRecipient;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class Day21 extends Day {
    public static void main(String[] args) {
        Day day = new Day21(new InputProvider());
        day.solvePuzzles();
    }

    public Day21(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        List<PlayerStart> data = getRegexData("^Player [1-2] starting position: ([0-9]+)$", PlayerStart.class);

        Die deterministicDie = new DeterministicDie();

        List<Player> playerList = new ArrayList<>();
        Player player1 = new Player();
        player1.setPos(data.get(0).getPosition());
        player1.setDie(deterministicDie);
        playerList.add(player1);
        Player player2 = new Player();
        player2.setPos(data.get(1).getPosition());
        player2.setDie(deterministicDie);
        playerList.add(player2);

        while (true) {
            Player currentPlayer = playerList.remove(0);
            currentPlayer.play();
            playerList.add(currentPlayer);
            if (currentPlayer.won()) {
                break;
            }
        }

        Player looser = playerList.get(0);


        setSolution1(looser.getScore() * deterministicDie.getRollCount());

        GameState state = new GameState(data.get(0).getPosition(), data.get(1).getPosition());

        List<GameState> states = new ArrayList<>();
        states.add(state);

        long player1wins = 0;
        long player2wins = 0;


        while (!states.isEmpty()) {
            GameState currentState = states.remove(0);
            List<GameState> newStates = currentState.play();
            for (GameState newState : newStates) {
                if (newState.player1won()) {
                    player1wins += newState.getCount();
                } else if (newState.player2won()) {
                    player2wins += newState.getCount();
                } else {
                    int index = states.indexOf(newState);
                    if (index > -1) {
                        states.get(index).increaseCount(newState.getCount());
                    } else {
                        states.add(newState);
                    }
                }
            }
        }

        setSolution2(Math.max(player1wins, player2wins));
    }

    private class GameState {
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

    private class PlayerStart implements RegexResultRecipient {
        private int playerPos;

        @Override
        public void setRegexResult(String[] listEntry) {
            playerPos = Integer.parseInt(listEntry[0]);
        }

        public int getPosition() {
            return playerPos;
        }
    }

    private abstract class Die {
        public abstract DieResult throwDie();

        public abstract int getRollCount();
    }

    private class DieResult {
        private final int movement;

        public DieResult(int movement) {
            this.movement = movement;
        }

        public int getMovement() {
            return movement;
        }
    }

    private class Player {
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

    private class DeterministicDie extends Die {
        int next = 0;
        int rollCount = 0;
        @Override
        public DieResult throwDie() {
            int roll = getNext() + getNext() + getNext();
            return new DieResult(roll);
        }

        @Override
        public int getRollCount() {
            return rollCount;
        }

        private int getNext() {
            next ++;
            if (next > 100) {
                next = 1;
            }
            rollCount ++;
            return next;
        }
    }
}
