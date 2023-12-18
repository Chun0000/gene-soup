import pandas as pd

ClinVar = pd.read_csv('./database/final_h_clinvar_single_37.txt', sep='\t')
DVD = pd.read_csv('./database/DVD_final_w_disease.txt', sep='\t')


def get_clinvar_variant(var):
    chr = var.split('-')[0]
    pos = int(var.split('-')[1])
    ref = var.split('-')[2]
    alt = var.split('-')[3]
    result = ClinVar[ClinVar['Chromosome'] == chr]
    result = result[result['Position'] == pos]
    result = result[result['Reference Allele'] == ref]
    result = result[result['Alternate Allele'] == alt]
    if result.empty:
        return {}
    else:
        return result.to_dict(orient='records')[0]


def get_gene_symbol(var):
    chr = var.split('-')[0]
    pos = int(var.split('-')[1])
    result = ClinVar[ClinVar['Position'] == pos]
    result = result[result['Chromosome'] == chr]
    gene_list = result['Gene Symbol'].head(1).to_list()
    if result.empty:
        return []
    else:
        return gene_list


def get_dvd_variant(var):
    pos = int(var.split('-')[1])
    ref = var.split('-')[2]
    alt = var.split('-')[3]
    result = DVD[DVD['Position'] == pos]
    result = result[result['Reference Allele'] == ref]
    result = result[result['Alternate Allele'] == alt]
    if result.empty:
        return {}
    else:
        return result.to_dict(orient='records')[0]
