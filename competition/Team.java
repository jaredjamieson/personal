package lab10;

public class Team implements Comparable<Team>{
	private int id;
	// Other instance variables here
	
	public Team(int number){
		this.id = number;
		//Add more code here as needed
	}
	
	public int compareTo(Team other){
		return 0; // Placeholder -- Write your own code to compare 2 teams
	}
}