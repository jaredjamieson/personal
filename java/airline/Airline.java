package lab9;

/**
 * @author Jared Jamieson
 * Airline constructs an object consisting of a string code
 */

public class Airline {
	
	// Declare variables
	private String code;
    
	/**
	 * Construct the AirLine object
	 * @param c : code
	 */
    public Airline(String c){
        code = c;
    }
    
    /**
     * @return the string code
     */
    public String getCode(){
        return code;
    }
    
}
