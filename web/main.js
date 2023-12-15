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
    data = await eel.search_by_variant(input)();
    if (Object.keys(data[0]).length === 0 && Object.keys(data[1]).length === 0) {
      alert("No variants found.");
    } else if (Object.keys(data[0]).length === 0 && Object.keys(data[1]).length !== 0) {
      returnEmptyResult("ClinVar");
      returnResult(data[1], "DVD");
    } else if (Object.keys(data[0]).length !== 0 && Object.keys(data[1]).length === 0) {
      returnResult(data[0], "ClinVar");
      returnEmptyResult("DVD");
    } else {
      returnResult(data[0], "ClinVar");
      returnResult(data[1], "DVD");
    }
  }

  function disableButton() {
    $("#submit-btn").prop("disabled", true);
  }

  function enableButton() {
    $("#submit-btn").prop("disabled", false);
  }

  function returnResult(variant, database) {
    $("#result").show();
    let result = $("#result");
    if (variant.length === 0) {
      $("#result").hide();
      alert("No variants found.");
    } else {
      let Info = $("<div></div>").addClass("box");
      const variantInfo = Object.entries(variant).map(([key, value]) => {
        return `<div><b>${key}:</b> &#9 ${value}</div>`;
      });
      Info.html(`
        <h3 class="database-header">${database}</h3>
        ${variantInfo.join("")}
      `);

      result.append(Info);
      enableButton();
    }
  }

  function returnEmptyResult(database) {
    $("#result").show();
    let result = $("#result");
    let Info = $("<div></div>").addClass("box");
    Info.html(`
      <h3 class="database-header">${database}</h3>
      <div>No variants found.</div>
    `);
    result.append(Info);
    enableButton();
  }
});
