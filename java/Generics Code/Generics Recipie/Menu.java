package menu_example;
import java.util.ArrayList;
/**
 * The Menu class represents a menu that contains recipes that
 * are used to create dishes for an event. 
 * Menu is a generic class as we will pass in specific types of 
 * recipes depending on the event being hosted. 
 * @author he302979
 *
 */
public class Menu<T> {
	// We'll use an ArrayList to hold the recipes
	private ArrayList<T> recipeList; 
	
	/**
	 * Zero argument constructor that creates an empty
	 * ArrayList with capacity 10. 
	 */
	public Menu() {
		// 
		recipeList = new ArrayList<T>();
	}
	
	/**
	 * Add a recipe to the menu
	 * @param recipe
	 */
	public void addRecipe(T recipe) {
		recipeList.add(recipe);
	}
	
	public String toString() {
		String temp = "";
		for(int i = 0; i < recipeList.size(); i++)
		{
		    temp = temp + recipeList.get(i);
		}
		return temp;
	}

}
