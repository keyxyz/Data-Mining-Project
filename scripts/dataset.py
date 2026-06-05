import pandas as pd

meta = pd.read_json("./data/meta_software.jsonl", lines=True)
print("metadata: shape\n")
print(meta.shape)

print("\nmetadata: columns\n")
print(meta.columns.tolist())

print("\nmetadata: info\n")
meta.info()

# print("\nmetadata: summary\n")
# print(meta.describe(include="all"))

print("\nmetadata: first 5 records\n")
print(meta.head())

# only first 100 rows since its huge
print("\ndataset: reading first 100 rows only")
df = pd.read_json("./data/software.jsonl", lines=True, nrows=100)

print("\ndataset: shape\n")
print(df.shape)

print("\ndataaset: columns\n")
print(df.columns.tolist())

print("\ndataset: info\n")
df.info()

# print("\ndataset: statistics\n")
# print(df.describe())

print("\ndataset: first 5 records\n")
print(df.head(5))

