let pagesForm = document.getElementById("pagesForm");
let curIndx = 0;

pagesForm.addEventListener("submit", (e) => {
  e.preventDefault();

  let pagesList = document.getElementById("pagesText");
  let interval = document.getElementById("ftime");
  if (!checkinput(pagesList, interval)) {
    alert("Ensure you input a value in both fields!");
  } else {
    let toShow = pagesList.value;
    const urls = toShow.trim().split(/\s|\n/).map(String);
    showPages(urls);
    let pageInterval = setInterval(
      () => showPages(urls),
      interval.value * 1000
    );
  }
});
function showPages(urls) {
  if (curIndx < urls.length) {
    console.log(curIndx);
    window.open(urls[curIndx], "_blank");
    curIndx++;
    console.log("ddddd");
  } else {
    console.log("AAAAAAAAAAAA");
    clearInterval(pageInterval);
  }
}

function checkinput(pagesList, interval) {
  //TODO дописать
  if (
    !pagesList.value.startsWith("https://") ||
    pagesList.value == "" ||
    interval.value == "" ||
    pagesList.value.match(" ")
  ) {
    return false;
  }
  return true;
}
