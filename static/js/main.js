let xhr = new XMLHttpRequest();
xhr.open("POST", "/mainjs");

xhr.responseType = "json";
xhr.setRequestHeader("Content-Type", "application/json");

xhr.onload = () => {
    rec_data = xhr.response;
    console.log(rec_data);
    html = ``;
    if (rec_data.length > 0) {
        for (let i = 0; i < rec_data.length; i++) {
            html += `
            <div class="bet">
                <h2>${rec_data[i][0]} ${rec_data[i][4]}:${rec_data[i][5]} ${rec_data[i][1]}</h2>
                <h3>${rec_data[i][3]}</h3>
                <h5>${rec_data[i][2]}</h5>
                <button class="bet_button">Make a bet!</button>
                <p class="not_started">Not Started</p>
            </div>`;
        }
    }
    document.getElementById("bets").innerHTML = html;
}
let data = JSON.stringify({});
xhr.send(data);