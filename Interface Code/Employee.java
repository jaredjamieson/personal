package classcode.interfaces;

public abstract class Employee implements Payable {

	String firstName;
	String lastName;

	public Employee(String firstName, String lastName) {
		this.firstName = firstName;
		this.lastName = lastName;	
	}
	/**
	 * Required for Payable interface
	 */
	public String getName() {
		// TODO Auto-generated method stub
		return null;
	}

	/** 
	 * Required for Payable interface
	 */
	public double getAmount() {
		// TODO Auto-generated method stub
		return 0;
	}

	public String toString() {
		return firstName + " " + lastName; 
	}


}
