window.PagedConfig = { auto: false };

function makeBookTableOfContents() {
    let tocTags = {};
    let rootList = document.createElement("OL");
    rootList.id = "contents";

    for (var sec of document.querySelectorAll("SECTION")) {
        let tocParent;
        if (sec.parentNode.tagName != "SECTION") {
            tocParent = rootList;
        } else {
            let tocParentLI = tocTags[sec.parentNode.id];
            tocParent = tocParentLI.querySelector("OL");
            if (!tocParent) {
                tocParent = document.createElement("OL");
                tocParentLI.appendChild(tocParent);
            }
        }

        let sectionLI = document.createElement("LI");
        let sectionA = document.createElement("A");
        sectionA.innerText = sec.querySelector("H1,H2,H3,H4,H5,H6").innerText;
        sectionA.href = "#" + sec.id;
        sectionLI.appendChild(sectionA);
        tocParent.appendChild(sectionLI);
        tocTags[sec.id] = sectionLI;
    }

    document.getElementById("single-page-toc").appendChild(rootList);
}

function paginate(pageFormat) {
    let pageStyle = document.createElement('style');
    pageStyle.id = 'pagedjs-page-style';
    pageStyle.innerHTML = `
    @page {
        size: ${pageFormat} portrait;
        margin: 25mm 25mm;
        @bottom-right { content: counter(page); }
    }`;
    document.head.appendChild(pageStyle);

    var script = document.createElement("script");
    script.src = "_static/paged.polyfill.js";
    script.onload = () => window.PagedPolyfill.preview();
    document.head.appendChild(script);
}

document.addEventListener('DOMContentLoaded', () => {
    makeBookTableOfContents();

    let searchParams = new URLSearchParams(window.location.search);
    if (searchParams.has("paginate")) {
        paginate(searchParams.get("paginate"));
    }
});
