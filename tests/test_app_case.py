# tests/test_app.py
#
# Simple, clear pytest examples.
# Show how to test basic EDA functions.
#
# Assumptions:
# - module is importable
# - pytest running from project root
#
# Run:
#   uv run python -m pytest


import pandas as pd
import pytest

from datafun import app


def test_load_data_returns_dataframe():
    """Test that load_data returns a pandas DataFrame."""
    df = app.load_data()
    assert isinstance(df, pd.DataFrame)


def test_load_data_has_expected_columns():
    """Test that the DataFrame has the expected columns."""
    df = app.load_data()
    expected_cols = [
        "species",
        "island",
        "bill_length_mm",
        "flipper_length_mm",
        "body_mass_g",
    ]
    for col in expected_cols:
        assert col in df.columns


def test_load_data_not_empty():
    """Test that the DataFrame is not empty."""
    df = app.load_data()
    assert len(df) > 0


def test_correlation_matrix_diagonal_is_one():
    """Test that diagonal values of correlation matrix are 1.0."""
    df = app.load_data()
    df_clean = app.make_clean_view(df)
    corr = app.correlation_matrix(df_clean)
    for col in corr.columns:
        assert corr.loc[col, col] == pytest.approx(1.0)
