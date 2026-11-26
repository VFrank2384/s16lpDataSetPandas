from parte1_exploracion import df

df.index = [f"F{i:03d}" for i in range(1, len(df) + 1)]

explicacion_loc_iloc = (
    ".loc selecciona por etiquetas (índice/columna) o condiciones booleanas e incluye el "
    "límite superior en slices; .iloc selecciona por posición entera (base 0) y excluye "
    "el límite superior en slices."
)

if __name__ == "__main__":
    print("=== 10. ÍNDICE PERSONALIZADO (primeros 5) ===")
    print(df.index[:5])

    print("\n=== 11. CARACTERÍSTICAS DE F025 (.loc) ===")
    print(df.loc["F025"])

    print("\n=== 12. PETAL_LENGTH Y PETAL_WIDTH DE F080 (.loc) ===")
    print(df.loc["F080", ["petal_length", "petal_width"]])

    print("\n=== 13. PRIMEROS 10 REGISTROS (.iloc) ===")
    print(df.iloc[:10])

    print("\n=== 14. POSICIONES 20 A 30 INCLUSIVE, PRIMERAS 4 COLUMNAS (.iloc) ===")
    print(df.iloc[20:31, 0:4])

    print("\n=== 15. DIFERENCIAS ENTRE .loc E .iloc ===")
    print(explicacion_loc_iloc)