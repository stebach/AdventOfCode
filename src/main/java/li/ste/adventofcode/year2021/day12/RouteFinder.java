package li.ste.adventofcode.year2021.day12;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class RouteFinder {
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
