package li.ste.adventofcode.utils;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.net.URISyntaxException;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.Scanner;

public class InputProvider {
    public List<String> loadData(String[] attributes) {
        Path path = getPath(attributes);
        try {
            return Files.readAllLines(path);
        } catch (IOException e) {
            throw new AdventOfCodeException(e);
        }
    }

    protected Path getPath(String[] attributes) {
        URL fileUrl = getClass().getResource("/" + attributes[0] + "/" + attributes[1] + ".txt");
        if (fileUrl == null) {
            throw new AdventOfCodeException("Ressource file for " + attributes[0] + "/" + attributes[1] + " not found!");
        }
        try {
            return Paths.get(fileUrl.toURI());
        } catch (URISyntaxException e) {
            throw new AdventOfCodeException(e);
        }
    }

    public Scanner getScanner(String[] attributes) {
        Path path = getPath(attributes);
        try {
            return new Scanner(path.toFile());
        } catch (FileNotFoundException e) {
            throw new AdventOfCodeException(e);
        }
    }
}
