package li.ste.adventofcode.year2021.day18;

import java.util.ArrayList;
import java.util.List;

public class Parentable {

    private Parentable parent;
    private final List<Parentable> children = new ArrayList<>();

    protected Parentable getParent() {
        return parent;
    }

    protected void setParent(Parentable parent) {
        this.parent = parent;
        this.parent.children.add(this);
    }

    protected void replacePart(Parentable oldChild, Parentable newChild) {
        int pos = children.indexOf(oldChild);
        children.set(pos, newChild);
        newChild.parent = this;
    }

    protected Parentable getChild(int i) {
        return children.get(i);
    }
}
