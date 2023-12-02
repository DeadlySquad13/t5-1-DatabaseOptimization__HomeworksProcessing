import os.path
import pandas as pd
import sys

def main(path: str, sep: str):
    df = pd.read_csv(path, sep=sep, skipinitialspace=True)
    if sep != ",":
        df.replace(sep, ",")
    df = df.drop_duplicates()
    df = df.loc[:, (df != df.iloc[0]).any()] # Удаление константных столбцов
    df = df.drop(columns=['whether he/she donated blood in March 2007'])
    df.to_csv(os.path.basename(path)+"_preprocessed-without-target.csv", index=False)

if __name__ == "__main__":
    if len(sys.argv) <= 2:
        print("Использование: python preprocessing.py /path/to/file separator")
    else:
        main(sys.argv[1], sys.argv[2])
