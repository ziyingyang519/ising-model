from dataclasses import dataclass


@dataclass
class SimulationConfig:
    """
    Configuration for Ising model Monte Carlo simulations.
    """

    # Lattice
    lattice_size: int = 32
    dimension: int = 2

    # Physical parameters
    coupling_constant: float = 1.0

    # Simulation
    equilibration_steps: int = 3000
    measurement_steps: int = 5000

    # Random seed
    random_seed: int = 42