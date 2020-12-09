package classcode.interfaces;

public class Invoice implements Payable{
	String companyName;
	double invoiceAmount; 

	public Invoice(String companyName, double invoiceAmount) {
		this.companyName = companyName; 
		this.invoiceAmount = invoiceAmount; 
	}
	/**
	 * Required to implement the Payable interface
	 */
	public String getName() {
		return companyName;
	}
	
	public double getAmount() {
		return invoiceAmount;
	}
	
	public String toString() {
		return companyName + " " + invoiceAmount;
	}

}
