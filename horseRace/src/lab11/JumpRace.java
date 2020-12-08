package lab11;

public class JumpRace extends Race implements JumpHeight {
	private double jumpHeight;
	private String groundType = "turf";
	
	// Jump Races always have fences and are run on turf
	public JumpRace(String tempType, String tempName, double tempLength, double tempPurse, String tempDirection, double tempJumpHeight) {
		super(tempType, tempName, tempLength, tempPurse, tempDirection);
		this.jumpHeight = tempJumpHeight;
	}
	
	/**
	 * @return double jump height
	 */
	public double getHeight() { return this.jumpHeight; }
	
	/**
	 * @return String ground type
	 */
	public String getGroundType() { return this.groundType; }
	
	/**
	 * Prints out the JumpRace object
	 */
	@Override
	public String toString() {
		return super.toString()
				+ "\nGround Type: " + this.groundType
				+ "\nJump Height: " + this.jumpHeight;
	}
	
	/**
	 * @param height - double to reset height to
	 */
	@Override
	public void setHeight(double height) {
		// TODO Auto-generated method stub
		this.jumpHeight = height;
	}
}
