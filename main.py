import numpy as np

from src.runner import MonteCarloRunner
from src.plotting import plot_curve

def main():

    temperatures = np.linspace(0.2, 10.0, 20)

    energies = []
    magnetizations = []
    specific_heats = []
    susceptibilities = []

    for temperature in temperatures:

        print(f"Running T = {temperature:.2f} K")

        runner = MonteCarloRunner(
            lattice_size=32,
            temperature=temperature,
            equilibration_steps=1000,
            measurement_steps=5000,
        )

        result = runner.run()
        energies.append(result["energy"])
        magnetizations.append(result["magnetization"])
        specific_heats.append(result["specific_heat"])
        susceptibilities.append(result["susceptibility"])

    print("\nSimulation completed.")

    plot_curve(
        temperatures,
        energies,
        "Temperature (K)",
        "Energy",
        "Energy vs Temperature",
        "energy.png",
    )

    plot_curve(
        temperatures,
        magnetizations,
        "Temperature (K)",
        "Magnetization",
        "Magnetization vs Temperature",
        "magnetization.png",
    )

    plot_curve(
        temperatures,
        specific_heats,
        "Temperature (K)",
        "Specific Heat",
        "Specific Heat vs Temperature",
        "specific_heat.png",
    )

    plot_curve(
        temperatures,
        susceptibilities,
        "Temperature (K)",
        "Susceptibility",
        "Susceptibility vs Temperature",
        "susceptibility.png",
    )

    print("All figures saved.")



if __name__ == "__main__":
    main()