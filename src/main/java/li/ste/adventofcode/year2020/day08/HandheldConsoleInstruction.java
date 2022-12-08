package li.ste.adventofcode.year2020.day08;

import li.ste.adventofcode.utils.AdventOfCodeException;
import li.ste.adventofcode.utils.RegexResultRecipient;

import java.util.concurrent.atomic.AtomicInteger;

public class HandheldConsoleInstruction implements RegexResultRecipient {
    private String operator;
    private int value;
    private boolean executed;

    @Override
    public void setRegexResult(String[] listEntry) {
        operator = listEntry[0];
        value = Integer.parseInt(listEntry[1]);
    }

    public boolean execute(AtomicInteger acc, AtomicInteger pointer) {
        if (executed) {
            return false;
        }
        executed = true;
        switch (operator) {
            case "jmp":
                pointer.addAndGet(value - 1);
                break;
            case "acc":
                acc.addAndGet(value);
                break;
            case "nop":
                // no operation
                break;
            default:
                throw new AdventOfCodeException("unknown operator: " + operator);
        }
        pointer.incrementAndGet();
        return true;
    }

    public boolean switchNopJmp() {
        if ("jmp".equals(operator)) {
            operator = "nop";
            return true;
        } else if ("nop".equals(operator)) {
            operator = "jmp";
            return true;
        }
        return false;
    }

    public void reset() {
        executed = false;
    }
}
