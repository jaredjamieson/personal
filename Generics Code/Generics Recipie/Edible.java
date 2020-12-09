/**
 * 
 */
package menu_example;

/**
 * The Edible interface describes the behavior of edible 
 * foodstuffs including serving size, calories, fat, etc.
 * @author he302979
 *
 */
public interface Edible {
	
	/**
	 * All edible items need a serving size
	 * @return
	 */
	
	public abstract String getServingSize(); 
	// Other methods that should be defined include
	// getCalories, getFat, etc. 

}
