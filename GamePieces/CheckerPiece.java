public class CheckerPiece extends GamePiece {

	public CheckerPiece() {
		// TODO Auto-generated constructor stub
	}

	public CheckerPiece(String name) {
		super(name);
		// TODO Auto-generated constructor stub
	}
	
	public String move() {
		return "Diagonal one or more blocks"; 
	}
	
	public String toString() {
		return super.toString() + ": " +  move(); 
	}

}
