import math


class Vector:
    """Three-dimensional Euclidian-space vector.

    :obj:`Vector` is an coordinate system-agnostic data structure for manipulating and storing Euclidian vectors. It
    currently supports manipulation in both Cartesian and spherical coordinate systems. Conversions between the two
    coordinate systems are handled automatically, so either representation can be read from or written to at any time.
    """

    def __init__(self, cart: tuple = None, sphr: tuple = None):
        """Class constructor.

        Initializes a new :obj:`Vector` object using the provided coordinate system.

        Args:
            cart (:obj:`tuple`, optional): length three tuple with Cartesian coordinates. Formatted (x, y, z)
            sphr (:obj:`tuple`, optional): length three tuple with Spherical coordinates. Formatted (r, θ, φ)

        Note:
            Only *one* of **cart** and **sphr** arguments should be set.
        """

        if (cart is None) == (sphr is None):
            raise ValueError("one and only one of cart and sphr must be specified")

        if cart is not None:
            if not type(cart) is tuple:
                raise TypeError("cart must be type `tuple`")
            elif not len(cart) == 3:
                raise TypeError("cart tuple must be length 3")
            else:
                self.__computed = "cartesian"
                self.__x, self.__y, self.__z = cart
        elif sphr is not None:
            if not type(sphr) is tuple:
                raise TypeError("sphr must be type `tuple`")
            elif not len(sphr) == 3:
                raise TypeError("sphr tuple must be length 3")
            else:
                self.__computed == "spherical"
                self.__r, self.__theta, self.__phi = sphr

    @property
    def cartesian(self) -> tuple:
        """Length three tuple with Cartesian coordinates. Formatted (x, y, z)"""

        if self.__computed == "spherical":
            self.__computed = None
            self.__x, self.__y, self.__z = Vector.__spherical_to_cartesian(self.spherical)
        return self.__x, self.__y, self.__z

    @property
    def x(self) -> float:
        """Cartesian x value."""

        return self.cartesian[0]

    @property
    def y(self) -> float:
        """Cartesian y value."""

        return self.cartesian[1]

    @property
    def z(self) -> float:
        """Cartesian z value."""

        return self.cartesian[2]

    @property
    def spherical(self) -> tuple:
        """Length three tuple with Spherical coordinates. Formatted (r, θ, φ)"""

        if self.__computed == "cartesian":
            self.__computed = None
            self.__r, self.__theta, self.__phi = Vector.__cartesian_to_spherical(self.cartesian)
        return self.__r, self.__theta, self.__phi

    @property
    def r(self) -> float:
        """Spherical r value."""

        return self.spherical[0]

    @property
    def theta(self) -> float:
        """Spherical theta value."""

        return self.spherical[1]

    @property
    def phi(self) -> float:
        """Spherical phi value."""

        return self.spherical[2]

    @staticmethod
    def __cartesian_to_spherical(cartesian: tuple) -> tuple:
        """Converts a Cartesian coordinate vector to a spherical one.

        Args:
            cartesian (:obj:`tuple`): Cartesian vector input. Formatted (x, y, z)

        Returns:
            Identical coordinate vector in spherical representation.

        See Also:
            https://en.wikipedia.org/wiki/Spherical_coordinate_system#Cartesian_coordinates
        """

        cart_x, cart_y, cart_z = cartesian
        r = math.sqrt(cart_x ** 2 + cart_y ** 2 + cart_z ** 2)
        theta = math.atan2(cart_y, cart_x)
        phi = math.atan2(math.sqrt(cart_x ** 2 + cart_y ** 2), cart_z)  # angle from z axis down
        return r, theta, phi

    @staticmethod
    def __spherical_to_cartesian(spherical: tuple) -> tuple:
        """Converts a spherical coordinate vector to a Cartesian one.

        Args:
            spherical (:obj:`tuple`): spherical vector input. Formatted (r, θ, φ)

        Returns:
            Identical coordinate vector in Cartesian representation.

        See Also:
            https://en.wikipedia.org/wiki/Spherical_coordinate_system#Cartesian_coordinates
        """

        sphr_r, sphr_theta, sphr_phi = spherical
        x = sphr_r * math.sin(sphr_theta) * math.cos(sphr_phi)
        y = sphr_r * math.sin(sphr_theta) * math.sin(sphr_phi)
        z = sphr_r * math.cos(sphr_theta)
        return x, y, z


class Position(Vector):
    pass


class Velocity(Vector):
    pass


class Acceleration(Vector):
    pass
