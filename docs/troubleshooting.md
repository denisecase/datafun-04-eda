# Troubleshooting

## Deployed Marimo Reactive Apps

We use GitHub pages to deploy marimo notebooks as reactive apps.

When we push changes to GitHub, the
**.github\workflows\deploy-zensical-marimo.yml**
Action gets triggered and it prepares the app and deploys it
(for free)!

We debug it like we debug any web app:

- Right-click in the browser window and select **Inspect**.
- Look for the **Console** tab - that's the terminal running in the browser.
- Look for errors.
- Address the errors and redeploy.
- When an error doesn't make sense, copy and paste to AI to see recommendations.

## Troubleshooting Jupyter Notebooks

If you've created the .venv environment,
installed the necessary packages with **uv sync**,
and selected a Kernel for your Jupyter Notebook, it should run -
even if VS Code shows a missing package error.

Check Kernel and **.venv**.
VS Code may show an issue, but may still work.
Sometimes closing and reopening the notebook file is helpful.

Make sure your **.venv** is selected for the kernel.

## Why Your Notebook May Not See a Package

If the Jupyter notebook kernel is not set to the same environment
where you installed the package, the package won't be found.
This can happen if:

- The terminal is using one environment, but Jupyter kernel is using another.
- You have multiple environments and accidentally select the wrong one.
- Path conflicts or misconfigurations prevent the notebook from recognizing packages.

## Recommendations

### Recommendation 1: Keep Environment and Kernel Aligned

The environment where the Jupyter server runs might differ from the environment
where the notebook kernel runs.
This can lead to scenarios where a package appears installed in the terminal
but isn't accessible within the notebook.

When using uv:

1. Run **uv sync** in your project folder to install dependencies from pyproject.toml
2. In VS Code, click **Select Kernel** in the top-right of your notebook
3. Choose **Python Environments** and select the **.venv** in your project folder

### Recommendation 2: Use uv to Add Missing Packages

If you need to add a package, add it
to your **pyproject.toml** and rerun **uv sync**.
Or in the terminal:

```shell
uv add pandas
```

Then restart your kernel: **Kernel > Restart Kernel**
or click the restart button.

### Recommendation 3: Use Magic Commands as a Fallback

If your project environment and kernel are aligned
but you still have issues, use **magic commands**.
Magic commands are interpreted by the IPython kernel
and install directly into the notebook's environment.

Note: Don't use **py -m** like we do in the terminal.

For example, in a Jupyter Python cell:

```python
%pip install pandas
```

### Avoid: Shell Commands for Installs

Do NOT use **!pip install** (with an exclamation mark).
This runs in the shell environment,
which might not be the same environment as your notebook kernel.
Use **%pip install** (with a percent sign) for a magic command instead.

---

[◄ Back to Home](index.md)
