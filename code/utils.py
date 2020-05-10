import pandas as pd


file_train_item_feat = "../data/underexpose_train/underexpose_item_feat.csv"
file_train_user_feat = "../data/underexpose_train/underexpose_user_feat.csv"
file_train_click = "../data/underexpose_train/underexpose_train_click-"
file_test_qtime0 = "../data/underexpose_test/underexpose_test_click-0/underexpose_test_qtime-0.csv"
file_test_click0 = "../data/underexpose_test/underexpose_test_click-0/underexpose_test_click-0.csv"


def read_train_item_feat(is_all=False):
    if is_all:
        df_train_item_feat = pd.read_csv(file_train_item_feat, sep=",\[", header=None)
    else:
        df_train_item_feat = pd.read_csv(file_train_item_feat, sep=",\[", header=None, nrows=10)
    df_train_item_feat.columns = ["item_id", "txt_vec", "img_vec"]
    return df_train_item_feat

def read_train_user_feat(is_all=False):
    if is_all:
        df_train_user_feat = pd.read_csv(file_train_user_feat, header=None)
    else:
        df_train_user_feat = pd.read_csv(file_train_user_feat, header=None, nrows=10)
    df_train_user_feat.columns = ["user_id", "user_age_level", "user_gender", "user_city_level"]
    return df_train_user_feat

def read_train_clicks(is_all=False, phase=0):
    if is_all:
        df_train_clicks = pd.read_csv(file_train_click + "0.csv", header=None)
        for i in range(1, phase + 1):
            df_train_click_t = pd.read_csv(file_train_click + str(i) + ".csv", header=None)
            df_train_clicks = pd.concat([df_train_clicks, df_train_click_t])
    else:
        df_train_clicks = pd.read_csv(file_train_click + "0.csv", header=None, nrows=10)
    df_train_clicks.columns = ["user_id", "item_id", "stamp"]
    return df_train_clicks

def read_test_clicks(is_all=False, phase=0):
    if is_all:
        df_test_clicks = pd.read_csv(file_test_click0, header=None)
        for i in range(1, phase + 1):
            df_test_click_t = pd.read_csv(file_test_click0.replace("0", str(i)), header=None)
            df_test_clicks = pd.concat([df_test_clicks, df_test_click_t])
    else:
        df_test_clicks = pd.read_csv(file_test_click0, header=None, nrows=10)
    df_test_clicks.columns = ["user_id", "item_id", "stamp"]
    return df_test_clicks

def read_test_qtimes(is_all=False, phase=0):
    if is_all:
        df_test_qtimes = pd.read_csv(file_test_qtime0, header=None)
        for i in range(1, phase + 1):
            df_test_qtime_t = pd.read_csv(file_test_qtime0.replace("0", str(i)), header=None)
            df_test_qtimes = pd.concat([df_test_qtimes, df_test_qtime_t])
    else:
        df_test_qtimes = pd.read_csv(file_test_qtime0, header=None, nrows=10)
    df_test_qtimes.columns = ["user_id", "stamp"]
    return df_test_qtimes


def test01():
    df_train_item_feat = read_train_item_feat()
    print(df_train_item_feat.head())
    df_train_user_feat = read_train_user_feat()
    print(df_train_user_feat.head())
    df_train_clicks = read_train_clicks(True, phase=2)
    print(len(df_train_clicks))
    print(df_train_clicks.head())
    df_test_clicks = read_test_clicks(True, phase=2)
    print(len(df_test_clicks))
    print(df_test_clicks.head())
    df_test_qtimes = read_test_qtimes(True, phase=2)
    print(len(df_test_qtimes))
    print(df_test_qtimes.head())



def tmp():
    df_train_item_feat = pd.read_csv(file_train_item_feat, sep=",\[", header=None, nrows=10)
    df_train_item_feat.columns = ["item_id", "txt_vec", "img_vec"]
    df_train_user_feat = pd.read_csv(file_train_user_feat, header=None, nrows=10)
    df_train_user_feat.columns = ["user_id", "user_age_level", "user_gender", "user_city_level"]
    df_train_click0 = pd.read_csv(file_train_click + "0.csv", header=None, nrows=10)
    df_train_click0.columns = ["user_id", "item_id", "stamp"]
    df_test_qtime0 = pd.read_csv(file_test_qtime0, header=None, nrows=10)
    df_test_qtime0.columns = ["user_id", "stamp"]
    df_test_click0 = pd.read_csv(file_test_click0, header=None, nrows=10)
    df_test_click0.columns = ["user_id", "item_id", "stamp"]
    print(df_train_item_feat)
    print(df_train_user_feat)
    print(df_train_click0)
    print(df_test_qtime0)
    print(df_test_click0)


