package lab11;

public class RaceAdaptor {
	
	/**
	 * @param tempRace - Race obj
	 * @return float length converted to miles
	 */
	public double convertFurlongToMiles(Race tempRace) {
		double length = tempRace.getLength();
		double newLength = (length * .125);
		return newLength;
	}
	
	/**
	 * @param tempRace - Race obj
	 * @return float purse converted to USD
	 */
	public double convertPoundsToUSD(Race tempRace) {
		double purse = tempRace.getPurse();
		double newPurse = (purse * 1.23);
		return newPurse;
	}
}

