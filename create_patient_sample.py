import csv
import numpy as np

gene_variant_probs = {}

csv_file = "variants.csv"
with open(csv_file, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        gene_variant_probs[row[0]] = row[1:]


def create_samples(sample_number):
    """
    sample_number: int: サンプル数
    return: list: サンプルのリスト
    [
        {"gene1": [variant1, variant2], "gene2: [variant1, variant2],....,"phenotype":boolean},
        {"gene1": [variant1, variant2], "gene2: [variant1, variant2],....,"phenotype":boolean},
        .....
    ]
    各サンプルは10個の遺伝子のvariantを2つ持つ。phenotypeはboolean型で、trueなら発症。
    """
    samples = []
    for i in range(sample_number):
        dict = {}
        for gene_name, frequency in gene_variant_probs.items():
            dict[gene_name] = list(np.random.choice(len(frequency), size=2, p=frequency))
        dict["phenotype"] = False
        samples.append(dict)
    
    return samples

# print(gene_variant_probs)

samples = create_samples(100)

# with open("samples.csv", "w") as f:
#     writer = csv.DictWriter(f, fieldnames=samples[0].keys())
#     writer.writeheader()
#     for sample in samples:
#         writer.writerow(sample)