from src.lattice import IsingLattice

lattice = IsingLattice(
    size=4,
    dimension=2,
    random_seed=42,
)

print(lattice.spins)
print(lattice.spins.shape)