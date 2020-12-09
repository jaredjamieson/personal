package lab9;

import java.util.List;

/**
 * @author Jared Jamieson
 * SinglePrice assumes all passengers pay the same economy-class fixed ticket price and the flight cost is the fixed rate.  
 */

public class SinglePrice implements RevenueModel {

	@Override
	/**
	 * getRevenue takes a list of flights
	 * @return total revenue of all flights within the flights list.
	 */
	public long getRevenue(List<Flight> flights) {
		
		long totalRevenue = 0; // Prime total revenue as a long
		long ticketPrice = this.constantBaseTicketPrice; // Calculate ticket price
		long flightCost = this.fixedFlightCost; // Calculate flight cost
		
		for (Flight tempFlight: flights) {
			
			// Add tempFlight's revenue to totalRevenue
			totalRevenue += ((tempFlight.getPassengers() * ticketPrice) - flightCost);
			}
		
		return totalRevenue;
	}
	
}