package genericsLab;

/**
 * @author Jared_Jamieson
 * Subclass of Semigroup containing a single positive integer.
 */
public class PositiveInteger extends Semigroup<PositiveInteger> {
	// Initialize integer for class
	private int storedInteger;
	/**
	 * @param tempint is a passed integer that should be positive
	 * Constructor verifying positive argument
	 */
	public PositiveInteger(int tempInt) throws IllegalArgumentException {
		// Throw exception is tempInt is not positive
		if (tempInt < 0) {
			throw new IllegalArgumentException("Passed argument must be "
					+ "positive! ");
		}
		// Set class integer to passed argument
		storedInteger = tempInt;
	}
	
	/**
	 * @param argument is the PositiveInteger to be added to.
	 * Operator returns the sum of this and argument.
	 */
	@Override
	PositiveInteger operator(PositiveInteger argument) {
		return (new PositiveInteger(storedInteger + 
				argument.storedInteger));
	}
	
	/**
	 * @param argument is a comparative PositiveInteger type
	 * Returns true if argument == this, false otherwise. 
	 */
	public boolean equals(PositiveInteger argument) {
		return storedInteger == argument.storedInteger;
	}
	
	/**
	 * Returns PositiveInteger as a string.
	 */
	public String toString() {
		return (String.valueOf(storedInteger));
	}
}

