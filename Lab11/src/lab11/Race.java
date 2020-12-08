package lab11;

/**
 * Race constructs a class of a race
 * @author JaredJamieson
 *
 */
public class Race implements PrizeWinnings {
	private String type; // Race type
	private String name;  // Race name
	private double length;  // Race length
	private double purse;  // Race purse
	private String direction;  // Race direction
	
	// Constructor
	public Race(String tempType, String tempName, double tempLength, double tempPurse, String tempDirection) {
		this.name = tempName;
		this.length = tempLength;
		this.purse = tempPurse;
		this.direction = tempDirection;
		this.type = tempType;
	}
	
	// Getters for Race attributes
	/**
	 * @return String name
	 */
	public String getName() { return this.name; }
	
	/**
	 * #return double length
	 */
	public double getLength() { return this.length; }
	
	/**
	 * @return double purse
	 */
	public double getPurse() { return this.purse; }
	
	/**
	 * @return String direction
	 */
	public String getDirection() { return this.direction; }
	
	/**
	 * @return String type
	 */
	public String getType() { return this.type; }
	
	// Setters for Race attributes
	/**
	 * @param tempName - Sets name to String tempName
	 */
	public void setName(String tempName) { this.name = tempName; }
	
	/**
	 * @param tempLength - Sets length to double tempLength
	 */
	public void setLength(double tempLength) { this.length = tempLength; }
	
	/**
	 * @param tempPurse - sets purse to double tempPurse
	 */
	public void setPurse(double tempPurse) { this.purse = tempPurse; }
	
	/**
	 * @param tempDirection - sets direction to String tempDirection
	 */
	public void setDirection(String tempDirection) { this.direction = tempDirection; }
	
	/**
	 * @param tempType - sets type to String tempType
	 */
	public void setType(String tempType) { this.type = tempType; }
	
	/**
	 * Prints out race object
	 */
	public String toString() {
		return "\nType: " + this.type
				+ "\nName:" + this.name
				+ "\nLength: " + this.length + " miles"
				+ "\nPurse: $" + this.purse + " USD"
				+"\nDirection:" + this.direction;
	}
	
}