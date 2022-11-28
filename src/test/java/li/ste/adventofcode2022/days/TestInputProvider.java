package li.ste.adventofcode2022.days;

import li.ste.adventofcode2022.utils.InputProvider;

import java.nio.file.Path;

public class TestInputProvider extends InputProvider {

    @Override
    protected Path getPath(String name) {
        return super.getPath(name + "Test");
    }
}
