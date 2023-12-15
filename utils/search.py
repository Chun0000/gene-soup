import pandas as pd


def get_clinvar_variant(var):
    raw = pd.read_csv('./database/final_h_clinvar_single_37.txt', sep='\t')
    chr = var.split('-')[0]
    pos = int(var.split('-')[1])
    ref = var.split('-')[2]
    alt = var.split('-')[3]
    result = raw[raw['Chromosome'] == chr]
    result = result[result['PositionVCF'] == pos]
    result = result[result['ReferenceAlleleVCF'] == ref]
    result = result[result['AlternateAlleleVCF'] == alt]
    if result.empty:
        return {}
    else:
        return result.to_dict(orient='records')[0]


def get_dvd_variant(var):
    raw = pd.read_csv('./database/DVD_final_w_disease.txt', sep='\t')
    pos = int(var.split('-')[1])
    ref = var.split('-')[2]
    alt = var.split('-')[3]
    result = raw[raw['POS'] == pos]
    result = result[result['REF'] == ref]
    result = result[result['ALT'] == alt]
    if result.empty:
        return {}
    else:
        return result.to_dict(orient='records')[0]
