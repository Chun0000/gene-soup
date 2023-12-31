import eel
import utils.search as search
import utils.refGene as refGene
import utils.popAF_plot as popAF
import utils.DVD_calling as DVD
import utils.ClinVar_calling as ClinVar


@eel.expose
def search_by_variant(var):
    result_clinvar = search.get_clinvar_variant(var)
    result_dvd = search.get_dvd_variant(var)
    result_refgene = refGene.return_refgene(var)
    result_popAF = popAF.popAF_plot(var)
    L = [result_clinvar, result_dvd, result_refgene[0],
         result_refgene[1], result_popAF]
    return L


@eel.expose
def search_by_gene(gene_name):
    gene_list = []
    gene_list.append(gene_name)
    result_refgene = refGene.get_result(gene_list)
    result_dvd = DVD.get_result(gene_list)
    clinvar_result = ClinVar.get_result(gene_list)
    L = [result_refgene[0], result_refgene[1], result_dvd, clinvar_result]
    return L


eel.init('web')
eel.start('main.html', size=(1000, 1000), port=8000)
