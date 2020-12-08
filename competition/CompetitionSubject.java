package lab10;

public interface CompetitionSubject{
	// Hint 1: Your subjects will need two lists of observers, one for RankingsObservers and one for MatchObservers
	// Hint 2: A class could implement either or both types of observer
	
	public void registerObserver(RankingsObserver o);
	public void registerObserver(MatchObserver o);
	public void removeObserver(RankingsObserver o);
	public void removeObserver(MatchObserver o);
	public void notifyRankingsObservers();
	public void notifyMatchObservers();
}