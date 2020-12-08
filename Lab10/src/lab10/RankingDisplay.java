/**
 * 
 */
package lab10;

/**
 * @author jared
 *
 */
public class RankingDisplay implements RankingsObserver {
	private int numTeams;
	
	public RankingDisplay(int tempNumTeams) {
		this.numTeams = tempNumTeams;
	}

	@Override
	public void update(Team[] rankings) {
		System.out.println("Entered rankings update");
		// Print out team ID and average score from sorted rankings
		for (int i = 0; i < rankings.length; i++ ) {
			int tempTeamId = rankings[i].get_id();
			double tempAvgScore = rankings[i].getAvgScore();
			System.out.println("Team: " + tempTeamId + " " + String.format("%.2f", tempAvgScore + "RP"));
		}
	}	
}
