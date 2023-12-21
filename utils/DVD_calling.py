import pandas as pd
from utils.search import get_gene_symbol
import utils.return_offical_symbol as offi

dvd = pd.read_csv(
    '/Volumes/ANTHONY/database/DVD_final_w_disease.txt', sep='\t')

def return_refgene(var):
    gene_list = get_gene_symbol(var)
    print(gene_list)
    if gene_list == []:
        result = ({}, {})
        return result
    else:
        result = get_result(gene_list)
    return result



def get_result(gene_list):
	gene_list = [offi.return_offical_symbol(i) for i in gene_list]
	dvd['Gene Symbol']=dvd['Gene Symbol'].astype('str')
	dvd['Clinical Significance']=dvd['Clinical Significance'].astype('str')
	for i in gene_list:
		select_gene=dvd[dvd['Gene Symbol']== i]
		p= int(select_gene[select_gene['Clinical Significance']== 'Pathogenic'].shape[0])
		lp=int(select_gene[select_gene['Clinical Significance']== 'Likely_pathogenic'].shape[0])
		vus=int(select_gene[select_gene['Clinical Significance']== 'Unknown_significance'].shape[0])
		lb=int(select_gene[select_gene['Clinical Significance']== 'Likely_benign'].shape[0])
		b=int(select_gene[select_gene['Clinical Significance']== 'Benign'].shape[0])

		new_data = pd.DataFrame(columns=['Gene','Pathogenic', 'Likely_pathogenic', 'Unknown_significance', 'Likely_benign', 'Benign'], index = ['a1', 'a2'])
		new_data['Gene']['a1']= i
		new_data['Pathogenic']['a1']=p
		new_data['Likely_pathogenic']['a1']=lp
		new_data['Unknown_significance']['a1']=vus
		new_data['Likely_benign']['a1']=lb
		new_data['Benign']['a1']=b
		t=p+lp+vus+lb+b
		new_data['Gene']['a2']= ''
		new_data['Pathogenic']['a2']=str(round((p/t)*100,1))+'%'
		new_data['Likely_pathogenic']['a2']=str(round((lp/t)*100,1))+'%'
		new_data['Unknown_significance']['a2']=str(round((vus/t)*100,1))+'%'
		new_data['Likely_benign']['a2']=str(round((lb/t)*100,1))+'%'
		new_data['Benign']['a2']=str(round((b/t)*100,1))+'%'
		return new_data.to_dict(orient='records')