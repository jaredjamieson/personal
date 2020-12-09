package uml;

/**
 * @author JaredJamieson
 * The Statement class holds a payment due date, finance charge and minimum payment.
 */
public class Statement {
	private int paymentDueDate;
	private double financeCharge;
	private double minimumPayment;
	private int statementDate;	// Connects to CreditCardAccount
	
	public Statement(int tempPaymentDueDate, double tempFinanceCharge, double tempMinimumPayment, int tempStatementDate) {
		this.paymentDueDate = tempPaymentDueDate;
		this.financeCharge = tempFinanceCharge;
		this.minimumPayment = tempMinimumPayment;
		this.statementDate = tempStatementDate;
	}
}
