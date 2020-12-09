package menu_example;
/**
 * This application is used to show to the differences 
 * between abstract classes, interfaces, and generics 
 * and how these are used. The idea is to allow the user to 
 * create menus for various events such as the SuperBowl, 
 * cookie swaps, and formal dinners. 
 * The MenuDriver class is used to create instances of 
 * menus and show
 * @author he302979
 *
 */

public class MenuDriver {

	public static void main(String[] args) {
		// Create a sugar cookie recipe
		String[] ingredients1 = {"2 3/4 C flour", "1 tsp baking soda", "1/2 tsp bakin powder", "1 C butter", "1 1/2 C sugar", "1 egg", "1 tsp vanilla"};
		SugarCookieRecipe myRecipe1 = new SugarCookieRecipe("Simple Sugar Cookies", ingredients1);
		myRecipe1.setMeasure("Directions: \nIn a small bowl, stir together flour, baking soda, and baking powder. Set aside.");
		myRecipe1.setMix("In a large bowl, cream together the butter and sugar until smooth. Beat in egg and vanilla. \nGradually blend in the dry ingredients. Roll rounded teaspoonfuls of dough into balls, \nand place onto ungreased cookie sheets.");
		myRecipe1.setBake("Bake 8 to 10 minutes in 350 degree oven.");
		myRecipe1.setServingSize("3 cookies");
//		System.out.println(myRecipe1);
		
		// Create another sugar cookie recipe
		String[] ingredients2 = {"3 C flour", "1/2 tsp bakin powder", "1 C butter", "1 1/2 C sugar", "1 egg", "2 T lemon juice", "1 tsp vanilla"};
		SugarCookieRecipe myRecipe2 = new SugarCookieRecipe("Lemon Sugar Cookies", ingredients2);
		myRecipe2.setMeasure("Directions: \nIn a small bowl, stir together flour and baking powder. Set aside.");
		myRecipe2.setMix("In a large bowl, cream together the butter and sugar until smooth. Beat in egg, lemon and vanilla. \nGradually blend in the dry ingredients. Roll rounded teaspoonfuls of dough into balls, \nand place onto ungreased cookie sheets");
		myRecipe2.setBake("Bake 8 to 10 minutes in 350 degree oven.");
		myRecipe2.setServingSize("2 cookies");
//		System.out.println(myRecipe2);
		
		// Create a menu for a cookie swap
		Menu<Edible> cookieSwap = new Menu<Edible>();
		cookieSwap.addRecipe(myRecipe1);
		cookieSwap.addRecipe(myRecipe2);
		System.out.println(cookieSwap);
	}

}
