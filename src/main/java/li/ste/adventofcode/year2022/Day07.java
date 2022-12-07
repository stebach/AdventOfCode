package li.ste.adventofcode.year2022;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.year2022.day07.FileSystemFolder;

import java.util.Comparator;
import java.util.List;

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
        FileSystemFolder fs = parseData();

        List<FileSystemFolder> folderWithMaxSize100000 = fs.getFoldersWithMaxSize(100000);
        long solution1 = 0;
        for (FileSystemFolder fileSystemFolder : folderWithMaxSize100000) {
            solution1 += fileSystemFolder.getSize();
        }
        setSolution1(solution1);

        List<FileSystemFolder> potentialFoldersToDelete = fs.getFoldersWithMinSize(
                30000000 - (70000000 - fs.getSize()));
        potentialFoldersToDelete.sort(Comparator.comparingLong(FileSystemFolder::getSize));

        setSolution2(potentialFoldersToDelete.get(0).getSize());
    }

    private FileSystemFolder parseData() {
        List<String> data = getData();
        FileSystemFolder fs = new FileSystemFolder();
        FileSystemFolder currentFolder = fs;
        for (int i=0; i<data.size(); i++) {
            String[] line = data.get(i).split(" ");
            if ("cd".equals(line[1])) {
                if ("/".equals(line[2])) {
                    currentFolder = currentFolder.goToRoot();
                } else if ("..".equals(line[2])) {
                    currentFolder = currentFolder.goToParent();
                } else {
                    currentFolder = currentFolder.goToFolder(line[2]);
                }
            } else if ("ls".equals(line[1])) {
                for (int j=i+1; j<data.size(); j++) {
                    i++;
                    if (data.get(j).charAt(0) == '$') {
                        i--;
                        break;
                    }
                    String[] file = data.get(j).split(" ");
                    if (!"dir".equals(file[0])) {
                        currentFolder.addFile(file[1], Long.parseLong(file[0], 10));
                    }
                }
            }
        }
        return fs;
    }
}
