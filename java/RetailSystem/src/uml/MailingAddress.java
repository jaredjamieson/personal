package uml;
import java.util.ArrayList;

/**
 * @author JaredJamieson
 * The MainingAddress class holds addresses and phone numbers
 */
public class MailingAddress {
	private String address;
	private int phoneNumber;
	private ArrayList<Customer> customers;
	
	public MailingAddress(String tempAddress, int tempPhoneNumber) {
		this.address = tempAddress;
		this.phoneNumber = tempPhoneNumber;
	}
	
	/**
	 * @param tempCustomer
	 * addCustomer adds a customer to customers.  
	 */
	public void addCustomer(Customer tempCustomer) {
		System.out.println("addCustomer would add a customer to customers. ");
	}
	
}
