// Edit modal population
const editModal = document.getElementById("editModal");
editModal.addEventListener("show.bs.modal", (event) => {
  const dataset = event.relatedTarget.dataset;
  const modal = event.currentTarget;

  // Map dataset keys to corresponding input field IDs
  const fields = ["id", "customer_id", "customer_name"];

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
    const response = await fetch("/customers/update", {
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

      // Notify user of success
      alert("Customer updated successfully!");
    } else {
      alert("Failed to update customer.");
      throw new Error("Failed to update customer.");
    }
  } catch (error) {
    console.error("Error:", error);
    alert(`An error occurred: ${error.message}`);
  }
});
