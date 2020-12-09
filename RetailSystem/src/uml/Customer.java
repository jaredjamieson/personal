package uml;
import java.util.ArrayList;

/**
 * @author JaredJamieson
 * Customer holds a customer's name
 */
public class Customer {
	private String name;
	private ArrayList<MailingAddress> addresses;
	
	public Customer(String tempName) {
		this.name = tempName;
	}
	
	/**
	 * @param tempAddress
	 * addAddress would add a MailingAddress to addresses.  
	 */
	public void addAddress(MailingAddress tempAddress) {
		System.out.println("addAddress would add a MailingAddress to addresses. ");
	}
}
