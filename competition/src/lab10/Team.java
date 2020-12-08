package lab10;

public class Team implements Comparable<Team>{
	private int id;
	private int rankingPoints;
	private int matchesPlayed;
	private int currentRank;
	
	// Other instance variables here
	
	/**
	 * Teams innitialize with a unique ID and 0 RP and 0 matches played.
	 * @param number - unique int ID.
	 */
	public Team(int number) {
		this.id = number;
		this.rankingPoints = 0;
		this.matchesPlayed = 0;
		this.currentRank = 0;
		//Add more code here as needed
	}
	
	
	/**
	 * @return the team's current rank.
	 */
	public int getCurrentRank() { return this.currentRank; }
	
	/**
	 * Sets the team's current rank.
	 * @param newRank - the team's new rank.
	 */
	public void setCurrentRank(int newRank) { this.currentRank = newRank; }
	
	/**
	 * @return the team id.
	 */
	public int get_id() { return this.id; }
	
	/**
	 * @return team's ranking points.
	 */
	public int getRP() { return this.rankingPoints; }
	
	/**
	 * @return team's matches played.
	 */
	public int getMatchesPlayed() { return this.matchesPlayed; }
	
	/**
	 * addRP adds earned points to team's rankingPoints.
	 * @param points - points team earned.
	 */
	public void addRP(int points) { this.rankingPoints += points; }
	
	/**
	 * Increases matches played by one.
	 */
	public void addMatchPlayed() { this.matchesPlayed += 1; }
	
	/**
	 * @return average team's score as a double. 
	 */
	public double getAvgScore() {
		double tempRP = this.rankingPoints;
		double tempMatches = this.matchesPlayed;
		double tempDouble = this.rankingPoints/tempMatches;
		if (this.matchesPlayed == 0) { return tempRP/1; } // Handles divide by zero exception
		else { return tempDouble; }
	}
	
	/**
	 * @return 0 is both Team's RP is equal, -1 if other RP is greater, and 1 if this RP is greater.
	 */
	public int compareTo(Team other){
		// Find both team's average scores
		double thisAvg = this.getAvgScore();
		double otherAvg = other.getAvgScore();
		// Return int corresponding to higher team's score
		if (thisAvg > otherAvg) { return 1; }
		else if (thisAvg < otherAvg) { return -1; }
		else { return 0; }
	}
}