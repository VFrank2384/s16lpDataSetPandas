import pandas as pd

try:
    import seaborn as sns
    df = sns.load_dataset("iris")
except Exception:
    try:
        from sklearn.datasets import load_iris
        iris_raw = load_iris(as_frame=True)
        df = iris_raw.frame.copy()
        df.columns = [
            "sepal_length",
            "sepal_width",
            "petal_length",
            "petal_width",
            "species_id"
        ]
        mapa_especies = dict(enumerate(iris_raw.target_names))
        df["species"] = df["species_id"].map(mapa_especies)
        df = df.drop(columns=["species_id"])
    except Exception:
        url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
        df = pd.read_csv(url)

df = df.rename(columns={
    "sepal length (cm)": "sepal_length",
    "sepal width (cm)": "sepal_width",
    "petal length (cm)": "petal_length",
    "petal width (cm)": "petal_width"
})

if __name__ == "__main__":
    
    print("=== 2. PRIMEROS 10 REGISTROS ===")
    print(df.head(10))

    print("\n=== 2. ÚLTIMOS 5 REGISTROS ===")
    print(df.tail(5))

    filas, columnas = df.shape
    print("\n=== 3. DIMENSIONES ===")
    print(f"Filas: {filas} | Columnas: {columnas}")

    print("\n=== 4. COLUMNAS Y TIPOS DE DATOS ===")
    print(df.dtypes)

    print("\n=== 5. VALORES FALTANTES POR COLUMNA ===")
    print(df.isnull().sum())
    print(f"¿Existen valores faltantes en total?: {df.isnull().any().any()}")