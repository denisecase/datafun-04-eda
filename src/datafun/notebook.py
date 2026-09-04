"""src/datafun/notebook.py - Reactive EDA notebook with Marimo.

Author: Denise Case
Date: 2026-08

DOMAIN: Penguins

Explore a dataset of penguins with a small reactive interface, reusing the
same EDA utilities (eda_vizkit) and visualization functions as the script
project.

Marimo adds reactive controls. Every function below is a marimo cell; change a
selected variable and the dependent chart updates automatically (no callbacks).

RUN LOCALLY:

  uv run marimo edit src/datafun/notebook.py     # edit
  uv run marimo run  src/datafun/notebook.py     # run as an app (CTRL+c quits)

DEPLOY AS A WASM PAGE IN THE DOCS SITE:

  uv run marimo export html-wasm src/datafun/notebook.py \\
      -o docs/notebook --mode run
  # then place penguins.csv at docs/notebook/public/penguins.csv
  # and link docs/notebook/index.html from the docs nav

WASM DEPENDENCIES:

Under WebAssembly (emscripten) the browser has no project environment, so the
first cell installs the third-party packages with micropip: eda_vizkit (this
project's own pure-Python helper, on PyPI) plus pandas.
matplotlib and marimo are already present in the marimo WASM runtime.
Locally, micropip is skipped and the packages come from the uv-managed .venv.

NO LOGGING:

A browser-based WASM app has no persistent Python server to store log files,
so this notebook configures no logging.

PLAN CELLS FIRST

1. Imports (installs WASM deps, returns shared imports and constants)
2. Load data (its own cell; runs locally and under WASM)
3. Opening title and introduction (Markdown)
4. _choose_first_column
5. _show_distribution
6. _choose_second_column
7. _show_relationship
8. Closing (Markdown)

Note: marimo triggers @app.cell functions automatically; we never call them.
The names starting with "_" are for our own organization; the engine ignores
them.

HOW MARIMO NOTEBOOKS WORK

Each cell is a FUNCTION.
The return value of one cell can be passed as an argument to another cell.
We never call the functions, so they don't need names other than `_` (underscore).
(You can give them names if you want, but the notebook engine ignores them.)

The notebook is REACTIVE: when a cell's code or inputs change,
the notebook engine reruns that cell and every cell that depends on it.

The notebook is always CONSISTENT with outputs reflecting current inputs.

The first cell imports all dependencies, so the notebook is SELF-CONTAINED.

All later cells include their dependencies in their argument list.
Some other cells return values that can be used in other cells.
A cell displays the value of its last expression.

A cell whose last line is an assignment or a bare return
(like data and view cells) displays nothing;
only markdown, control, and render cells are meant to show.

RULE: Each variable must be defined in exactly one cell.
Defining the same name in two cells is a marimo error.

INPUT WIDGETS/CONTROLS: A cell that builds an input widget
resets that widget to its default every time the cell reruns.
marimo reruns a cell whenever any argument in its signature changes.
So a widget-building cell must depend only on what genuinely determines its options.
"""

# === ONLY THIS AT THE TOP OF THE FILE ===

import marimo

__generated_with_marimo_version__ = "0.24.0"
app = marimo.App(width="medium")

# === FIRST CELL IMPORTS AND RETURNS DEPS TO MAKE IT SELF-CONTAINED ===


@app.cell
async def _():
    """Install WASM deps, import everything, and hand it to later cells.

    This cell has no arguments: it is the root of the dependency graph.

    Under WASM (emscripten) the browser has no project environment, so it
    micropip-installs the third-party packages first:
    eda_vizkit (this project's pure-Python helper, published to PyPI) and pandas.
    matplotlib and marimo are already shipped in the marimo WASM runtime.
    Locally the install is  skipped and the packages come from the .venv.

    Returns DATASET_NAME, NUMERIC_COLUMNS, mo, pd,
    show_numeric_distribution, and show_numeric_relationship.
    """
    import sys

    if sys.platform == "emscripten":
        import micropip

        await micropip.install(["eda_vizkit", "pandas"])

    from eda_vizkit import (
        show_numeric_distribution,
        show_numeric_relationship,
    )
    import marimo as mo
    import pandas as pd

    DATASET_NAME = "penguins"

    NUMERIC_COLUMNS = [
        "bill_length_mm",
        "bill_depth_mm",
        "flipper_length_mm",
        "body_mass_g",
    ]

    return (
        DATASET_NAME,
        NUMERIC_COLUMNS,
        mo,
        pd,
        show_numeric_distribution,
        show_numeric_relationship,
        sys,
    )


# === LOAD DATA (ITS OWN CELL, RUNS IN TWO ENVIRONMENTS) ===


