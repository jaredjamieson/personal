package menu_example;
/**
 * The Recipe class represents a recipe that can be
 * used to create a menu dish. Since recipes can be 
 * very specific, here we are going to define what behaviors
 * are needed, but not exactly how to implement them. 
 * @author he302979
 *
 */

public abstract class Recipe implements Edible {
	// Represent the ingredients in the recipe as
	// an array of strings. If we were more sophisticated,
	// we could use an ArrayList of foods or food pairs
	private String recipeName; 
	private String[] ingredients;

	/**
	 * Default constructor creates sufficient space to hold
	 * 20 ingredients. 
	 */
	public Recipe() {
		ingredients = new String[20];
 	}
	
	/**
	 * This constructor creates sufficient space to hold
	 * numIngredients ingredients. 
	 */
	public Recipe(String name, int numIngredients) {
		recipeName = name; 
		ingredients = new String[numIngredients];
 	}
	
	/**
	 * This constructor is passed a list of ingredients and
	 * adds them to the ingredients for the recipe
	 */
	public Recipe(String name, String[] ingreds) {
		recipeName = name; 
		ingredients = new String[ingreds.length];
		for (int i=0; i<ingreds.length; i++){
			ingredients[i] = ingreds[i];
		}
 	}
	
	public String getRecipeName() {
		return recipeName; 
	}
	
	/**
	 * This method returns a string array of ingredients.
	 * @return
	 */
	public String[] getIngredients() {
		return ingredients; 
	}
	
	/** 
	 * This method returns a string indicating how to
	 * measure the ingredients
	 * @return
	 */
	public abstract String measureIngredients();
	
	/**
	 * This method returns a string indicating how the 
	 * ingredients should be mixed together
	 * @return
	 */
	public abstract String mixIngredients();
	
	public String toString() {
		String temp = "\n" + recipeName + "\n" + "Ingredients: \n";
		for (int i=0; i<ingredients.length; i++){
			temp = temp + ingredients[i] + "\n";
		}
		return temp;
	}
	
   // We'll delay the bake method to CookieRecipe and other
   // subtypes as not all recipes require baking (e.g., punch)

}
/*
• An abstract classes is like the general cookie recipe.
◦ You know that you'll need some ingredients, but the exact ingredients aren't defined for you. 
◦ You know the behaviors, but not exactly how to implement all of them. 
• In the MyCookie abstract class below, there are no ingredients listed, and the instructions are very general. 
◦ So you can't actually make a Cookie, but you know the actions to be taken generally to bake a cookie. 
◦ Cookie tells you what to do to make a cookie, but not all of the details of how to do that.
*/ 