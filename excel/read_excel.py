import pandas as pd

dateipfad = "excel/Gesamt_bereinigt.csv" 

df = pd.read_csv(dateipfad, sep=";")

print(df.head())