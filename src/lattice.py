import numpy as np


class IsingLattice:
    """
    Represent a 2D or 3D Ising spin lattice.
    """

    def __init__(
        self,
        size: int,
        dimension: int,
        random_seed: int | None = None,
    ):
        self.size = size
        self.dimension = dimension

        if random_seed is not None:
            np.random.seed(random_seed)

        self.spins = self.initialize()

    def initialize(self) -> np.ndarray:
        """
        Create a random spin configuration.
        """

        shape = (self.size,) * self.dimension

        return np.random.choice(
            [-1, 1],
            size=shape,
        )
    
    def wrap_index(self, index: int) -> int:
        """
        Wrap an index to implement periodic boundary conditions.
        """

        return index % self.size