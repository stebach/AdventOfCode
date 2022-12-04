package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.year2021.day21.*;

import java.util.ArrayList;
import java.util.List;

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
}
