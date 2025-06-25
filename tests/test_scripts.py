import os
from scripts import task2_fft, task3_correlation, task4_filtering


def test_task2_fft(tmp_path):
    wave, spec, noisy_wave, noisy_spec = task2_fft.main(output_dir=str(tmp_path))
    for path in [wave, spec, noisy_wave, noisy_spec]:
        assert os.path.exists(path) and os.path.getsize(path) > 0


def test_task3_correlation(tmp_path):
    fig_dir = tmp_path / "fig"
    audio_dir = tmp_path / "aud"
    fig_dir.mkdir()
    audio_dir.mkdir()
    outputs = task3_correlation.main(fig_dir=str(fig_dir), audio_dir=str(audio_dir), delay=0.001, scale=0.9)
    for path in outputs:
        assert os.path.exists(path) and os.path.getsize(path) > 0


def test_task4_filtering(tmp_path):
    outputs = task4_filtering.main(fig_dir=str(tmp_path))
    for path in outputs:
        assert os.path.exists(path) and os.path.getsize(path) > 0
