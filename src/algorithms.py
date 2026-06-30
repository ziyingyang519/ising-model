import numpy as np

from src.lattice import IsingLattice


class WolffAlgorithm:
    def __init__(
        self,
        lattice: IsingLattice,
        temperature: float,
        coupling_constant: float = 1.0,
    ):
        self.lattice = lattice
        self.temperature = temperature
        self.J = coupling_constant

    @property
    def beta(self) -> float:
        return 1.0 / self.temperature

    @property
    def bond_probability(self) -> float:
        return 1.0 - np.exp(-2.0 * self.beta * self.J)
    
    def step(self) -> None:
        spins = self.lattice.spins
        N = self.lattice.size

        seed = tuple(np.random.randint(N) for _ in range(self.lattice.dimension))

        spin0 = spins[seed]

        in_cluster = np.zeros_like(spins, dtype=bool)
        in_cluster[seed] = True

        stack = [seed]

        while stack:

            site = stack.pop()

            for neighbor in self.lattice.neighbors(site):
                if (
                    not in_cluster[neighbor]
                    and spins[neighbor] == spin0
                    and np.random.random() < self.bond_probability
                ):
                    in_cluster[neighbor] = True
                    stack.append(neighbor)

        spins[in_cluster] *= -1