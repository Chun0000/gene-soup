// query variant

$(document).ready(function () {
  $("#result").hide();
  $("#submit-btn").click(checkMode);
  function checkMode(event) {
    event.preventDefault(); // Prevent page refresh
    $("#result").empty();
    let input = $("#user").val();
    let searchMode = $("input[name='search-mode']:checked").attr("id");
    if (input === "") {
      alert("Input is empty.");
    } else if (searchMode === "gene-mode") {
      disableButton();
      geneMode(input);
    } else if (searchMode === "variant-mode") {
      disableButton();
      variantMode(input);
    }
  }

  async function geneMode(input) {
    await eel.search_by_gene(input)(returnClinVarResult);
  }

  async function variantMode(input) {
    await eel.search_by_variant(input)(returnClinVarResult);
  }

  function returnClinVarResult(variant) {
    $("#result").show();
    let result = $("#result");
    variant = JSON.parse(variant)[0];
    if (variant.length === 0) {
      $("#result").hide();
      alert("No variants found.");
    } else {
      let Info = $("<div></div>").addClass("box");
      Info.html(`
        <h3 class="database-header">ClinVar</h3>
        <div><b>Official Gene Symbol:</b> &#9 ${variant["GeneSymbol"]}</div>
        <div><b>Chromosome:</b> &#9 ${variant["Chromosome"]}</div>
        <div><b>Position (VCF):</b> &#9 ${variant["PositionVCF"]}</div>
        <div><b>Reference Allele (VCF):</b> &#9 ${variant["ReferenceAlleleVCF"]}</div>
        <div><b>Alternate Allele (VCF):</b> &#9 ${variant["AlternateAlleleVCF"]}</div>
        <div><b>Clinical Significance:</b> &#9 ${variant["ClinicalSignificance"]}</div>
        <div><b>Name:</b> &#9 ${variant["Name"]}</div>
        <div><b>RS# (dbSNP):</b> &#9 ${variant["RS# (dbSNP)"]}</div>
        <div><b>Phenotype List:</b> &#9 ${variant["PhenotypeList"]}</div>
      `);

      result.append(Info);
      enableButton();
    }
  }

  function disableButton() {
    $("#submit-btn").prop("disabled", true);
  }

  function enableButton() {
    $("#submit-btn").prop("disabled", false);
  }
});
