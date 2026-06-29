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

        i0 = np.random.randint(N)
        j0 = np.random.randint(N)

        spin0 = spins[i0, j0]

        in_cluster = np.zeros_like(spins, dtype=bool)
        in_cluster[i0, j0] = True

        stack = [(i0, j0)]

        while stack:
            i, j = stack.pop()

            neighbors = [
                (self.lattice.wrap_index(i + 1), j),
                (self.lattice.wrap_index(i - 1), j),
                (i, self.lattice.wrap_index(j + 1)),
                (i, self.lattice.wrap_index(j - 1)),
            ]

            for ni, nj in neighbors:
                if (
                    not in_cluster[ni, nj]
                    and spins[ni, nj] == spin0
                    and np.random.random() < self.bond_probability
                ):
                    in_cluster[ni, nj] = True
                    stack.append((ni, nj))

        spins[in_cluster] *= -1