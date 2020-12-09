package uml;

/**
 * @author JaredJamieson
 * CreditCardAccount holds a maximum credit, current balance and account number.  
 */
public class CreditCardAccount {
	private double maximumCredit;
	private double currentBalance;
	private int accountNumber;	// Connects to Institution
	
	public CreditCardAccount(float tempMaximumCredit, int tempAccountNumber) {
		this.maximumCredit = tempMaximumCredit;
		this.accountNumber = tempAccountNumber;
		this.currentBalance = 0.0;
	}
	
	public CreditCardAccount(float tempMaximumCredit, float tempCurrentBalance, int tempAccountNumber) {
		this.maximumCredit = tempMaximumCredit;
		this.accountNumber = tempAccountNumber;
		this.currentBalance = tempCurrentBalance;
	}
	
	/**
	 * 
	 * @param tempStatementDate
	 * @return
	 */
	public Statement findStatement(Statement tempStatementDate) {
		System.out.println("findStatement would return a Statment matching tempStatementDate.  ");
		return null;
	}
}
