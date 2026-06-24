#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Full Reproduction Script for:
"A Dynamic Three-Level Hybrid Framework for Solving Large-Scale Fuzzy Systems"

This script automatically:
1. Generates all 6 figures from the paper
2. Creates requirements.txt, README.md, LICENSE files
3. Saves raw data to CSV
4. Creates the complete GitHub repository structure

Author: N. Hassasi
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from matplotlib.lines import Line2D

# ============================================================================
# PART 0: CREATE ALL SUPPORTING FILES
# ============================================================================

def create_requirements_txt():
    """Create requirements.txt file"""
    content = 'matplotlib>=3.5.0\nnumpy>=1.21.0\npandas>=1.3.0\n'
    with open('requirements.txt', 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ Created: requirements.txt")


def create_readme_md():
    """Create README.md file"""
    content = ('# Reproduction of Results for "A Dynamic Three-Level Hybrid Framework for Solving Large-Scale Fuzzy Systems"\n\n'
               'This repository contains the complete code and data to reproduce all figures and tables from the paper.\n\n'
               '**Author:** N. Hassasi  \n'
               '**Affiliation:** Department of Mathematics, Mal.C., Islamic Azad University, Malayer, Iran  \n'
               '**Email:** naderhassasi@iau.ac.ir\n\n'
               '---\n\n'
               '## Contents\n\n'
               '- `full_reproduction.py`: Main Python script to generate all figures\n'
               '- `requirements.txt`: Required Python packages\n'
               '- `reproduction_results/`: Output directory containing:\n'
               '  - `figures/`: All 6 figures in PNG format (300 DPI, RGB, 24-bit color)\n'
               '  - `data/`: Raw data in CSV format\n\n'
               '---\n\n'
               '## Requirements\n\n'
               '- Python 3.7 or higher\n'
               '- Required packages: matplotlib, numpy, pandas\n\n'
               '---\n\n'
               '## Installation\n\n'
               'Clone the repository and install dependencies:\n\n'
               '```\n'
               'git clone https://github.com/yourusername/reproduction.git\n'
               'cd reproduction\n'
               'pip install -r requirements.txt\n'
               '```\n\n'
               '---\n\n'
               '## Usage\n\n'
               'Run the main script:\n\n'
               '```\n'
               'python full_reproduction.py\n'
               '```\n\n'
               '---\n\n'
               '## Output\n\n'
               'All figures will be saved in the `reproduction_results/figures/` directory:\n\n'
               '| Filename | Description |\n'
               '|----------|-------------|\n'
               '| `Fig1_Example1_Algorithm_Switching.png` | Algorithm switching vs. alpha for triangular system (Example 1) |\n'
               '| `Fig2_Example1_Performance_Metrics.png` | Key performance indicators vs. alpha for triangular system |\n'
               '| `Fig3_Example1_Comparison_vs_Standalone.png` | Performance comparison for Example 1 at alpha = 0.5 |\n'
               '| `Fig4_Example2_Algorithm_Performance.png` | Algorithm switching and parallel performance for trapezoidal system (Example 2) |\n'
               '| `Fig5_Example2_Comparison_vs_Standalone.png` | Performance comparison for Example 2 at alpha = 0.6 |\n'
               '| `Fig6_Example2_Relative_Improvement.png` | Relative improvement (speedup and memory saving) for Example 2 |\n\n'
               '---\n\n'
               '## Data\n\n'
               'Raw data is saved in `reproduction_results/data/raw_data.csv`.\n\n'
               '---\n\n'
               '## Figure Specifications\n\n'
               '- **Format:** PNG\n'
               '- **Resolution:** 300 DPI\n'
               '- **Color Mode:** RGB (24-bit)\n'
               '- **Font:** Times New Roman / Arial (size 10-12)\n'
               '- **File Size:** < 2 MB per figure\n\n'
               '---\n\n'
               '## License\n\n'
               'This code is released under the MIT License. See LICENSE file for details.\n\n'
               '---\n\n'
               '## Citation\n\n'
               'If you use this code in your research, please cite the original paper:\n\n'
               '```\n'
               '@article{hassasi2024dynamic,\n'
               '  title={A Dynamic Three-Level Hybrid Framework for Solving Large-Scale Fuzzy Systems: Intelligent Integration of GMRES, BiCGSTAB, and IDR(s) with Real-Time Decision Making},\n'
               '  author={Hassasi, N.},\n'
               '  journal={To be published},\n'
               '  year={2024}\n'
               '}\n'
               '```\n')
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ Created: README.md")


def create_license():
    """Create LICENSE file (MIT License)"""
    content = ('MIT License\n\n'
               'Copyright (c) 2024 N. Hassasi\n\n'
               'Permission is hereby granted, free of charge, to any person obtaining a copy\n'
               'of this software and associated documentation files (the "Software"), to deal\n'
               'in the Software without restriction, including without limitation the rights\n'
               'to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n'
               'copies of the Software, and to permit persons to whom the Software is\n'
               'furnished to do so, subject to the following conditions:\n\n'
               'The above copyright notice and this permission notice shall be included in all\n'
               'copies or substantial portions of the Software.\n\n'
               'THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n'
               'IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n'
               'FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n'
               'AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n'
               'LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n'
               'OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n'
               'SOFTWARE.\n')
    with open('LICENSE', 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ Created: LICENSE")


# ============================================================================
# PART 1: CONFIGURATION
# ============================================================================

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 11
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 13
plt.rcParams['legend.fontsize'] = 10
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['savefig.bbox'] = 'tight'
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'white'

# Create output directories
os.makedirs('reproduction_results/figures', exist_ok=True)
os.makedirs('reproduction_results/data', exist_ok=True)

# ============================================================================
# PART 2: DATA FROM TABLES (Example 1 - Triangular System)
# ============================================================================

# Table 2: Results for Example 1
alpha_ex1 = np.array([0.0, 0.2, 0.5, 0.8, 1.0])
iterations_ex1 = np.array([312, 278, 195, 114, 82])
time_ex1 = np.array([876.4, 765.8, 543.2, 324.7, 234.9])
parallel_eff_ex1 = np.array([83, 85, 89, 92, 94])
condition_ex1 = np.array([5.12e8, 2.87e8, 8.45e7, 1.92e7, 4.76e6])
residual_ex1 = np.array([6.45e-9, 5.92e-9, 4.13e-9, 2.87e-9, 1.54e-9])
algo_labels_ex1 = ['IDR(12)', 'IDR(12)', 'BiCGSTAB', 'GMRES', 'GMRES']
colors_ex1 = ['#DC143C', '#DC143C', '#1E90FF', '#228B22', '#228B22']

# Table 3: Performance Metrics for Example 1
metrics_names = ['Residual Reduction Rate', 'Parallel Efficiency', 
                 'Memory Efficiency', 'Speedup Factor', 'Convergence Rate']
alpha0_metrics = [0.892, 83, 42, 65, 1.124]
alpha1_metrics = [0.961, 94, 52, 78, 1.456]

# Table 4: Comparison with Standalone Methods (Example 1, alpha=0.5)
methods_ex1 = ['Proposed\nThree-Level', 'GMRES\n(Standard)', 
               'BiCGSTAB\n(Base)', 'IDR(12)\n(Standalone)']
time_comp_ex1 = [543.2, 1023.6, 765.8, 874.3]
memory_comp_ex1 = [35.5, 67, 41, 45]
iter_comp_ex1 = [195, 312, 245, 287]
conv_rate_comp_ex1 = [1.287, 0.954, 1.123, 1.045]
parallel_eff_comp_ex1 = [89, 74, 81, 78]

# ============================================================================
# PART 3: DATA FROM TABLES (Example 2 - Trapezoidal System)
# ============================================================================

# Table 5: Results for Example 2
alpha_ex2 = np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
iterations_ex2 = np.array([387, 342, 274, 201, 132, 87])
time_ex2 = np.array([1245.6, 1087.3, 876.9, 654.2, 432.8, 287.5])
parallel_eff_ex2 = np.array([81, 83, 86, 89, 92, 94])
condition_ex2 = np.array([8.24e8, 4.13e8, 1.76e8, 5.92e7, 1.45e7, 3.28e6])
residual_ex2 = np.array([7.82e-9, 6.95e-9, 5.43e-9, 3.87e-9, 2.15e-9, 1.28e-9])
algo_labels_ex2 = ['IDR(16)', 'IDR(16)', 'IDR(12)', 'BiCGSTAB', 'GMRES', 'GMRES']
colors_ex2 = ['#DC143C', '#DC143C', '#FF8C00', '#1E90FF', '#228B22', '#228B22']

# Table 6: Performance Metrics for Example 2
alpha0_metrics_ex2 = [0.891, 81, 48, 62, 1.087]
alpha06_metrics_ex2 = [0.924, 89, 53, 74, 1.345]
alpha1_metrics_ex2 = [0.956, 94, 57, 82, 1.523]

# Table 7: Comparison with Standalone Methods (Example 2, alpha=0.6)
methods_ex2 = ['Proposed\nThree-Level', 'GMRES\n(Standard)', 
               'BiCGSTAB\n(Base)', 'IDR(12)\n(Standalone)']
time_comp_ex2 = [654.2, 1247.8, 892.5, 987.3]
memory_comp_ex2 = [59, 128, 68, 74]
iter_comp_ex2 = [201, 345, 267, 287]
conv_rate_comp_ex2 = [1.345, 0.987, 1.123, 1.089]
parallel_eff_comp_ex2 = [89, 72, 78, 76]

# ============================================================================
# PART 4: SAVE RAW DATA
# ============================================================================

# Example 1 data (5 rows)
df_ex1 = pd.DataFrame({
    'alpha': alpha_ex1,
    'iterations': iterations_ex1,
    'time_sec': time_ex1,
    'parallel_efficiency': parallel_eff_ex1,
    'condition_number': condition_ex1,
    'residual_norm': residual_ex1,
    'algorithm': algo_labels_ex1,
    'example': ['Example 1'] * len(alpha_ex1)
})

# Example 2 data (6 rows)
df_ex2 = pd.DataFrame({
    'alpha': alpha_ex2,
    'iterations': iterations_ex2,
    'time_sec': time_ex2,
    'parallel_efficiency': parallel_eff_ex2,
    'condition_number': condition_ex2,
    'residual_norm': residual_ex2,
    'algorithm': algo_labels_ex2,
    'example': ['Example 2'] * len(alpha_ex2)
})

# Combined data
df_combined = pd.concat([df_ex1, df_ex2], ignore_index=True)
df_combined.to_csv('reproduction_results/data/raw_data.csv', index=False)
print("✓ Saved: raw_data.csv")

# ============================================================================
# PART 5: FIGURE 1 - Algorithm Switching vs. alpha (Example 1)
# ============================================================================

fig1, ax1 = plt.subplots(figsize=(6.5, 4.5))

for i, (a, t, algo, col) in enumerate(zip(alpha_ex1, time_ex1, algo_labels_ex1, colors_ex1)):
    ax1.scatter(a, t, s=120, color=col, label=algo if i in [0, 2, 4] else "", 
                zorder=5, edgecolor='black', linewidth=1.5)
    ax1.text(a, t + 35, algo, ha='center', va='bottom', fontsize=9, fontweight='bold')

ax1.plot(alpha_ex1, time_ex1, color='gray', linestyle='-', linewidth=1.5, alpha=0.5, zorder=1)
ax1.set_xlabel(r'$\alpha$ (certainty level)', fontsize=12)
ax1.set_ylabel('Solution Time (s)', fontsize=12)
ax1.set_title('Fig 1: Algorithm Switching vs. $\\alpha$ (Triangular System, Example 1)', fontsize=13)
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.set_xlim(-0.05, 1.05)

handles = [Line2D([0], [0], marker='o', color='w', markerfacecolor='#DC143C', 
                  markersize=10, label='IDR(12)'),
           Line2D([0], [0], marker='o', color='w', markerfacecolor='#1E90FF', 
                  markersize=10, label='BiCGSTAB'),
           Line2D([0], [0], marker='o', color='w', markerfacecolor='#228B22', 
                  markersize=10, label='GMRES')]
ax1.legend(handles=handles, loc='upper right', fontsize=10)

fig1.tight_layout()
fig1.savefig('reproduction_results/figures/Fig1_Example1_Algorithm_Switching.png', 
             dpi=300, bbox_inches='tight', facecolor='white')
plt.close(fig1)
print("✓ Saved: Fig1_Example1_Algorithm_Switching.png")

# ============================================================================
# PART 6: FIGURE 2 - Key Performance Indicators vs. alpha (Example 1)
# ============================================================================

fig2, ax2 = plt.subplots(figsize=(9.5, 4.5))

x_metrics = np.arange(len(metrics_names))
width = 0.35

bars1 = ax2.bar(x_metrics - width/2, alpha0_metrics, width, 
                label=r'$\alpha = 0.0$ (max uncertainty)', 
                color='#F08080', edgecolor='black', linewidth=1)
bars2 = ax2.bar(x_metrics + width/2, alpha1_metrics, width, 
                label=r'$\alpha = 1.0$ (full certainty)', 
                color='#90EE90', edgecolor='black', linewidth=1)

ax2.set_xlabel('Performance Metric', fontsize=12)
ax2.set_ylabel('Metric Value', fontsize=12)
ax2.set_title('Fig 2: Key Performance Indicators vs. $\\alpha$ (Triangular System, Example 1)', fontsize=13)
ax2.set_xticks(x_metrics)
ax2.set_xticklabels(metrics_names, fontsize=10, rotation=20, ha='right')
ax2.legend(fontsize=10, loc='upper left')
ax2.grid(True, axis='y', linestyle='--', alpha=0.5)

for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2, height + 0.5, 
                 f'{height:.2f}' if height < 5 else f'{height:.0f}',
                 ha='center', va='bottom', fontsize=8)

fig2.tight_layout()
fig2.savefig('reproduction_results/figures/Fig2_Example1_Performance_Metrics.png', 
             dpi=300, bbox_inches='tight', facecolor='white')
plt.close(fig2)
print("✓ Saved: Fig2_Example1_Performance_Metrics.png")

# ============================================================================
# PART 7: FIGURE 3 - Performance Comparison (Example 1, alpha=0.5)
# ============================================================================

fig3, ax3 = plt.subplots(figsize=(8.5, 5.5))

x_comp = np.arange(len(methods_ex1))
width_comp = 0.35

bars_time = ax3.bar(x_comp - width_comp/2, time_comp_ex1, width_comp,
                    label='Execution Time (s)', color='#4169E1', edgecolor='black', linewidth=1)
ax3.set_xlabel('Solution Method', fontsize=12)
ax3.set_ylabel('Time (s)', fontsize=12, color='#4169E1')
ax3.tick_params(axis='y', labelcolor='#4169E1')
ax3.set_xticks(x_comp)
ax3.set_xticklabels(methods_ex1, fontsize=10)
ax3.grid(True, axis='y', linestyle='--', alpha=0.5)

ax3_twin = ax3.twinx()
bars_mem = ax3_twin.bar(x_comp + width_comp/2, memory_comp_ex1, width_comp,
                        label='Memory Usage (TB)', color='#FF8C00', edgecolor='black', linewidth=1)
ax3_twin.set_ylabel('Memory (TB)', fontsize=12, color='#FF8C00')
ax3_twin.tick_params(axis='y', labelcolor='#FF8C00')

for i, (it, t) in enumerate(zip(iter_comp_ex1, time_comp_ex1)):
    ax3.text(i - width_comp/2, t + 25, f'{it} iters', ha='center', va='bottom',
             fontsize=9, fontweight='bold', color='#8B0000')

lines1, labels1 = ax3.get_legend_handles_labels()
lines2, labels2 = ax3_twin.get_legend_handles_labels()
ax3.legend(lines1 + lines2, labels1 + labels2, loc='upper right', fontsize=10)

ax3.set_title('Fig 3: Performance Comparison – Proposed vs. Standalone Methods\n(Example 1, $\\alpha=0.5$)', fontsize=13)

fig3.tight_layout()
fig3.savefig('reproduction_results/figures/Fig3_Example1_Comparison_vs_Standalone.png', 
             dpi=300, bbox_inches='tight', facecolor='white')
plt.close(fig3)
print("✓ Saved: Fig3_Example1_Comparison_vs_Standalone.png")

# ============================================================================
# PART 8: FIGURE 4 - Algorithm Switching and Parallel Performance (Example 2)
# ============================================================================

fig4, (ax4a, ax4b) = plt.subplots(1, 2, figsize=(12.5, 5.5))

# Left: Algorithm Switching
for i, (a, t, algo, col) in enumerate(zip(alpha_ex2, time_ex2, algo_labels_ex2, colors_ex2)):
    ax4a.scatter(a, t, s=120, color=col, label=algo if i in [0, 2, 4] else "", 
                 zorder=5, edgecolor='black', linewidth=1.5)
    ax4a.text(a, t + 40, algo, ha='center', va='bottom', fontsize=9, fontweight='bold')

ax4a.plot(alpha_ex2, time_ex2, color='gray', linestyle='-', linewidth=1.5, alpha=0.5, zorder=1)
ax4a.set_xlabel(r'$\alpha$ (certainty level)', fontsize=12)
ax4a.set_ylabel('Solution Time (s)', fontsize=12)
ax4a.set_title('(a) Algorithm Switching vs. $\\alpha$', fontsize=12)
ax4a.grid(True, linestyle='--', alpha=0.5)
ax4a.set_xlim(-0.05, 1.05)

handles_a = [Line2D([0], [0], marker='o', color='w', markerfacecolor='#DC143C', 
                    markersize=10, label='IDR(16)'),
             Line2D([0], [0], marker='o', color='w', markerfacecolor='#FF8C00', 
                    markersize=10, label='IDR(12)'),
             Line2D([0], [0], marker='o', color='w', markerfacecolor='#1E90FF', 
                    markersize=10, label='BiCGSTAB'),
             Line2D([0], [0], marker='o', color='w', markerfacecolor='#228B22', 
                    markersize=10, label='GMRES')]
ax4a.legend(handles=handles_a, loc='upper right', fontsize=9)

# Right: Parallel Efficiency and Condition Number
ax4b.plot(alpha_ex2, parallel_eff_ex2, 's-', linewidth=2.5, color='#006400', label='Parallel Efficiency (%)')
ax4b.set_xlabel(r'$\alpha$ (certainty level)', fontsize=12)
ax4b.set_ylabel('Parallel Efficiency (%)', fontsize=12, color='#006400')
ax4b.tick_params(axis='y', labelcolor='#006400')
ax4b.set_ylim(75, 100)
ax4b.grid(True, linestyle='--', alpha=0.5)
ax4b.set_title('(b) Parallel Efficiency & Condition Number', fontsize=12)

ax4b_twin = ax4b.twinx()
ax4b_twin.plot(alpha_ex2, condition_ex2, 'd--', linewidth=2.5, color='#8B0000', label=r'Condition Number $\kappa(A)$')
ax4b_twin.set_ylabel(r'Condition Number $\kappa(A)$', fontsize=12, color='#8B0000')
ax4b_twin.tick_params(axis='y', labelcolor='#8B0000')
ax4b_twin.set_yscale('log')

lines1, labels1 = ax4b.get_legend_handles_labels()
lines2, labels2 = ax4b_twin.get_legend_handles_labels()
ax4b.legend(lines1 + lines2, labels1 + labels2, loc='upper right', fontsize=9)

fig4.suptitle('Fig 4: Algorithm Switching and Parallel Performance (Trapezoidal System, Example 2)', fontsize=14, y=1.02)
fig4.tight_layout()
fig4.savefig('reproduction_results/figures/Fig4_Example2_Algorithm_Performance.png', 
             dpi=300, bbox_inches='tight', facecolor='white')
plt.close(fig4)
print("✓ Saved: Fig4_Example2_Algorithm_Performance.png")

# ============================================================================
# PART 9: FIGURE 5 - Performance Comparison (Example 2, alpha=0.6)
# ============================================================================

fig5, ax5 = plt.subplots(figsize=(8.5, 5.5))

x_comp2 = np.arange(len(methods_ex2))
width_comp2 = 0.35

bars_time2 = ax5.bar(x_comp2 - width_comp2/2, time_comp_ex2, width_comp2,
                     label='Execution Time (s)', color='#4169E1', edgecolor='black', linewidth=1)
ax5.set_xlabel('Solution Method', fontsize=12)
ax5.set_ylabel('Time (s)', fontsize=12, color='#4169E1')
ax5.tick_params(axis='y', labelcolor='#4169E1')
ax5.set_xticks(x_comp2)
ax5.set_xticklabels(methods_ex2, fontsize=10)
ax5.grid(True, axis='y', linestyle='--', alpha=0.5)

ax5_twin = ax5.twinx()
bars_mem2 = ax5_twin.bar(x_comp2 + width_comp2/2, memory_comp_ex2, width_comp2,
                         label='Memory Usage (TB)', color='#FF8C00', edgecolor='black', linewidth=1)
ax5_twin.set_ylabel('Memory (TB)', fontsize=12, color='#FF8C00')
ax5_twin.tick_params(axis='y', labelcolor='#FF8C00')

for i, (it, t) in enumerate(zip(iter_comp_ex2, time_comp_ex2)):
    ax5.text(i - width_comp2/2, t + 25, f'{it} iters', ha='center', va='bottom',
             fontsize=9, fontweight='bold', color='#8B0000')

lines1, labels1 = ax5.get_legend_handles_labels()
lines2, labels2 = ax5_twin.get_legend_handles_labels()
ax5.legend(lines1 + lines2, labels1 + labels2, loc='upper right', fontsize=10)

ax5.set_title('Fig 5: Performance Comparison – Proposed vs. Standalone Methods\n(Example 2, $\\alpha=0.6$)', fontsize=13)

fig5.tight_layout()
fig5.savefig('reproduction_results/figures/Fig5_Example2_Comparison_vs_Standalone.png', 
             dpi=300, bbox_inches='tight', facecolor='white')
plt.close(fig5)
print("✓ Saved: Fig5_Example2_Comparison_vs_Standalone.png")

# ============================================================================
# PART 10: FIGURE 6 - Relative Improvement (Example 2, alpha=0.6)
# ============================================================================

fig6, (ax6a, ax6b) = plt.subplots(1, 2, figsize=(12.5, 5.5))

# Left: Speedup relative to each standalone method
speedup_vs_gmres = [1247.8 / t for t in time_comp_ex2]
speedup_vs_bicg = [892.5 / t for t in time_comp_ex2]
speedup_vs_idr = [987.3 / t for t in time_comp_ex2]

x_speed = np.arange(len(methods_ex2))
width_speed = 0.25

ax6a.bar(x_speed - width_speed, speedup_vs_gmres, width_speed, 
         label='vs. GMRES', color='#4682B4', edgecolor='black', linewidth=1)
ax6a.bar(x_speed, speedup_vs_bicg, width_speed, 
         label='vs. BiCGSTAB', color='#B22222', edgecolor='black', linewidth=1)
ax6a.bar(x_speed + width_speed, speedup_vs_idr, width_speed, 
         label='vs. IDR(12)', color='#2E8B57', edgecolor='black', linewidth=1)

ax6a.set_xlabel('Solution Method', fontsize=12)
ax6a.set_ylabel('Speedup Ratio', fontsize=12)
ax6a.set_xticks(x_speed)
ax6a.set_xticklabels(methods_ex2, fontsize=10, rotation=15, ha='right')
ax6a.axhline(y=1.0, color='gray', linestyle='--', linewidth=1.5)
ax6a.set_title('(a) Computational Speedup', fontsize=12)
ax6a.legend(fontsize=10)
ax6a.grid(True, axis='y', linestyle='--', alpha=0.5)

for i in range(len(methods_ex2)):
    ax6a.text(i - width_speed, speedup_vs_gmres[i] + 0.05, f'{speedup_vs_gmres[i]:.2f}x', 
              ha='center', va='bottom', fontsize=8)
    ax6a.text(i, speedup_vs_bicg[i] + 0.05, f'{speedup_vs_bicg[i]:.2f}x', 
              ha='center', va='bottom', fontsize=8)
    ax6a.text(i + width_speed, speedup_vs_idr[i] + 0.05, f'{speedup_vs_idr[i]:.2f}x', 
              ha='center', va='bottom', fontsize=8)

# Right: Memory saving relative to GMRES
memory_saving_vs_gmres = [(128 - m) / 128 * 100 for m in memory_comp_ex2]

bars_saving = ax6b.bar(x_speed, memory_saving_vs_gmres, width=0.5, 
                       color='#800080', edgecolor='black', linewidth=1)
ax6b.set_xlabel('Solution Method', fontsize=12)
ax6b.set_ylabel('Memory Saving vs. GMRES (%)', fontsize=12)
ax6b.set_xticks(x_speed)
ax6b.set_xticklabels(methods_ex2, fontsize=10, rotation=15, ha='right')
ax6b.axhline(y=0, color='gray', linestyle='--', linewidth=1.5)
ax6b.set_title('(b) Memory Efficiency Improvement', fontsize=12)
ax6b.grid(True, axis='y', linestyle='--', alpha=0.5)

for i, v in enumerate(memory_saving_vs_gmres):
    ax6b.text(i, v + 1.5, f'{v:.1f}%', ha='center', va='bottom', fontsize=9, fontweight='bold')

fig6.suptitle('Fig 6: Relative Improvement of Proposed Framework (Example 2, $\\alpha=0.6$)', fontsize=14, y=1.02)
fig6.tight_layout()
fig6.savefig('reproduction_results/figures/Fig6_Example2_Relative_Improvement.png', 
             dpi=300, bbox_inches='tight', facecolor='white')
plt.close(fig6)
print("✓ Saved: Fig6_Example2_Relative_Improvement.png")

# ============================================================================
# PART 11: CREATE SUPPORTING FILES (requirements.txt, README.md, LICENSE)
# ============================================================================

print("\n" + "=" * 60)
print("Creating supporting files...")
print("=" * 60)

create_requirements_txt()
create_readme_md()
create_license()

# ============================================================================
# PART 12: SUMMARY
# ============================================================================

print("\n" + "=" * 60)
print("REPRODUCTION COMPLETE")
print("=" * 60)
print("\nGenerated figures:")
print("  - Fig1_Example1_Algorithm_Switching.png")
print("  - Fig2_Example1_Performance_Metrics.png")
print("  - Fig3_Example1_Comparison_vs_Standalone.png")
print("  - Fig4_Example2_Algorithm_Performance.png")
print("  - Fig5_Example2_Comparison_vs_Standalone.png")
print("  - Fig6_Example2_Relative_Improvement.png")
print("\nData saved:")
print("  - reproduction_results/data/raw_data.csv")
print("\nSupporting files created:")
print("  - requirements.txt")
print("  - README.md")
print("  - LICENSE")
print("\nAll files are in the current directory and 'reproduction_results' folder.")
print("=" * 60)
