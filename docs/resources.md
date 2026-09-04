# Optional: Resources

We'll introduce a lot of powerful tools.
Find the ones that interest you and explore them further.

## Marimo Resources

Marimo is a powerful new reactive app option for Python.

- [**Marimo Documentation**](https://docs.marimo.io/)
- [**Marimo for Learners**](https://marimo.io/for-learners)
- [**Marimo Primer for Education**](https://cms.marimo.io/education/marimo-primer-education.pdf)

Marimo also includes interactive tutorials. From the project folder, run:

```shell
uv run marimo tutorial intro
```

## Jupyter Notebook Resources

- [**Project Jupyter**](https://jupyter.org/)
- [**Jupyter Notebook Documentation**](https://jupyter-notebook.readthedocs.io/en/stable/)
- [**VS Code Jupyter Documentation**](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)

## Jupyter Shortcut Keys

Press **Esc** to enter command mode (cell border turns blue), then:

- **Shift + Enter**: Run the current cell and move to the next one.
- **Ctrl + Enter**: Run the current cell without moving.
- **A**: Insert a new cell above.
- **B**: Insert a new cell below.
- **M**: Change cell to Markdown.
- **Y**: Change cell to Code.

## Numpy and pandas

These are key libraries for data analysis.
Pandas is built on NumPy arrays.
Pandas has some new competitors in big data - you might check out polars.

## Matplotlib

Matplotlib is the core plotting library for Python.
If you enjoy data visualization and want to excel,
spend some time understanding this key library.

## Seaborn Charts

Do a search for Seaborn Gallery to see examples of charts you can create with Seaborn.
Seaborn is a Python data visualization library based on matplotlib.
It provides a high-level interface for drawing attractive
and informative statistical graphics.

## EDA VizKit

[**EDA VizKit**](https://github.com/analytics-toolworks/eda-vizkit)
provides reusable examples of professional Python code for exploratory
data visualization.

Explore the source code if curious how simple visualization
functions can be organized and reused.

---

## Community Resilience (NIST TraCR)

For more examples of reactive charting (with Python, marimo,
Altair, Plotly, and Matplotlib), see the following.

| App | Question | Visual | Interactive Explorer | Repository |
| --- | --- | --- | --- | --- |
| `trend-tracr` | How does one indicator change over time? | Line chart | [Trend Charts](https://civic-interconnect.github.io/trend-tracr/) | [Repository](https://github.com/civic-interconnect/trend-tracr) |
| `compare-tracr` | How do counties compare on one indicator? | Line / bar chart | [Compare Charts](https://civic-interconnect.github.io/compare-tracr/) | [Repository](https://github.com/civic-interconnect/compare-tracr) |
| `distribution-tracr` | How is one indicator distributed across counties? | Histogram / bar chart | [Distribution Charts](https://civic-interconnect.github.io/distribution-tracr/) | [Repository](https://github.com/civic-interconnect/distribution-tracr) |
| `relationship-tracr` | How are two indicators related? | Scatter plot | [Relationship Charts](https://civic-interconnect.github.io/relationship-tracr/) | [Repository](https://github.com/civic-interconnect/relationship-tracr) |

Each repository uses the same layered architecture.
To point an app at a different dataset, rewrite its `s00` source adapter
so the output matches the canonical schema.
Everything from `s01` onward keeps working.

---

[◄ Back to Home](index.md)
