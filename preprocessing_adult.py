import os.path
import pandas as pd
import sys

def main(path: str, sep: str):
    # Чтение файла.
    df = pd.read_csv(path, sep=sep, skipinitialspace=True)

    # Приведение к разделителю - запятой.
    if sep != ",":
        df.replace(sep, ",")
    df = df.loc[:, (df != df.iloc[0]).any()] # Удаление константных столбцов.
    # df = df.drop(columns=['income']) # Удаление целевого признака.
    df = df.drop_duplicates(subset=list( # Устранение дубликатов по всем столбцам кроме целевого ('income').
        filter(lambda col_name: col_name != 'income',df.columns)
    ))
    df.to_csv(os.path.basename(path)+"_preprocessed-without-target.csv", index=False)

if __name__ == "__main__":
    if len(sys.argv) <= 2:
        print("Использование: python preprocessing.py /path/to/file separator")
    else:
        main(sys.argv[1], sys.argv[2])

