# Parkinso disease variant data generation
Parkinson病に関連した遺伝子のvariantについて、zipf分布に従う様にデータを生成するscriptです。
```
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
```
例えばATP13A2という遺伝子にはwild typeの他に94個の遺伝子多型が存在する。94個のvariantの出現頻度を生成する。

## コードの流れ

Zipf分布から10万件の値をサンプリング

各数字（=バリアントID）の出現回数をカウント

その頻度を正規化して確率ベクトルに変換

variant出現頻度をshuffle。

その確率に基づいてvariantをサンプリングできるようにする。
