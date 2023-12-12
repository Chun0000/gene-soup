// query variant

$(document).ready(function () {
  $("#result").hide();
  $("#submit-bnt").click(getVariant);
  async function getVariant() {
    $(".result_row").remove();
    let gene_name = $("#gene_name").val();
    let code_change = $("#code_change").val();
    let protein_change = $("#protein_change").val();

    if (gene_name === "" && code_change === "" && protein_change === "") {
      alert("Please at least fill one field.");
      return;
    }

    await eel.get_variant(gene_name, code_change, protein_change)(returnResult);
  }

  function returnResult(variants) {
    $("#result").show();
    let result = $("#result");
    variants = JSON.parse(variants);
    if (variants.length === 0) {
      $("#result").hide();
      alert("No variants found.");
    } else {
      variants.forEach((variant) => {
        let Info = $("<div></div>").addClass("result_row");
        Info.html(`
          <div>${variant["Gene Symbol"]}</div>
          <div>${variant.Position}</div>
          <div>${variant["Code change"]}</div>
          <div>${variant["Protein change"]}</div>
        `);
        result.append(Info);
        delete variant["Gene Symbol"];
        delete variant.Position;
        delete variant["Code change"];
        delete variant["Protein change"];
        let AddiInfo = $("<div></div>").addClass("addi_info");
        AddiInfo.html(`
          ${Object.keys(variant)
            .map((key) => `<div><b>${key}</b> &#9${variant[key]}</div>`)
            .join("")}
        `);
        result.append(AddiInfo);
      });
      $(".result_row").click(function () {
        $(this).next(".addi_info").slideToggle("slow");
      });
    }
  }
});
