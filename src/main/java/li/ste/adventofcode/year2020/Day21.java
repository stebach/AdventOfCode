package li.ste.adventofcode.year2020;

import li.ste.adventofcode.utils.AdventOfCodeException;
import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day21 extends Day {
    public static void main(String[] args) {
        Day day = new Day21(new InputProvider());
        day.solvePuzzles();
    }

    public Day21(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        Scanner scanner = getScanner();
        Pattern ingredientsAndAllergensPattern = Pattern.compile("^(.+) \\(contains ([^\\)]+)\\)$");
        Matcher matcher;
        Set<String> ingredients = new HashSet<>();
        Map<String, List<String>> allergens = new HashMap<>();
        Map<List<String>, List<String>> ingredientsList = new HashMap<>();
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            matcher = ingredientsAndAllergensPattern.matcher(line);
            if (!matcher.find()) {
                throw new AdventOfCodeException("NO MATCH FOR : " + line);
            } else {
                ingredientsList.put(Arrays.stream(matcher.group(1).split(" ")).toList(), Arrays.stream(matcher.group(0).split(", ")).toList());
                ingredients.addAll(Arrays.stream(matcher.group(1).split(" ")).toList());
                for (String allergen : matcher.group(2).split(", ")) {
                    if (allergens.containsKey(allergen)) {
                        allergens.get(allergen).retainAll(Arrays.stream(matcher.group(1).split(" ")).toList());
                    } else {
                        allergens.put(allergen, new ArrayList<>(Arrays.stream(matcher.group(1).split(" ")).toList()));
                    }
                }
            }
        }

        Set<String> cleanIngredients = new HashSet<>(ingredients);

        for (List<String> value : allergens.values()) {
            cleanIngredients.removeAll(value);
        }

        int solution1 = 0;
        Set<String> filteredList = new HashSet<>();
        for (Map.Entry<List<String>, List<String>> listEntry : ingredientsList.entrySet()) {
            filteredList.clear();
            filteredList.addAll(listEntry.getKey());
            filteredList.retainAll(cleanIngredients);
            solution1 += filteredList.size();
        }

        setSolution1(solution1);

        int max = 1000;
        while (allergens.values().stream().mapToInt(List::size).max().getAsInt() > 1 && max-- > 0) {
            List<String> found = allergens.values().stream().filter(r -> r.size() == 1).map(r -> r.get(0)).toList();
            for (String f : found) {
                for (List<String> value : allergens.values()) {
                    if (value.size() > 1) {
                        value.remove(f);
                    }
                }
            }
        }



        setSolution2(String.join(",", allergens.entrySet().stream().sorted(Map.Entry.comparingByKey()).map(r->r.getValue().get(0)).toList()));
    }
}
