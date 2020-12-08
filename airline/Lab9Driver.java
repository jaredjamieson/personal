package lab9;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * @author Jared Jamieson
 *
 */
public class Lab9Driver {
	
	public static void main(String[] args) throws FileNotFoundException, IllegalArgumentException, IllegalStateException {

		Scanner fileName = new Scanner(System.in);
		System.out.println("Enter path of file: "); // C:\\Users\\jared\\Desktop\\FlightsText.txt
		String userFilePath = fileName.nextLine();
		
		// Create Flight list
        List<Flight> flightArr = new ArrayList<Flight>();
		
		File file = new File(userFilePath);
        try {
            // Read file by line
            Scanner scanner = new Scanner(file);
            // While more lines in file
            while (scanner.hasNextLine()) {
            	String temp = scanner.nextLine();
            	String[] tempArr = temp.split(",");
            	// Set file elements to variables
            	String a = tempArr[0].trim();
            	Airline airlineObj = new Airline(a);
            	String plane = tempArr[1].trim();
            	int flightNum = Integer.parseInt(tempArr[2].trim());
            	if (flightNum < 0) {
            		throw new IllegalArgumentException("Flight Number must be greater than 0!" );
            	}
            	String depAirport = tempArr[3].trim();
            	String arrAirport = tempArr[4].trim();
            	int tempTime = Integer.parseInt(tempArr[5].trim());
            	if ((tempTime <= 0) && (tempTime >= 24)) {
            		throw new IllegalArgumentException("Time must be an integer between 0 and 24!");
            	}
            	int passengers = Integer.parseInt(tempArr[6].trim());
            	if (passengers < 0) {
            		throw new IllegalArgumentException("Passegers cannot be a negative number! ");
            	}
            	// Add variables to Flight object
            	Flight tempFlight = new Flight(airlineObj, plane, flightNum, depAirport, arrAirport, tempTime, passengers);
            	flightArr.add(tempFlight);
            } 
        } 
        // Throw error if file is not found or does not exist
        catch (FileNotFoundException e) {
            System.out.println("File not found! Check spelling or file location. ");
        	}
		// Scanner to read user's revenue choice (1, 2 or 3)
        Scanner choice = new Scanner(System.in);
		System.out.println("Enter (1) for SinglePrice, (2) for TwoClasses, and (3) for MultiClass ");
		int userChoice = choice.nextInt();
		// Scanner to read user's airline code
		Scanner airlineCode = new Scanner(System.in);
		System.out.println("Enter airline to limit by: ");
		String airlineChoice = airlineCode.nextLine();
		// Create new array limited to the user's choice airline code
		List<Flight> newArr = new ArrayList<Flight>();
		for (Flight flight: flightArr) {
			if (flight.getAirline().getCode() == airlineChoice) {
				newArr.add(flight);
			}
		}
		// Throw error if no flights match given code
		if (newArr.size() == 0) {
			throw new IllegalStateException ("No flights match your airline code! ");
		}
		
		long answer = 0; // Prime answer as long
		// Call correct file for userChoice
		if (userChoice == 1) {
			SinglePrice tempCall = new SinglePrice();
			answer = tempCall.getRevenue(newArr);
		}
		else if (userChoice == 2) {
			TwoClasses tempCall = new TwoClasses();;
			System.out.println(tempCall.getRevenue(newArr));
		}
		else if (userChoice == 3) {
			MultiClass tempCall = new MultiClass();
			System.out.println(tempCall.getRevenue(newArr));
		}
		else {
			throw new IllegalArgumentException("Response must be 1, 2 or 3! ");
		}
		// Print out the final answer
		System.out.println(answer);

        
        
        
        
        
        
	}
	
}
