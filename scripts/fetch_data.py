#!/usr/bin/env python3

from itertools import combinations
import pandas as pd


def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text


df = pd.read_csv('../../../apathy/RUNDMC_data/RUNDMC_long_normed.csv')
df = df[df['TP'] == 2011]
df.dropna(subset=['FA_kurtosis_AllWM', 'AEStotal', 'CESDtotal'], inplace=True)
df['intercept'] = 1

d = {'AEStotal': 'apathy', 'CESDtotal': 'dep', 'MMSE': 'cog'}

_list = ['AEStotal', 'CESDtotal', 'MMSE']

for i in range(1, 4):
    comb = combinations(_list, i)
    for j in comb:
        var = [x for x in j] + ['age'] + ['eTIV'] + ['intercept']
        fname = '_'.join([d[x] for x in var if x in d])
        sub = df[var]
        # with open(f'matrices/{fname}.mat', 'w+') as f:
        #     f.write(f'\\NumWaves {sub.shape[1]}\n')
        #     f.write(f'\\NumPoints {sub.shape[0]}\n')
        #     f.write(f'\\Matrix\n')
        sub.to_csv(f'matrices/{fname}.txt', mode='w+', sep='\t', header=False, index=False)

        template_file = 'randomise_template.batch'
        rand_file = f'randomise_scripts/{fname}.batch'
        contrasts = f'{len(var)-1}cov.con'

        replacement_d = {'design.mat': f'{fname}.mat',
                         'design.con': f'{contrasts}',
                         'output_prefix': fname}

        with open(template_file, 'r') as a, open(rand_file, 'w+') as b:
            for line in a:
                b.write(replace_all(line, replacement_d))
