import argparse
import os 

import pandas as pd
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser()
parser.add_argument("--file", help="Spectrum CSV file", type=str)

args = parser.parse_args()

if not args.file:
    raise Exception("--file argument not specified.")

(file_root, file_ext) = os.path.splitext(args.file)
file_base = os.path.basename(file_root)
df = pd.read_csv(args.file, sep='\t')

# print(df)

df.plot(kind='line',
        x='Frequency (Hz)',
        y='Level (dB)',
        logy=False,
        logx=False,
        # logx=True,
        # xlim=(1,2**14),
        ylim=(-130,0),
        lw=0.25,
        grid=True,
        figsize=(20, 10),
        title=file_base,
        xlabel='Frequency (Hz)',
        ylabel="Level (dB)",
        )
# plt.show()

plt.savefig(file_root+".png")
