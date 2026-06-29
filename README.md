# Ising Model Monte Carlo Simulation

A modular Python implementation of the **2D Ising Model** using the **Wolff Cluster Algorithm** for Monte Carlo simulations of phase transitions.

---

## Overview

The Ising model is one of the most important models in statistical physics for studying ferromagnetism and critical phenomena.

This project implements a two-dimensional square-lattice Ising model with periodic boundary conditions and the Wolff Cluster Algorithm, which efficiently reduces critical slowing down near the phase transition.

---

## Features

- 2D square lattice Ising model
- Wolff Cluster Monte Carlo algorithm
- Periodic boundary conditions
- Temperature sweep simulation
- Automatic calculation of
  - Energy
  - Magnetization
  - Specific Heat
  - Magnetic Susceptibility
- Automatic generation of result figures

---

## Project Structure

```text
ising-model/
│
├── figures/
├── notebooks/
├── src/
│   ├── algorithms.py
│   ├── lattice.py
│   ├── observables.py
│   ├── plotting.py
│   ├── runner.py
│   └── simulation.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

```bash
git clone https://github.com/ziyingyang519/ising-model.git

cd ising-model

pip install -r requirements.txt
```

---

## Usage

```bash
python main.py
```

Running the program automatically:

- performs Monte Carlo simulations
- sweeps over a range of temperatures
- computes thermodynamic observables
- saves all figures into the `figures/` folder

---

## Results

### Energy

![Energy](figures/energy.png)

---

### Magnetization

![Magnetization](figures/magnetization.png)

---

### Specific Heat

![Specific Heat](figures/specific_heat.png)

---

### Magnetic Susceptibility

![Susceptibility](figures/susceptibility.png)

---

## Physics Background

The Ising model describes interacting magnetic spins

\[
s_i=\pm1
\]

with Hamiltonian

\[
H=-J\sum_{\langle i,j\rangle}s_is_j
\]

The Wolff Cluster Algorithm greatly improves sampling efficiency near the critical temperature by flipping clusters of aligned spins instead of individual spins.

---

## Future Work

- 3D Ising Model
- Metropolis Algorithm
- Finite-size scaling analysis
- Binder cumulant
- Parallel simulations

---

## Author

**Tzu-Ying Yang**

Department of Bio-Industrial Mechatronics Engineering

National Taiwan University

---

## License

MIT License