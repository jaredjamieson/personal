package lab10;

public interface CompetitionSubject{
	
	public void registerObserver(RankingsObserver o);
	public void registerObserver(MatchObserver o);
	public void removeObserver(RankingsObserver o);
	public void removeObserver(MatchObserver o);
	public void notifyRankingsObservers();
	public void notifyMatchObservers();
}