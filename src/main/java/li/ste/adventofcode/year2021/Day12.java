package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.year2021.day12.MapLocation;
import li.ste.adventofcode.year2021.day12.RouteEntry;
import li.ste.adventofcode.year2021.day12.RouteFinder;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Day12 extends Day {
    public static void main(String[] args) {
        Day day = new Day12(new InputProvider());
        day.solvePuzzles();
    }

    public Day12(InputProvider provider) {
        super(provider);
    }

    private final Map<String, MapLocation> locationHashMap = new HashMap<>();

    @Override
    public void run() {
        List<RouteEntry> routeEntryList = getRegexData("^([^\\-]+)\\-([^\\-]+)$", RouteEntry.class);
        for (RouteEntry routeEntry : routeEntryList) {
            locationHashMap.putIfAbsent(routeEntry.getFrom(), new MapLocation());
            locationHashMap.putIfAbsent(routeEntry.getTo(), new MapLocation());

            locationHashMap.get(routeEntry.getFrom()).addRoute(routeEntry.getTo());
            locationHashMap.get(routeEntry.getTo()).addRoute(routeEntry.getFrom());
        }

        RouteFinder routeFinder = new RouteFinder();
        routeFinder.findRoutes(locationHashMap, "start", "end", false);

        RouteFinder routeFinder2 = new RouteFinder();
        routeFinder2.findRoutes(locationHashMap, "start", "end", true);

        setSolution1(routeFinder.getCount());
        setSolution2(routeFinder2.getCount());
    }
}
