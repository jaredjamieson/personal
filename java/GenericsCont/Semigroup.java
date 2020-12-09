package genericsLab;

import java.io.IOException;
import java.util.AbstractList;

/**
 * @author Jared_Jamieson
 * The GenericSemigroup class specifies an operator method and takes
 * one argument of the parameterized type.  
 */
public abstract class Semigroup<T> {
	// operator method to be overridden by implemented classes
	abstract T operator(T argument);
	
	static public <T extends Semigroup<T>> T combine(AbstractList<T> tempList) throws IOException {
		
		if (tempList.size() == 0) {
			throw new IOException();
		}
		T total;
		int i = 0;
		// Loop through elements of tempList
		for(T t: tempList) {
			// Add all t's together
			//total += (t.operator(tempList.get(i+1))); // This doesn't work :'(
			//T total = add(t, tempList); // This also does not work :'(
			i ++;
		}
		// Return the total
		return total;
	}
}

