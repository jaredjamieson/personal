package classcode.inheritance;
import java.util.*;
import java.time.LocalDate;

public class Edible extends GroceryItem {
	protected double size;        // Size of item
	protected int	 calories;    // Number of calories
	protected double fat;         // Fat grams
	protected String expirationDate; // Expiration date of item

	/** 
	 * Constructor calls supertype constructor and sets 
	 * @param name
	 * @param wholesalePrice
	 * @param retailPrice
	 * @param taxable
	 * @param size
	 * @param fat
	 * @param expirationDate
	 */
	public Edible(String name, double wholesalePrice, double retailPrice, boolean taxable,
			double size, int calories, double fat, String expirationDate) {
		super(name, wholesalePrice, retailPrice, taxable);
		this.size = size;
		this.calories = calories;
		this.fat = fat;
		this.expirationDate = expirationDate; 
	}
	/**
	 * constructor to create an empty edible item
	 */
	public Edible(){}
	
	/**
	 * @return  the size of the food item
	 */
	public double getSize(){
		return size; 
	}
	
	/**
	 * @return  the number of calories in the item
	 */
	public int getCalories(){
		return calories; 
	}
	
	/**
	 * @return  the fat in grams of the food item
	 */
	public double getFat(){
		return fat; 
	}
	/**
	 * @return  the expiration date of the item
	 */
	public String getExpirationDate(){
		return expirationDate; 
	}
	
	/**
	 * 
	 * @param   size of item
	 */
	public void setSize(double size){
		this.size = size;
	}
	/**
	 * @param  the number of calories in the item
	 */
	public void setCalories(int calories){
		this.calories = calories;
	}
	/**
	 * 
	 * @param fat grams of the item
	 */
	public void setFat(double fat){
		this.fat = fat; 
	}
	/**
	 * 
	 * @param  set expiration date
	 */
	public void setExpirationDate(String expirationDate){
		this.expirationDate = expirationDate; 
	}
	
	/**
	 * 
	 * @return  true if the item is expired and false otherwise
	 */
	
	public boolean isExpired(){
		LocalDate today = LocalDate.now();
		return today.isAfter(LocalDate.parse(expirationDate));
	}
	 
	public String toString(){
		return super.toString() + " Size: " + size + " Calories: " + calories + 
				" Fat: " + fat + " Expiration Date: " + expirationDate;
	}

}
