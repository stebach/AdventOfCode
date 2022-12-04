package li.ste.adventofcode.year2021;

import li.ste.adventofcode.utils.TestInputProvider;
import li.ste.adventofcode.year2021.day18.SnailfishNumber;
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
        SnailfishNumber test = new SnailfishNumber(testInput);
        assertEquals(testInput, test.toString());
    }

    @Test
    void simpleSumTest() {
        SnailfishNumber num1 = new SnailfishNumber("[1,2]");
        SnailfishNumber num2 = new SnailfishNumber("[[3,4],5]");
        assertEquals("[[1,2],[[3,4],5]]", num1.add(num2).toString());
    }

    @Test
    void simpleExplodeTest() {
        SnailfishNumber explode1 = new SnailfishNumber("[[[[[9,8],1],2],3],4]");
        assertEquals("[[[[0,9],2],3],4]", explode1.toString());

        SnailfishNumber explode2 = new SnailfishNumber("[7,[6,[5,[4,[3,2]]]]]");
        assertEquals("[7,[6,[5,[7,0]]]]", explode2.toString());

        SnailfishNumber explode3 = new SnailfishNumber("[[6,[5,[4,[3,2]]]],1]");
        assertEquals("[[6,[5,[7,0]]],3]", explode3.toString());

        SnailfishNumber explode4 = new SnailfishNumber("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]");
        assertEquals("[[3,[2,[8,0]]],[9,[5,[7,0]]]]", explode4.toString());

    }


    @Test
    void listAddTests() {
        SnailfishNumber num1 = new SnailfishNumber("[[[[4,3],4],4],[7,[[8,4],9]]]");
        SnailfishNumber num2 = new SnailfishNumber("[1,1]");

        assertEquals("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]", num1.add(num2).toString());

        SnailfishNumber num3 = new SnailfishNumber("[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]");
        SnailfishNumber num4 = new SnailfishNumber("[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]");
        SnailfishNumber num5 = new SnailfishNumber("[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]");
        SnailfishNumber num6 = new SnailfishNumber("[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]");
        SnailfishNumber num7 = new SnailfishNumber("[7,[5,[[3,8],[1,4]]]]");
        SnailfishNumber num8 = new SnailfishNumber("[[2,[2,2]],[8,[8,1]]]");
        SnailfishNumber num9 = new SnailfishNumber("[2,9]");
        SnailfishNumber num10 = new SnailfishNumber("[1,[[[9,3],9],[[9,0],[0,7]]]]");
        SnailfishNumber num11 = new SnailfishNumber("[[[5,[7,4]],7],1]");
        SnailfishNumber num12 = new SnailfishNumber("[[[[4,2],2],6],[8,7]]");

        assertEquals("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]", num3.add(num4).add(num5).add(num6).add(num7).add(num8).add(num9).add(num10).add(num11).add(num12).toString());
    }

   @Test
    void magnitudeTests() {
        assertEquals(143, new SnailfishNumber("[[1,2],[[3,4],5]]").getMagnitude());
        assertEquals(1384, new SnailfishNumber("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]").getMagnitude());
        assertEquals(445, new SnailfishNumber("[[[[1,1],[2,2]],[3,3]],[4,4]]").getMagnitude());
        assertEquals(791, new SnailfishNumber("[[[[3,0],[5,3]],[4,4]],[5,5]]").getMagnitude());
        assertEquals(1137, new SnailfishNumber("[[[[5,0],[7,4]],[5,5]],[6,6]]").getMagnitude());
        assertEquals(3488, new SnailfishNumber("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]").getMagnitude());
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
