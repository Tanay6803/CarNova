const VEHICLE_API = "/api/vehicles/";

function getAccessToken() {

    return localStorage.getItem("access");

}

async function deleteVehicle(id) {

    if (!confirm("Delete this vehicle?")) {

        return;

    }

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

        alert("Vehicle Deleted Successfully");

        location.reload();

    }

    else {

        alert("Unable to delete vehicle.");

    }

}

async function purchaseVehicle(id) {

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

        alert(data.message);

        location.reload();

    }

    else {

        alert(data.error || "Purchase Failed");

    }

}

async function restockVehicle(id, quantity) {

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

        alert(data.message);

        location.reload();

    }

    else {

        alert(data.detail || "Restock Failed");

    }

}