package classcode.interfaces;

public class InterfaceDriver {

	public static void main(String[] args) {
		// Create a new Invoice and print
		Invoice myInvoice = new Invoice("ACME", 200000);
//		System.out.println(myInvoice);
		
		SalaryEmployee salaryEmp = new SalaryEmployee("Greta", "Great", 150000);
//		System.out.println(salaryEmp);
		
		Payable[] payments = new Payable[3];
		payments[0] = myInvoice;
		payments[1] = salaryEmp;
		for (int i=0; i<2; i++) {
			System.out.println(payments[i] + " Payment: " + payments[i].getAmount());
		}
		

	}

}
