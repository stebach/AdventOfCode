package li.ste.adventofcode.year2020.day02;

import li.ste.adventofcode.utils.RegexResultRecipient;

public class PasswordEntry implements RegexResultRecipient {
    private String password;
    private int minCount;
    private int maxCount;
    private char character;

    @Override
    public void setRegexResult(String[] listEntry) {
        minCount = Integer.parseInt(listEntry[0]);
        maxCount = Integer.parseInt(listEntry[1]);
        character = listEntry[2].charAt(0);
        password = listEntry[3];
    }

    public boolean isValid() {
        long count = password.chars().filter(c -> c == character).count();
        return count >= minCount && count <= maxCount;
    }

    public boolean isValid2() {
        return (password.charAt(minCount-1) == character ? 1 : 0) + (password.charAt(maxCount-1) == character ? 1 : 0) == 1;
    }
}
