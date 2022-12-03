package li.ste.adventofcode;

import li.ste.adventofcode.utils.AdventOfCodeException;

import java.lang.reflect.Method;

public class DisplayNameGenerator implements org.junit.jupiter.api.DisplayNameGenerator {
    @Override
    public String generateDisplayNameForClass(Class<?> aClass) {
        String[] parts = aClass.toString().split("\\.");
        return parts[parts.length -2].substring(4) + "-" + parts[parts.length-1].substring(7);
    }

    @Override
    public String generateDisplayNameForNestedClass(Class<?> aClass) {
        throw new AdventOfCodeException("todo: generate nested class name");
    }

    @Override
    public String generateDisplayNameForMethod(Class<?> aClass, Method method) {
        String[] parts = method.toString().split("\\.");
        String methodName = parts[parts.length - 1];
        return methodName.substring(0,methodName.length()-2);
//        throw new AdventOfCodeException("todo: generate metod name");
    }
}
