import pandas as pd


# dataset de reservas - Casa MamaEmma
datosReservas = {
    'cliente':      ['Juan', 'David', 'Ruiz', 'Jara', 'Ariel', 'Jean', 'Jose', 'Daniel', 'Jorge', 'Andrea'],
    'habitacion':   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'diasReserva':  [3, 5, 2, 7, 4, 1, 6, 3, None, 5],
    'fechaIngreso': ['2024-01-10', '2024-01-11', None, '2024-01-12', '2024-01-13',
                     '2024-01-14', None, '2024-01-15', '2024-01-16', '2024-01-17']
}


def cargarDatos(datos):
    dfReservas = pd.DataFrame(datos)
    return dfReservas


def verificarNulos(dfReservas):
    print("valores nulos por columna:")
    print(dfReservas.isnull().sum())
    print()


def limpiarDatos(dfReservas):
    dfLimpio = dfReservas.copy()
    dfLimpio['diasReserva']  = dfLimpio['diasReserva'].fillna(1)
    dfLimpio['fechaIngreso'] = dfLimpio['fechaIngreso'].fillna('sin fecha')
    dfLimpio['cliente']      = dfLimpio['cliente'].str.upper()
    return dfLimpio


def mostrarResumen(dfLimpio):
    print("estadisticas de dias de reserva:")
    print(dfLimpio['diasReserva'].describe())


# ---- ejecucion ----
dfReservas = cargarDatos(datosReservas)

print("------ DATASET ORIGINAL (con valores faltantes) ------")
print(dfReservas.to_string(index=False))
print()
verificarNulos(dfReservas)

dfLimpio = limpiarDatos(dfReservas)

print("------ DATASET PROCESADO (limpio y normalizado) ------")
print(dfLimpio.to_string(index=False))
print()
mostrarResumen(dfLimpio)
