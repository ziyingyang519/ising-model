import numpy as np


def energy(spins: np.ndarray) -> float:
    """
    Compute the dimensionless Ising energy E/J.
    """

    lattice_size = spins.shape[0]
    dimension = spins.ndim

    total_energy = 0.0

    for site in np.ndindex(spins.shape):

        spin = spins[site]
        neighbor_sum = 0

        for axis in range(dimension):

            positive = list(site)
            negative = list(site)

            positive[axis] = (positive[axis] + 1) % lattice_size
            negative[axis] = (negative[axis] - 1) % lattice_size

            neighbor_sum += spins[tuple(positive)]
            neighbor_sum += spins[tuple(negative)]

        total_energy += -spin * neighbor_sum

    return total_energy / (2 * dimension)


def magnetization(spins: np.ndarray) -> float:
    """
    Compute the total magnetization.
    """

    return float(np.sum(spins))