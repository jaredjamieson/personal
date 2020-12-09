package classcode.inheritance;

public class GroceryItem {
	protected String name; 
	protected double wholesalePrice;
	protected double retailPrice;
	protected boolean taxable;

	/**
	 * @param wholesalePrice - wholesale price of a Grocery Item
	 * @param retailPrice    - retail price of a Grocery Item
	 * @param taxable	     - indication of whether the item is taxable or not
	 */
	public GroceryItem(String name, double wholesalePrice, double retailPrice, boolean taxable) {
		this.name = name;
		this.wholesalePrice = wholesalePrice;
		this.retailPrice = retailPrice;
		this.taxable = taxable;
	}
	
	/**
	 * constructor to create an empty grocery item
	 */
	public GroceryItem(){}
	
	/**
	 * @return  the wholesale price of the item
	 */
	public double getWholesalePrice(){
		return wholesalePrice; 
	}
	
	/**
	 * @return  the retail price of the item
	 */
	public double getRetailPrice(){
		return retailPrice; 
	}
	/**
	 * @return  whether the item is taxable or not
	 */
	public boolean isTaxable(){
		return taxable; 
	}
	
	/**
	 * 
	 * @param   wholesale price of the item
	 */
	public void setWholesalePrice(double wholesalePrice){
		this.wholesalePrice = wholesalePrice; 
	}
	/**
	 * 
	 * @param retail price of the item
	 */
	public void setRetailPrice(double retailPrice){
		this.retailPrice = retailPrice; 
	}
	/**
	 * 
	 * @param  set whether item is taxable or not
	 */
	public void setTaxable(boolean taxable){
		this.taxable = taxable; 
	}
	/** 
	 * @return  the price margin for the item
	 */
	public double calcPriceMargin(){
		return wholesalePrice = retailPrice; 
	}
	
	/** 
	 * prints the name, wholesale and retail prices and whether it is taxable or not. 
	 */
	public String toString(){
		String tax = ""; 
		if (taxable){
			tax = " is taxable";
		}
		return ("Name: " + name + " Wholesale price: " + wholesalePrice + " Retail price: " + 
		     retailPrice + tax);
	}

}
