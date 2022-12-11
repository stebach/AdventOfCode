package li.ste.adventofcode.year2022.day11;

import li.ste.adventofcode.utils.AdventOfCodeException;

import java.util.ArrayList;
import java.util.List;

public class Monkey {
    private List<Long> items = new ArrayList<>();
    private char operation;
    private boolean operationAgainstOld;
    private long operationNumber;
    private int testDivisableBy;
    private int targetTrue;
    private int targetFalse;
    private int inspectionCount;
    private boolean noRelief;
    private long commonMultiple;

    public void setStartingItems(long[] startingItems) {
        for (long startingItem : startingItems) {
            items.add(startingItem);
        }
    }

    public void setOperation(char operation) {
        this.operation = operation;
        this.operationAgainstOld = true;
    }

    public void setOperation(char operation, int number) {
        this.operation = operation;
        this.operationNumber = number;
    }

    public void setTest(int number) {
        testDivisableBy = number;
    }

    public void setTrueTarget(int number) {
        targetTrue = number;
    }
    public void setFalseTarget(int number) {
        targetFalse = number;
    }

    public void throwItems(List<Monkey> monkeys) {
        while (!items.isEmpty()) {
            Long item = items.remove(0);
            long number = operationNumber;
            if (operationAgainstOld) {
                number = item;
            }

            inspectionCount ++;

            switch (operation) {
                case '*' -> item *= number;
                case '+' -> item += number;
                default -> throw new AdventOfCodeException("unknwon operation: " + operation);
            }

            if (!noRelief) {
                item = Math.floorDiv(item, 3);
            } else {
                if (item % commonMultiple == 0) {
                    item = commonMultiple;
                } else {
                    item = item % commonMultiple;
                }
            }

            if (item % testDivisableBy == 0) {
                monkeys.get(targetTrue).getNewItem(item);
            } else {
                monkeys.get(targetFalse).getNewItem(item);
            }


        }
    }

    private void getNewItem(long item) {
        items.add(item);
    }

    public int getInspections() {
        return inspectionCount;
    }

    public Monkey withoutRelief() {
        Monkey retVal = new Monkey();
        retVal.items = new ArrayList<>(items);
        retVal.operation = operation;
        retVal.operationAgainstOld = operationAgainstOld;
        retVal.operationNumber = operationNumber;
        retVal.testDivisableBy = testDivisableBy;
        retVal.targetTrue = targetTrue;
        retVal.targetFalse = targetFalse;
        retVal.inspectionCount = inspectionCount;
        retVal.commonMultiple = commonMultiple;
        retVal.noRelief = true;

        return retVal;
    }

    public void setCommonMultiple(long commonMultiple) {
        this.commonMultiple = commonMultiple;
    }
}
