package lab10;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;


/**
 * @author Jared Jamieson
 *
 */

public class Competition implements CompetitionSubject {
	String tf;  // Team File
	String cf;  // Competition File
	LinkedList<Team> innerList = new LinkedList<Team>();  // linked list to hold teams
	HashMap<Integer, Match> matchMap = new HashMap<>();  // hash map to hold matches, Integer is the match number
	Match mostRecentMatch;  // variable to hold latest match (to notify observers)
	ArrayList<MatchObserver> matchObsArr = new ArrayList<MatchObserver>();  // array to hold matchObservers
	ArrayList<RankingsObserver> rankObsArr = new ArrayList<RankingsObserver>();  // array to hold rankObserver
	
	public Competition(String teamFile, String competitionFile) {
		tf = teamFile;
		cf = competitionFile;
	}
	
	/**
	 * readTeamFile add teams to the innerList
	 * @param tempFile - A string of a file to read through
	 */
	public void readTeamFile(String tempFile) {
		try {
			File teamFileObj = new File(tempFile);
			Scanner reader = new Scanner(teamFileObj);
			
			while (reader.hasNextLine()) {
				String contents = reader.nextLine();
				Team tempTeam = new Team(Integer.parseInt(contents));
				// ability to get team via id - hashmap ### WHY-QUESTION ###
				innerList.add(tempTeam);  // Add team to liked list
			}
			reader.close();
		}
		
		catch (FileNotFoundException ex) { System.out.println("File not found: " + ex.getMessage()); }
	}
	
	/**
	 * readCompetitionFile adds matches to matchMap
	 * @param tempFile - A string of the file to read through
	 * This function simulates the actual competition (plays the matches)
	 */
	public void readCompetitionFile(String tempFile) {
		try {
			// open file
			File compFileObj = new File(tempFile);
			Scanner reader = new Scanner(compFileObj);
			// loop through file
			while (reader.hasNextLine()) {
				// read in line
				String contents = reader.nextLine();
				String[] tempLine = contents.split(",");  // Create array of match variables
				Match tempMatch = createTempMatch(tempLine);  // Create temp match object
				addTempMatch(tempLine, tempMatch);  // Add temp match object to matchMap
			}
			// play through each match
			// k - int match num, v - Match object
			this.matchMap.forEach((k, v) -> { playMatch(v);
				// sort ranking (team arr via avg scores)
				Collections.sort(this.innerList, Collections.reverseOrder());
				// track most recent match
				this.mostRecentMatch = v;
				// update/notify match observers
				this.notifyRankingsObservers();
				this.notifyMatchObservers();
			} );
			reader.close();
		}
		// Exception handler if given files cannot be found.
		catch (FileNotFoundException ex) { System.out.println("File not found: " + ex.getMessage()); }
	}

	@Override
	public void registerObserver(RankingsObserver o) { rankObsArr.add(o); }  // Add rank observer

	@Override
	public void registerObserver(MatchObserver o) { matchObsArr.add(o); }  // Add match observer

	@Override
	public void removeObserver(RankingsObserver o) { rankObsArr.remove(o); }  // Remove ranking observer

	@Override
	public void removeObserver(MatchObserver o) { matchObsArr.remove(o); }  // Remove match observer

	@Override
	public void notifyRankingsObservers() {
		// Inner List to Arr
		Team[] updatedList = innerList.toArray(new Team[innerList.size()]); 
		System.out.println("AFTER MATCH " + mostRecentMatch.getMatchNum() + ": ");
		// for loop ranking observers
		for (RankingsObserver o: rankObsArr) { o.update(updatedList); }
		//for (int i = 0; i < rankObsArr.size(); i++) {
		//	rankObsArr.get(i).update(updatedList);
		//}
		//System.out.println("After rankings observer loop");
	}

	@Override
	public void notifyMatchObservers() {
		// Inner List to Arr
		Team[] updatedList = innerList.toArray(new Team[innerList.size()]);
		// Update the match observer for the most recent match
		for (RankingsObserver o: rankObsArr) { o.update(updatedList); }
		for (MatchObserver o: matchObsArr) { o.update(this.mostRecentMatch); }
	}
		
