#!/bin/bash

# 一键创建目录
mkdir -p data \
         notebooks \
         src \
         results/figures \
         results/audio \
         reports

# 初始化顶层文件
touch README.md requirements.txt

# 创建 Notebooks 占位
touch notebooks/tutorial5_task2_fft.ipynb \
      notebooks/tutorial5_task3_correlation.ipynb \
      notebooks/tutorial5_task4_filtering.ipynb

# 创建源码模块占位
touch src/signal_generation.py \
      src/fft_utils.py \
      src/correlation_utils.py \
      src/filter_design.py

# 创建结果占位
touch results/figures/task2_waveform.png \
      results/figures/task2_spectrum.png
touch results/audio/stereo_example.wav \
      results/audio/noisy_correlation.png

# 创建报告占位
touch reports/Tutorial5_Report.pdf

echo "目录结构已创建完毕！"
