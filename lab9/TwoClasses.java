package lab9;

import java.util.List;

/**
 * @author Jared Jamieson
 * TwoClasses assumes 20% of passengers are in the business-class paying 1.5 * fixed ticket price.  Additionally, 80% of
 * passengers are in the economy-class paying .75 * fixed ticket price.  The flight costs are 1.1 * fixed flight costs.  
 */
public class TwoClasses implements RevenueModel {

	@Override
	/**
	 * getRevenue takes a list of flights
	 * @return total revenue of all flights within the flights list.
	 */
	public long getRevenue(List<Flight> flights) {
		
		long totalRevenue = 0;
		long ticketPrice = this.constantBaseTicketPrice;
		long flightCost = (long) (this.fixedFlightCost * 1.1);
		
		for (Flight tempFlight: flights) {
			
			// Get number of passengers of "this" flight
			long totalPassengers = tempFlight.getPassengers();
			// Calculate percent of passengers per class, then multiply by class ticket price
			long businessTicketPrices = (long) (((long) (totalPassengers * .2)) * (1.5 * ticketPrice));
			long coachTicketPrices = (long) (((totalPassengers * .8)) * (.75 * ticketPrice));
			
			// Add tempFlight's revenue to totalRevenue
			totalRevenue += ((businessTicketPrices + coachTicketPrices) - flightCost);
		}
		
		return totalRevenue;
	}
	
}
