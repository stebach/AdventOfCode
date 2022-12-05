package li.ste.adventofcode.year2020;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day04 extends Day {
    private Pattern patternHgt;
    private Pattern patternHcl;
    private Pattern patternPid;

    public static void main(String[] args) {
        Day day = new Day04(new InputProvider());
        day.solvePuzzles();
    }

    public Day04(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        List<String> requiredAttributes = new ArrayList<>(Arrays.asList(
            "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"
        ));

        List<String> data = getData();
        data.add(""); // make sure an empty line is the last entry

        patternHgt = Pattern.compile("^([0-9]+)(cm|in)$");
        patternHcl = Pattern.compile("^#[0-9a-f]{6}$");
        patternPid = Pattern.compile("^[0-9]{9}$");

        Map<String, String> requiredDocumentAttributes = new HashMap<>();
        int validCount = 0;
        int validCount2 = 0;
        for (String row : data) {
            if (row.length() == 0) {
                if (requiredDocumentAttributes.keySet().size() == requiredAttributes.size()) {
                    validCount ++;
                    validCount2 += checkByr(requiredDocumentAttributes.get("byr"))
                            && checkIyr(requiredDocumentAttributes.get("iyr"))
                            && checkEyr(requiredDocumentAttributes.get("eyr"))
                            && checkHgt(requiredDocumentAttributes.get("hgt"))
                            && checkHcl(requiredDocumentAttributes.get("hcl"))
                            && checkEcl(requiredDocumentAttributes.get("ecl"))
                            && checkPid(requiredDocumentAttributes.get("pid")) ? 1 : 0;
                }
                requiredDocumentAttributes = new HashMap<>();
            } else {
                String[] parts = row.split(" ");
                for (String part : parts) {
                    String[] attribute = part.split(":", 2);
                    if (requiredAttributes.contains(attribute[0])) {
                        requiredDocumentAttributes.put(attribute[0], attribute[1]);
                    }
                }
            }
        }
        
        setSolution1(validCount);
        setSolution2(validCount2);
    }

    private boolean checkPid(String attribute) {
        return patternPid.matcher(attribute).find();
    }

    private boolean checkEcl(String attribute) {
        return Arrays.asList("amb","blu","brn","gry","grn","hzl","oth").contains(attribute);
    }

    private boolean checkHcl(String attribute) {
        return patternHcl.matcher(attribute).find();
    }

    private boolean checkHgt(String attribute) {
        Matcher matcher = patternHgt.matcher(attribute);
        if (matcher.find()) {
            int height = Integer.parseInt(matcher.group(1));
            String type = matcher.group(2);
            return ("cm".equals(type) && (height >= 150 && height <= 193)) ||
                    ("in".equals(type) && (height >= 59 && height <= 76));
        }
        return false;
    }

    private boolean checkEyr(String attribute) {
        int intVal = Integer.parseInt(attribute);
        return intVal >= 2020 && intVal <= 2030;
    }

    private boolean checkIyr(String attribute) {
        int intVal = Integer.parseInt(attribute);
        return intVal >= 2010 && intVal <= 2020;
    }

    private boolean checkByr(String attribute) {
        int intVal = Integer.parseInt(attribute);
        return intVal >= 1920 && intVal <= 2002;
    }
}
