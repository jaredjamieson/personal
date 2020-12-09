package classcode.inheritance;

public class Beverage extends Edible {
	
	boolean alcohol;   // Indicates whether beverage is alcoholic or not

	public Beverage(String name, double wholesalePrice, double retailPrice,
			boolean taxable, double size, int calories, double fat, 
			String expirationDate, boolean alcohol) {
		super(name, wholesalePrice, retailPrice, taxable, 
				size, calories, fat, expirationDate);
		this.alcohol = alcohol; 
 	}
	/**
	 * constructor to create an empty beverage
	 */
	public Beverage(){}
	
	/**
	 * @return  whether the item contains alcohol
	 */
	public boolean isAlcohol(){
		return alcohol; 
	}
	
	/**
	 * @param  sets whether the item contains alcohol
	 */
	public void setAlcohol(boolean alcohol){
		this.alcohol = alcohol; 
	}
	
	public String toString(){
		return super.toString() + " Contains alcohol: " + alcohol;
	}



}
