import numpy as np
import matplotlib.pyplot as plt
import random
import csv

csv_file = "variants.csv"

rng = np.random.default_rng()


def random_zipf_distribution(n, a=1.01):
    """
    n: int: variantの数
    a: float: 1より大きい。zipf分布のパラメータ, zipf分布の形態を規定する。値が大きいほどzipf分布は急峻になる。
    return: np.ndarray: variantの出現頻度を表した配列。

    zipf分布に従う配列を生成する関数.100000個のランダムな値を生成し、その値の出現頻度を配列に格納する。
    returnの配列はindex 0 が wild typeを想定している。
    """
    a = a
    s = rng.zipf(a, 100000) - 1  # zipfの法則に従う. index0が最大になるように-1を行う。

    arr = np.zeros(n + 1)

    for i in s:
        if i > n:  # 0~nの範囲外の値は無視する。
            continue
        arr[int(i)] += 1
    monitor_distribution(arr, maximum_frequency=0.1)
    # plt.plot(arr)
    # plt.show()
    arr = arr / arr.sum()
    return list(arr)


def shuffle(arr):  # wild type以外の確率分布をシャッフルする。
    wild_type = arr[0]  # index 0はwild typeで固定とする。
    arr = random.sample(arr[1:], len(arr)-1)  # index 1〜nまでをランダムに並び替える。
    arr = [wild_type] + arr
    return arr


def param_adjuster(n):
    """
    n: int: variantの数
    return: float: zipf分布のパラメータaを調整するための関数。
    50はマジックナンバー。nの値が大きいほど、aのは小さくなり、zipf分布はなだらかになる。
    """
    a = 50 / n / n * rng.random()
    return 1 + a

def monitor_distribution(arr, maximum_frequency=0.1):
    """
    maximum_frequency: int: variantの出現頻度の最大値（wild typeを除く）
    return: list: 出現頻度を調整した配列
    variantの出現頻度が最大値を超えないように調整する。最大値を超えるものは出現頻度を下げ、その分wild typeの出現頻度を上げる。
    """

    maximum_number = int(arr.sum() * maximum_frequency)
    for i, val in enumerate(arr):
        if i == 0:
            continue
        if val < maximum_number:
            break
        else:
            # 0~10%までのランダムな値をひく。ランダム性を持たせる。rng.integer()の項は削除可能
            difference = maximum_number - rng.integers(maximum_number // 10)
            arr[i] = difference
            arr[0] += val - difference
    return arr


variants = {
    "ATP13A2": 94,
    "GBA": 39,
    "GPNMB": 52,
    "INPP5F": 80,
    "LRRK2": 54,
    "PLA2G6": 98,
    "Rab29": 19,
    "TMEM175": 83,
    "VPS35": 11,
    "VPS13C": 13,
}

for variant, number in variants.items():
    print(variant, number)
    a = param_adjuster(number) #variantの数に応じて、zipf分布のパラメータ調整。
    # a = 1.01 #固定の場合
    arr = random_zipf_distribution(number, a)
    arr = shuffle(arr)
    with open(csv_file, "a") as f:
        writer = csv.writer(f)
        writer.writerow([variant] + arr)
