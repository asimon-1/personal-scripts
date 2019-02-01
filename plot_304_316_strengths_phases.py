import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import interp1d


def f_to_c(f):
    """Converts a temperature given in Fahrenheit to Celsius"""
    return (f - 32.0) * 5.0 / 9.0


def c_to_f(c):
    """Converts a temperature given in Celsius to Fahrenheit"""
    return 9.0 / 5.0 * c + 32


def ksi_to_mpa(p):
    """Converts a stress given in ksi to MPa"""
    return p * 6.895


def replace_0_fe(value, _):
    """Replaces the value with "Fe" if it is 0, else return the argument unchanged."""
    if value == 0:
        return "Fe"
    else:
        return value


def quadratic_fit(*args):
    """Returns two np series for a quadratic fit to the provided points. If only
    two arguments are given, a line is returned. Otherwise, a quadratic fit is
    returned. The returned fit spans only between the minimum and maximum x
    coordinate provided.

    Arguments: args {lists/tuples of length 2} -- The points to be fit. There must be
        at least two of these provided.
    """
    x = [p[0] for p in args]
    y = [p[1] for p in args]
    assert len(x) >= 2
    if len(x) > 2:
        fit = interp1d(x, y, kind="quadratic")
    else:
        fit = interp1d(x, y, kind="linear")
    x = np.linspace(min(x), max(x))
    y = fit(x)
    return x, y


def ss_strengths():
    """Generates a plot comparing the yield strength and ultimate tensile
    strength of type 304 and type 316 stainless steels.
    """

    STYLES = ["ro--", "bo--", "go--", "co--"]
    DF = pd.DataFrame(
        data={
            "TemperatureF": [70.0, 200.0, 400.0, 600.0],
            "Type 304 Tensile Strength": [85.0, 78.0, 69.0, 64.0],
            "Type 304 Yield Strength": [35.0, 33.0, 28.0, 24.0],
            "Type 316 Tensile Strength": [85.0, 84.0, 82.0, 77.0],
            "Type 316 Yield Strength": [38.5, 38.0, 36.0, 34.0],
        }
    )

    plt.figure()
    ax_1 = plt.subplot(111)
    for data, style in zip(
        [
            DF["Type 304 Tensile Strength"],
            DF["Type 304 Yield Strength"],
            DF["Type 316 Tensile Strength"],
            DF["Type 316 Yield Strength"],
        ],
        STYLES,
    ):
        ax_1.plot(DF["TemperatureF"], data, style, label=data.name)

    pad = 10  # Padding between labels and axes

    ax_1.set_xlim(50.0, 650.0)
    ax_1.set_ylim(0.0, 90.0)
    ax_1.set_xlabel(r"Temperature [$^\circ\mathrm{F}$]", labelpad=pad)
    ax_1.set_ylabel("[ksi]", labelpad=pad)

    ax_2 = ax_1.twiny()  # Create alternate axis for x
    ax_2.set_xlim(f_to_c(ax_1.get_xlim()[0]), f_to_c(ax_1.get_xlim()[1]))
    ax_2.set_xlabel(r"Temperature [$^\circ\mathrm{C}$]", labelpad=pad)

    ax_3 = ax_1.twinx()  # Create alternate axis for y
    ax_3.set_ylim(ksi_to_mpa(ax_1.get_ylim()[0]), ksi_to_mpa(ax_1.get_ylim()[1]))
    ax_3.set_ylabel("[MPa]", labelpad=pad)
    ax_3.yaxis.set_label_position("right")
    ax_1.grid()
    ax_1.legend()


