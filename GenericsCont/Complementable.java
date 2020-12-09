package genericsLab;

/**
 * @author JaredJamieson
 * The complementable interface specifies the compliment operations for
 * any type T to the classes implementing it.
 * 
 * Complement is a unary operation that returns an object's inverse.
 */
public interface Complementable<T> {
	public T complement();
}
