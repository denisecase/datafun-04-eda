# Concepts

> Key concepts introduced in this module.

<!--
Only the first sentence/paragraph of h3 entries
are used for the integrated quiz.

Wrap code terms in double asterisks
rather than single backtics so they can be read aloud.
-->

## Exploratory Data Analysis

### Exploratory Data Analysis (EDA)

**Exploratory data analysis (EDA)** examines a dataset from several angles
before applying a model or formal statistical test.

An analyst examines structure, quality, patterns, and limits
to understand what the data can support.

EDA can reveal unusual observations, differences between groups,
relationships between variables, and questions worth pursuing.

### Evidence

Calculations, tables, and charts produced during analysis are **evidence**.

Evidence is what the data and analysis actually show.

The analyst uses evidence to support observations and interpretations.

### Finding

A **finding** is an interpretation the analyst draws from evidence.

For example, a scatter plot and a correlation value are evidence.

The statement that two variables show a strong positive relationship
is a finding based on that evidence.

### Data Quality

**Data quality** describes how suitable a dataset is for analysis.

Common issues include missing values, duplicate rows,
inconsistent categories, invalid values, and incorrect types.

### Missing Value

A **missing value** is information that is absent, unknown,
or unrecorded for an observation.

In pandas, missing values commonly appear as **NaN**.

There is no universal rule that every row with a missing value
should be removed.

An analyst considers what is missing, how much is missing,
and whether it matters for the analysis.

### Duplicate Row

A row that appears more than once in a dataset is a **duplicate row**.

A duplicate may be valid, accidental,
or a sign of a data collection problem.

Duplicates are investigated before they are removed.

### Outlier

An **outlier** is a value that falls far from most other observed values.

An outlier may be an error, a rare event, or an important signal.

Removing a real signal can be as damaging as keeping a real error.

### Distribution

A **distribution** describes how observed values spread
across their possible values.

For a numeric variable, this includes center, variation,
common and uncommon values, gaps, extreme values,
and whether the values are symmetric or skewed.

Numerical summaries can hide the shape of a distribution,
so analysts also examine distributions visually.

### Median

The **median** is the middle value after numeric observations are ordered.

It is usually less affected by extreme values than the mean.

When the median and mean differ substantially,
the distribution may be skewed or contain outliers.

### Quartile

A **quartile** divides ordered numeric observations into four parts.

The 25th percentile, median, and 75th percentile
are commonly used quartiles.

Together they describe how values are distributed
around the center of the data.

### Categorical Variable

A **categorical variable** places observations into groups.

Examples include region, species, department, or class label.

Counts and proportions are often useful first summaries
for categorical variables.

### Group Comparison

A **group comparison** examines how a measure differs across categories.

For example, an analyst might compare a numeric measure
across regions or product categories.

Differences between groups are evidence,
but sample size, variation, quality, and context still matter.

### Numeric Relationship

A **numeric relationship** describes how two numeric variables
appear to change together.

A visual comparison may suggest a positive relationship,
a negative relationship, little relationship,
clusters, unusual points, or a nonlinear pattern.

### Correlation

**Pearson correlation** summarizes the direction and strength
of a linear relationship between two numeric variables.

It ranges from -1 to 1.

```text
near +1    strong positive linear relationship
near  0    weak or no linear relationship
near -1    strong negative linear relationship
```

**Correlation does not establish causation.**

Correlation can hide separate groups or nonlinear patterns,
so it should be interpreted with visual evidence and context.

A correlation matrix displays correlations
among several numeric variables at once.

### Grouping

**Grouping** splits observations into categories before summarizing them.

For example, observations might be grouped by species,
department, region, or product category.

### Aggregation

**Aggregation** calculates a summary value for each group.

Examples include a count, median, minimum, maximum,
or another summary calculated separately for each category.

Grouping and aggregation together turn individual observations
into comparisons across groups.

### Limitation

A **limitation** is something the available data or analysis
cannot fully answer or support.

Recognizing limitations helps prevent claims
that go beyond the available evidence.

### Next Question

EDA often produces a **next question** worth investigating.

An interesting pattern may raise questions about what explains it,
whether it holds under different conditions,
or what additional evidence would help.

## Notebooks

### Notebook

A **notebook** is an interactive document that combines code,
output, formatted text, tables, charts, and notes.

Notebooks support exploration because code and results
can sit next to an explanation of what they mean.

This module uses both reactive and sequential notebooks.

### Reactive Notebook

A **reactive notebook** tracks how cells depend on one another
and keeps dependent results consistent automatically.

When a value changes, cells that depend on it update.

Reactive notebooks in this module use marimo.

