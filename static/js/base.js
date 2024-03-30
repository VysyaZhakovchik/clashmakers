let xhr = new XMLHttpRequest();
xhr.open("POST", "/basejs");

xhr.responseType = "json";
xhr.setRequestHeader("Content-Type", "application/json");

xhr.onload = () => {
    rec_data = xhr.response;
    console.log(rec_data);
    html = ``;
    if (rec_data) {
        html += `
        <a href="/profile" class="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-dark text-decoration-none">
            <img src="../static/src/profile.jpg" class="pic">
        </a>`;
    } else {
        html += `<li class="nav-item"><a href="/sign_up" class="nav-link"><p class="header-nav">Sign Up</p></a></li>
        <li class="nav-item"><a href="/login" class="nav-link active" id="login-btn" aria-current="page">Log In</a></li>`;
    }
    document.getElementById("profile").innerHTML = html;
}
let data = JSON.stringify({});
xhr.send(data);