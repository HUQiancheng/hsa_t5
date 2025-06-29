Utilities for Tutorial 5: Acoustic Sensors and Signal Processing
================================================================

This repository provides helper functions and standalone Python scripts to
complete the FFT, correlation and filtering exercises from the tutorial.

The scripts are located in the `scripts/` directory and can be executed
directly. They prepend the repository root to `PYTHONPATH` so they work even
when invoked via an absolute path from a different directory. Typical usage is:

```
python scripts/task2_fft.py
python scripts/task3_correlation.py
python scripts/task4_filtering.py
```

Results such as plots and audio files are stored in the `results/` folder.
Generated files use the naming scheme `taskX_Y_<description>` so they can be
matched to the task numbers in the assignment.
The repository keeps empty directories under version control via `.gitkeep`
files so scripts can create their outputs without additional setup.

Tests are provided in `tests/`. Install the dependencies listed in
`requirements.txt` and run `pytest` to verify everything works.
