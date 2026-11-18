import pandas as pd
import matplotlib.pyplot as plt
# Angela Correa NC = 0037
# Problema 14. Mecánicos del taller
mecanicos_taller = {
    'id_mecanico': [301, 302, 303, 304, 305, 306],
    'nombre': ['Roberto', 'Luis', 'Carlos', 'Fernando', 'Jorge', 'Miguel'],
    'especialidad': ['Motor', 'Suspension', 'Electrico', 'Frenos', 'Transmision', 'General'],
    'anos_experiencia': [15, 8, 12, 5, 20, 10],
    'salario_base': [18000, 15000, 17000, 14000, 20000, 16000],
    'comision_porcentaje': [10, 10, 10, 10, 10, 10],
    'ordenes_completadas_mes': [25, 30, 20, 15, 35, 28],
    'calificacion_cliente': [4.8, 4.5, 4.9, 4.2, 5.0, 4.6],
    'turno': ['Matutino', 'Vespertino', 'Matutino', 'Vespertino', 'Matutino', 'Vespertino'],
    'certificacion': [True, True, True, False, True, True]
}
print("Análisis Exploratorio de Datos EDA")
print("Exploratory Data Analysis por Angela Correa NC = 0037")
print("5. Crear el diccionario con 10 listas y 6 elementos")
# 2. Convertir diccionario en DataFrame
df = pd.DataFrame(mecanicos_taller)
print("\n--- TABLA ORIGINAL DE MECANICOS ---")
print(df)
# 3. Exportar los datos a CSV
print("-+-+-+-++-+- Convertir el DataFrame en archivo CSV +--+-+-+-++--")
df.to_csv(
    'mecanicos_taller_0037.csv',
    index=False,
    encoding='utf-8-sig'
)
print("\n✅ Archivo CSV creado correctamente")
print("+--+-++-+-+-+- 8. Leer los datos desde el archivo CSV +-+-+-+-+-+-+-")
print("mecanicos_taller_0037.csv")
# 4. Leer el archivo CSV
df = pd.read_csv('mecanicos_taller_0037.csv')
print("\n--- DATOS LEÍDOS DESDE CSV ---")
print(df)

print("+--+-++-+--+-+ 9. Análisis Exploratorio de Datos (EDA) +--++-+-+-+-+-+-+-")
# 5. Primeros y últimos registros
print("-++-++- \n1. PRIMEROS REGISTROS (Head): -++-+-+-+-")
print(df.head(3)) # Muestra los primeros 3

print("+-+-+-+- \n2. ÚLTIMOS REGISTROS (Tail):")
print(df.tail(2)) # Muestra los últimos 2
# 6. Dimensiones y estructura
print("+-+-+-+- 6. Dimensiones y estructura +--+-++-+")
print(df) # mostrar tabla o matriz

print("\n3. DIMENSIONES (Filas, Columnas):", df.shape)
print("\n4. NOMBRES DE COLUMNAS:\n", df.columns)
print("\n5. TIPOS DE DATOS:\n", df.dtypes)

print("\n6. INFORMACIÓN GENERAL:")
df.info()
# 7. Estadísticas y limpieza
print("+--+-+-++- \n7. ESTADÍSTICAS DESCRIPTIVAS: -+-+-++-+-+-+")
print(df.describe())

print("\n8. VALORES FALTANTES (Nulls):")
print(df.isnull().sum())

print("\n9. REGISTROS DUPLICADOS:")
print(df.duplicated().sum())

print("\n10. VALORES ÚNICOS POR COLUMNA:")
print(df.nunique())

print("Especialidades únicas:", df['especialidad'].unique())
# 8. Análisis específico
print(df)
print("-----------------------------------------------------------------------------------")

print("\n11. MECANICOS POR ESPECIALIDAD:")
print(df['especialidad'].value_counts())

print("\n12. PROMEDIO DE SALARIO: $", df['salario_base'].mean())
print("13. SALARIO MÁXIMO: $", df['salario_base'].max())
print("14. SALARIO MÍNIMO: $", df['salario_base'].min())

# 9. Ordenamiento, filtrado y agrupación
print("# 9. Ordenamiento, filtrado y agrupación")

print("-+-+-+-++-++- \n15. MECANICOS ORDENADOS POR SALARIO (Mayor a menor): -+-+-+-++-+")
print(df.sort_values(by='salario_base', ascending=False))

print("\n16. MECANICOS CON SALARIO MAYOR A $15,000:")
filtro = df[df['salario_base'] > 15000]
print(filtro)

print("\n17. RESUMEN POR ESPECIALIDAD:")
resumen = df.groupby('especialidad').agg(
    mecanicos=('id_mecanico', 'count'),
    salario_promedio=('salario_base', 'mean'),
    salario_maximo=('salario_base', 'max')
)
print(resumen)
# 18. Gráfica de barras: Mecanicos por especialidad
print("18. Gráfica de barras: Mecanicos por especialidad")

conteo = df['especialidad'].value_counts()
plt.figure(figsize=(8, 5))
plt.bar(conteo.index, conteo.values, color='skyblue')
plt.title('Mecanicos por especialidad Angela Correa NC = 0037')
plt.xlabel('Especialidad')
plt.ylabel('Cantidad de mecanicos')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 19. Gráfica de barras: Salarios por mecanico
plt.figure(figsize=(8, 5))
plt.bar(df['nombre'], df['salario_base'], color='lightgreen')
plt.title('Salario mensual por mecanico EDA por Correa 0037')
plt.xlabel('Mecanico')
plt.ylabel('Salario en pesos')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 20. Histograma: Distribución de años de experiencia
plt.figure(figsize=(8, 5))
plt.hist(df['anos_experiencia'], bins=5, color='orange', edgecolor='black')
plt.title('Distribución de años de experiencia de mecanicos EDA Correa 0037')
plt.xlabel('Años de experiencia')
plt.ylabel('Frecuencia')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 21. Gráfica de dispersión: Experiencia vs Salario
plt.figure(figsize=(8, 5))
plt.scatter(df['anos_experiencia'], df['salario_base'], color='red', s=100)
plt.title('Relación entre experiencia y salario EDA por Angela Correa 0037')
plt.xlabel('Años de experiencia')
plt.ylabel('Salario mensual')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 22. Diagrama de caja: Distribución de salarios
plt.figure(figsize=(7, 5))
plt.boxplot(df['salario_base'], patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title('Distribución de salarios (Boxplot) EDA Angela Correa 0037')
plt.ylabel('Salario mensual')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 23. Matriz de correlación
correlacion = df.corr(numeric_only=True)
print("\n--- MATRIZ DE CORRELACIÓN ---")
print(correlacion)

plt.figure(figsize=(9, 6))
plt.imshow(correlacion, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(correlacion.columns)), correlacion.columns, rotation=45)
plt.yticks(range(len(correlacion.columns)), correlacion.columns)
plt.title('Matriz de correlación de variables numéricas EDA Angela Correa 0037')
plt.tight_layout()
plt.show()