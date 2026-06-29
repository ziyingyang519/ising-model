import numpy as np

from src.simulation import Simulation
from src.lattice import IsingLattice


class MonteCarloRunner:

    def __init__(
        self,
        lattice_size: int,
        temperature: float,
        equilibration_steps: int,
        measurement_steps: int,
    ):

        self.sim = Simulation(
            lattice=IsingLattice(
                size=lattice_size,
                dimension=2,
            ),
            temperature=temperature,
        )

        self.eq_steps = equilibration_steps
        self.mc_steps = measurement_steps

    def run(self):

        for _ in range(self.eq_steps):
            self.sim.step()

        energies = []
        magnetizations = []

        for _ in range(self.mc_steps):
            self.sim.step()

            energies.append(self.sim.energy())
            magnetizations.append(abs(self.sim.magnetization()))

        return (
            np.array(energies),
            np.array(magnetizations),
        )