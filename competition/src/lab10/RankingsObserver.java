package lab10;

public interface RankingsObserver {
	/**
	Receives the updated rankings as an array of Teams.
	@param rankings A sorted array of Team objects where the object in the 0th index is the highest ranked team (1st place).
	*/
	public void update(Team[] rankings);
}
