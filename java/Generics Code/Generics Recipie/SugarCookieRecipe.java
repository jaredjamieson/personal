package menu_example;
/**
 * This class represents a sugar cookie recipe
 * We'll have to provide directions for measuring and mixing 
 * and baking
 * @author he302979
 *
 */
public class SugarCookieRecipe extends CookieRecipe {
    // Variable to hold the instructions to measure, mix and bake
	protected String measureInst; 
	protected String mixInst;
	protected String bakeInst; 
	protected String servingSize;
	
	/**
	 * No argument constructor
	 */
	public SugarCookieRecipe() {
		super();
	}
	
	/**
	 * Constructor that takes ingredients
	 * @param ingreds
	 */
	public SugarCookieRecipe(String name, String[] ingreds) {
		super(name, ingreds);
 	}

	/**
	 * Set the instructions to measure ingredients
	 * @param measure
	 */
	public void setMeasure(String measure) {
		measureInst = measure;
	}
	/**
	 * Set the instructions to mix ingredients
	 * @param mix
	 */
	public void setMix(String mix) {
		mixInst = mix;
	}
	/**
	 * Set the instructions to bake the cookies
	 * @param bake
	 */
	public void setBake(String bake) {
		bakeInst = bake;
	}
	
	public void setServingSize(String serving) {
		servingSize = serving; 
	}
	
	/**
	 * Must implement this method to fulfill the Edible interface
	 */
	public String getServingSize() {
		return servingSize;
	}
	
	/** 
	 * Retrieve the baking instructions
	 */
	@Override
	public String bake() {
		return bakeInst;
	}

	/**
	 * Retrieve the instructions for measuring ingredients
	 */
	@Override
	public String measureIngredients() {
		return measureInst;
	}

	/**
	 * Retrieve the instructions for mixing
	 */
	@Override
	public String mixIngredients() {
		return mixInst;
	}
	
	public String toString() {
		return super.toString() + "\n" + measureInst + 
				"\n" + mixInst + "\n" + bakeInst +
				"\n" + "Serving size: " + servingSize; 
		
	}

}
