document.addEventListener("DOMContentLoaded", function () {
  // Convert code blocks with language-mermaid class to mermaid divs
  document.querySelectorAll("code.language-mermaid").forEach(function (el) {
    var div = document.createElement("div");
    div.className = "mermaid";
    div.textContent = el.textContent;
    el.parentElement.replaceWith(div);
  });
  mermaid.initialize({ startOnLoad: true, theme: "neutral" });
});
