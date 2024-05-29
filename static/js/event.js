let xhr = new XMLHttpRequest();
xhr.open("POST", "/eventjs");

xhr.responseType = "json";
xhr.setRequestHeader("Content-Type", "application/json");

xhr.onload = () => {
    rec_data = xhr.response;
    console.log(rec_data);
    html = `<h>event_id=${rec_data}</h>`;
    document.getElementById("event_id").innerHTML = html;
}
let data = JSON.stringify({});
xhr.send(data);