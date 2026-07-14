# ScikitLearn

A learning repository for practicing core machine learning concepts using [scikit-learn](https://scikit-learn.org/), with a focus on **prediction** (regression and classification).

## 📂 Contents

| File | Description |
|---|---|
| `first.py` | Simple **Linear Regression** example — predicts marks based on hours studied (`Y = mx + C`), and prints the model's R² score. |
| `task.py` | A set of **practice problems** (salary vs. experience, house price vs. size, ice cream sales vs. temperature, car price vs. age, battery capacity vs. backup, ad budget vs. sales, petrol usage vs. distance, electricity bill vs. units, employee bonus vs. performance) solved using Linear Regression. Most are currently commented out — uncomment a section to run that example. |
| `decision_tree.ipynb` | Notebook demonstrating a **Decision Tree Classifier**, using a small example dataset (price vs. purchase decision). |
| `logistic_Regression.ipynb` | Notebook demonstrating **Logistic Regression** for binary classification (e.g., pass/fail based on hours), including predictions on multiple new data points. |
| `Untitled.ipynb` | Scratch notebook for experimentation. |
| `amazon.csv` | Sample e-commerce dataset (Amazon product listings with prices, ratings, and reviews) for practicing data analysis and prediction tasks on real-world data. |

## 🧠 Concepts Covered

- **Linear Regression** — predicting continuous values
- **Logistic Regression** — binary classification
- **Decision Trees** — classification with `DecisionTreeClassifier`
- Basic **data handling** with `pandas` (DataFrames, feature/target splitting)
- Model training, prediction, and evaluation (`model.fit()`, `model.predict()`, `model.score()`)

## 🛠️ Requirements

```bash
pip install pandas scikit-learn jupyter
```

## 🚀 Usage

Run a script directly:

```bash
python first.py
```

Or open a notebook:

```bash
jupyter notebook decision_tree.ipynb
```

## 📌 Notes

This is a personal learning repository — code and examples will evolve as more ML concepts are explored and implemented.
