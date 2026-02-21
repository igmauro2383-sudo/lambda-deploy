import pandas as pd

def es_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def handler(event, context):
    # Crear un DataFrame simple
    df = pd.DataFrame({
        "a": [1, 2, 3],
        "b": [4, 5, 6]
    })

    suma_columna_a = int(df["a"].sum())

    # Tomar n desde event si viene, si no usar 29
    n = 29
    if isinstance(event, dict) and "n" in event:
        n = event["n"]

    resultado_primo = es_primo(n)

    print("hello lambda from zappa")
    print("DataFrame:")
    print(df)
    print(f"n={n} -> es_primo={resultado_primo}")

    return {
        "mensaje": "Pandas funciona correctamente",
        "suma_columna_a": suma_columna_a,
        "filas": int(df.shape[0]),
        "columnas": int(df.shape[1]),
        "n": int(n) if str(n).isdigit() else n,
        "es_primo": resultado_primo
    }