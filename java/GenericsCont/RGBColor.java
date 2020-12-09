package genericsLab;

/**
 * @author Jared_Jamieson
 * RGBColor class is a subclass of Semigroup that stores 3 integers
 * between 0 and 255.
 */
public class RGBColor extends Semigroup<RGBColor> implements Complementable<RGBColor> {
	// Hold Red, Green and Blue values
	private int red;
	private int green;
	private int blue; 
	
	public RGBColor(int a, int b, int c) throws IllegalArgumentException {
		// Set input integers to private variables if between 0 and 255
		try {
			if ((a >= 0) && (a <= 255)) {
				this.red = a;
			}
			if ((b >= 0) && (b <= 255)) {
				this.green = b;
			}
			if ((c >= 0) && (c <= 255)) {
				this.blue = c;
			}
		}
		// Throw error is colors are not between 0 and 255
		catch (IllegalArgumentException ex) {
			System.out.println("RGBColor inputs must be between 0 and "
					+ "255! ");
		}
	}
	
	/**
	 * @param argument is the comparative RGBColor
	 * Operator returns the RGBColor compliment of two RGBColors
	 */
	@Override
	RGBColor operator(RGBColor argument) {
		// Calculate operator values
		int operatorRed = (this.red + argument.red) / 2;
		int operatorGreen = (this.green + argument.green) / 2;
		int operatorBlue = (this.blue + argument.blue) / 2;
		// Return new RGBColor of final values
		return new RGBColor(operatorRed, operatorGreen, operatorBlue);
	}

	/**
	 * Returns a new color whose components are each 255 - the
	 * original value. 
	 */
	@Override
	public RGBColor complement() {
		// Calculate the complement value
		int complimentRed = 255 - this.red;
		int complimentGreen = 255 - this.green;
		int complimentBlue = 255 - this.blue;
		// Return new RGBColor with calculated values
		return new RGBColor(complimentRed, complimentGreen, complimentBlue);
	}
	
	/**
	 * Prints RGBColor as a string
	 */
	public String toString() {
		String tempStr = "";
		tempStr += "(";
		tempStr += this.red;
		tempStr += ",";
		tempStr += this.green;
		tempStr += ",";
		tempStr += this.blue;
		tempStr += ")";
		// Return final string
		return tempStr;
	}
}
