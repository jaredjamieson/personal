package classcode.generics;
import java.util.ArrayList;

/**
   This program demonstrates that an ArrayList can accept
   a mixture of object types as its elements.
*/

public class UnsafeArrayList
{
   public static void main(String[] args)
   {
      // Create an ArrayList object.
      ArrayList list = new ArrayList();
      
      // Store a variety of objects in the list.
      list.add("Java is fun!");         // Add a String
      list.add(new Double(2.5));        // Add a Double
      list.add(new Rectangle(10, 12));  // Add a Rectangle
      
      // Retrieve a reference to each object in the list.
      // Note that the reference returned from the get
      // method must be cast to the correct type.
      Double d = (Double)list.get(1);
      String s = (String)list.get(0);
      Rectangle r = (Rectangle)list.get(2);
      System.out.println(s);
   }
}