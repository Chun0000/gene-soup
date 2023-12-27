import numpy as np

symbol_dict = np.load("./database/gene_symbol_conversion_dict.npy",
                      allow_pickle=True).item()


def return_offical_symbol(gene_name):
    if gene_name in symbol_dict:
        return symbol_dict[gene_name]
    else:
        return gene_name
