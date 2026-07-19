const VEHICLE_API = "/api/vehicles/";

function getAccessToken() {
    return localStorage.getItem("access");
}

function showMessage(message, success = true) {
    alert(message);
}

async function deleteVehicle(id) {

    const confirmed = confirm(
        "Are you sure you want to delete this vehicle?\n\nThis action cannot be undone."
    );

    if (!confirmed) {
        return;
    }

    try {

        const response = await fetch(
            VEHICLE_API + id + "/delete/",
            {
                method: "DELETE",
                headers: {
                    "Authorization": "Bearer " + getAccessToken(),
                    "Content-Type": "application/json"
                }
            }
        );

        if (response.ok) {

            showMessage("Vehicle deleted successfully.");

            location.reload();

        } else {

            const data = await response.json();

            showMessage(
                data.detail || "Unable to delete vehicle.",
                false
            );

        }

    } catch (error) {

        showMessage(
            "Network error while deleting vehicle.",
            false
        );

        console.error(error);

    }

}

async function purchaseVehicle(id) {

    const confirmed = confirm(
        "Are you sure you want to purchase this vehicle?"
    );

    if (!confirmed) {
        return;
    }

    const purchaseButton = event.target;

    const originalText = purchaseButton.innerHTML;

    purchaseButton.disabled = true;
    purchaseButton.innerHTML = "Processing...";

    try {

        const response = await fetch(
            VEHICLE_API + id + "/purchase/",
            {
                method: "POST",
                headers: {
                    "Authorization": "Bearer " + getAccessToken(),
                    "Content-Type": "application/json"
                }
            }
        );

        const data = await response.json();

        if (response.ok) {

            showMessage(data.message);

            location.reload();

        } else {

            showMessage(
                data.error || "Purchase failed.",
                false
            );

            purchaseButton.disabled = false;
            purchaseButton.innerHTML = originalText;

        }

    } catch (error) {

        showMessage(
            "Network error while purchasing vehicle.",
            false
        );

        purchaseButton.disabled = false;
        purchaseButton.innerHTML = originalText;

        console.error(error);

    }

}

async function restockVehicle(id, quantity) {

    quantity = parseInt(quantity);

    if (isNaN(quantity) || quantity <= 0) {

        showMessage(
            "Please enter a valid quantity.",
            false
        );

        return;

    }

    try {

        const response = await fetch(
            VEHICLE_API + id + "/restock/",
            {
                method: "POST",
                headers: {
                    "Authorization": "Bearer " + getAccessToken(),
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    quantity: quantity
                })
            }
        );

        const data = await response.json();

        if (response.ok) {

            showMessage(data.message);

            location.reload();

        } else {

            showMessage(
                data.detail ||
                data.error ||
                "Restock failed.",
                false
            );

        }

    } catch (error) {

        showMessage(
            "Network error while restocking vehicle.",
            false
        );

        console.error(error);

    }

}