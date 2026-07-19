const API_BASE = "/api/auth/";

function saveTokens(data) {

    localStorage.setItem("access", data.access);
    localStorage.setItem("refresh", data.refresh);

}

function logout() {

    localStorage.removeItem("access");
    localStorage.removeItem("refresh");

    window.location.href = "/login/";

}

const loginForm = document.getElementById("loginForm");

if (loginForm) {

    loginForm.addEventListener("submit", async function (e) {

        e.preventDefault();

        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        const response = await fetch(API_BASE + "login/", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                username,
                password

            })

        });

        const data = await response.json();

        if (response.ok) {

            saveTokens(data);

            window.location.href = "/dashboard/";

        }

        else {

            alert("Invalid Username or Password");

        }

    });

}

const registerForm = document.getElementById("registerForm");

if (registerForm) {

    registerForm.addEventListener("submit", async function (e) {

        e.preventDefault();

        const username = document.getElementById("reg_username").value;
        const email = document.getElementById("reg_email").value;
        const password = document.getElementById("reg_password").value;

        const response = await fetch(API_BASE + "register/", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                username,
                email,
                password

            })

        });

        if (response.status === 201) {

            alert("Registration Successful");

            window.location.href = "/login/";

        }

        else {

            const data = await response.json();

            alert(JSON.stringify(data));

        }

    });

}

const logoutBtn = document.getElementById("logoutBtn");

if (logoutBtn) {

    logoutBtn.addEventListener("click", logout);

}