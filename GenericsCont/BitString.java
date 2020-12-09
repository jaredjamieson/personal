	package genericsLab;
	import java.util.BitSet;

	/**
	 * @author JaredJamieson
	 * The BitString class returns the compliment of an argument string 
	 * consisting of 1's and 0's
	 */
	public class BitString implements Complementable<BitString> {
		// Internal storage of 1's and 0's as a string
		private BitSet storage;
		private int storageSize;
		
		public BitString() {
			// Constructs and empty BitSet
			storage = new BitSet();
			storageSize = 0;
		}
		
		public BitString(String something) throws IllegalArgumentException {
			try {
				// Constructs a BitSet of a string
				storageSize = something.length();
				storage = new BitSet(storageSize);
				//System.out.println(storageSize);
				for (int i = 0; i < storageSize; i++) {
					if (something.charAt(i) == '1') {
						storage.set(i);  // Sets all 1's to True
					}
					else if (something.charAt(i) != '0') {
						throw new IllegalArgumentException(); // Any nonzero 
						                            // arguments throw error
					}
				}
			}
			catch (IllegalArgumentException msg) {
				System.out.println("Arguments must consist of 1's and/or 0's!");
			}
		}

		/**
		* @return 
		* @Override
		* Complement returns the inversion of a bitString
		*/
		public BitString complement() {
			storage.flip(0, storageSize);
			return this;
		}
		
		/**
		 * @return string representation of BitSet
		 */
		public String toString() {
			String tempStr = ""; // Initialized empty string
			for (int i = 0; i < storageSize; i++) {
				if (storage.get(i) == true) {
					tempStr += '1'; // Append 1 for true values
				}
				else {
					tempStr += '0'; // Append 0 for false values
				}
			}
			return tempStr; // Return string
		}
		
		/**
		 * @param obj is the BitString being compared to
		 * Returns true if both BitSets are the same length and have the same
		 * arguments or false otherwise.
		 */
		public boolean equals (BitString obj) {
			if (storageSize != obj.storageSize) {
				return false;
			}
			BitSet objBit = obj.storage;
			return objBit.equals(storage);
		}
	}
