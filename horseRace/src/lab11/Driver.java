package lab11;

public class Driver {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String raceFile = "races.txt";
		FileReader tempReader = new FileReader(raceFile);  // Create new file reader
		tempReader.readRaces();  // Read through file and create races
		tempReader.printAll();  // Print out each race
		tempReader.printTotalInfo();  // Print out final total races and average race purse
	}

}
