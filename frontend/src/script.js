const API_URL = '/api/users/';

async function fetchUsers() {
    const res = await fetch(API_URL);
    const users = await res.json();
    const table = document.getElementById('usersTable');
    table.innerHTML = '';

    users.forEach(user => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${user.id}</td>
            <td>${user.username}</td>
            <td>${user.public_key}</td>
            <td><a href="${user.config_file}" target="_blank">Download</a></td>
            <td><canvas class="qr"></canvas></td>
        `;
        table.appendChild(tr);

        const qr = new QRious({
            element: tr.querySelector('canvas'),
            value: fetchConfig(user.config_file),
            size: 100
        });
    });
}

async function fetchConfig(url) {
    const res = await fetch(url);
    if (!res.ok) return '';
    return await res.text();
}

document.getElementById('addUserForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const res = await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username })
    });

    if (res.ok) {
        document.getElementById('username').value = '';
        fetchUsers();
    } else {
        alert('Error adding user');
    }
});

fetchUsers();
