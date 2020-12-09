package classcode.interfaces;

public class SalaryEmployee extends Employee {

	double salary; 

	public SalaryEmployee(String firstName, String lastName, double salary) {
		super(firstName, lastName);
		this.salary = salary;
	}
	
	/**
	 * Inherited from Employee but must be implemented to fulfill Payable interface
	 */
	public String getName() {
		return this.firstName + this.lastName;
	}

	/** 
	 * Required for Payable interface
	 */
	public double getAmount() {
		// TODO Auto-generated method stub
		return getWeeklyPay();
	}


	public double getWeeklyPay() {
		return salary/52; 
	}
	
	public String toString() {
		return super.toString() + " Salary: " + salary; 
	}
}

