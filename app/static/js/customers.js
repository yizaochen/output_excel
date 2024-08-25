function toggleSearchField() {
  const searchType = document.getElementById("searchType").value;
  const searchByNameForm = document.getElementById("searchByNameForm");
  const searchByIDForm = document.getElementById("searchByIDForm");
  const showAllForm = document.getElementById("showAllForm");

  if (searchType === "name") {
    searchByNameForm.style.display = "block";
    searchByIDForm.style.display = "none";
    showAllForm.style.display = "none";
  } else if (searchType === "id") {
    searchByNameForm.style.display = "none";
    searchByIDForm.style.display = "block";
    showAllForm.style.display = "none";
  } else if (searchType === "all") {
    searchByNameForm.style.display = "none";
    searchByIDForm.style.display = "none";
    showAllForm.style.display = "block";
  }
}
