package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.TestInputProvider;
import org.junit.jupiter.api.DisplayNameGeneration;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

@DisplayNameGeneration(li.ste.adventofcode.DisplayNameGenerator.class)

public class TestDay18 {
    private static Day18 day;

    @BeforeAll
    public static void prepareTest() {
        day = new Day18(new TestInputProvider());
        day.run();
    }

    @Test
    void parseTest() {
        String testInput = "[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]";
        Day18.SnailfishNumber test = new Day18.SnailfishNumber(testInput);
        assertEquals(testInput, test.toString());
    }

    @Test
    void simpleSumTest() {
        Day18.SnailfishNumber num1 = new Day18.SnailfishNumber("[1,2]");
        Day18.SnailfishNumber num2 = new Day18.SnailfishNumber("[[3,4],5]");
        assertEquals("[[1,2],[[3,4],5]]", num1.add(num2).toString());
    }

    @Test
    void simpleExplodeTest() {
        Day18.SnailfishNumber explode1 = new Day18.SnailfishNumber("[[[[[9,8],1],2],3],4]");
        assertEquals("[[[[0,9],2],3],4]", explode1.toString());

        Day18.SnailfishNumber explode2 = new Day18.SnailfishNumber("[7,[6,[5,[4,[3,2]]]]]");
        assertEquals("[7,[6,[5,[7,0]]]]", explode2.toString());

        Day18.SnailfishNumber explode3 = new Day18.SnailfishNumber("[[6,[5,[4,[3,2]]]],1]");
        assertEquals("[[6,[5,[7,0]]],3]", explode3.toString());

        Day18.SnailfishNumber explode4 = new Day18.SnailfishNumber("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]");
        assertEquals("[[3,[2,[8,0]]],[9,[5,[7,0]]]]", explode4.toString());

    }


    @Test
    void listAddTests() {
        Day18.SnailfishNumber num1 = new Day18.SnailfishNumber("[[[[4,3],4],4],[7,[[8,4],9]]]");
        Day18.SnailfishNumber num2 = new Day18.SnailfishNumber("[1,1]");

        assertEquals("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]", num1.add(num2).toString());

        Day18.SnailfishNumber num3 = new Day18.SnailfishNumber("[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]");
        Day18.SnailfishNumber num4 = new Day18.SnailfishNumber("[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]");
        Day18.SnailfishNumber num5 = new Day18.SnailfishNumber("[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]");
        Day18.SnailfishNumber num6 = new Day18.SnailfishNumber("[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]");
        Day18.SnailfishNumber num7 = new Day18.SnailfishNumber("[7,[5,[[3,8],[1,4]]]]");
        Day18.SnailfishNumber num8 = new Day18.SnailfishNumber("[[2,[2,2]],[8,[8,1]]]");
        Day18.SnailfishNumber num9 = new Day18.SnailfishNumber("[2,9]");
        Day18.SnailfishNumber num10 = new Day18.SnailfishNumber("[1,[[[9,3],9],[[9,0],[0,7]]]]");
        Day18.SnailfishNumber num11 = new Day18.SnailfishNumber("[[[5,[7,4]],7],1]");
        Day18.SnailfishNumber num12 = new Day18.SnailfishNumber("[[[[4,2],2],6],[8,7]]");

        assertEquals("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]", num3.add(num4).add(num5).add(num6).add(num7).add(num8).add(num9).add(num10).add(num11).add(num12).toString());
    }

   @Test
    void magnitudeTests() {
        assertEquals(143, new Day18.SnailfishNumber("[[1,2],[[3,4],5]]").getMagnitude());
        assertEquals(1384, new Day18.SnailfishNumber("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]").getMagnitude());
        assertEquals(445, new Day18.SnailfishNumber("[[[[1,1],[2,2]],[3,3]],[4,4]]").getMagnitude());
        assertEquals(791, new Day18.SnailfishNumber("[[[[3,0],[5,3]],[4,4]],[5,5]]").getMagnitude());
        assertEquals(1137, new Day18.SnailfishNumber("[[[[5,0],[7,4]],[5,5]],[6,6]]").getMagnitude());
        assertEquals(3488, new Day18.SnailfishNumber("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]").getMagnitude());
    }

    @Test
    void testSolution1() {
        assertEquals("4140", day.getSolution1());
    }

    @Test
    void testSolution2() {
        assertEquals("3993", day.getSolution2());
    }
}
