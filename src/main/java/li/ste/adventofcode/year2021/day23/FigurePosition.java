package li.ste.adventofcode.year2021.day23;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class FigurePosition {
    private final List<Integer> positions;
    private int cost;
    private FigurePosition parent;

    public FigurePosition(List<Integer> positions) {
        this.positions = positions;
    }

    public int figureAtPosition(int position) {
        return positions.get(position);
    }

    public FigurePosition clone() {
        return new FigurePosition(new ArrayList<>(positions));
    }

    public void addCost(FigurePosition newParent, int costToAdd) {
        if (parent == null || newParent.getCost() + costToAdd < parent.getCost() + cost) {
            parent = newParent;
            cost += costToAdd;
        }
    }

    public void setFigureAtPosition(int target, int figure) {
        positions.set(target, figure);
    }

    public int getCost() {
        if (parent == null) {
            return 0;
        }
        return cost + parent.getCost();
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        FigurePosition that = (FigurePosition) o;
        return positions.equals(that.positions);
    }

    @Override
    public int hashCode() {
        return Objects.hash(positions);
    }
}
