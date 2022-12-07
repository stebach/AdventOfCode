package li.ste.adventofcode.year2022;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;

import java.util.*;
import java.util.concurrent.atomic.AtomicLong;

public class Day07 extends Day {
    public static void main(String[] args) {
        Day day = new Day07(new InputProvider());
        day.solvePuzzles();
    }

    public Day07(InputProvider provider) {
        super(provider);
    }

    @Override
    public void run() {
        Map<String, Long> folderSizes = parseData();


        long solution1 = 0;
        long solution2 = Long.MAX_VALUE;
        long minSizeForSolution2 = 30000000 - (70000000 - folderSizes.get("/"));
        for (Long value : folderSizes.values()) {
            if (value <= 100000) {
                solution1 += value;
            }
            if (value < solution2 && value >= minSizeForSolution2) {
                solution2 = value;
            }
        }
        setSolution1(solution1);
        setSolution2(solution2);
    }

    private Map<String, Long> parseData() {
        List<String> data = getData();
        List<String> currentFolder = new ArrayList<>();
        Map<String, Long> folderSizes = new HashMap<>();
        folderSizes.put("/", 0L);

        for (int i=0; i<data.size(); i++) {
            String[] line = data.get(i).split(" ");
            if ("cd".equals(line[1])) {
                if ("/".equals(line[2])) {
                    currentFolder.clear();
                } else if ("..".equals(line[2])) {
                    currentFolder.remove(currentFolder.size()-1);
                } else {
                    currentFolder.add(line[2]);
                }
            } else if ("ls".equals(line[1])) {
                AtomicLong folderSize = new AtomicLong();
                for (int j=i+1; j<data.size(); j++) {
                    i++;
                    if (data.get(j).charAt(0) == '$') {
                        i--;
                        break;
                    }
                    String[] file = data.get(j).split(" ");
                    if (!"dir".equals(file[0])) {
                        folderSize.addAndGet(Long.parseLong(file[0], 10));
                    }
                }
                for (int j=currentFolder.size(); j>=0; j--) {
                    String folder = "/" + String.join("/", currentFolder.subList(0,j));
                    folderSizes.putIfAbsent(folder, 0L);
                    folderSizes.compute(folder, (k,v)->v +=  folderSize.longValue());
                }
            }
        }
        return folderSizes;
    }
}
