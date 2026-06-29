from src.lattice import IsingLattice
from src.simulation import Simulation

lattice = IsingLattice(
    size=8,
    dimension=2,
    random_seed=42,
)

sim = Simulation(
    lattice=lattice,
    temperature=2.5,
)

print("Energy =", sim.energy())
print("Magnetization =", sim.magnetization())

sim.step()

print("After one Wolff step")

print("Energy =", sim.energy())
print("Magnetization =", sim.magnetization())