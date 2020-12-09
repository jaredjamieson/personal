package uml;

/**
 * @author JaredJamieson
 *
 */
public class Driver {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Institution myInst = new Institution("Visa", "1010 Address Rd.", 1234567890); // Creates Institution object
		System.out.println(myInst.getName()); // Prints Visa
		System.out.println(myInst.getAddress()); // Prints 1010 Address Rd.
		System.out.println(myInst.getPhoneNumber()); // Prints 123456890
		
	}

}
