package li.ste.adventofcode.year2021.day12;

import java.util.ArrayList;
import java.util.List;

public class MapLocation {
    private final List<String> routes = new ArrayList<>();

    public void addRoute(String targetName) {
        routes.add(targetName);
    }

    public List<String> getRoutes() {
        return routes;
    }
}
