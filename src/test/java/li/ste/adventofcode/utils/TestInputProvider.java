package li.ste.adventofcode.utils;

import java.nio.file.Path;

public class TestInputProvider extends InputProvider {

    @Override
    protected Path getPath(String[] attributes) {
        return super.getPath(new String[] {
                attributes[0],
                "Test" + attributes[1]
        });
    }
}
