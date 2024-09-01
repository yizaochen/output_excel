// Excel generation
document.getElementById("generate-excel").addEventListener("click", () => {
  const data = Array.from(document.querySelectorAll("table tr")).map((row) =>
    Array.from(row.querySelectorAll("th, td")).map((cell) => cell.innerText)
  );

  const worksheet = XLSX.utils.aoa_to_sheet(data);
  const workbook = XLSX.utils.book_new();
  XLSX.utils.book_append_sheet(workbook, worksheet, "Transactions");

  const timestamp = new Date().toISOString().slice(0, 19).replace(/:/g, "-");
  const filename = `${timestamp}.xlsx`;

  XLSX.writeFile(workbook, filename);
});

// Edit modal population
const editModal = document.getElementById("editModal");
editModal.addEventListener("show.bs.modal", (event) => {
  const dataset = event.relatedTarget.dataset;
  const modal = event.currentTarget;

  // Map dataset keys to corresponding input field IDs
  const fields = [
    "id",
    "bank_slip_date",
    "customer_id",
    "bank_code",
    "bank_slip_currency",
    "bank_slip_amount",
    "customer_name",
    "bank_slip_customer",
    "country",
    "file_path",
    "predict_type",
    "process_status",
    "reference_number",
    "remit_type",
    "bank_slip_remark",
    "change_date",
    "ar_no",
  ];

  // Populate modal form fields
  fields.forEach((field) => {
    const input = modal.querySelector(`#edit-${field}`);
    if (input) input.value = dataset[field] || "";
  });
});

const editForm = document.getElementById("editForm");
editForm.addEventListener("submit", async function (event) {
  event.preventDefault(); // Prevent the default form submission

  const formData = new FormData(this);
  const data = Object.fromEntries(formData.entries());

  try {
    const response = await fetch("/transactions/update", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    if (response.ok) {
      // Update table row with new data
      const tr = document.getElementById(`tr-${data.id}`);
      if (tr) {
        Object.keys(data).forEach((key) => {
          const cell = tr.querySelector(`.${key}`);
          if (cell) cell.textContent = data[key];
        });
      }

      // Close the modal
      const modal = bootstrap.Modal.getInstance(editModal);
      modal.hide();
    } else {
      alert("Failed to update transaction.");
      throw new Error("Failed to update transaction.");
    }
  } catch (error) {
    console.error("Error:", error);
    alert(`An error occurred: ${error.message}`);
  }
});
