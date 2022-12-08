package li.ste.adventofcode.utils;

import java.lang.reflect.InvocationTargetException;
import java.util.*;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public abstract class Day {

    private final List<String> data;
    private List<Integer> intData;
    private List<Integer> binData;
    private String solution1;
    private String solution2;

    public abstract void run();

    protected Day(InputProvider provider) {
        data = provider.loadData(getClassNameLastPart());
    }

    private String[] getClassNameLastPart() {
        String[] classParts = getClass().toString().split("\\.");
        return new String[] {
                classParts[classParts.length - 2].substring(4),
                classParts[classParts.length - 1]
        };
    }

    public List<String> getData() {
        return data;
    }

    protected List<Integer> getIntData() {
        if (intData == null) {
            intData = new ArrayList<>();
            for (String line : data) {
                intData.add(Integer.parseInt(line, 10));
            }
         }
        return intData;
    }

    protected List<Integer> getBinaryData() {
        if (binData == null) {
            binData = new ArrayList<>();
            for (String line : data) {
                binData.add(Integer.parseInt(line, 2));
            }
         }
        return binData;
    }

    protected <T extends RegexResultRecipient> List<T> getRegexData(String patternString, Class<T> type) {
        List<T> retVal = new ArrayList<>();
        Pattern pattern = Pattern.compile(patternString);
        for (String line : getData()) {
            Matcher matcher = pattern.matcher(line);
            if (matcher.find()) {
                String[] newListEntry = new String[matcher.groupCount()];
                for (int i=0; i<matcher.groupCount(); i++) {
                    newListEntry[i] = matcher.group(i+1);
                }

                T newResult;
                try {
                    newResult = type.getConstructor().newInstance();
                    newResult.setRegexResult(newListEntry);
                    retVal.add(newResult);
                } catch (InstantiationException|IllegalAccessException|InvocationTargetException|NoSuchMethodException e) {
                    throw new AdventOfCodeException(e);
                }
            } else {
                throw new AdventOfCodeException("no result for matcher!");
            }
        }
        return retVal;
    }

    @java.lang.SuppressWarnings("java:S106")
    protected void out(String message) {
        System.out.println(message);
    }

    protected void out(int message) {
        out(String.valueOf(message));
    }

    public void solvePuzzles() {
        run();
        if (!"@todo".equals(getSolution1())) {
            out("solution 1: " + getSolution1());
            out("solution 2: " + getSolution2());
        }
    }

    public String getSolution1() {
        return solution1;
    }
    public String getSolution2() {
        return solution2;
    }

    protected void setSolution1(String solution) {
        solution1 = solution;
    }
    protected void setSolution1(int solution) {
        solution1 = Integer.toString(solution);
    }

    protected void setSolution1(long solution) {
        solution1 = Long.toString(solution);
    }
    protected void setSolution1(AtomicInteger solution) {
        solution1 = solution.toString();
    }
    protected void setSolution2(String solution) {
        solution2 = solution;
    }
    protected void setSolution2(int solution) {
        solution2 = Integer.toString(solution);
    }
    protected void setSolution2(long solution) {
        solution2 = Long.toString(solution);
    }

    protected void setSolution2(AtomicInteger solution) {
        solution2 = solution.toString();
    }
}