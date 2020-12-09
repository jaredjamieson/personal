package lab10;

public interface MatchObserver {
	/**
	Receives the most recent match of the competition.
	@param m A match object that contains all pertinent match data.
	*/
	public void update(Match m);
}
