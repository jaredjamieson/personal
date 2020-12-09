public class ChessPiece extends GamePiece {

	public ChessPiece() {
		// TODO Auto-generated constructor stub
	}

	public ChessPiece(String name) {
		super(name);
		// TODO Auto-generated constructor stub
	}

	@Override
	public String move() {
		// TODO Auto-generated method stub
		if (name.equals("pawn"))
			return "One square horizontally or laterally";
		else if (name.equals("queen"))
			return "One or more squares diagonally";
		return "Unknown";
	}
	
	public String toString() {
		return super.toString() + ": " +  move(); 
	}

}
