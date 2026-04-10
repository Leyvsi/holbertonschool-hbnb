document.addEventListener('DOMContentLoaded', () => {
    setupLogin();
    checkAuthIndex();
    handlePlacePage();
    handleReviewPage();

    const filter = document.getElementById('price-filter');
    if (filter) filter.addEventListener('change', filterPlaces);
});

let allPlaces = [];

/* ================= AUTH ================= */

function getCookie(name) {
    const cookies = document.cookie.split('; ');
    for (let c of cookies) {
        const [k, v] = c.split('=');
        if (k === name) return v;
    }
    return null;
}

/* ================= LOGIN ================= */

function setupLogin() {
    const form = document.getElementById('login-form');

    if (!form) return;

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        const res = await fetch('http://127.0.0.1:5000/api/v1/auth/login', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ email, password })
        });

        if (res.ok) {
            const data = await res.json();
            document.cookie = `token=${data.access_token}; path=/`;
            window.location.href = 'index.html';
        } else {
            document.getElementById('error-message').textContent = "Login failed";
        }
    });
}

/* ================= INDEX ================= */

function checkAuthIndex() {
    const token = getCookie('token');
    const login = document.getElementById('login-link');

    if (!login) return;

    if (!token) login.style.display = 'block';
    else {
        login.style.display = 'none';
        fetchPlaces(token);
    }
}

async function fetchPlaces(token) {
    const res = await fetch('http://127.0.0.1:5000/api/v1/places', {
        headers: { Authorization: `Bearer ${token}` }
    });

    const data = await res.json();
    allPlaces = data;
    displayPlaces(allPlaces);
}

function displayPlaces(places) {
    const container = document.getElementById('places-list');
    if (!container) return;

    container.innerHTML = '';

    places.forEach(p => {
        const div = document.createElement('div');
        div.className = 'place-card';

        div.innerHTML = `
            <h2>${p.name}</h2>
            <p>$${p.price_per_night}</p>
            <a class="details-button" href="place.html?id=${p.id}">View Details</a>
        `;

        container.appendChild(div);
    });
}

function filterPlaces() {
    const val = document.getElementById('price-filter').value;

    if (val === 'all') return displayPlaces(allPlaces);

    const filtered = allPlaces.filter(p => p.price_per_night <= val);
    displayPlaces(filtered);
}

/* ================= PLACE DETAILS ================= */

function getPlaceId() {
    return new URLSearchParams(window.location.search).get('id');
}

function handlePlacePage() {
    const id = getPlaceId();
    const token = getCookie('token');

    if (!id) return;

    if (token) {
        document.getElementById('add-review').style.display = 'block';
    }

    fetch(`http://127.0.0.1:5000/api/v1/places/${id}`, {
        headers: token ? { Authorization: `Bearer ${token}` } : {}
    })
    .then(r => r.json())
    .then(displayPlace);
}

function displayPlace(p) {
    const container = document.getElementById('place-details');

    container.innerHTML = `
        <div class="place-card">
            <h1>${p.name}</h1>
            <p>${p.description}</p>
            <p>$${p.price_per_night}</p>
            <p>Amenities: ${p.amenities?.join(', ')}</p>
        </div>

        <h3>Reviews</h3>
    `;

    (p.reviews || []).forEach(r => {
        const div = document.createElement('div');
        div.className = 'review-card';

        div.innerHTML = `
            <p>${r.text}</p>
            <p>${r.rating}/5</p>
        `;

        container.appendChild(div);
    });
}

/* ================= REVIEW ================= */

function handleReviewPage() {
    const form = document.getElementById('review-form');
    if (!form) return;

    const token = getCookie('token');
    const id = getPlaceId();

    if (!token) window.location.href = 'index.html';

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const text = document.getElementById('review-text').value;
        const rating = document.getElementById('review-rating').value;

        const res = await fetch(`http://127.0.0.1:5000/api/v1/places/${id}/reviews`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                Authorization: `Bearer ${token}`
            },
            body: JSON.stringify({ text, rating })
        });

        const msg = document.getElementById('message');

        if (res.ok) {
            msg.style.color = 'green';
            msg.textContent = "Review added!";
            form.reset();
        } else {
            msg.style.color = 'red';
            msg.textContent = "Error";
        }
    });
}
