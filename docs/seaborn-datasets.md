# Seaborn Built-in Datasets

Seaborn includes several clean, ready-to-use datasets for practice.
These are ideal for EDA and regression projects because they load instantly
with no file management required.

## List Available Datasets

```python
import seaborn as sns

print(sns.get_dataset_names())
```

## Load a Dataset

```python
df = sns.load_dataset("dataset_name")
```

## Good for EDA (Module 4)

| Dataset    | Rows  | Columns | Good for                                   |
| ---------- | ----- | ------- | ------------------------------------------ |
| `penguins` | 344   | 7       | Grouping, scatter, missing values, example |
| `tips`     | 244   | 7       | Numeric and categorical, distributions     |
| `iris`     | 150   | 5       | Classic grouping, clean data, few missing  |
| `mpg`      | 398   | 9       | Mixed types, missing values, real-world    |
| `diamonds` | 53940 | 10      | Large dataset, skewed distributions        |
| `titanic`  | 891   | 15      | Survival analysis, many missing, challenge |

## Good for Regression (Module 6)

| Dataset    | Rows  | Predict?      | Notes          |
| ---------- | ----- | ------------- | -------------- |
| `mpg`      | 398   | `mpg`         | Missing values |
| `tips`     | 244   | `tip`         | real-world     |
| `penguins` | 344   | `body_mass_g` |                |
| `diamonds` | 53940 | `price`       | Challenging    |

---

[◄ Back to Home](index.md)
