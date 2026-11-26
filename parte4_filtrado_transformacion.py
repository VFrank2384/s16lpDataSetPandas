from parte3_indexacion import df

setosa_df = df[df["species"].str.lower() == "setosa"]

petal_mayor_4 = df[df["petal_length"] > 4.0]

virginica_ancho_mayor_2 = df[
    (df["species"].str.lower() == "virginica") & (df["petal_width"] > 2.0)
]

df["petal_area_estimada"] = df["petal_length"] * df["petal_width"]

df["sepal_area_estimada"] = df["sepal_length"] * df["sepal_width"]

df_ordenado_petal_area = df.sort_values(by="petal_area_estimada", ascending=False)

top_5_petal_area = df_ordenado_petal_area.head(5)

if __name__ == "__main__":
    print("=== 16. ESPECIE SETOSA (primeros 5) ===")
    print(setosa_df.head())

    print("\n=== 17. PETAL_LENGTH > 4 CM (primeros 5) ===")
    print(petal_mayor_4.head())

    print("\n=== 18. VIRGINICA CON PETAL_WIDTH > 2 CM ===")
    print(virginica_ancho_mayor_2)

    print("\n=== 19 Y 20. ÁREAS ESTIMADAS (primeros 5) ===")
    print(df[["petal_area_estimada", "sepal_area_estimada"]].head())

    print("\n=== 21. ORDENADO POR PETAL_AREA_ESTIMADA DESC (primeros 5) ===")
    print(df_ordenado_petal_area[["species", "petal_area_estimada"]].head())

    print("\n=== 22. TOP 5 MAYOR PETAL_AREA_ESTIMADA ===")
    print(top_5_petal_area)