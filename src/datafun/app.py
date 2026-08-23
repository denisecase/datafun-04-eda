"""src/datafun/app.py - Project script (example).

Author: Denise Case
Date: 2026-08

DOMAIN: Penguins

Explore a dataset of penguins using a simple,
repeatable exploratory data analysis (EDA) process.

EDA:

Exploratory Data Analysis helps us understand a new dataset.
A simple EDA process is:

1. Load the data.
2. Inspect the data.
3. Check data quality.
4. Describe numeric variables.
5. Visualize distributions.
6. Explore a relationship between two numeric variables.
7. Summarize what you found.

DESIGN:

Use this file to document your analysis
and orchestrate the work.

The reusable functions that do the data work live in utils_eda.py.
Reusable visualization functions come from eda-vizkit.
We import functions and pass in what they need.

RUN:

Open this project folder in VS Code.
Open an integrated Terminal in the root project folder
and paste the following command.

uv run python -m datafun.app

SKILLS:

This project illustrates several core Python and analytics skills:

- calling functions in another file
- passing information to functions
- working with pandas DataFrames
- exploratory data analysis

"""

# === DECLARE IMPORTS (BRING IN FREE CODE) ===

import logging
from pathlib import Path
from typing import Final

from datafun_toolkit.logger import get_logger, log_header
from eda_vizkit import (
    save_chart,
    show_categorical_distribution,
    show_missing_values,
    show_numeric_distribution,
    show_numeric_relationship,
)
import matplotlib.pyplot as plt
import pandas as pd

from datafun.utils_eda import (
    build_data_dictionary,
    get_correlation,
    get_duplicate_count,
    get_missing_counts,
    get_numeric_summary,
    inspect,
    load_data,
)

# === CONFIGURE LOGGER ONCE FOR THE APPLICATION ===

LOG: logging.Logger = get_logger("P04", level="DEBUG")

# === DECLARE GLOBAL CONSTANTS ===

# Some global variables are CONSTANT.
# They do NOT change while the program runs.
# By convention, constants use UPPERCASE_WITH_UNDERSCORES.
# Final indicates that the value should not be reassigned.

CHART_DIR: Final[Path] = Path("docs") / "images"
CHART_DIR.mkdir(parents=True, exist_ok=True)

# === DEFINE THE DATASET ===

DATASET_NAME: Final[str] = "penguins"

# === DETERMINE WHAT ONE ROW REPRESENTS ===

# This is the GRAIN of the dataset.
# Grain answers:
# What does one row represent?

GRAIN: Final[str] = "one observed penguin"

# === CHOOSE IMPORTANT NUMERIC VARIABLES ===

# These are continuous numeric variables
# we want to inspect during EDA.

NUMERIC_COLUMNS: Final[list[str]] = [
    "bill_length_mm",
    "bill_depth_mm",
    "flipper_length_mm",
    "body_mass_g",
]

# === CHOOSE IMPORTANT CATEGORICAL VARIABLES ===

CATEGORICAL_COLUMNS: Final[list[str]] = [
    "species",
    "island",
    "sex",
]

# === CHOOSE ONE RELATIONSHIP TO EXPLORE ===

X_COLUMN: Final[str] = "flipper_length_mm"
Y_COLUMN: Final[str] = "body_mass_g"


# === DEFINE THE MAIN FUNCTION ===


