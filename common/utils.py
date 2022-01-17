import dvc.api
import pandas as pd


def read_remote_file(file, remote='helios'):
    return dvc.api.read(file, repo='https://github.com/ArturGogiyan/NLP_research', remote=remote)


def read_remote_dataset(remote='helios'):
    with dvc.api.open('dataset/post_processed.csv', repo='https://github.com/ArturGogiyan/NLP_research',
                      remote=remote) as fd:
        return pd.read_csv(fd)


def get_train_and_test(df, class_name="All", test_percentage=50):
    minimum_classes = 0
    if 0 < test_percentage <= 100:
        texts = []
        Ys = []
        classes = (list(df.columns.values))
        for index, row in df.iterrows():
            texts.append(row['comment'])
            if class_name == "All":
                for col in df.columns.values:
                    if row[col] == 1:
                        Ys.append(classes.index(col))
                        break
            else:
                Ys.append(row[class_name])

        ys_chk = 0
        if class_name != "All":
            for ys in Ys:
                ys_chk += ys
            if ys_chk < minimum_classes:
                return [], [], [], []

        test_size = int(len(texts) * test_percentage / 100)
        train_size = len(texts) - test_size
        texts_train = texts[:train_size]
        texts_test = texts[:-test_size]
        y_train = Ys[:train_size]
        y_test = Ys[:-test_size]

        return texts_train, texts_test, y_train, y_test
