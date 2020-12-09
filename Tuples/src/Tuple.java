import java.util.AbstractList;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Random;

/**
 * @author Jared Jamieson
 * Extends AbstractList class to create a concrete tuples class
 */
public class Tuple extends AbstractList<Comparable> implements Comparable<Tuple> {
	// Comparable array used for in-class storage of tuples 
	private Comparable[] innerArr;
	
	/**
	 * Empty tuple constructor
	 */
	public Tuple() {
		this.innerArr = new Comparable[0];
	}
	/**
	 * Constructor to copy array to tuple
	 * @param tempArr
	 */
	public Tuple(Comparable[] tempArr) {
		this.innerArr = tempArr;
	}
	/**
	 * Constructor to copy collection into tuple
	 * @param newList
	 */
	public Tuple(Collection<Comparable> newList) {
		innerArr = new Comparable[newList.size()];
		int i = 0; // Prime for-loop
		for (Comparable element: newList) {
			innerArr[i] = element;
			i ++;
		}
	}
	/**
	 * Returns the element at the specified position in the list
	 */
	@Override
	public Comparable get(int index) throws IndexOutOfBoundsException {
		return innerArr[index];
	}
	/**
	 * Returns the size of innerArr
	 */
	@Override
	public int size() {
		return innerArr.length;
	}
	/**
	 * Returns innerArr == tempTuple: 0, innerArr > tempTuple or innerArr is longer: +1, 
	 * or innerArr < tempTuple or innerArr is shorter: -1
	 */
	public int compareTo(Tuple tempTuple) {
		if (innerArr.length == 0 && tempTuple.size() == 0) {
			return 0;
		}
		if (innerArr.length > tempTuple.size()) {
			// If inner length > temp length
			return 1;
		}
		else if (innerArr.length < tempTuple.size()) {
			// If inner length < temp length
			return -1;
		}
		int i = 0;
		while (i < innerArr.length){
			Comparable inner = innerArr[i];
			Comparable temp = tempTuple.get(i);
			
			if (inner.compareTo(temp) == 1) {
				// If inner > temp
				return 1;
			}
			else if (inner.compareTo(temp) == -1) {
				// If inner < temp
				return -1;
			}
			i++; // Increase slot in array
		} 
		
		return 0; // Base Case
	}
	/**
	 * Returns Tuple object contents
	 * @return 
	 */
	public String toString() {
		if (innerArr.length == 0) {
			return "()";
		}
		int i = 0;
		String output = "("; // Concatenate first '('
		while (i < (innerArr.length - 1)) {
			output += innerArr[i] + ","; // Concatenate each element + ','
			i++;
		}
		output += innerArr[i]; // Concatenate last element
		
		return output + ")"; // Return and concatenate last ')'
	}
	/**
	 * Creates 3 tuples of random size and values, prints, sorts, prints
	 */
	public static void sortTest() {
		// Random class usage
		Random randint = new Random();
		int tempSize = randint.nextInt(3);
		// Create first random obj
		Integer[] obj1 = new Integer[tempSize];
		for (int i = 0; i < tempSize; i++) {
			obj1[i] = (int)(10.0 * Math.random());
		}
		// Create 2nd random obj
		Integer[] obj2 = new Integer[tempSize];
		for (int i = 0; i < tempSize; i++) {
			obj2[i] = (int)(10.0 * Math.random());
		}
		// Create 3rd random obj
		Integer[] obj3 = new Integer[tempSize];
		for (int i = 0; i < tempSize; i++) {
			obj3[i] = (int)(10.0 * Math.random());
		}
		// Convert objects to type Tuple
		Tuple tup1 = new Tuple(obj1);
		Tuple tup2 = new Tuple(obj2);
		Tuple tup3 = new Tuple(obj3);
		// Create Tuple array of tuples
		Tuple[] tupArr = {tup1, tup2, tup3};
		// Print contents of Tuple array
		int i = 0; // Prime for-loop
		for (Tuple element: tupArr) {
			System.out.println(tupArr[i]);
			i ++;
		}
		// Sort Tuple array
		Arrays.sort(tupArr);
		// Print contents of Tuple array
		int j = 0; // Prime for-loop
		for (Tuple ele: tupArr) {
			System.out.println(tupArr[j]);
			j ++;
		}
	}
	
	
}
