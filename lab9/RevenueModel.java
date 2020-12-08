package lab9;

import java.util.List;

/**
 * @author Jared Jamieson
 * RevenueModel defines a constant ticket price of $300 and a constant flight cost of $50,000,
 * additionally, a getRevenue method must be implemented by each class.
 */

public interface RevenueModel {
	
	static long constantBaseTicketPrice = 300;
	static long fixedFlightCost = 50000;
	
	public long getRevenue(List<Flight> flights);
}
