# Project-Specific Instructions

## Phase 4: First Technical Modification

Make one small change technical change.
Run the project again and see what happens.
If your change causes an error, read the message, correct the problem,
and rerun the project.
You can always revert (CTRL z) changes or return to the example code.
Follow this debugging process
until your initial technical modification runs successfully.

Suggestions:

- Add a new Markdown cell with a section heading and one observation about the data
- Change the color palette or chart style in a seaborn plot
- Add a second chart of a different type (e.g., add a box plot alongside a histogram)
- Add a cell that prints the number of missing values per column using **df.isnull().sum()**
- Add a cell that filters the DataFrame to a subset of rows
  and re-runs a chart on the subset

Re-run all cells after your change and confirm the notebook executes cleanly.
Commit with output visible.

## Phase 5 Suggestions

### Phase 5 Suggestion 1. EDA on a Built-in Dataset

Use seaborn's built-in datasets to perform EDA on a dataset different from the example.
Being able to conduct an EDA on your own is a critical skill.
You will do this again in the capstone.
Seek to understand the process and be able to explore any data that interests you.

Steps:

- Choose a dataset from seaborn (see list below)
- Create a new notebook file: **notebooks/eda_yourname.ipynb**
- Follow the same numbered section structure as the example
- Include: shape, dtypes, missing values, descriptive statistics,
  and at least two charts
- Add Markdown narrative cells explaining your observations after each section

Good seaborn datasets for practice:

- **tips** - restaurant tipping data (244 rows, 7 columns)
- **iris** - flower measurements (150 rows, 5 columns)
- **mpg** - car fuel efficiency (398 rows, 9 columns)
- **titanic** - passenger survival data (891 rows, 15 columns)
- **diamonds** - diamond prices and attributes (53940 rows, 10 columns)

Load with: **df = sns.load_dataset('dataset_name')**

Then:

- All column names will change.
- Update the notebook to reflect the columns and content of your data.
- Describe the dataset: what each column represents and where the data comes from
- Identify one surprising or interesting pattern you found
- Explain what a next analytical step might be (e.g., grouping, filtering, modeling)

### Extend the EDA using existing functions

Find these existing functions:

- make_analytical_view()
- get_grouped_numeric_summary()
- get_correlation_matrix()

Suggestions:

- Create an analytical view using selected required columns.
- Compare numeric summaries across a categorical group.
- Create and interpret a correlation matrix for selected numeric variables.

### Phase 5 Suggestion 2. EDA on Your Own Dataset (Original)

Perform EDA on a dataset you bring yourself.
Being able to **get value out of data** is one of key skills of a data analyst.
Try it on any data you find interesting.

Steps:

- Find a tabular dataset (CSV) relevant to your field or interests
  (e.g., from <https://www.kaggle.com>, <https://data.gov>, or your own work)
- Place the file in **data/raw/**
- Create a new notebook: **notebooks/eda_yourname.ipynb**
- Load the data with **pd.read_csv()**
- All column names will change.
- Update the notebook to reflect the columns and content of your data.
- Follow the same numbered section structure as the example
- Include: shape, dtypes, missing values, descriptive statistics,
  and at least two charts
- Add Markdown narrative explaining your observations

Then:

- Cite the data source and describe what it contains
- Identify at least one data quality issue you found
  (missing values, outliers, wrong types)
- Describe what question you would investigate next if you had more time

## Key Skill Focus

As you work, focus on:

- how notebooks combine narrative and code for exploratory work
- how **df.info()**, **df.describe()**, and **df.isnull()**
  give a quick dataset overview
- how distributions reveal shape, spread, and outliers
- how grouping and filtering expose patterns within subsets
- how Markdown narrative turns a notebook into a readable analysis

Produce a narrated notebook that tells a clear story about a dataset.

## Professional Communication

Make sure your repository correctly presents and reflects **your work**.
Remove educational instructions that are no
longer needed and verify key areas **showcase your skills**:

- README.md
- docs/
- src/

The example projects are MIT licensed.
You are free to use and modify as you like.

---

[◄ Back to Home](index.md)
