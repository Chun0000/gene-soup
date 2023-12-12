import eel
import utils.search as search


@eel.expose
def get_variant(gene_name, code_change, protein_change):
    result = search.get_all_variants(gene_name, code_change, protein_change)
    return result.to_json(orient='records')


eel.init('web')
eel.start('main.html', size=(1000, 1000), port=8000)
