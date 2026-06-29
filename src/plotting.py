import matplotlib.pyplot as plt


def plot_curve(
    x,
    y,
    xlabel,
    ylabel,
    title,
    filename,
):
    plt.figure(figsize=(6, 4))

    plt.plot(
        x,
        y,
        "o-",
        linewidth=2,
        markersize=5,
    )

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    plt.grid(True)
    plt.tight_layout()

    plt.savefig(f"figures/{filename}")

    plt.close()