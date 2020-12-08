package lab11;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class FileReader {
	private String raceFile;  // String race file
	private ArrayList<PrizeWinnings> raceArr = new ArrayList<PrizeWinnings>();  // Array list of races
	private int totalRaces;  // Total races
	private double totalRacePurse;  // Total race purse
	// Constructor
	public FileReader(String tempFile) {
		this.raceFile = tempFile;
	}
		
	/**
	 * Read a file of races and add races to raceArr
	 * One line = one race
	 */
	public void readRaces() {
		
	try {
		File raceFileObj = new File(raceFile);
		Scanner reader = new Scanner(raceFileObj);
		//RaceFactory tempFactory = new RaceFactory(this.raceFile);
		while (reader.hasNextLine()) {
			String contents = reader.nextLine();
			String[] tempLine = contents.trim().split(",");  // Create string array of race variables
			RaceFactory tempFactory = new RaceFactory(tempLine);
			Race tempRace = tempFactory.getRace();  // Create a temporary flat or jump race object
			if (tempRace.getDirection().contentEquals(" Counterclockwise")) {  // If race is run in UK
				RaceAdaptor tempAdaptor = new RaceAdaptor();  // Initialize RaceAdaptor
				tempRace.setPurse(tempAdaptor.convertPoundsToUSD(tempRace));  // Convert pounds to USD and reassign to this race
				tempRace.setLength(tempAdaptor.convertFurlongToMiles(tempRace));  // Converts furlongs to miles and reassign to this race
			}
			raceArr.add(tempRace);  // Add race obj to raceArr
			totalRaces += 1;  // Increase total races by 1
			totalRacePurse += tempRace.getPurse();  // Increase totalRacePurse by tempRace purse
		}
		reader.close();
	}
	
	catch (FileNotFoundException ex) { System.out.println("File not found: " + ex.getMessage()); }
	}
	
	/**
	 * @return ArrayList<Race> race array
	 */
	public ArrayList<PrizeWinnings> getRaceList() { return this.raceArr; }
	
	/**
	 * Print all races
	 */
	public void printAll() {
		for (PrizeWinnings tempRace: raceArr) {
			System.out.println(tempRace);
		}
	}
	
	/**
	 * Print the number of races and the average race purse
	 */
	public void printTotalInfo() {
		System.out.println("\nTotal number of races: " + this.totalRaces
				 + "\nAverage race purse: " + this.getAverageRacePurse());
	}
	
	/**
	 * @return int total races
	 */
	public int getTotalRaces() { return this.totalRaces; }
	
	/**
	 * @return total race purse
	 */
	public double getTotalRacePurse() { return this.totalRacePurse; }
	
	/**
	 * @return average race purse
	 */
	public double getAverageRacePurse() {
		return this.totalRacePurse/this.totalRaces;
	}
}
