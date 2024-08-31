// Add form submission
const addForm = document.getElementById("addForm");
addForm.addEventListener("submit", async function (event) {
  event.preventDefault(); // Prevent the default form submission

  const formData = new FormData(this);
  const data = Object.fromEntries(formData.entries());

  try {
    const response = await fetch("/d_customers/add", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    if (response.ok) {
      // Get the response data
      const response_data = await response.json;
      const id_in_db = response_data.id;
      const customer_name = response_data.customer_name;

      // Add new row to table
      const table = document.getElementById("table-body");
      const newRow = table.insertRow();
      newRow.id = `tr-${id_in_db}`;
      newRow.innerHTML = `
        <td class="id">${id_in_db}</td>
        <td class="customer_name">${customer_name}</td>
        <td>
          <button
            type="button"
            class="btn btn-primary"
            data-bs-toggle="modal"
            data-bs-target="#editModal"
            data-id="${customer_name}"
            data-customer_name="${customer_name}"
          >
            Edit
          </button>
          <button
            type="button"
            class="btn btn-danger"
            data-bs-toggle="modal"
            data-bs-target="#deleteModal"
            data-id="${id_in_db}"
          >
            Delete
          </button>
        </td>
      `;
      // Clear the form
      this.reset();

      // Close the modal
      const modal = bootstrap.Modal.getInstance(addModal);
      modal.hide();

      // Notify user of success
      alert("Customer added successfully!");
    }
  } catch (error) {
    console.error("Error:", error);
    alert(`An error occurred: ${error.message}`);
  }
});

// Edit modal population
const editModal = document.getElementById("editModal");
editModal.addEventListener("show.bs.modal", (event) => {
  const dataset = event.relatedTarget.dataset;
  const modal = event.currentTarget;

  // Map dataset keys to corresponding input field IDs
  const fields = ["id", "customer_name"];

  // Populate modal form fields
  fields.forEach((field) => {
    const input = modal.querySelector(`#edit-${field}`);
    if (input) input.value = dataset[field] || "";
  });
});

// Edit form submission
const editForm = document.getElementById("editForm");
editForm.addEventListener("submit", async function (event) {
  event.preventDefault(); // Prevent the default form submission

  const formData = new FormData(this);
  const data = Object.fromEntries(formData.entries());

  try {
    const response = await fetch("/d_customers/update", {
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
