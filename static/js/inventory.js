document.addEventListener("DOMContentLoaded", () => {

    const token = localStorage.getItem("access");

    // ===========================
    // ADD VEHICLE
    // ===========================

    const addVehicleForm = document.getElementById("addVehicleForm");

    if (addVehicleForm) {

        addVehicleForm.addEventListener("submit", async (e) => {

            e.preventDefault();

            const formData = new FormData();

            formData.append(
                "make",
                document.getElementById("make").value
            );

            formData.append(
                "model",
                document.getElementById("model").value
            );

            formData.append(
                "category",
                document.getElementById("category").value
            );

            formData.append(
                "price",
                document.getElementById("price").value
            );

            formData.append(
                "quantity",
                document.getElementById("quantity").value
            );

            const image = document.getElementById("image").files[0];

            if (image) {

                formData.append(
                    "image",
                    image
                );

            }

            try {

                const response = await fetch(
                    "/api/vehicles/",
                    {
                        method: "POST",
                        headers: {
                            "Authorization": `Bearer ${token}`
                        },
                        body: formData
                    }
                );

                if (response.ok) {

                    alert("Vehicle added successfully.");

                    window.location.href = "/dashboard/";

                } else {

                    const error = await response.json();

                    alert(JSON.stringify(error, null, 2));

                }

            } catch (err) {

                console.error(err);

                alert("Unable to connect to the server.");

            }

        });

    }

    // ===========================
    // EDIT VEHICLE
    // ===========================

    const editVehicleForm = document.getElementById("editVehicleForm");

    if (editVehicleForm) {

        editVehicleForm.addEventListener("submit", async (e) => {

            e.preventDefault();

            const vehicleId = editVehicleForm.dataset.vehicleId;

            const formData = new FormData();

            formData.append(
                "make",
                document.getElementById("make").value
            );

            formData.append(
                "model",
                document.getElementById("model").value
            );

            formData.append(
                "category",
                document.getElementById("category").value
            );

            formData.append(
                "price",
                document.getElementById("price").value
            );

            formData.append(
                "quantity",
                document.getElementById("quantity").value
            );

            const image = document.getElementById("image").files[0];

            if (image) {

                formData.append(
                    "image",
                    image
                );

            }

            try {

                const response = await fetch(
                    `/api/vehicles/${vehicleId}/`,
                    {
                        method: "PUT",
                        headers: {
                            "Authorization": `Bearer ${token}`
                        },
                        body: formData
                    }
                );

                if (response.ok) {

                    alert("Vehicle updated successfully.");

                    window.location.href = "/dashboard/";

                } else {

                    const error = await response.json();

                    alert(JSON.stringify(error, null, 2));

                }

            } catch (err) {

                console.error(err);

                alert("Unable to connect to the server.");

            }

        });

    }

});