/**
 * @author Jared Jamieson
 * @author Jordan Vaglivelo
 * Lab 4
 *
 */
import java.io.File;
import java.util.Scanner;
import java.io.FileNotFoundException;
import java.lang.Math;
/*
 * DunkinFinder returns the closest Dunkin Donuts to the given longitude and latitude
 */
public class DunkinFinder {
	/**
	 * findNearest calculates distance between longitudes and latitudes to return the closest store
	 */
	public static String findNearest(double longitude, double latitude) throws FileNotFoundException{
		// Open csv file and create reader
		File myfile = new File("./dunkindonuts.csv");
		Scanner reader = new Scanner (myfile);
		// Prime nearestStore with an empty string and nearestDistance to unnaturally large numbers
		String nearestStore = "";
		double nearestDistance = 9999999.99;
		// Skip over first line of file
		reader.nextLine();
		
		while(reader.hasNextLine()) {
			String[] values = reader.nextLine().replace("/n", "").split(",");
			// Variables indexing current lines longitude and latitude
			double currLong = Double.valueOf(values[6]);
			double currLat = Double.valueOf(values[7]);
			// Math to find distance
			double x = (Math.cos(Math.toRadians(currLat)) * Math.cos(Math.toRadians(currLong))) - (Math.cos(Math.toRadians(latitude)) * Math.cos(Math.toRadians(longitude)));
			double y = (Math.cos(Math.toRadians(currLat)) * Math.sin(Math.toRadians(currLong))) - (Math.cos(Math.toRadians(latitude)) * Math.sin(Math.toRadians(longitude)));
			double z = Math.sin(Math.toRadians(currLat)) - Math.sin(Math.toRadians(latitude)); 
			double distance = 3958.761 * Math.sqrt((Math.pow(x, 2)) + (Math.pow(y, 2)) + (Math.pow(z, 2)));
			// If current store is closer, reassign closest store to current
			if (distance < nearestDistance) {
				nearestDistance = distance;
				nearestStore = values[1] + ", " + values[2] + ", " + values[3];
			}	
		}
		// Close reader and return closest store
		reader.close();
		return nearestStore;
	}

	public static void main(String[] args) throws FileNotFoundException {
		// Main Function
		System.out.println(findNearest(38.8978, -77.0364));
	}
}
