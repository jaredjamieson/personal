/**
 * A GamePiece represents a general game piece that has a move. 
 * 
 * @author he302979
 *
 */

public abstract class GamePiece {
	protected String name;   // Allows me to access the name in subclasses

	public GamePiece() {
		// TODO Auto-generated constructor stub
	}
	
	public GamePiece(String name) {
		this.name = name;
	}
	
	public abstract String move(); 

	public String toString() {
		return name;
	}

}
