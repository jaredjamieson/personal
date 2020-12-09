package classcode.inheritance;

public class Medicine extends Inedible {
	protected boolean prescription;  // Indicates whether a medication is prescription or not

	public Medicine(String name, double wholesalePrice, double retailPrice,
			boolean taxable, String manufacturer, String material, boolean prescription) {
		super(name, wholesalePrice, retailPrice, taxable, manufacturer,
				material);
	}
	/**
	 * constructor to create an empty medicine
	 */
	public Medicine(){}
	
	/**
	 * @return  whether the item is prescription
	 */
	public boolean isPrescription(){
		return prescription; 
	}
	
	/**
	 * @param  sets whether the item is prescription
	 */
	public void setAlcohol(boolean prescription){
		this.prescription = prescription; 
	}
	
	public String toString(){
		return super.toString() + " Prescription: " + prescription;
	}

	

}