def main() -> None:
    """The main entry point where execution begins.

    Arguments:
        None.

    Returns:
        None.
    """
    log_header(LOG, "P04 - EXPLORATORY DATA ANALYSIS")

    LOG.info("===================================")
    LOG.info("START main()")
    LOG.info("===================================")

    # ============================================================
    # 01. LOAD
    # ============================================================

    LOG.info("-------------------------------")
    LOG.info("01. LOAD the data.")
    LOG.info("-------------------------------")

    df: pd.DataFrame = load_data(
        dataset_name=DATASET_NAME,
        log=LOG,
    )

    # ============================================================
    # 02. INSPECT
    # ============================================================

    LOG.info("-------------------------------")
    LOG.info("02. INSPECT the data.")
    LOG.info("-------------------------------")

    inspection_string: str = inspect(
        df=df,
        grain=GRAIN,
        log=LOG,
    )

    LOG.info(inspection_string)

    # ============================================================
    # 03. CHECK DATA QUALITY
    # ============================================================

    LOG.info("-------------------------------")
    LOG.info("03. CHECK data quality.")
    LOG.info("-------------------------------")

    # Call the imported function build_data_dictionary()
    # to create a starter data dictionary.
    # Pass in the df and the logger.

    data_dictionary: pd.DataFrame = build_data_dictionary(
        df=df,
        log=LOG,
    )
    LOG.info(f"\n{data_dictionary}")

    # Call the imported function get_missing_counts()
    # to count missing values in each column.
    # Pass in the df and the logger.
    missing_counts: pd.Series = get_missing_counts(
        df=df,
        log=LOG,
    )

    LOG.info(f"\nMissing values:\n{missing_counts}")

    # Call the imported function get_duplicate_count()
    # to count duplicate rows.
    # Pass in the df and the logger.
    duplicate_count: int = get_duplicate_count(
        df=df,
        log=LOG,
    )

    LOG.info(f"Duplicate rows: {duplicate_count}")

    # Call the imported function show_missing_values()
    # to visualize missing values.
    # Pass in the df.
    # get back the Axes object so we can save the chart.
    missing_ax = show_missing_values(df)

    # Save the missing values chart to the designated directory.
    save_chart(
        missing_ax,
        CHART_DIR / "missing-values.png",
    )

    # ============================================================
    # 04. DESCRIBE NUMERIC VARIABLES
    # ============================================================

    LOG.info("-------------------------------")
    LOG.info("04. DESCRIBE numeric variables.")
    LOG.info("-------------------------------")

    numeric_summary: pd.DataFrame = get_numeric_summary(
        df=df,
        numeric_columns=NUMERIC_COLUMNS,
        log=LOG,
    )

    LOG.info(f"\n{numeric_summary}")

    # ============================================================
    # 05. VISUALIZE DISTRIBUTIONS
    # ============================================================

    LOG.info("-------------------------------")
    LOG.info("05. VISUALIZE distributions.")
    LOG.info("-------------------------------")

    # For each column in the list of numeric columns,
    # call the imported function show_numeric_distribution()
    # to visualize the distribution of the column.

    for column in NUMERIC_COLUMNS:
        numeric_ax = show_numeric_distribution(
            df,
            column=column,
        )

        # Save the numeric distribution chart to the designated directory.
        save_chart(
            numeric_ax,
            CHART_DIR / f"{column}-distribution.png",
        )

    # For each column in the list of categorical columns,
    # call the imported function show_categorical_distribution()
    # to visualize the distribution of the column.

    for column in CATEGORICAL_COLUMNS:
        categorical_ax = show_categorical_distribution(df, column=column)

        # Save the categorical distribution chart to the designated directory.
        save_chart(
            categorical_ax,
            CHART_DIR / f"{column}-distribution.png",
        )

    # ============================================================
    # 06. EXPLORE A RELATIONSHIP BETWEEN TWO NUMERIC VARIABLES
    # ============================================================

    LOG.info("-------------------------------")
    LOG.info("06. EXPLORE a relationship between two numeric variables.")
    LOG.info("-------------------------------")

    # Call the imported function get_correlation()
    # to compute the correlation between the two numeric variables.
    # Pass in the df, the x column, the y column, and the log.

    correlation: float = get_correlation(
        df=df,
        x=X_COLUMN,
        y=Y_COLUMN,
        log=LOG,
    )

    LOG.info(f"Correlation between {X_COLUMN} and {Y_COLUMN}: {correlation:.3f}")

    # Call the imported function show_numeric_relationship()
    # to visualize the relationship between two numeric variables.
    # Pass in the df, the x column, the y column.
    # It returns a Matplotlib Axes object representing the plot.
    relationship_ax = show_numeric_relationship(
        df,
        x=X_COLUMN,
        y=Y_COLUMN,
    )

    # CUSTOM: Analyst must customize the Matplotlib Axes object with a title and axis labels.
    relationship_ax.set_title("Penguin Flipper Length vs. Body Mass")
    relationship_ax.set_xlabel("Flipper Length (mm)")
    relationship_ax.set_ylabel("Body Mass (g)")

    save_chart(
        relationship_ax,
        CHART_DIR / "one-relationship.png",
    )

    # ============================================================
    # 07. SUMMARIZE
    # ============================================================

    LOG.info("-------------------------------")
    LOG.info("07. SUMMARIZE what you found.")
    LOG.info("-------------------------------")

    # Run this app first.
    # Get some insights into data.
    # After seeing the information, record your CUSTOM observations
    # in a simple multi-line (triple-quoted) raw string (see the leading `r`).

    LOG.info(r"""CUSTOM OBSERVATIONS:
    The dataset contains penguin measurements.
    Some observations (rows) are complete, but some are missing values.

    I reviewed the relationship between:
    Flipper length vs. body mass
    and it shows a positive relationship.

    Based on this EDA, I would next like to review additional
    relationships between other numeric variables.
    Marimo (reactive notebook cells) might be a good choice
    for additional exploration.
    """)

    # ============================================================
    # DISPLAY VISUALIZATIONS
    # ============================================================

    # eda-vizkit just returns Matplotlib Axes objects.
    # The client (like this script or a marimo notebook),
    # determines how and when to display the plots).

    LOG.info("In a script, call plt.show() at the end to display all charts.")
    LOG.info("Close all chart windows (with the close button) to continue.")

    plt.show()

    LOG.info("===================================")
    LOG.info("END main() - Executed successfully!")
    LOG.info("===================================")


# === CONDITIONAL EXECUTION GUARD ===

# WHY: If this file is run as a script, call main().
#
# If another file imports this module,
# Python can reuse its definitions without automatically
# running the entire analysis.

if __name__ == "__main__":
    main()
