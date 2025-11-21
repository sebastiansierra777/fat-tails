# Popular Stocks Fat Tails Analysis

Analysis of histograms of empirical daily log-returns for popular stocks, 
overlaid with the probability density functions of their fitted normal distributions.

## 📋 Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Data Sources](#data-sources)
- [Requirements](#requirements)
- [Author](#author)

## 🎯 Overview

This project analyzes the daily log-returns of major tech stocks: Palantir, Tesla, NVIDIA, Broadcom, Meta, Microsoft, and Apple. 

Using Python, I will build empirical histograms from these daily log-returns and compare them against their 
overlaid fitted normal distribution probability density functions, with the goal of contrasting the observed empirical results 
with theoretical expectations. 

In the end, these stocks will exhibit fat-tail behaviour that deviates from the Normal Distribution, 
supporting the views of Mandelbrot and Taleb on markets and finance.

## 🚀 Installation

### Prerequisites

- [Anaconda](https://www.anaconda.com/products/distribution) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- Git

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/sebastiansierra777/fat-tails.git
cd fat-tails
```

2. **Create the conda environment**
```bash
conda env create -f environment.yml
```

3. **Activate the environment**
```bash
conda activate fat_tails
```

Alternatively, if using pip:
```bash
pip install -r requirements.txt
```
## 📁 Project Structure
```
fat-tails/
├── src/                 # Python source code
├── data/
│   ├── raw/            # Original, unmodified datasets
│   └── processed/      # Cleaned and transformed datasets
├── figures/            # Generated plots and visualizations
├── environment.yml     # Conda environment specification
├── requirements.txt    # Python package requirements
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation
```

## 💻 Usage

1. **Activate the environment**
```bash
conda activate fat_tails
```

2. **Run any stock-specific script from the project root**
```bash
python src/palantir.py
python src/tesla.py
python src/nvidia.py
python src/broadcom.py
python src/meta.py
python src/microsoft.py
python src/apple.py
```

## 📊 Data Sources
All historical stock price data is downloaded from Investing.com and stored in data/raw/.
Cleaned and preprocessed versions of these files are saved in data/processed/ and used for the analysis.

## 📦 Requirements

### Main Dependencies

- python=3.13.9
- numpy==2.3.4
- pandas==2.3.3
- matplotlib==3.10.6
- seaborn==0.13.2
- statsmodels==0.14.5
- scipy==1.15.3
- scikit-learn==1.7.2

## 👤 Author

**Sebastian Sierra Garcia**

- GitHub: [@sebastiansierra777]
- (https://github.com/sebastiansierra777)

## 📝 Notes

This project uses Jupyter-style cell markers (`# %%`) in Python files for interactive development in PyCharm or VS Code.

---

*Last updated: November 2025*