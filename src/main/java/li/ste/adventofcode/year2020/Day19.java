package li.ste.adventofcode.year2020;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day19 extends Day {
    public static void main(String[] args) {
        Day day = new Day19(new InputProvider());
        day.solvePuzzles();
    }

    public Day19(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        Scanner scanner = getScanner();
        Map<String, String> rawRules = new HashMap<>();
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            if (line.length() == 0) {
                break;
            }
            String[] parts = line.split(": ", 2);
            rawRules.put(parts[0], parts[1]);
        }
        List<String> lines = new ArrayList<>();
        while (scanner.hasNextLine()) {
            lines.add(scanner.nextLine());
        }

        Map<String, String> compiledRules = new HashMap<>();
        Pattern pattern = Pattern.compile("^" + compileRules(rawRules, compiledRules, "0") + "$");

        Matcher matcher;
        int matches = 0;
        for (String line : lines) {
            matcher = pattern.matcher(line);
            if (matcher.find()) {
                matches += 1;
            }
        }
        setSolution1(matches);

        compiledRules = new HashMap<>();
        compileRules(rawRules, compiledRules, "42");
        compileRules(rawRules, compiledRules, "31");
        compiledRules.put("11", compiledRules.get("42") + "(" + compiledRules.get("42") + "(" + compiledRules.get("42") + "(" + compiledRules.get("42") + "(" + compiledRules.get("42") + "(" + compiledRules.get("42") + "(" + compiledRules.get("42") + "(" + compiledRules.get("42") + compiledRules.get("31") + ")?" + compiledRules.get("31") + ")?" + compiledRules.get("31") + ")?" + compiledRules.get("31") + ")?" + compiledRules.get("31") + ")?" + compiledRules.get("31") + ")?" + compiledRules.get("31") + ")?" + compiledRules.get("31"));
        compiledRules.put("8", "(" + compiledRules.get("42") + ")+");

        pattern = Pattern.compile("^" + compileRules(rawRules, compiledRules, "0") + "$");
        matches = 0;
        for (String line : lines) {
            matcher = pattern.matcher(line);
            if (matcher.find()) {
                matches += 1;
            }
        }

        setSolution2(matches);
    }

    private String compileRules(Map<String, String> rawRules, Map<String, String> compiledRules, String key) {
        if (!compiledRules.containsKey(key)) {
            if (rawRules.get(key).charAt(0) == '"') {
                compiledRules.put(key, rawRules.get(key).substring(1,2));
            } else {
                String[] parts = rawRules.get(key).split(" \\| ");
                for (int i = 0; i < parts.length; i++) {
                    String[] parts2 = parts[i].split(" ");
                    StringBuilder compiled = new StringBuilder();
                    for (String s : parts2) {
                        compiled.append(compileRules(rawRules, compiledRules, s));
                    }
                    parts[i] = compiled.toString();
                }
                if (parts.length > 1) {
                    compiledRules.put(key, "(" + String.join("|", parts) + ")");
                } else {
                    compiledRules.put(key, parts[0]);
                }
            }
        }
        return compiledRules.get(key);
    }
}
