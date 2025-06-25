import os
import sys
from matplotlib import pyplot as plt
import numpy as np

# Ensure imports work when running the script directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.signal_generation import sum_sine_waves
from src.filter_design import (
    butter_lowpass,
    butter_highpass,
    butter_bandpass,
    apply_filter,
    rc_lowpass,
    rc_highpass,
    rc_bandpass,
)


def main(fig_dir="results/figures"):
    os.makedirs(fig_dir, exist_ok=True)

    fs = 10000
    duration = 0.1
    components = [(50, 1.0), (500, 0.5)]
    t, signal = sum_sine_waves(components, fs, duration)

    plt.figure()
    plt.plot(t, signal)
    plt.xlabel("Time [s]")
    plt.title("Original signal")
    orig_path = os.path.join(fig_dir, "task4_2_sum_of_two_sine_waves.png")
    plt.savefig(orig_path)
    plt.close()

    # Analog RC calculations
    r_lp, c_lp = rc_lowpass(50)
    r_hp, c_hp = rc_highpass(500)
    rbp, cbp = rc_bandpass(400, 600)
    print(f"RC low-pass: R={r_lp:.1f} Ohm, C={c_lp:.2e} F")
    print(f"RC high-pass: R={r_hp:.1f} Ohm, C={c_hp:.2e} F")
    print(f"RC band-pass (400-600 Hz): R={rbp:.1f} Ohm, C={cbp:.2e} F")

    # Digital low-pass
    b_lp, a_lp = butter_lowpass(50, fs, order=1)
    filtered_lp = apply_filter(signal, b_lp, a_lp)
    plt.figure()
    plt.plot(t, filtered_lp)
    plt.xlabel("Time [s]")
    plt.title("Low-pass filtered")
    lp_path = os.path.join(fig_dir, "task4_5_lowpass_filtered.png")
    plt.savefig(lp_path)
    plt.close()

    # Digital high-pass
    b_hp, a_hp = butter_highpass(500, fs, order=1)
    filtered_hp = apply_filter(signal, b_hp, a_hp)
    plt.figure()
    plt.plot(t, filtered_hp)
    plt.xlabel("Time [s]")
    plt.title("High-pass filtered")
    hp_path = os.path.join(fig_dir, "task4_8_highpass_filtered.png")
    plt.savefig(hp_path)
    plt.close()

    # Add 1000 Hz component and band-pass
    _, sig1000 = sum_sine_waves([(1000, 1.0)], fs, duration)
    composite = signal + sig1000
    plt.figure()
    plt.plot(t, composite)
    plt.xlabel("Time [s]")
    plt.title("Three-sine composite")
    comp_path = os.path.join(fig_dir, "task4_9_sum_three_sine_waves.png")
    plt.savefig(comp_path)
    plt.close()
    b_bp, a_bp = butter_bandpass(400, 600, fs, order=1)
    filtered_bp = apply_filter(composite, b_bp, a_bp)
    plt.figure()
    plt.plot(t, filtered_bp)
    plt.xlabel("Time [s]")
    plt.title("Band-pass filtered")
    bp_path = os.path.join(fig_dir, "task4_12_bandpass_filtered.png")
    plt.savefig(bp_path)
    plt.close()

    return orig_path, lp_path, hp_path, comp_path, bp_path


if __name__ == "__main__":
    main()
