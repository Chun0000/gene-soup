import eel
import utils.search as search


@eel.expose
def search_by_variant(var):
    result_clinvar = search.get_clinvar_variant(var)
    result_dvd = search.get_dvd_variant(var)
    L = [result_clinvar, result_dvd]
    return L


# @eel.expose
# def search_by_gene(gene_name):
#     result = search.get_all_variants(gene_name)
#     return result.to_json(orient='records')


eel.init('web')
eel.start('main.html', size=(1000, 1000), port=8000)
