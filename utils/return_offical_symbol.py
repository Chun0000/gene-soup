import numpy as np

# symbol_dict = np.load("/Users/chun/Documents/GitHub/variant-search-engine/database/gene_symbol_conversion_dict.npy",
#                       allow_pickle=True).item()
symbol_dict = np.load("/Volumes/ANTHONY/database/gene_symbol_conversion_dict.npy",
                      allow_pickle=True).item()


def return_offical_symbol(gene_name):
    if gene_name in symbol_dict:
        return symbol_dict[gene_name]
    else:
        return gene_name
