package lab9;

import java.io.IOException;

/**
 * @author Jared Jamieson
 * Flight constructs airline flights containing an airline, airplane, flight number, departing airport,
 * arriving airport, time and passengers.
 */

public class Flight {
	
	// Prime all necessary variables
	private Airline airline;
    private String airplane;
    private int flightNum;
    private String depAirport;
    private String arrAirport;
    private int time;
    private int passengers;
    
    /**
     * Assign passed variables to primed variables
     * @param a : airline
     * @param pl : airplane
     * @param fn : flight number
     * @param dep : departing airport
     * @param arr : arriving airport
     * @param t : time
     * @param p : passengers
     * @throws IOException 
     */
    public Flight(Airline a, String pl, int fn, String dep, String arr, int t, int p) {
        airline = a;
        airplane = pl;
        flightNum = fn;
        depAirport = dep;
        arrAirport = arr;
        time = t;
        passengers = p;
    }
    
    /**
     * @return the integer of the number of passengers.
     */
    public int getPassengers(){
        return passengers;
    }
	
    /**
     * @return the AirLine object
     */
	public Airline getAirline(){
		return airline;
	}
	
	/**
	 * @return the string of the airplane
	 */
	public String getAirplane(){
		return airplane;
	}
	
	/**
	 * @return the integer of the flight number
	 */
	public int getFlightNumber(){
		return flightNum;
	}
	
	/**
	 * @return the string of the departing airport
	 */
	public String getDeparture(){
		return depAirport;
	}
	
	/**
	 * @return the string of the arriving airport
	 */
	public String getArrival(){
		return arrAirport;
	}
	
	/**
	 * @return the time of the flight
	 */
	public int getTime(){
		return time;
	}
}




