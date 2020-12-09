package lab11;

public class RaceFactory {
	private static Race race;  // Initialize race object
	private static String[] line; // Initialize String[] of possible variables
	
	/**
	 * @param tempLine String[] of possible variables
	 */
	public RaceFactory(String[] tempLine) {
		this.line = tempLine;
	}
	
	/**
	 * @return race object of either FLAT or JUMP race
	 */
	public static Race getRace() {
		
		if (line[0].contentEquals("JUMP")) {  // If jump race, create jumpRace obj
			String tempType = line[0];
			String tempName = line[1];
			double tempLength = Double.valueOf(line[2]);
			double tempPurse = Double.valueOf(line[3]);
			String tempDirection = line[4];
			double tempJumpHeight = Double.valueOf(line[6]);
			// reassign race to newly built jumpRace obj
			race = new JumpRace(tempType, tempName, tempLength, tempPurse, tempDirection, tempJumpHeight);
		}
		
		if (line[0].contentEquals("FLAT")) {  // If flat race, create flatRace obj
			String tempType = line[0];
			String tempName = line[1];
			double tempLength = Double.valueOf(line[2]);
			double tempPurse = Double.valueOf(line[3]);
			String tempDirection = line[4];
			String tempGroundType = line[5];
			// reassign race to newly built flatRace obj
			race = new FlatRace(tempType, tempName, tempLength, tempPurse, tempDirection, tempGroundType);
		}
		return race;
		
	}

}
