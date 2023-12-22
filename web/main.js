// query variant

$(document).ready(function () {
  $("#result").hide();
  $("#figure").hide();
  $("#alert-box").hide();
  $("#submit-btn").click(checkMode);

  function checkMode(event) {
    event.preventDefault(); // Prevent page refresh
    $("#result").empty();
    let input = $("#user").val();
    let searchMode = $("input[name='search-mode']:checked").attr("id");
    if (input === "") {
      showAlertBox("Input is empty.");
      $("#alert-btn").click(closeAlertBox);
    } else if (searchMode === "gene-mode") {
      if (input.split("-").length > 3) {
        showAlertBox("Please enter a valid gene name.");
        $("#alert-btn").click(closeAlertBox);
      } else {
        disableButton();
        geneMode(input);
      }
    } else if (searchMode === "variant-mode") {
      if (input.split("-").length == 1) {
        showAlertBox("Please enter a valid variant format.");
        $("#alert-btn").click(closeAlertBox);
      } else {
        disableButton();
        variantMode(input);
      }
    }
  }

  async function geneMode(input) {
    data = await eel.search_by_gene(input)();
    if (Object.keys(data[0]).length === 0 && Object.keys(data[1]).length === 0 && Object.keys(data[2]).length === 0) {
      showAlertBox("No genes found.");
      $("#alert-btn").click(closeAlertBox);
      enableButton();
    } else {
      returnResult(data[1], "RefGene - Overview");
      returnResult(data[0], "RefGene - Transcript");
      returnResult(data[2], "DVD - Overview");
      returnResult(data[3], "Clinvar - Overview");
    }
  }

  async function variantMode(input) {
    data = await eel.search_by_variant(input)();
    if (
      Object.keys(data[0]).length === 0 &&
      Object.keys(data[1]).length === 0 &&
      Object.keys(data[2]).length === 0 &&
      data[4] !== true
    ) {
      showAlertBox("No variants found.");
      $("#alert-btn").click(closeAlertBox);
      enableButton();
    } else {
      showFigure(data[4]);
      returnResult(data[3], "RefGene - Overview");
      returnResult(data[2], "RefGene - Transcript");
      returnResult(data[0], "ClinVar");
      returnResult(data[1], "DVD");
    }
  }

  function showAlertBox(message) {
    $("#alert-box").show();
    let Box = $("#alert-content");
    Box.empty();
    Box.append(`
    <h3 class="CAUTION">CAUTION</h3>
    <div>${message}</div>
  `);
  }
  function closeAlertBox() {
    $("#alert-box").hide();
  }

  function showFigure(data) {
    if (data === true) {
      $("#figure").show();
    } else {
      $("#figure").hide();
    }
    enableButton();
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
    if (Object.keys(variant).length === 0) {
      returnEmptyResult(database);
    } else if (database === "RefGene - Transcript") {
      let Info = $("<div></div>").addClass("box");
      const header = Object.keys(variant[0]).map((key) => {
        return `<th>${key}</th>`;
      });
      const variantInfo = variant.map((data) => {
        return `<tr>${Object.values(data)
          .map((value) => {
            return `<td>${value}</td>`;
          })
          .join("")}</tr>`;
      });
      Info.append(`
          <h3 class="database-header">${database}</h3>
          <table>
          <thead>
            <tr>
              ${header.join("")}
            </tr>
          </thead>
          <tbody>
            ${variantInfo.join("")}
          </table>
        `);
      result.append(Info);
    } else if ((database === "DVD - Overview") | (database === "Clinvar - Overview")) {
      let Info = $("<div></div>").addClass("box");
      const header = Object.keys(variant[0]).map((key) => {
        return `<th>${key}</th>`;
      });
      const variantInfo = variant.map((data) => {
        return `<tr>${Object.values(data)
          .map((value) => {
            return `<td>${value}</td>`;
          })
          .join("")}</tr>`;
      });
      Info.append(`
          <h3 class="database-header">${database}</h3>
          <table>
          <thead>
            <tr>
              ${header.join("")}
            </tr>
          </thead>
          <tbody>
            ${variantInfo.join("")}
          </table>
        `);
      result.append(Info);
    } else {
      let Info = $("<div></div>").addClass("box");
      if (database === "RefGene - Overview") {
        variant = variant[0];
      }
      const variantInfo = Object.entries(variant).map(([key, value]) => {
        return `<div><b>${key}:</b> &#9 ${value}</div>`;
      });
      Info.html(`
        <h3 class="database-header">${database}</h3>
        ${variantInfo.join("")}
      `);
      result.append(Info);
    }
    enableButton();
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