@app.cell
def _(DATASET_NAME, mo, pd, sys):
    """Load the dataset and return it as `df`.

    Two environments, one cell:
    - Locally, pandas reads the CSV from data/raw.
    - Under WASM (emscripten), Python runs in the browser, so Pyodide's
      open_url() fetches the CSV from public/ and pandas reads its text.

    Depends on `mo` (for notebook_location), `pd`, and `DATASET_NAME`. Reruns
    only when those change, so the read does not repeat when a control is
    touched. Returns `df` for the result cells.
    """
    notebook_location = mo.notebook_location()

    if notebook_location is None:
        raise RuntimeError("Unable to determine notebook location.")

    filename = f"{DATASET_NAME}.csv"

    if sys.platform == "emscripten":
        from pyodide.http import open_url  # ty: ignore[unresolved-import]

        data_url = notebook_location / "public" / filename
        df = pd.read_csv(open_url(str(data_url)))
    else:
        data_path = notebook_location.parents[1] / "data" / "raw" / filename
        df = pd.read_csv(data_path)

    return (df,)


# ===  TYPICALLY START WITH A MARKDOWN TITLE AND OPENING ===


@app.cell
def _(mo):
    """Render the opening title and instructions. Depends only on `mo`."""
    mo.md(r"""
    # Reactive Exploratory Data Analysis

    Explore the Palmer Penguins dataset interactively.

    Use the controls below to change the variable being explored.
    Marimo automatically updates dependent results.

    [Project Source](https://github.com/denisecase/datafun-04-eda/blob/main/src/datafun/notebook.py)
    | [Project Docs](https://denisecase.github.io/datafun-04-eda/)
    """)
    return


# ===  CONTROL: CHOOSE THE DISTRIBUTION VARIABLE ===


@app.cell
def _choose_first_column(mo, NUMERIC_COLUMNS):
    """Build the numeric-variable dropdown for the distribution.

    Depends on `mo` and its fixed options `NUMERIC_COLUMNS`, and nothing the
    user toggles - so this widget-building cell is not rerun by other controls
    and never resets its selection once made.

    Returns the `numeric_column` widget.
    """
    numeric_column = mo.ui.dropdown(
        options=NUMERIC_COLUMNS,
        value="flipper_length_mm",
        label="Choose a numeric variable",
    )

    # display
    numeric_column

    return (numeric_column,)


# ===  RESULT: DISTRIBUTION OF THE CHOSEN VARIABLE ===


@app.cell
def _show_distribution(df, numeric_column, show_numeric_distribution):
    """Plot the distribution of the selected numeric column.

    Depends on `numeric_column` (the user's choice) plus `df` and the helper.
    It consumes a control rather than creating one, so it is meant to rerun
    whenever the selection changes - that is the reactive update.
    """
    distribution_ax = show_numeric_distribution(
        df,
        column=numeric_column.value,
    )

    distribution_ax.set_title(f"Distribution of {numeric_column.value}")

    # display
    distribution_ax


# ===  CONTROL: CHOOSE THE X AND Y VARIABLES ===


@app.cell
def _choose_second_column(mo, NUMERIC_COLUMNS):
    """Build the X and Y dropdowns for the relationship scatter.

    Depends on `mo` and `NUMERIC_COLUMNS` only, so toggling other controls
    does not rerun this cell or reset the chosen X and Y variables.

    Returns the `x_column` and `y_column` widgets.
    """
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

    # hstack = horizontal stack; vstack = vertical stack
    mo.vstack(
        [
            x_column,
            y_column,
        ]
    )

    return (
        x_column,
        y_column,
    )


# ===  RESULT: RELATIONSHIP BETWEEN X AND Y ===


@app.cell
def _show_relationship(df, show_numeric_relationship, x_column, y_column):
    """Plot the relationship between the selected X and Y columns.

    Depends on `x_column` and `y_column` (the user's choices) plus `df` and
    the helper. Consumes controls rather than creating them, so it reruns and
    re-renders whenever either selection changes.
    """
    relationship_ax = show_numeric_relationship(
        df,
        x=x_column.value,
        y=y_column.value,
    )

    relationship_ax.set_title(f"{y_column.value} by {x_column.value}")

    # display it
    relationship_ax


# ===  TYPICALLY END WITH A MARKDOWN SOURCE LINK AND CLOSING ===


@app.cell
def _closing(mo, x_column, y_column):
    """Render the closing prompt, echoing the current X and Y choices.

    Depends on `mo` and the current `x_column`/`y_column` values, so the
    prompt text updates live as the selections change.
    """
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


if __name__ == "__main__":
    app.run()
