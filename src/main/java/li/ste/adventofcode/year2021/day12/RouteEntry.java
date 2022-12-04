package li.ste.adventofcode.year2021.day12;

import li.ste.adventofcode.utils.RegexResultRecipient;

public class RouteEntry implements RegexResultRecipient {
    private String from;
    private String to;

    @Override
    public void setRegexResult(String[] listEntry) {
        from = listEntry[0];
        to = listEntry[1];
    }

    public String getFrom() {
        return from;
    }
    public String getTo() {
        return to;
    }
}
