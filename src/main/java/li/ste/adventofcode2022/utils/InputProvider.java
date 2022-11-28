package li.ste.adventofcode2022.utils;

import java.io.IOException;
import java.net.URISyntaxException;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

public class InputProvider {
    public List<String> loadData(String name) {
        Path path = getPath(name);
        try {
            return Files.readAllLines(path);
        } catch (IOException e) {
            throw new AdventOfCodeException(e);
        }
    }

    protected Path getPath(String name) {
        URL fileUrl = getClass().getResource("/" + name + ".txt");
        if (fileUrl == null) {
            throw new AdventOfCodeException("Ressource file for " + name + " not found!");
        }
        try {
            return Paths.get(fileUrl.toURI());
        } catch (URISyntaxException e) {
            throw new AdventOfCodeException(e);
        }
    }
}
