package lab10;

import java.util.Scanner;

public class lab10Driver {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Competition test = new Competition("teams.txt", "competition.csv");
		test.readTeamFile(test.tf);
		//System.out.println("Teams objects added.");
		test.readCompetitionFile(test.cf);
		//System.out.println("Matches objects added.");
		
		Scanner numTeams = new Scanner(System.in);
		System.out.println("Enter number of results to show: ");
		int userNumTeams = numTeams.nextInt();
		
		Scanner teamId = new Scanner(System.in);
		System.out.println("Enter team ID: ");
		int userTeamId = teamId.nextInt();
		
		
		
	}

}