	/**
	 * findID searches the innerList Teams to match to the given ID.
	 * @param tempID - int ID being looked for.
	 * @return the locations of the Team in the innerList.
	 */
	public Team findID(int tempID) {
		Team[] newList = innerList.toArray(new Team[30]);  // Create Team arr from Linked List
		for (int i = 0; i < innerList.size(); i++) {
			if (newList[i].get_id() == tempID) { return newList[i]; }  // Return Matching ID
		} return null; }
	
	/**
	 * Play out match matchNum from matchMap
	 */
	public void playMatch(Match tempMatch) {
		tempMatch.matchPlayed(); // Increase the matches played of each team of the match by 1
		
		// If blue alliance completed "Return to Base", add 1 RP per blue team
		if (tempMatch.getBlueBase() == true) { tempMatch.addAllianceRP(1, "blue"); }
		
		// If red alliance completed "Return to Base", add 1 RP per red team
		if (tempMatch.getRedBase() == true) { tempMatch.addAllianceRP(1, "red"); }
		
		// If blue alliance completed "Light the Lamp", add 1 RP per blue team
		if (tempMatch.getBlueLamp() == true) { tempMatch.addAllianceRP(1, "blue"); }
		
		// If red alliance completed "Light the Lamp", add 1 RP per red team
		if (tempMatch.getRedLamp() == true) { tempMatch.addAllianceRP(1, "red"); }
		
		// If blue alliance wins match, add 2 RP per blue team
		if (tempMatch.getBlueScore() > tempMatch.getRedScore()) { tempMatch.addAllianceRP(2, "blue"); }
		
		// If red alliance wins match, add 2 RP per red team
		else if (tempMatch.getRedScore() > tempMatch.getBlueScore()) { tempMatch.addAllianceRP(2, "red"); }
		
		// If alliances draw, add 1 RP per team
		else {
			tempMatch.addAllianceRP(1, "blue");
			tempMatch.addAllianceRP(1, "red");
		}
	}
	
	/**
	 * createTempMatch takes parameters to create a match obj.
	 * @param tempLine - String arr of parameters.
	 * @return match object.
	 */
	public Match createTempMatch(String[] tempLine) {
		// create obj match from line
		int matchNum = Integer.valueOf(tempLine[0]);  // Change string to int
		Team redTeam1 = findID(Integer.valueOf(tempLine[1]));  // Find teams via team num then assign to each team for match
		Team redTeam2 = findID(Integer.valueOf(tempLine[2]));
		Team redTeam3 = findID(Integer.valueOf(tempLine[3]));
		Team blueTeam1 = findID(Integer.valueOf(tempLine[4]));
		Team blueTeam2 = findID(Integer.valueOf(tempLine[5]));
		Team blueTeam3 = findID(Integer.valueOf(tempLine[6]));
		int redScore = Integer.valueOf(tempLine[7]);
		int blueScore = Integer.valueOf(tempLine[8]);
		boolean redLamp = (Boolean.parseBoolean(tempLine[9]));  // Change string to boolean
		boolean blueLamp = (Boolean.parseBoolean(tempLine[10]));
		boolean redBase = (Boolean.parseBoolean(tempLine[11]));
		boolean blueBase = (Boolean.parseBoolean(tempLine[12]));
		Match tempMatch = new Match(matchNum, redTeam1, redTeam2, redTeam3, blueTeam1, blueTeam2,
				blueTeam3, redScore, blueScore, redLamp, blueLamp, redBase, blueBase);  // Create and return temp match
		return tempMatch;
	}
	
	/**
	 * addTempMatch adds a match to the matchMap.
	 * @param tempLine - String arr of variables.
	 * @param tempMatch - Match obj.
	 */
	public void addTempMatch(String[] tempLine, Match tempMatch) {
		int matchNum = Integer.valueOf(tempLine[0]);
		matchMap.put(matchNum, tempMatch);  // Assign temp match to hash map (Key: match num, Value: tempMatch obj)
	}

}
