import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os


def tsv_process(tsvfile_path, search_str):

    df = pd.read_csv(tsvfile_path, sep='\t')
    if search_str not in df['#Chr_Pos_Ref_Alt'].values:
        print(f'{search_str} is not in the database.')
        return False

    filtered_df = df[df['#Chr_Pos_Ref_Alt'] == search_str].copy()
    # Convert the columns to numeric and fill the mark "." with 0
    columns_to_percentage = ['Global', 'SAS', 'AMR',
                             'EAS', 'NFE', 'FIN', 'ASJ', 'TWB1492']
    for column in columns_to_percentage:
        filtered_df[column] = pd.to_numeric(
            filtered_df[column], errors='coerce').fillna(0)
        filtered_df[column] = (filtered_df[column] * 100).astype(float)
    filtered_df = filtered_df.reset_index(drop=True)

    sorted_df = filtered_df.transpose().reset_index(inplace=False).iloc[1:].sort_values(
        by=[0], key=lambda x: x.astype(float), ascending=False).reset_index(drop=True).transpose()
    # sorted_df = sorted_df.reset_index(drop=True)
    return sorted_df


def plot(sorted_df, var):
    data = sorted_df.iloc[1].astype(float)
    labels = sorted_df.iloc[0]
    colors = ['#9A031E', '#E36414', '#FFC436', '#739072',
              '#00A9FF', '#E95793', '#7071E8', '#C683D7']

    plt.style.use('ggplot')

    plt.bar(labels, data, color=colors, width=0.5, align='center')

    plt.xlabel('Population', fontdict={
               'fontsize': 12, 'fontweight': 'bold', 'fontname': 'Arial'})
    plt.ylabel('Allele frequency (%)', fontdict={
               'fontsize': 12, 'fontweight': 'bold', 'fontname': 'Arial'})
    plt.title(f'{var}', fontdict={'fontsize': 16,
              'fontweight': 'bold', 'fontname': 'Arial'})

    for label, d in zip(labels, data):
        plt.text(label, d, f'{d:.2f}', ha='center',
                 va='bottom', fontsize=10, color='black')
    plt.savefig('./web/Image/popAF.png', dpi=300, bbox_inches='tight')
    plt.close()


def popAF_plot(var):
    search_str = var.replace('-', '_')
    filename = var.split('-')[0]
    # Change this path to your local path
    tsvfile_path = f'./database/gnomAD_TWB_merge_chrom{filename}.tsv'
    if not os.path.exists(tsvfile_path):
        print(f'{tsvfile_path} is not exist.')
        return False
    sorted_df = tsv_process(tsvfile_path, search_str)
    if sorted_df is False:
        return False
    else:
        plot(sorted_df, search_str)
        return True
