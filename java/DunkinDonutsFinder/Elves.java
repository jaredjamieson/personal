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

public class Elves {
	public static double calculateDimmensions() throws FileNotFoundException {
		// Open txt file and create reader
		File myfile = new File("./small.txt");
		Scanner reader = new Scanner (myfile);
		// Prime totalDimmensions with 0.0
		double totalDimmensions = 0.0;
		// Iterate while there are more line in the file
		while(reader.hasNextLine()) {
			String[] values = reader.nextLine().replace("/n", "").split("x");
			// Assign values in file to length, width, or height
			double l = Double.valueOf(values[0]);
			double w = Double.valueOf(values[1]);
			double h = Double.valueOf(values[2]);
			// Assign sides to calculations
			double side1 = (l * w);
			double side2 = (w * h);
			double side3 = (h * l);
			// Find the smallest side
			double smallestSide = Math.min(Math.min(side1, side2), side3);
			// Multiply each side by 2 and add sum
			double surfaceArea = (2 * side1) + (2 * side2) + (2 * side3);
			// Increase total surface area and total dimensions
			surfaceArea += smallestSide;
			totalDimmensions += surfaceArea;
			
		}
		// Close scanner and return total
		reader.close();
		return totalDimmensions;
	}
	/**
	 * @return - returns total dimmensions value
	 */
	
	
	
	/**
	 * @param args
	 */
	public static void main(String[] args) throws FileNotFoundException{
		// Main method
		System.out.println(calculateDimmensions());
	}

}
