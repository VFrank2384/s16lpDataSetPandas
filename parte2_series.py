from parte1_exploracion import df

petal_length_serie = df["petal_length"]

long_max = petal_length_serie.max()
long_min = petal_length_serie.min()
long_prom = petal_length_serie.mean()

species_serie = df["species"]
conteo_especies = species_serie.value_counts()

explicacion_serie_df = (
    "Una Serie (pd.Series) es un arreglo unidimensional etiquetado (una sola columna "
    "con índice), mientras que un DataFrame (pd.DataFrame) es una estructura tabular "
    "bidimensional (filas y columnas) donde cada columna puede tener distinto dtype."
)

if __name__ == "__main__":
    print("=== 6. SERIE PETAL_LENGTH (primeros 5 valores) ===")
    print(petal_length_serie.head())

    print("\n=== 7. ESTADÍSTICAS DE PETAL_LENGTH ===")
    print(f"Máxima: {long_max} | Mínima: {long_min} | Promedio: {long_prom:.4f}")

    print("\n=== 8. CANTIDAD DE FLORES POR ESPECIE ===")
    print(conteo_especies)

    print("\n=== 9. DIFERENCIA ENTRE SERIE Y DATAFRAME ===")
    print(explicacion_serie_df)