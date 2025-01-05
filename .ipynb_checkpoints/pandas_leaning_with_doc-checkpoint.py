import marimo

__generated_with = "0.10.5"
app = marimo.App(width="full")


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell
def _(pd):
    df = pd.read_csv("data/survey_results_public.csv")
    return (df,)


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    df.head(8)
    return


@app.cell
def _(df):
    df.dtypes
    return


@app.cell
def _(df):
    df.info()
    return


@app.cell
def _(pd):
    titanic = pd.read_csv("./data/titanic.csv")
    return (titanic,)


@app.cell
def _(titanic):
    titanic.head()
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""i'm interested in the age of the titanic passengers """)
    return


@app.cell
def _(titanic):
    ages = titanic["Age"]
    ages.head()
    return (ages,)


@app.cell
def _(titanic):
    type(titanic["Age"])
    return


@app.cell
def _(titanic):
    titanic["Age"].shape
    return


@app.cell
def _(titanic):
    age_sex = titanic[["Age","Sex"]]
    age_sex.head()
    return (age_sex,)


@app.cell
def _(titanic):
    type(titanic[["Age","Sex"]])

    return


@app.cell
def _(titanic):
    titanic[["Age","Sex"]].shape
    return


@app.cell
def _(mo):
    mo.md(r"""filtering rows from the <kdb>DataFrame</kdb>""")
    return


@app.cell
def _(titanic):
    above_35 = titanic[titanic["Age"] > 35]
    above_35.head()
    return (above_35,)


@app.cell
def _(above_35):
    above_35.shape
    return


@app.cell
def _(titanic):
    class_23 = titanic[titanic["Pclass"].isin([2,3])]
    class_23.head()
    return (class_23,)


@app.cell
def _(titanic):
    age_no_na = titanic[titanic["Age"].notna()]
    age_no_na.head()
    return (age_no_na,)


@app.cell
def _(age_no_na):
    age_no_na.shape
    return


@app.cell
def _(titanic):
    adult_names = titanic.loc[titanic["Age"] > 35, "Name"]
    adult_names.head()
    return (adult_names,)


@app.cell
def _(titanic):
    titanic.loc[10:"Name"]
    return


@app.cell
def _(titanic):
    titanic.iloc[9:25, 2:5]
    return


@app.cell
def _(titanic):
    titanic.iloc[0:3, 3] = "anonymous"
    titanic.head()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
