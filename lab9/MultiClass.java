package lab9;

import java.util.List;

/**
 * @author Jared Jamieson
 * MultiClass assumes 10% of passengers are in first-class paying 4 * fixed ticket price.  20% of passengers are in 
 * business-class paying 1.5 * fixed ticket price, and 70% of passengers are in the economy-class paying .75 * fixed
 * ticket price.  The flight costs are 1.2 * fixed flight costs.
 */
public class MultiClass implements RevenueModel {

	@Override
	/**
	 * getRevenue takes a list of flights
	 * @return total revenue of all flights within the flights list.
	 */
	public long getRevenue(List<Flight> flights) {
		
		long totalRevenue = 0;
		long ticketPrice = this.constantBaseTicketPrice;
		long flightCost = (long) (this.fixedFlightCost * 1.2);
		
		for (Flight tempFlight: flights) {
			
			// Get number of passengers of "this" flight
			long totalPassengers = tempFlight.getPassengers();
			// Calculate percent of passengers per class, then multiply by class ticket price
			long firstTicketPrices = (long) (((long) (totalPassengers * .1)) * (4 * ticketPrice));
			long businessTicketPrices = (long) (((long) (totalPassengers * .2)) * (1.5 * ticketPrice));
			long coachTicketPrices = (long) (((totalPassengers * .7)) * (.75 * ticketPrice));
			
			// Add tempFlight's revenue to toalRevenue
			totalRevenue += ((businessTicketPrices + coachTicketPrices + firstTicketPrices) - flightCost);
		}
		
		return totalRevenue;
	}
	
}