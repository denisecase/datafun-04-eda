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

| Dataset    | Rows  | Columns | Good for                                               |
| ---------- | ----- | ------- | ------------------------------------------------------ |
| `penguins` | 344   | 7       | Grouping, scatter, missing values, course example      |
| `tips`     | 244   | 7       | Numeric and categorical, distributions                 |
| `iris`     | 150   | 5       | Classic grouping, clean data, minimal missing values   |
| `mpg`      | 398   | 9       | Mixed types, missing values, real-world context        |
| `diamonds` | 53940 | 10      | Large dataset, skewed distributions                    |
| `titanic`  | 891   | 15      | Survival analysis, many missing values, good challenge |

## Good for Regression (Module 7)

| Dataset    | Rows  | Predictor           | Outcome       | Notes                                  |
| ---------- | ----- | ------------------- | ------------- | -------------------------------------- |
| `mpg`      | 398   | `horsepower`        | `mpg`         | Natural pair, missing values to handle |
| `tips`     | 244   | `total_bill`        | `tip`         | Intuitive real-world relationship      |
| `penguins` | 344   | `flipper_length_mm` | `body_mass_g` | Strong R² (~0.76)                      |
| `diamonds` | 53940 | `carat`             | `price`       | Nonlinear, stretch goal                |

## Notes
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

| Dataset | Rows | Columns | Good for |
|---|---|---|---|
| `penguins` | 344 | 7 | Grouping, scatter, missing values — course example |
| `tips` | 244 | 7 | Numeric and categorical, distributions |
| `iris` | 150 | 5 | Classic grouping, clean data, minimal missing values |
| `mpg` | 398 | 9 | Mixed types, missing values, real-world context |
| `diamonds` | 53940 | 10 | Large dataset, skewed distributions |
| `titanic` | 891 | 15 | Survival analysis, many missing values, good challenge |

## Good for Regression (Module 7)

| Dataset | Rows | Predictor | Outcome | Notes |
|---|---|---|---|---|
| `mpg` | 398 | `horsepower` | `mpg` | Natural pair, missing values to handle |
| `tips` | 244 | `total_bill` | `tip` | Intuitive real-world relationship |
| `penguins` | 344 | `flipper_length_mm` | `body_mass_g` | Strong R² (~0.76) |
| `diamonds` | 53940 | `carat` | `price` | Nonlinear — stretch goal |

## Notes

- `mpg` is recommended for Module 7; it uses a different dataset than Module 4,
  which reinforces that the regression workflow transfers to new data.
- `np.ptp()` is deprecated in newer numpy. Use `np.max(x) - np.min(x)` for range.
- Seaborn datasets require an internet connection on first load; they are cached locally after that.
  which reinforces that the regression workflow transfers to new data.
- `np.ptp()` is deprecated in newer numpy. Use `np.max(x) - np.min(x)` for range.
- Seaborn datasets require an internet connection on first load; they are cached locally after that.
