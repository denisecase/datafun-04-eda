# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "datafun-toolkit",
#     "eda-vizkit",
#     "marimo",
#     "pandas",
# ]
# ///
"""src/datafun/notebook.py - Reactive EDA notebook with Marimo.

Author: Denise Case
Date: 2026-08

DOMAIN: Penguins

Explore a dataset of penguins with a small reactive interface.

This notebook reuses the same EDA utilities and visualization
functions used by the script project.

Marimo adds reactive controls.
Every function definition below makes a marimo cell.

Change a selected variable and the dependent chart updates
automatically. (No callbacks required.)

RUN:

Open an integrated Terminal in the project root folder
and run:

uv run marimo edit src/datafun/notebook.py

To run as an app:

uv run marimo run src/datafun/notebook.py

ABOUT THE FILE OPENING ABOVE:

Marimo's WASM dependency mechanism
uses the notebook's PEP 723 metadata.
Marimo's current WASM guidance says that
without a script block first, imported packages
do not auto-install in WASM.
"""

# === DECLARE IMPORTS AND CREATE APP ===

import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium")

with app.setup:
    import sys

    from eda_vizkit import (
        show_numeric_distribution,
        show_numeric_relationship,
    )
    import marimo as mo
    import pandas as pd

    from datafun.utils_eda import load_data

    DATASET_NAME = "penguins"

    NUMERIC_COLUMNS = [
        "bill_length_mm",
        "bill_depth_mm",
        "flipper_length_mm",
        "body_mass_g",
    ]

    # The same notebook can run in two environments:
    #
    # - In the deployed WebAssembly app, Python runs in the browser.
    #   The browser does not have access to our local src/datafun package,
    #   so read the dataset packaged with the deployed app.
    #
    # - When running locally, use our regular project utilities.
    #
    # IMPORTANT:
    # Local-only imports must stay inside the else branch.
    # If imported above this condition, the browser will try to import
    # them before it knows which execution path to use.
    if sys.platform == "emscripten":
        data_path = mo.notebook_location() / "public" / "penguins.csv"
        df = pd.read_csv(str(data_path))
    else:
        from datafun_toolkit.logger import get_logger

        from datafun.utils_eda import load_data

        LOG = get_logger("P04-MARIMO", level="DEBUG")

        df: pd.DataFrame = load_data(
            dataset_name=DATASET_NAME,
            log=LOG,
        )


@app.cell
def _():
    # Use mo.md() to display markdown content in the opening cell.
    mo.md(r"""
    # Reactive Exploratory Data Analysis

    Explore the Palmer Penguins dataset interactively.

    Use the controls below to change the variable being explored.
    Marimo automatically updates dependent results.

    [Source code](https://github.com/denisecase/datafun-04-eda/blob/main/src/datafun/notebook.py)
    """)
    return


@app.cell
def _():

    # Use mo.ui.dropdown() to create a dropdown control for selecting a numeric column.
    numeric_column = mo.ui.dropdown(
        options=NUMERIC_COLUMNS,
        value="flipper_length_mm",
        label="Choose a numeric variable",
    )

    # Display it
    numeric_column

    # Return it to be used by other cells.
    # The return value is a tuple.
    return (numeric_column,)


@app.cell
def _(numeric_column):

    # Use a helper function imported above
    # To generate and return a distribution plot
    # for the selected numeric column.
    distribution_ax = show_numeric_distribution(
        df,
        column=numeric_column.value,
    )

    # Customize the plot title
    distribution_ax.set_title(f"Distribution of {numeric_column.value}")

    # Display it
    distribution_ax
    return


@app.cell
def _():

    # Use mo.ui.dropdown() to create a dropdown control for selecting the X variable.
    x_column = mo.ui.dropdown(
        options=NUMERIC_COLUMNS,
        value="flipper_length_mm",
        label="X variable",
    )

    # Use mo.ui.dropdown() to create a dropdown control for selecting the Y variable.
    y_column = mo.ui.dropdown(
        options=NUMERIC_COLUMNS,
        value="body_mass_g",
        label="Y variable",
    )

    # Display the X and Y variable controls.
    # Use mo.hstack() to display a list of items side by side.
    #   hstack = horizontal stack
    #   vstack = vertical stack
    mo.hstack(
        [
            x_column,
            y_column,
        ]
    )

    # Return the selected X and Y columns to be used by other cells.
    return x_column, y_column


@app.cell
def _(x_column, y_column):

    # Use the helper function imported above
    # To generate and return a scatter plot
    # for the selected X and Y columns that
    # shows their numeric relationship.

    # Pass in the df, and the selected X and Y columns.
    relationship_ax = show_numeric_relationship(
        df,
        x=x_column.value,
        y=y_column.value,
    )

    # Customize the plot title to indicate the relationship being shown.
    relationship_ax.set_title(f"{y_column.value} by {x_column.value}")

    # Display it.
    relationship_ax
    return


@app.cell
def _(x_column, y_column):
    mo.md(f"""
    ## What do you notice?

    Currently comparing:

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
    """)
    return


if __name__ == "__main__":
    app.run()
