package li.ste.adventofcode.year2022.day04;

import li.ste.adventofcode.utils.RegexResultRecipient;

public class SectionRangePair implements RegexResultRecipient {
    private int from1;
    private int to1;
    private int from2;
    private int to2;

    @Override
    public void setRegexResult(String[] listEntry) {
        from1 = Integer.parseInt(listEntry[0]);
        to1 = Integer.parseInt(listEntry[1]);
        from2 = Integer.parseInt(listEntry[2]);
        to2 = Integer.parseInt(listEntry[3]);
    }

    public boolean firstContainsSecond() {
        return from1 <= from2 && to1 >= to2;
    }

    public boolean secondContainsFirst() {
        return from2 <= from1 && to2 >= to1;
    }

    public boolean overlaps() {
        return !(to1 < from2 || from1 > to2);
    }
}

