package li.ste.adventofcode;

import org.junit.jupiter.api.DisplayNameGeneration;
import org.junit.platform.suite.api.ExcludeClassNamePatterns;
import org.junit.platform.suite.api.ExcludeTags;
import org.junit.platform.suite.api.SelectPackages;

@org.junit.platform.suite.api.Suite
@SelectPackages({"li.ste.adventofcode"})
@DisplayNameGeneration(li.ste.adventofcode.DisplayNameGenerator.class)

public class Suite {
}
