#!/usr/bin/env python3

from itertools import combinations
import pandas as pd

df = pd.read_csv('../../../apathy/RUNDMC_data/RUNDMC_long_normed.csv')
df = df[df['TP'] == 2011]
df.dropna(subset=['FA_kurtosis_AllWM', 'AEStotal', 'CESDtotal'], inplace=True)
df['intercept'] = 1

d = {'AEStotal': 'apathy', 'CESDtotal': 'dep', 'MMSE': 'cog'}

_list = ['AEStotal', 'CESDtotal', 'MMSE']

for i in range(1, 4):
    comb = combinations(_list, i)
    for j in comb:
        var = [x for x in j] + ['age'] + ['intercept']
        fname = 'matrices/' + '_'.join([d[x] for x in var if x in d]) + '.mat'
        sub = df[var]
        with open(fname, 'w+') as f:
            f.write(f'\\NumWaves {sub.shape[1]}\n')
            f.write(f'\\NumPoints {sub.shape[0]}\n')
            f.write(f'\\Matrix\n')
        sub.to_csv(fname, mode='a', sep='\t', header=False, index=False)