def ss_phases():
    """Generates a plot of the phase diagram for steels."""
    # Create figure and set up the axes
    plt.figure(figsize=(6, 8))

    ax_1 = plt.subplot(111)
    ax_1.set_xlim(0.0, 5.0)
    ax_1.set_ylim(500.0, 1800.0)
    ax_1.set_xlabel("Carbon Content, wt%")
    ax_1.set_ylabel(r"Temperature, $^\circ\mathrm{C}$")
    ax_1.xaxis.set_major_locator(plt.MaxNLocator(10))
    ax_1.yaxis.set_major_locator(plt.MaxNLocator(13))
    ax_1.xaxis.set_major_formatter(plt.FuncFormatter(replace_0_fe))

    ax_2 = ax_1.twiny()
    ax_2.set_xlabel("Carbon Content, at%")
    ax_2.set_xlim(0.0, 20.0)
    ax_2.xaxis.set_major_locator(plt.MaxNLocator(10))
    ax_2.xaxis.set_major_formatter(plt.FuncFormatter(replace_0_fe))

    ax_3 = ax_2.twinx()
    ax_3.set_ylabel(r"Temperature, $^\circ\mathrm{F}$")
    ax_3.yaxis.set_label_position("right")
    ax_3.set_ylim(c_to_f(ax_1.get_ylim()[0]), c_to_f(ax_1.get_ylim()[1]))
    ax_3.yaxis.set_ticks(np.arange(1000, 3272, 200))

    # Plot the phase boundaries
    ax_1.plot(*quadratic_fit([2.1, 1140], [5, 1140]), "k")  # E to C
    ax_1.plot(*quadratic_fit([0.08, 730], [5, 730]), "k")  # P to K
    ax_1.plot(*quadratic_fit([0, 520], [0.05, 700], [0.08, 730]), "k")  # lower to P
    ax_1.plot(*quadratic_fit([0, 910], [0.3, 800], [0.8, 732]), "k")  # upper to S
    ax_1.plot(*quadratic_fit([0, 830], [0.03, 780], [0.08, 730]), "k")  # upper to P
    ax_1.plot(*quadratic_fit([0.8, 732], [1.5, 1000], [2.1, 1140]), "k")  # S to E
    ax_1.plot(*quadratic_fit([4.25, 1140], [5, 1200]), "k")  # C to D
    ax_1.plot(*quadratic_fit([0.5, 1490], [2.5, 1340], [4.25, 1140]), "k")  # B to C
    ax_1.plot(*quadratic_fit([0, 1534], [0.3, 1510], [0.5, 1490]), "k")  # A to B
    ax_1.plot(*quadratic_fit([0.2, 1488], [1.5, 1285], [2.1, 1140]), "k")  # H to E
    ax_1.plot(*quadratic_fit([0, 1534], [0.1, 1490]), "k")  # A to H
    ax_1.plot(*quadratic_fit([0.1, 1490], [0.5, 1490]), "k")  # H to B
    ax_1.plot(*quadratic_fit([0, 1350], [0.05, 1440], [0.1, 1490]), "k")  # lower to H
    ax_1.plot(*quadratic_fit([0, 1350], [0.05, 1400], [0.2, 1488]), "k")  # lower to H

    # Add text labels to the phases
    ax_1.text(3.5, 1550, "Liquid", ha="center")
    ax_1.text(2.5, 600, "Ferrite + Cementite", ha="center")
    ax_1.text(3, 900, "Austenite + Cementite", ha="center")
    ax_1.text(1, 1100, "Austenite", ha="center")
    ax_1.text(2.5, 1210, "Liquid\n+\nAustenite", ha="center")
    ax_1.annotate(
        "Austenite\n+\nFerrite",
        xy=(0.4, 800),
        xytext=(0.5, 900),
        ha="center",
        arrowprops={"arrowstyle": "->", "facecolor": "k"},
    )
    ax_1.annotate(
        "Ferrite",
        xy=(0.1, 700),
        xytext=(0.5, 620),
        ha="center",
        arrowprops={"arrowstyle": "->", "facecolor": "k"},
    )


if __name__ == "__main__":
    ss_phases()
    plt.tight_layout()
    plt.savefig("ss_phase_diagram.png", dpi=300, bbox_inches="tight")
    ss_strengths()
    plt.tight_layout()
    plt.savefig("304_316_Strengths.png", dpi=300, bbox_inches="tight")
