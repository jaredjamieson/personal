package uml;

/**
 * @author JaredJamieson
 * The Transaction class holds a transaction date, explanation and amount.  
 */
public class Transaction {
	private int transactionDate;
	private String explanation;
	private double amount;
	private int transactionNumber;
	
	public Transaction(int tempTransactionDate, String tempExplanation, double tempAmount, int tempTransactionNumber) {
		this.transactionDate = tempTransactionDate;
		this.explanation = tempExplanation;
		this.amount = tempAmount;
		this.transactionDate = tempTransactionNumber;
	}
}
