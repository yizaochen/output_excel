document.getElementById("generate-excel").addEventListener("click", () => {
  const data = [];
  const rows = document.querySelectorAll("table tr");

  rows.forEach((row) => {
    const rowData = Array.from(row.querySelectorAll("th, td")).map(
      (cell) => cell.innerText
    );
    data.push(rowData);
  });

  const worksheet = XLSX.utils.aoa_to_sheet(data);
  const workbook = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(workbook, worksheet, "Transactions");

  // Get the current date and time in ISO format and remove milliseconds and colons
  const timestamp = new Date()
    .toISOString()
    .replace(/\.\d{3}Z$/, "")
    .replace(/:/g, "-");
  const filename = `${timestamp}.xlsx`;

  XLSX.writeFile(workbook, filename);
});