A marimo notebook is stored as an ordinary Python file
that can be run as a script or served as an application.

### Sequential Notebook

A **sequential notebook** runs cells in the order chosen by the user
and remembers results produced during the session.

Jupyter Notebook is a common sequential notebook format for Python.

Jupyter notebooks are commonly saved with the **.ipynb** extension.

Cells can be run out of order,
so visible output may not match a clean top-to-bottom execution.

### Kernel

A **kernel** is the running Python process behind a sequential notebook.

It holds information created while notebook cells run.

Restarting the kernel clears that accumulated information.

### Reproducible Notebook

A **reproducible notebook** can run from a clean start,
top to bottom, and produce the expected results.

For a sequential notebook, restarting the kernel
and then running all cells is an important reproducibility check.

Reactive notebooks manage dependencies automatically.

### Markdown Cell

A **Markdown cell** contains formatted narrative text rather than Python code.

Markdown cells can provide headings, explanations,
observations, interpretations, and conclusions.

### Code Cell

A **code cell** contains executable code.

Running a code cell may produce text, tables, charts,
or other analytical output.

### Cell Output

The result displayed after a code cell runs is its **cell output**.

Output can include text, tables, charts, warnings, or errors.

### Run All

**Run All** executes every notebook cell from top to bottom.

For a sequential notebook, using Run All after restarting the kernel
helps confirm that the notebook works from a clean start.

## Working with Data in EDA

### Data Dictionary

A **data dictionary** describes the variables in a dataset.

It may include names, meanings, types, units,
valid values, and information about missing values.

A data dictionary helps an analyst interpret columns correctly.

### Series

A pandas **Series** is a one-dimensional labeled collection of values.

Selecting one column from a DataFrame commonly returns a Series.

### Index

The **Index** contains the row labels of a pandas DataFrame or Series.

A default pandas Index usually begins at 0,
but row labels do not have to be consecutive integers.

### Subset

A **subset** is a selected part of a dataset.

A subset may contain selected rows, selected columns, or both.

Analysts often create subsets to focus on a particular question.

### Filter

A **filter** selects observations that meet a condition.

For example, an analyst might keep only records
from one category or values above a threshold.

### Clean View

A **clean view** is a modified copy used for analysis
while the original data is preserved.

A clean view can support analysis without overwriting
the original source values.

### Chaining

**Chaining** calls methods in sequence so one result feeds the next operation.

For example:

```python
missing_counts = df.isna().sum().sort_values()
```

Chaining can make a short sequence of related operations concise,
but long chains can become difficult to read.

## Visualization Terms

### Visualization

A **visualization** is a graphical representation of data.

Charts can reveal distributions, comparisons,
relationships, patterns, and unusual observations.

The chart type should match the analytical question
and the kinds of variables being examined.

### Figure

A **Figure** is the complete Matplotlib drawing area.

A Figure can contain one or more individual plot areas.

### Axes

An **Axes** object is the plot area where data is drawn.

Titles, labels, limits, and many formatting choices
are applied through the Axes object.

### Bar Chart

A **bar chart** compares values across categories.

Bar length represents the quantity associated with each category.

### Histogram

A **histogram** shows the distribution of a numeric variable
by dividing values into bins and counting observations in each bin.

The overall shape can reveal concentration, skew,
gaps, and unusual values.

### Scatter Plot

A **scatter plot** shows paired values for two numeric variables.

Each point represents one observation.

Patterns in the points can reveal relationships,
clusters, and unusual observations.

### Box Plot

A **box plot** summarizes a numeric distribution
using the median, quartiles, spread, and possible outliers.

Box plots are especially useful for comparing
numeric distributions across categories.

### Heatmap

A **heatmap** represents numeric values with color intensity.

Correlation matrices are often displayed as heatmaps
to make stronger and weaker relationships easier to compare.

### Color Encoding

**Color encoding** uses color to represent categories or numeric values.

Color can distinguish groups or communicate magnitude,
but it should add information rather than decoration.

## Communicating Notebook Work

### Standard Header

A **standard header** identifies what a notebook is and where it belongs.

It can include the title, author, repository,
purpose, date, and dataset information.

### Purpose

A notebook's **purpose** states why the analysis exists
and what it is intended to investigate.

A clear purpose helps readers understand
why particular analytical choices were made.

### Dataset Source

A **dataset source** identifies where the analyzed data came from.

Recording the source supports credibility,
reproducibility, and appropriate attribution.

### Citation

A **citation** gives credit to the creators or source of data or other work.

When a data source provides citation information,
that information should be preserved with the analysis.

---

[◄ Back to Home](index.md)
