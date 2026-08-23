"""src/datafun/notebook.py - Reactive EDA notebook with Marimo.

Author: Denise Case
Date: 2026-08

DOMAIN: Penguins

Explore a dataset of penguins with a small reactive interface.

This notebook reuses the same EDA utilities and visualization
functions used by the script project.

Marimo adds reactive controls.

Change a selected variable and the dependent chart updates
automatically. No callback functions are required.

RUN:

Open an integrated Terminal in the project root folder
and run:

uv run marimo edit src/datafun/notebook.py

To run as an app:

uv run marimo run src/datafun/notebook.py

"""

# === DECLARE IMPORTS AND CREATE APP ===

import marimo

__generated_with = "0.13.10"
app = marimo.App(width="medium")


# === SET UP SHARED IMPORTS AND DATA ===

with app.setup:
    from datafun_toolkit.logger import get_logger
    from eda_vizkit import (
        show_numeric_distribution,
        show_numeric_relationship,
    )
    import marimo as mo
    import pandas as pd

    from datafun.utils_eda import load_data

    LOG = get_logger("P04-MARIMO", level="DEBUG")

    DATASET_NAME = "penguins"

    NUMERIC_COLUMNS = [
        "bill_length_mm",
        "bill_depth_mm",
        "flipper_length_mm",
        "body_mass_g",
    ]

    df: pd.DataFrame = load_data(
        dataset_name=DATASET_NAME,
        log=LOG,
    )


# === TITLE ===


@app.cell
def _():
    mo.md(
        r"""
        # Reactive Exploratory Data Analysis

        Explore the Palmer Penguins dataset interactively.

        Use the controls below to change the variable being explored.
        Marimo automatically updates dependent results.
        """
    )


# === CHOOSE ONE NUMERIC VARIABLE ===


@app.cell
def _():
    numeric_column = mo.ui.dropdown(
        options=NUMERIC_COLUMNS,
        value="flipper_length_mm",
        label="Choose a numeric variable",
    )

    numeric_column
    return (numeric_column,)


# === SHOW THE SELECTED NUMERIC DISTRIBUTION ===


@app.cell
def _(numeric_column):
    distribution_ax = show_numeric_distribution(
        df,
        column=numeric_column.value,
    )

    distribution_ax.set_title(f"Distribution of {numeric_column.value}")

    distribution_ax


# === CHOOSE TWO NUMERIC VARIABLES ===


@app.cell
def _():
    x_column = mo.ui.dropdown(
        options=NUMERIC_COLUMNS,
        value="flipper_length_mm",
        label="X variable",
    )

    y_column = mo.ui.dropdown(
        options=NUMERIC_COLUMNS,
        value="body_mass_g",
        label="Y variable",
    )

    mo.hstack(
        [
            x_column,
            y_column,
        ]
    )

    return x_column, y_column


# === SHOW THE SELECTED RELATIONSHIP ===


@app.cell
def _(x_column, y_column):
    relationship_ax = show_numeric_relationship(
        df,
        x=x_column.value,
        y=y_column.value,
    )

    relationship_ax.set_title(f"{y_column.value} by {x_column.value}")

    relationship_ax


# === REFLECT ===


@app.cell
def _(x_column, y_column):
    mo.md(
        f"""
        ## What do you notice?

        You are currently comparing:

        - **X:** `{x_column.value}`
        - **Y:** `{y_column.value}`

        Look at the pattern.

        Does the relationship appear:

        - positive,
        - negative,
        - weak,
        - strong,
        - or unclear?

        What question would you investigate next?
        """
    )


if __name__ == "__main__":
    app.run()
