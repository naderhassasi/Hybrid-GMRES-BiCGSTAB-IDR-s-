# Reproduction of Results for "A Dynamic Three-Level Hybrid Framework for Solving Large-Scale Fuzzy Systems"

This repository contains the complete code and data to reproduce all figures and tables from the paper.

**Author:** N. Hassasi  
**Affiliation:** Department of Mathematics, Mal.C., Islamic Azad University, Malayer, Iran  
**Email:** naderhassasi@iau.ac.ir

---

## Contents

- `full_reproduction.py`: Main Python script to generate all figures
- `requirements.txt`: Required Python packages
- `reproduction_results/`: Output directory containing:
  - `figures/`: All 6 figures in PNG format (300 DPI, RGB, 24-bit color)
  - `data/`: Raw data in CSV format

---

## Requirements

- Python 3.7 or higher
- Required packages: matplotlib, numpy, pandas

---

## Installation

Clone the repository and install dependencies:

```
git clone https://github.com/yourusername/reproduction.git
cd reproduction
pip install -r requirements.txt
```

---

## Usage

Run the main script:

```
python full_reproduction.py
```

---

## Output

All figures will be saved in the `reproduction_results/figures/` directory:

| Filename | Description |
|----------|-------------|
| `Fig1_Example1_Algorithm_Switching.png` | Algorithm switching vs. alpha for triangular system (Example 1) |
| `Fig2_Example1_Performance_Metrics.png` | Key performance indicators vs. alpha for triangular system |
| `Fig3_Example1_Comparison_vs_Standalone.png` | Performance comparison for Example 1 at alpha = 0.5 |
| `Fig4_Example2_Algorithm_Performance.png` | Algorithm switching and parallel performance for trapezoidal system (Example 2) |
| `Fig5_Example2_Comparison_vs_Standalone.png` | Performance comparison for Example 2 at alpha = 0.6 |
| `Fig6_Example2_Relative_Improvement.png` | Relative improvement (speedup and memory saving) for Example 2 |

---

## Data

Raw data is saved in `reproduction_results/data/raw_data.csv`.

---

## Figure Specifications

- **Format:** PNG
- **Resolution:** 300 DPI
- **Color Mode:** RGB (24-bit)
- **Font:** Times New Roman / Arial (size 10-12)
- **File Size:** < 2 MB per figure

---

## License

This code is released under the MIT License. See LICENSE file for details.

---

## Citation

If you use this code in your research, please cite the original paper:

```
@article{hassasi2024dynamic,
  title={A Dynamic Three-Level Hybrid Framework for Solving Large-Scale Fuzzy Systems: Intelligent Integration of GMRES, BiCGSTAB, and IDR(s) with Real-Time Decision Making},
  author={Hassasi, N.},
  journal={To be published},
  year={2024}
}
```
