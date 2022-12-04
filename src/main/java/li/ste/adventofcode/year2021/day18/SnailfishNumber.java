package li.ste.adventofcode.year2021.day18;

import li.ste.adventofcode.utils.AdventOfCodeException;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class SnailfishNumber extends Parentable {
    List<SnailfishNumberNumberPart> allParts = new ArrayList<>();

    public SnailfishNumber(String input) {
        this(SnailfishNumber.prepareCharList(input));
    }

    private static List<Character> prepareCharList(String input) {
        List<Character> charList = input.chars().mapToObj(c -> (char) c).collect(Collectors.toList());
        charList.remove(0);
        charList.remove(charList.size()-1);
        return charList;
    }

    private SnailfishNumber(List<Character> input) {

        int level = 0;
        List<SnailfishNumberNumberPart> currentParts = new ArrayList<>();
        SnailfishNumberNumberPart nextPart;

        while (!input.isEmpty()) {
            Character nextChar = input.remove(0);
            switch (nextChar) {
                case '[':
                    level += 1;
                    nextPart = new SnailfishNumberNumberPartComplex();
                    nextPart.setLevel(level);
                    allParts.add(nextPart);

                    if (!currentParts.isEmpty()) {
                        nextPart.setParent(currentParts.get(currentParts.size()-1));
                    } else {
                        nextPart.setParent(this);
                    }

                    currentParts.add(nextPart);
                    break;
                case '0','1','2','3','4','5','6','7','8','9':
                    SnailfishNumberNumberPartSimple simplePart = new SnailfishNumberNumberPartSimple(nextChar - 48);
                    simplePart.setLevel(level);
                    if (!currentParts.isEmpty()) {
                        simplePart.setParent(currentParts.get(currentParts.size()-1));
                    } else {
                        simplePart.setParent(this);
                    }
                    allParts.add(simplePart);
                    break;
                case ',':
                    // ignore
                    break;
                case ']':
                    level -= 1;
                    currentParts.remove(currentParts.size()-1);
                    break;
                default:
                    throw new AdventOfCodeException("UNKNWON CHAR: " + nextChar);
            }
        }

        boolean repeat = true;
        while (repeat) {
            repeat = checkForExplosion() || checkForSplit();
        }
    }

    private boolean checkForSplit() {
        int splitPos = -1;
        for (int i=0; i<allParts.size(); i++) {
            if (allParts.get(i).shouldSplit()) {
                splitPos = i;
                break;
            }
        }

        if (splitPos > -1) {

            SnailfishNumberNumberPartSimple splitElement = (SnailfishNumberNumberPartSimple)allParts.get(splitPos);

            SnailfishNumberNumberPartSimple leftPart = new SnailfishNumberNumberPartSimple((int)Math.floor(splitElement.getValue()/2.0));
            SnailfishNumberNumberPartSimple rightPart = new SnailfishNumberNumberPartSimple((int)Math.ceil(splitElement.getValue()/2.0));
            leftPart.setLevel(splitElement.getLevel()+1);
            rightPart.setLevel(splitElement.getLevel()+1);


            SnailfishNumberNumberPartComplex newComplexPart = new SnailfishNumberNumberPartComplex();
            newComplexPart.setLevel(splitElement.getLevel()+1);

            leftPart.setParent(newComplexPart);
            rightPart.setParent(newComplexPart);


            allParts.add(splitPos+1, rightPart);
            allParts.add(splitPos+1, leftPart);
            allParts.set(splitPos, newComplexPart);

            splitElement.getParent().replacePart(splitElement, newComplexPart);

            return true;
        }
        return false;
    }

    private boolean checkForExplosion() {
        int explodingPos = -1;
        for (int i=0; i<allParts.size(); i++) {
            if (allParts.get(i).shouldExplode()) {
                explodingPos = i;
                break;
            }
        }

        if (explodingPos > -1) {

            SnailfishNumberNumberPartComplex explodingElement = (SnailfishNumberNumberPartComplex) allParts.get(explodingPos);

            for (int i=explodingPos -1; i>-1; i--) {
                if (allParts.get(i).getClass() == SnailfishNumberNumberPartSimple.class) {
                    ((SnailfishNumberNumberPartSimple)allParts.get(i)).increaseValue(
                            explodingElement.leftValue()
                    );
                    break;
                }
            }
            for (int i=explodingPos +3; i<allParts.size(); i++) {
                if (allParts.get(i).getClass() == SnailfishNumberNumberPartSimple.class) {
                    ((SnailfishNumberNumberPartSimple)allParts.get(i)).increaseValue(
                            explodingElement.rightValue()
                    );
                    break;
                }
            }

            SnailfishNumberNumberPartSimple replacement = new SnailfishNumberNumberPartSimple(0);
            replacement.setLevel(explodingElement.getLevel()-1);
            replacement.setParent(explodingElement.getParent());

            explodingElement.getParent().replacePart(explodingElement, replacement);

            allParts.set(explodingPos, replacement);
            allParts.remove(explodingElement.getChild(0));
            allParts.remove(explodingElement.getChild(1));

            return true;
        }

        return false;
    }


    public SnailfishNumber add(SnailfishNumber num2) {
        return new SnailfishNumber("[" + this + "," + num2.toString() + "]");
    }

    public int getMagnitude() {
        return ((SnailfishNumberNumberPart)getChild(0)).getMagnitude() * 3 + ((SnailfishNumberNumberPart)getChild(1)).getMagnitude() * 2;
    }

    @Override
    public String toString() {
        return "[" + getChild(0).toString() +
                "," +
                getChild(1).toString() +
                "]";
    }
}