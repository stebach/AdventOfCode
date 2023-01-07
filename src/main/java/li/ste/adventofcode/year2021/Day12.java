package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.Day;
import li.ste.adventofcode.utils.InputProvider;
import li.ste.adventofcode.utils.RegexResultRecipient;

import java.util.ArrayList;
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

    private class MapLocation {
        private final List<String> routes = new ArrayList<>();

        public void addRoute(String targetName) {
            routes.add(targetName);
        }

        public List<String> getRoutes() {
            return routes;
        }
    }

    private class RouteEntry implements RegexResultRecipient {
        private String from;
        private String to;

        @Override
        public void setRegexResult(String[] listEntry) {
            from = listEntry[0];
            to = listEntry[1];
        }

        public String getFrom() {
            return from;
        }
        public String getTo() {
            return to;
        }
    }

    private class RouteFinder {
        private int count;
        private final List<String> routeNames = new ArrayList<>();
        private Map<String, MapLocation> locations;
        private boolean doubleAllowed;
        private boolean doubleUsed;

        public int getCount() {
            return count;
        }

        public void findRoutes(Map<String, MapLocation> locationHashMap, String start, String end, boolean doubleAllowed) {
            locations = locationHashMap;
            routeNames.add(start);
            this.doubleAllowed = doubleAllowed;
            lookForEnd(locations.get(start), end, start);
        }

        private void lookForEnd(MapLocation current, String end, String start) {
            for (String route : current.getRoutes()) {
                // check for end
                if (route.equals(end)) {
                    count++;
                } else if (
                        (route.toCharArray()[0] >= 'A' && route.toCharArray()[0] <= 'Z')
                                || (!route.equals(start) && (!routeNames.contains(route) || (!doubleUsed && doubleAllowed)))
                ) {
                    boolean useDouble = (route.toCharArray()[0] >= 'a' && route.toCharArray()[0] <= 'z') && !route.equals(start) && routeNames.contains(route);

                    doubleUsed = doubleUsed || useDouble;

                    routeNames.add(route);
                    lookForEnd(locations.get(route), end, start);
                    routeNames.remove(routeNames.size()-1);


                    if (useDouble) {
                        doubleUsed = false;
                    }
                }
            }
        }
    }
}
