r"""utils_eda.py - Reusable exploratory data analysis utilities.

Author: Denise Case
Date: 2026-08

Purpose:

Provide reusable computations for exploratory data analysis.

Visualization is handled separately by eda-vizkit.

These functions calculate evidence.
They do not decide what conclusions the analyst should make.
"""

# === DECLARE IMPORTS (BRING IN FREE CODE) ===

from collections.abc import Sequence
import logging

import pandas as pd
import seaborn as sns

# === LOAD DATA ===


def load_data(
    *,
    dataset_name: str,
    log: logging.Logger,
) -> pd.DataFrame:
    """Load a built-in Seaborn dataset.

    Args:
        dataset_name: Name of the Seaborn dataset.
        log: Logger used to report progress.

    Returns:
        DataFrame containing the loaded data.
    """
    log.info(f"Loading Seaborn dataset: {dataset_name}")

    df: pd.DataFrame = sns.load_dataset(dataset_name)

    log.info(f"Loaded: {df.shape[0]} rows, {df.shape[1]} columns")

    return df


# === INSPECT DATA ===


def inspect(
    *,
    df: pd.DataFrame,
    grain: str,
    log: logging.Logger,
) -> str:
    """Describe the basic structure of a DataFrame.

    Args:
        df: DataFrame to inspect.
        grain: Description of what one row represents.
        log: Logger used to report progress.

    Returns:
        Formatted inspection string.
    """
    num_rows, num_columns = df.shape
    columns = list(df.columns)

    inspection = rf"""
DATA INSPECTION

Grain:
{grain}

Shape:
{num_rows} rows
{num_columns} columns

Columns:
{columns}
"""

    log.debug(inspection)

    return inspection


# === DATA DICTIONARY ===


def build_data_dictionary(
    *,
    df: pd.DataFrame,
    log: logging.Logger,
) -> pd.DataFrame:
    """Build a starter data dictionary.

    Args:
        df: DataFrame to inspect.
        log: Logger used to report progress.

    Returns:
        DataFrame containing one row per source column.
    """
    dictionary = pd.DataFrame(
        {
            "column": df.columns,
            "dtype": [str(dtype) for dtype in df.dtypes],
            "non_missing_count": (df.notna().sum().values),
            "missing_count": (df.isna().sum().values),
            "missing_pct": (df.isna().mean() * 100).round(2).values,
            "unique_count": [df[column].nunique(dropna=True) for column in df.columns],
        }
    )

    log.debug(f"\n{dictionary}")

    return dictionary


# === BASIC QUALITY INSPECTION ===


def get_missing_counts(
    *,
    df: pd.DataFrame,
    log: logging.Logger,
) -> pd.Series:
    """Return missing-value counts by column."""
    missing = df.isna().sum().sort_values(ascending=False)

    log.debug(f"\n{missing}")

    return missing


def get_duplicate_count(
    *,
    df: pd.DataFrame,
    log: logging.Logger,
) -> int:
    """Return the number of duplicate rows."""
    count = int(df.duplicated().sum())

    log.info(f"Duplicate rows detected: {count}")

    return count


# === ANALYTICAL VIEW ===


def make_analytical_view(
    *,
    df: pd.DataFrame,
    required_columns: Sequence[str],
    log: logging.Logger,
) -> pd.DataFrame:
    """Create a view with required values present.

    Args:
        df: DataFrame to inspect.
        required_columns: List of required column names.
        log: Logger used to report progress.

    Returns:
        DataFrame containing rows with required values present.
    """
    required = list(required_columns)

    df_view = df.dropna(subset=required).copy()

    dropped = df.shape[0] - df_view.shape[0]

    log.info(f"Analytical view: {df_view.shape[0]} rows")
    log.info(f"Rows excluded: {dropped}")

    return df_view


# === NUMERIC DISTRIBUTIONS ===


def get_numeric_summary(
    *,
    df: pd.DataFrame,
    numeric_columns: Sequence[str],
    log: logging.Logger,
) -> pd.DataFrame:
    """Return descriptive statistics for numeric variables.

    Args:
        df: DataFrame to inspect.
        numeric_columns: List of numeric column names.
        log: Logger used to report progress.

    Returns:
        DataFrame containing descriptive statistics.
    """
    columns = list(numeric_columns)

    summary = df[columns].describe().T

    log.debug(f"\n{summary}")

    return summary


# === GROUP COMPARISONS ===


def get_grouped_numeric_summary(
    *,
    df: pd.DataFrame,
    numeric_columns: Sequence[str],
    group_column: str,
    log: logging.Logger,
) -> pd.DataFrame:
    """Return numeric summaries grouped by category.

    Args:
        df: DataFrame to inspect.
        numeric_columns: List of numeric column names.
        group_column: Column name to group by.
        log: Logger used to report progress.

    Returns:
        DataFrame containing grouped numeric summaries.
    """
    columns = list(numeric_columns)

    summary = df.groupby(
        group_column,
        observed=True,
    )[columns].agg(
        [
            "count",
            "mean",
            "std",
            "min",
            "median",
            "max",
        ]
    )

    log.debug(f"\n{summary}")

    return summary


# === NUMERIC RELATIONSHIPS ===


def get_correlation(
    *,
    df: pd.DataFrame,
    x: str,
    y: str,
    log: logging.Logger,
) -> float:
    """Return Pearson correlation for two numeric variables.

    Args:
        df: DataFrame to inspect.
        x: Name of the first numeric column.
        y: Name of the second numeric column.
        log: Logger used to report progress.

    Returns:
        Pearson correlation coefficient as a float.
    """
    complete = df[[x, y]].dropna()

    correlation = float(complete[x].corr(complete[y]))

    log.info(f"Correlation between {x} and {y}: {correlation:.3f}")

    return correlation


def get_correlation_matrix(
    *,
    df: pd.DataFrame,
    numeric_columns: Sequence[str],
    log: logging.Logger,
) -> pd.DataFrame:
    """Return a correlation matrix.

    Args:
        df: DataFrame to inspect.
        numeric_columns: List of numeric column names.
        log: Logger used to report progress.

    Returns:
        DataFrame containing the correlation matrix.
    """
    columns = list(numeric_columns)

    correlation_matrix = df[columns].corr()

    log.debug(f"\n{correlation_matrix}")

    return correlation_matrix
