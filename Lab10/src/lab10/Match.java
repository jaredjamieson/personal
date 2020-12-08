package lab10;

//import java.util.ArrayList;

public class Match {
	// Declare attributes of a match
	private int matchNum;
	private Team redTeam1; private Team redTeam2; private Team redTeam3;  // Red Team
	private Team blueTeam1; private Team blueTeam2; private Team blueTeam3;  // Blue Team
	private double redScore; private double blueScore;  // Scores
	private boolean redLamp; private boolean blueLamp;  // Lamps
	private boolean redBase; private boolean blueBase;  // Bases
	//private ArrayList<Team> redAlliance = new ArrayList<Team>();  // Arr list of all red teams
	//private ArrayList<Team> blueAlliance = new ArrayList<Team>(); // Arr list of all blue teams
	
	/**
	 * @param matchNum - int match number.
	 * @param redTeam1 - first Team red team.
	 * @param redTeam2 - second Team red team.
	 * @param redTeam3 - thirst Team red team.
	 * @param blueTeam1 - first Team blue team.
	 * @param blueTeam2 - second Team blue team.
	 * @param blueTeam3 - third Team blue team.
	 * @param redScore - int red team's score.
	 * @param blueScore - int blue team's score.
	 * @param redLamp - boolean if red team completed "Light the Lamp"
	 * @param blueLamp - boolean if blue team completed "Light the Lamp"
	 * @param redBase - boolean if red team completed "Return to Base"
	 * @param blueBase - boolean if blue team completed "Return to Base"
	 */
	public Match(int matchNum, Team redTeam1, Team redTeam2, Team redTeam3, Team blueTeam1, Team blueTeam2, Team blueTeam3,
			long redScore, long blueScore, boolean redLamp, boolean blueLamp, boolean redBase, boolean blueBase) {
		this.matchNum = matchNum;
		this.redTeam1 = redTeam1; this.redTeam2 = redTeam2; this.redTeam3 = redTeam3;
		this.blueTeam1 = blueTeam1; this.blueTeam2 = blueTeam2; this.blueTeam3 = blueTeam3;
		this.redScore = redScore; this.blueScore = blueScore;
		this.redLamp = redLamp; this.blueLamp = blueLamp;
		this.redBase = redBase; this.blueBase = blueBase;
	}
	
	// Get match number
	public int getMatchNum() { return this.matchNum; }
	// Getters for Team red and blue teams
	public Team getRedTeam1() { return this.redTeam1; }
	public Team getRedTeam2() { return this.redTeam2; }
	public Team getRedTeam3() { return this.redTeam3; }
	public Team getBlueTeam1() { return this.blueTeam1; }
	public Team getBlueTeam2() { return this.blueTeam2; }
	public Team getBlueTeam3() { return this.blueTeam3; }
	// Getters for Boolean red and blue bases
	public Boolean getRedBase() { return this.redBase; }
	public Boolean getBlueBase() { return this.blueBase; }
	// Getters for Boolean red and blue lamps
	public Boolean getRedLamp() { return this.redLamp; }
	public Boolean getBlueLamp() { return this.blueLamp; } 
	// Getters for double red and blue scores
	public double getRedScore() { return this.redScore; }
	public double getBlueScore() { return this.blueScore; }
	
	/**
	 * Add RP to each team in an alliance. 
	 * @param RP - Int amount of RP to add per team.
	 * @param alliance - String alliance color to add point to.
	 */
	public void addAllianceRP(int RP, String alliance) {
		if (alliance.toLowerCase() == "red") {
			//for (Team tempTeam : redAlliance) {
			//	tempTeam.addRP(RP);
			redTeam1.addRP(RP);
			redTeam2.addRP(RP);
			redTeam3.addRP(RP);
		}
			
		if (alliance.toLowerCase() == "blue") {
			//for (Team tempTeam : redAlliance) {
			//	tempTeam.addRP(RP);
			blueTeam1.addRP(RP);
			blueTeam2.addRP(RP);
			blueTeam3.addRP(RP);
		}
	}
	
	/**
	 * Increases matches played for each team in each alliance.
	 */
	public void matchPlayed() {
		redTeam1.addMatchPlayed();
		redTeam2.addMatchPlayed();
		redTeam3.addMatchPlayed();
		blueTeam1.addMatchPlayed();
		blueTeam2.addMatchPlayed();
		blueTeam3.addMatchPlayed();
	}
}