package classcode.inheritance;

public class Food extends Edible {
	protected String category; /* plant, meat, processed */  

	public Food(String name, double wholesalePrice, double retailPrice,
			boolean taxable, double size, int calories, double fat, 
			String expirationDate, String category) {
		super(name, wholesalePrice, retailPrice, taxable, size, calories, 
				fat, expirationDate);
		// TODO Auto-generated constructor stub
	}
	/**
	 * constructor to create an empty food
	 */
	public Food(){}

	/**
	 * @return  food category
	 */
	public String getCategory(){
		return category; 
	}
	/**
	 * @param   category of the food
	 */
	public void setCategory(String category){
		this.category = category;
	}
	
	public String toString(){
		return super.toString() + " Category: " + category;
	}


}
