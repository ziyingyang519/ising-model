from src.algorithms import WolffAlgorithm
from src.lattice import IsingLattice
from src.observables import energy, magnetization


class Simulation:

    def __init__(
        self,
        lattice: IsingLattice,
        temperature: float,
    ):
        self.lattice = lattice

        self.algorithm = WolffAlgorithm(
            lattice=lattice,
            temperature=temperature,
        )

    def step(self):
        self.algorithm.step()

    def energy(self):
        return energy(self.lattice.spins)

    def magnetization(self):
        return magnetization(self.lattice.spins)