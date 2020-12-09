package menu_example;
/**
 * The CookieRecipe class extendsthe Recipe class
 * with the "bake" method as all cookies must be 
 * baked to some degree. Baking might imply putting
 * in the fridge or putting on a plate for presentation.
 * @author he302979
 *
 */

public abstract class CookieRecipe extends Recipe {
	
	/**
	 * Default constructor
	 */
	
	public CookieRecipe() {
		super();
	}
	
	/** 
	 * Constructor that takes ingredients
	 * @param ingreds
	 */
	public CookieRecipe(String name, String[] ingreds) {
		super(name, ingreds);
 	}
	
	/**
	 * This method returns a string that describes 
	 * how a recipe needs to be baked. 
	 * @return
	 */
	public abstract String bake();
	
	public String toString() {
		return super.toString();
	}

}
