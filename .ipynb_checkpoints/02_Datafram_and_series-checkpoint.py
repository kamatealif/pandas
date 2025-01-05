import marimo

__generated_with = "0.10.5"
app = marimo.App(width="full")


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
