package classcode.inheritance;

public class Inedible extends GroceryItem {
		protected String manufacturer;
		protected String material; 

		public Inedible(String name, double wholesalePrice, double retailPrice,
				boolean taxable, String manufacturer, String material) {
			super(name, wholesalePrice, retailPrice, taxable);
			this.manufacturer = manufacturer;
			this.material = material;
		}
		
		/**
		 * constructor to create an empty inedible item
		 */
		public Inedible(){}

		/**
		 * @return  the manufacturer of the nonfood item
		 */
		public String getManufacturer(){
			return manufacturer; 
		}
		/**
		 * @return  the material of the nonfood item
		 */
		public String getMaterial(){
			return material; 
		}
		
		/**
		 * 
		 * @param    manufacturer of nonfood item
		 */
		public void setManufacturer(String manufacturer){
			this.manufacturer = manufacturer;
		}
		/**
		 * 
		 * @param    material of nonfood item
		 */
		public void setMaterial(String material){
			this.material = material;
		}
		
		public String toString(){
			return super.toString() + " Manufacturer: " + manufacturer + 
					" Material: " + material; 		}


}
