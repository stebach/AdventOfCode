package li.ste.adventofcode.year2022.day07;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class FileSystemFolder {
    private final FileSystemFolder parent;
    private final Map<String, FileSystemFolder> subfolders = new HashMap<>();
    private final HashMap<String, Long> files = new HashMap<>();
    private long totalSize;

    public FileSystemFolder(FileSystemFolder parentFolder) {
        parent = parentFolder;
    }

    public FileSystemFolder() {
        parent = null;
    }

    public List<FileSystemFolder> getFoldersWithMaxSize(int maxSize) {
        List<FileSystemFolder> retVal = new ArrayList<>();
        if (getSize() <= maxSize) {
            retVal.add(this);
        }
        for (FileSystemFolder subfolder : subfolders.values()) {
            retVal.addAll(subfolder.getFoldersWithMaxSize(maxSize));
        }
        return retVal;
    }

    public List<FileSystemFolder> getFoldersWithMinSize(long minSize) {
        List<FileSystemFolder> retVal = new ArrayList<>();
        if (getSize() >= minSize) {
            retVal.add(this);
        }
        for (FileSystemFolder subfolder : subfolders.values()) {
            retVal.addAll(subfolder.getFoldersWithMinSize(minSize));
        }
        return retVal;
    }


    public FileSystemFolder goToFolder(String folder) {
        subfolders.putIfAbsent(folder, new FileSystemFolder(this));
        return subfolders.get(folder);
    }

    public FileSystemFolder goToParent() {
        return parent;
    }

    public FileSystemFolder goToRoot() {
        FileSystemFolder folder = this;
        while (folder.goToParent() != null) {
            folder = folder.goToParent();
        }
        return folder;
    }

    public void addFile(String name, long size) {
        files.put(name, size);
        totalSize += size;
    }

    public long getSize() {
        long retVal = totalSize;
        for (FileSystemFolder folder : subfolders.values()) {
            retVal += folder.getSize();
        }
        return retVal;
    }

}
