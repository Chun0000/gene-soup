import pandas as pd
import utils.return_offical_symbol as offi

clinvar = pd.read_csv(
    './database/CLINVAR.txt', sep='\t')


def get_result(gene_list):
    gene_list = [offi.return_offical_symbol(i) for i in gene_list]
    clinvar['Gene Symbol'] = clinvar['Gene Symbol'].astype('str')
    clinvar['Clinical Significance'] = clinvar['Clinical Significance'].astype(
        'str')

    for i in gene_list:
        select_gene = clinvar[clinvar['Gene Symbol'] == i]
        if select_gene.shape[0] == 0:
            continue
        else:
            p = int(
                select_gene[select_gene['Clinical Significance'] == 'Pathogenic'].shape[0])
            p_lp = int(select_gene[select_gene['Clinical Significance']
                       == 'Pathogenic/Likely pathogenic'].shape[0])
            lp = int(
                select_gene[select_gene['Clinical Significance'] == 'Likely pathogenic'].shape[0])
            vus = int(
                select_gene[select_gene['Clinical Significance'] == 'Unknown significance'].shape[0])
            lb = int(
                select_gene[select_gene['Clinical Significance'] == 'Likely benign'].shape[0])
            lb_b = int(
                select_gene[select_gene['Clinical Significance'] == 'Benign/Likely benign'].shape[0])
            b = int(
                select_gene[select_gene['Clinical Significance'] == 'Benign'].shape[0])
            new_data = pd.DataFrame(columns=['Gene', 'Pathogenic', 'Pathogenic/Likely pathogenic', 'Likely pathogenic',
                                    'Unknown significance', 'Likely benign', 'Benign/Likely benign', 'Benign'], index=['a1', 'a2'])
            new_data['Gene']['a1'] = i
            new_data['Pathogenic']['a1'] = p
            new_data['Pathogenic/Likely pathogenic']['a1'] = p_lp
            new_data['Likely pathogenic']['a1'] = lp
            new_data['Unknown significance']['a1'] = vus
            new_data['Likely benign']['a1'] = lb
            new_data['Benign/Likely benign']['a1'] = lb_b
            new_data['Benign']['a1'] = b
            t = p+p_lp+lp+vus+lb+lb_b+b
            new_data['Gene']['a2'] = ''
            new_data['Pathogenic']['a2'] = str(round((p/t)*100, 1))+'%'
            new_data['Pathogenic/Likely pathogenic']['a2'] = str(
                round((p_lp/t)*100, 1))+'%'
            new_data['Likely pathogenic']['a2'] = str(round((lp/t)*100, 1))+'%'
            new_data['Unknown significance']['a2'] = str(
                round((vus/t)*100, 1))+'%'
            new_data['Likely benign']['a2'] = str(round((lb/t)*100, 1))+'%'
            new_data['Benign/Likely benign']['a2'] = str(
                round((lb_b/t)*100, 1))+'%'
            new_data['Benign']['a2'] = str(round((b/t)*100, 1))+'%'
            return new_data.to_dict(orient='records')
    return {}
