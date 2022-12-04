package li.ste.adventofcode.year2021.day21;

import li.ste.adventofcode.utils.RegexResultRecipient;

public class PlayerStart implements RegexResultRecipient {
    private int playerPos;

    @Override
    public void setRegexResult(String[] listEntry) {
        playerPos = Integer.parseInt(listEntry[0]);
    }

    public int getPosition() {
        return playerPos;
    }
}
