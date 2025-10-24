const API_URL = "/api/users";

async function fetchUsers() {
    const res = await fetch(API_URL);
    const users = await res.json();
    const tbody = document.querySelector("#usersTable tbody");
    tbody.innerHTML = "";
    users.forEach(u => {
        const tr = document.createElement("tr");
        tr.innerHTML = `
            <td>${u.id}</td>
            <td><input value="${u.username}" onchange="updateUser(${u.id}, this.value)"></td>
            <td><input type="checkbox" ${u.active ? "checked" : ""} onchange="toggleActive(${u.id}, this.checked)"></td>
            <td><button onclick="deleteUser(${u.id})">Delete</button></td>
        `;
        tbody.appendChild(tr);
    });
}

async function addUser() {
    const username = document.getElementById("newUsername").value;
    const vpnKey = document.getElementById("newVpnKey").value;
    await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, vpn_key: vpnKey })
    });
    document.getElementById("newUsername").value = "";
    document.getElementById("newVpnKey").value = "";
    fetchUsers();
}

async function updateUser(id, username) {
    await fetch(`${API_URL}/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username })
    });
}

async function toggleActive(id, active) {
    await fetch(`${API_URL}/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ active })
    });
}

async function deleteUser(id) {
    await fetch(`${API_URL}/${id}`, { method: "DELETE" });
    fetchUsers();
}

// Initial load
fetchUsers();
