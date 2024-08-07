import pandas as pd
import numpy as np
import os
import sys
import subprocess

file = sys.argv[1]
data = pd.read_csv(file, sep='\t')
minimum = data.score.argmin()
row = data.loc[minimum]
print(row)
print(f"mean score: {data.score.mean():.2f}")
print(f"median score: {data.score.median():.2f}")
print(f"best out of {len(data)} searched")

if len(sys.argv) <= 2:
    sys.exit(0)
save = input("save this layout? (y/N): ") 
if save != 'y':
    sys.exit(0)
name = input("name: ")
filename = name.lower().replace(' ', '_')
kb = input("keyboard: ")

result = subprocess.run(["keywhisker", "layout-data", row.layout, kb, "--fixed", "--name", name],
                        capture_output = True,
                        text = True)
result.stdout
path = os.path.join("/home/semi/.local/share/keymeow/layouts/", f"{filename}.json")
with open (path, 'w') as file:
    file.write(result.stdout)
