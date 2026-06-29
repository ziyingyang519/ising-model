import numpy as np


def energy(spins: np.ndarray) -> float:
    """
    Compute the dimensionless Ising energy E/J.
    """

    lattice_size = spins.shape[0]

    total_energy = 0.0

    for i in range(lattice_size):
        for j in range(lattice_size):

            spin = spins[i, j]

            neighbors = (
                spins[(i + 1) % lattice_size, j]
                + spins[(i - 1) % lattice_size, j]
                + spins[i, (j + 1) % lattice_size]
                + spins[i, (j - 1) % lattice_size]
            )

            total_energy += -spin * neighbors

    return total_energy / 4.0


def magnetization(spins: np.ndarray) -> float:
    """
    Compute the total magnetization.
    """

    return float(np.sum(spins))