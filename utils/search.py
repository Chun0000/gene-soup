import pandas as pd


def get_all_variants(gene_name, code_change, protein_change):
    result = pd.read_csv('./database/data.csv')
    if gene_name != '':
        def is_in_aliases(aliases):
            return gene_name in aliases
        result = result[result['Symbol Alias'].apply(is_in_aliases)]
        if result.empty:
            result = result[result['Gene Symbol'] == gene_name]
    if code_change != '':
        result = result[result['code change'] == code_change]
    if protein_change != '':
        result = result[result['protein change'] == protein_change]
    return result
