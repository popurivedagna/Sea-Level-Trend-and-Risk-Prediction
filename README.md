# Sea-Level-Trend-and-Risk-Prediction
Sea Level Trend and Risk Prediction System that analyzes historical sea level data, detects extreme events, and predicts future levels using statistical analysis and regression.

# Sea Level Trend and Risk Prediction

## Overview

The Sea Level Trend and Risk Prediction System is a Python-based data analysis project that studies historical sea level measurements to understand trends, identify extreme levels, and detect potential environmental risks.

The system performs statistical analysis on sea level data, visualizes long-term changes, and estimates future sea levels using a simple linear regression model.

This project demonstrates data analysis, visualization, and predictive modeling using Python.

---

## Features

* Monthly sea level analysis to calculate average, minimum, and maximum levels.
* Detection of dangerous sea level thresholds.
* Visualization of long-term sea level trends.
* Identification of highest and lowest sea level observations.
* Prediction of future sea levels using regression.

---

## Technologies Used

* Python
* Pandas (data analysis and manipulation)
* Matplotlib (data visualization)
* NumPy (numerical computation)

---

## Project Structure

```
sea-level-analysis
│
├── sea_level_analysis.py
├── sea_level.csv
├── requirements.txt
└── README.md
```

---

## Dataset Format

The dataset should contain the following columns:

```
date,sea_level
2023-01-01,4.1
2023-02-01,4.3
2023-03-01,4.7
```

* date – date of observation
* sea_level – recorded sea level measurement

---

## Installation

Clone the repository:

```
git clone https://github.com/yourusername/sea-level-analysis.git
```

Install required dependencies:

```
pip install -r requirements.txt
```

---

## How to Run

Run the program using:

```
python sea_level_analysis.py
```

The program will:

1. Load the dataset
2. Perform statistical analysis
3. Detect extreme and dangerous sea levels
4. Predict future sea levels
5. Display a visualization of sea level trends

---

## Example Output

The program generates:

* Highest sea level recorded
* Lowest sea level recorded
* Monthly sea level statistics
* List of dangerous sea level events
* Predicted future sea level
* Graph showing sea level trends

---

## Learning Outcomes

This project demonstrates:

* Data cleaning and preprocessing
* Time-series data analysis
* Statistical aggregation using Pandas
* Data visualization with Matplotlib
* Predictive modeling using regression

---

## Author

Popuri Sai Vedagna

---

## License

This project is intended for educational and research purposes.
