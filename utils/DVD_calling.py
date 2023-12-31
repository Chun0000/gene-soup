import pandas as pd
import utils.return_offical_symbol as offi

dvd = pd.read_csv('./database/DVD.txt', sep='\t')


def get_result(gene_list):
    gene_list = [offi.return_offical_symbol(i) for i in gene_list]
    dvd['Gene Symbol'] = dvd['Gene Symbol'].astype('str')
    dvd['Clinical Significance'] = dvd['Clinical Significance'].astype('str')
    for i in gene_list:
        select_gene = dvd[dvd['Gene Symbol'] == i]
        if select_gene.shape[0] == 0:
            continue
        else:
            p = int(
                select_gene[select_gene['Clinical Significance'] == 'Pathogenic'].shape[0])
            lp = int(select_gene[select_gene['Clinical Significance']
                                 == 'Likely_pathogenic'].shape[0])
            vus = int(select_gene[select_gene['Clinical Significance']
                                  == 'Unknown_significance'].shape[0])
            lb = int(
                select_gene[select_gene['Clinical Significance'] == 'Likely_benign'].shape[0])
            b = int(
                select_gene[select_gene['Clinical Significance'] == 'Benign'].shape[0])

            new_data = pd.DataFrame(columns=['Gene', 'Pathogenic', 'Likely pathogenic',
                                             'Unknown Significance', 'Likely Benign', 'Benign'], index=['a1', 'a2'])
            new_data['Gene']['a1'] = i
            new_data['Pathogenic']['a1'] = p
            new_data['Likely pathogenic']['a1'] = lp
            new_data['Unknown Significance']['a1'] = vus
            new_data['Likely Benign']['a1'] = lb
            new_data['Benign']['a1'] = b
            t = p+lp+vus+lb+b
            new_data['Gene']['a2'] = ''
            new_data['Pathogenic']['a2'] = str(round((p/t)*100, 1))+'%'
            new_data['Likely pathogenic']['a2'] = str(round((lp/t)*100, 1))+'%'
            new_data['Unknown Significance']['a2'] = str(
                round((vus/t)*100, 1))+'%'
            new_data['Likely Benign']['a2'] = str(round((lb/t)*100, 1))+'%'
            new_data['Benign']['a2'] = str(round((b/t)*100, 1))+'%'
            return new_data.to_dict(orient='records')
    return {}
