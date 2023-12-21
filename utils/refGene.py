import pandas as pd
from utils.search import get_gene_symbol
import utils.return_offical_symbol as offi

refgenes = pd.read_csv(
    './database/refGene_transcript_transLen_final.txt', sep='\t')


def return_refgene(var):
    gene_list = get_gene_symbol(var)
    if gene_list == []:
        result = ({}, {})
        return result
    else:
        result = get_result(gene_list)
    return result


def get_result(gene_list):
    gene_list = [offi.return_offical_symbol(i) for i in gene_list]
    refgenes['gene_name'] = refgenes['gene_name'].astype('str')
    refgenes['start'] = refgenes['start'].astype('int')
    refgenes['end'] = refgenes['end'].astype('int')
    for i in gene_list:
        select_gene = refgenes[refgenes['gene_name'] == i]
        if select_gene.shape[0] == 0:
            continue
        else:
            select_gene.reset_index(drop=True, inplace=True)
            start_min = select_gene['start'].min()
            end_max = select_gene['end'].max()
            chromosome = select_gene['chromosome'][0]
            new_data = pd.DataFrame(
                columns=['gene_name', 'chromosome', 'start', 'end', 'gene_len'], index=['a1'])
            new_data['gene_name']['a1'] = i
            new_data['chromosome']['a1'] = chromosome
            new_data['start']['a1'] = start_min
            new_data['end']['a1'] = end_max
            new_data['gene_len']['a1'] = new_data['end']['a1'] - \
                new_data['start']['a1'] + 1
            return select_gene.to_dict(orient='records'), new_data.to_dict(orient='records')
    return {}, {}
