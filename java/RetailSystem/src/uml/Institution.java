package uml;
import java.util.ArrayList;

/**
 * @author JaredJamieson
 * Institution takes a name, address and phone number and holds account numbers in an
 * array. 
 */
public class Institution {
	private ArrayList<CreditCardAccount> accounts;  // The institution's collection of 
													// credit card accounts
	private String name;
	private String address;
	private int phoneNumber;
	
	/**
	 * Constructs the institution class
	 * @param tempName
	 * @param tempAddress
	 * @param tempPhoneNumber
	 */
	public Institution(String tempName, String tempAddress, int tempPhoneNumber) {
		this.name = tempName;
		this.address = tempAddress;
		this.phoneNumber = tempPhoneNumber;
	}
	
	/**
	 * Adds a credit card account to internal array
	 * @param tempAccount
	 */
	public void addAccount(CreditCardAccount accountNumber) {
		System.out.println("This would add a customer's account to the institution");
	}
	
	public CreditCardAccount findAccount(CreditCardAccount tempAccount) {
		System.out.println("findAccount would return a specific account from the accounts. ");
		return tempAccount;
	}
	
	/**
	 * @return Institution's name
	 */
	public String getName() {
		return this.name;
	}
	
	/**
	 * @return Institution's address
	 */
	public String getAddress() {
		return this.address;
	}
	
	/**
	 * @return Institution's phone number
	 */
	public int getPhoneNumber() {
		return this.phoneNumber;
	}

}
