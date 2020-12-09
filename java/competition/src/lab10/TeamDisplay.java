/**
 * 
 */
package lab10;

/**
 * @author jared
 * TeamDisplay takes in an int team number and displays the results of that team's matches
 */
public class TeamDisplay implements RankingsObserver, MatchObserver{
	private int teamNumber;
	private int currentRank;
	
	public TeamDisplay(int tempTeamNumber) {
		this.teamNumber = tempTeamNumber;
		this.currentRank = 0;
	}
	
	@Override
	public void update(Match m) {
		// Prints out match info
		// If Red team won:
		if (m.getRedScore() > m.getBlueScore()) { 
			System.out.println("Team " + this.teamNumber + " won Match " + m.getMatchNum() 
			+ " " + m.getRedScore() + "-" + m.getBlueScore() + ". Current Rank: " + this.currentRank); }
		// If Blue team won:
		if (m.getRedScore() < m.getBlueScore()) { 
			System.out.println("Team " + this.teamNumber + " lost Match " + m.getMatchNum() + " " 
		+ m.getRedScore() + "-" + m.getBlueScore() + ". Current Rank: " + this.currentRank); }
		// If teams tied:
		else { 
			System.out.println("Team " + this.teamNumber + " tied Match " + m.getMatchNum() 
			+ " " + m.getRedScore() + "-" + m.getBlueScore() + ". Current Rank: " + this.currentRank); }
	}

	@Override
	public void update(Team[] rankings) {
		// TODO Auto-generated method stub
		for (int i = 0; i < rankings.length; i++) {
			if (this.teamNumber == rankings[i].get_id()) {
				rankings[i].setCurrentRank(i + 1);
				this.currentRank = rankings[i].getCurrentRank();
			}
		}
	}
}
