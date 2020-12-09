import java.util.ArrayList;

public class Driver {

	public static void main(String[] args) {
		// Main method
		//Tuple test = new Tuple();
		//Object[] myArr = new Object[3];
		//myArr[0] = 1;
		//myArr[1] = 2;
		//myArr[2] = 3;
		
		//Tuple otherTest = new Tuple(myArr);
		
		//System.out.println(otherTest); // Tests one parameter Tuple
		//System.out.println("Index 1: " + otherTest.get(1)); // Tests get method (index)
		//System.out.println("Size: " + otherTest.size()); // Tests size method
		
		//System.out.println(test); // Tests no parameter Tuple
		//System.out.println("Index 1: " + test.get(1)); // Tests get method (index)
		//System.out.println("Size: " + test.size()); // Tests size method
		
		Tupletest();
		
	}
	
	public static void Tupletest() {
		/* // Tests Collections Constructor
	    ArrayList<Comparable> arr = new ArrayList();
		arr.add(0, 1);
		arr.add(1, 2);
		System.out.println(arr);
		
		Tuple myTuple = new Tuple(arr);
		System.out.println(myTuple);
		
	}
	*/
		/* // Tests compareTo function
		Integer[] obj1 = new Integer[2];
		obj1[0] = 1;
		obj1[1] = 2;
		Integer[] obj2 = new Integer[2];
		obj2[0] = 1;
		obj2[1] = 2;
		
		Tuple test1 = new Tuple(obj1);
		Tuple test2 = new Tuple(obj2);
		
		System.out.println(test1.compareTo(test2));
	}
	*/
		/*
		Integer[] obj1 = new Integer[2];
		obj1[0] = 1;
		obj1[1] = 2;
		Tuple test = new Tuple(obj1);
		System.out.println(test);
	}
	*/
	Tuple.sortTest();
		
	}
}
