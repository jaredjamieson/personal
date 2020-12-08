package lab11;

public class FlatRace extends Race {
	// Flat races have no jumps and are run on dirt, turf, or synthetic ground
	private String groundType;
	
	public FlatRace(String tempType, String tempName, double tempLength, double tempPurse, String tempDirection, String tempGroundType) {
		super(tempType, tempName, tempLength, tempPurse, tempDirection);
		this.groundType = tempGroundType;
	}
	
	/**
	 * @return String ground type
	 */
	public String getGroundType() {
		return this.groundType;
	}
	
	/**
	 * @param tempGroundType - String to set ground type to
	 */
	public void setGroundType(String tempGroundType) {
		this.groundType = tempGroundType;
	}
	
	/**
	 * Prints out the flat race object
	 */
	@Override
	public String toString() {
		return super.toString()
				+ "\nGround Type:" + this.groundType;
	}
}
