package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.year2021.day10.ChunkLine;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Day10 extends Day {
    public static void main(String[] args) {
        Day day = new Day10(new InputProvider());
        day.solvePuzzles();
    }

    public Day10(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        int score = 0;
        List<Long> autocompleteScore = new ArrayList<>();
        for(String line: getData()) {
            ChunkLine chunkLine = new ChunkLine(line);
            score += chunkLine.getScore();
            long missingScore = chunkLine.getMissingScore();
            if (missingScore > 0) {
                autocompleteScore.add(missingScore);
            }
        }

        Collections.sort(autocompleteScore);

        setSolution1(score);
        setSolution2(autocompleteScore.get((autocompleteScore.size()-1)/2));
    }
}
