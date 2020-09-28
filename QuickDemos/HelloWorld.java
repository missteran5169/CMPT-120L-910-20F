package QuickDemos;

import java.util.logging.Logger;

/**
 * HelloWorld
 */
public class HelloWorld {
    public static void main(String[] args) {
        String name = "Aaron";
        System.out.println("Hello World");
        heyThere(name);
    }

    public static void heyThere(String name){
        System.out.println("Hello " + name + "!");
    }
}