import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys
import numpy as np

def tsv_process(tsvfile_path, search_str):

    df = pd.read_csv(tsvfile_path, sep='\t')

    filtered_df = df[df['#Chr_Pos_Ref_Alt'] == search_str].copy()
    # Convert the columns to numeric and fill the mark "." with 0
    columns_to_percentage = ['Global', 'SAS', 'AMR', 'EAS', 'NFE', 'FIN', 'ASJ', 'TWB1492']
    for column in columns_to_percentage:
        filtered_df[column] = pd.to_numeric(filtered_df[column], errors='coerce').fillna(0)
        filtered_df[column] = (filtered_df[column] * 100).astype(float)
    filtered_df = filtered_df.reset_index(drop=True)
    
    sorted_df = filtered_df.transpose().reset_index(inplace=False).iloc[1:].sort_values(by=[0], key=lambda x: x.astype(float), ascending=False).reset_index(drop=True).transpose()
    sorted_df = sorted_df.reset_index(drop=True)
    return sorted_df

def plot(sorted_df, search_str):
    data = sorted_df.iloc[1].astype(float)
    labels = sorted_df.iloc[0]
    colors = ['#9A031E', '#E36414', '#FFC436', '#739072', '#00A9FF', '#E95793', '#7071E8', '#C683D7']
    fig, ax = plt.subplots()

    plt.style.use('ggplot')

    plt.bar(labels, data, color=colors, width=0.5, align='center')

    plt.xlabel('Population', fontdict={'fontsize': 12, 'fontweight': 'bold', 'fontname': 'Arial'})
    plt.ylabel('Allele frequency (%)', fontdict={'fontsize': 12, 'fontweight': 'bold', 'fontname': 'Arial'})
    plt.title(f'{search_str}', fontdict={'fontsize': 16, 'fontweight': 'bold', 'fontname': 'Arial'})
    
    plt.show()

def main():
    search_str = sys.argv[1] 
    tsvfile_path = '/Users/anthony/Desktop/hg19_gnomad211_part_head.tsv' ## Change this path to your local path
    sorted_df = tsv_process(tsvfile_path, search_str)
    plot(sorted_df, search_str)

main()
