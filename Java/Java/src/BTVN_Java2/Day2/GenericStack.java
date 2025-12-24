package BTVN_Java2.Day2;

import java.util.EmptyStackException;
import java.util.LinkedList;

public class GenericStack<T> {
    private LinkedList<T> stack =  new LinkedList<>();

    public void push(T value) {
        stack.add(value);
    }
    public T pop() {
        if(stack.isEmpty()) throw new RuntimeException("Stack is empty");
        return stack.removeLast();
    }

    public T peek() {
        if(stack.isEmpty()) throw new RuntimeException("Stack is empty");
        return stack.getFirst();
    }
    public boolean isEmpty() {
        return stack.isEmpty();
    }
}
