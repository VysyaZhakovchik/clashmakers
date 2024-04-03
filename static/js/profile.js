let xhr = new XMLHttpRequest();
xhr.open("POST", "/profilejs");

xhr.responseType = "json";
xhr.setRequestHeader("Content-Type", "application/json");

xhr.onload = () => {
    rec_data = xhr.response;
    console.log(rec_data);
    html = `
    <div class="coins">
        <img src="../static/src/coin.png" alt="" class="coin">
        <b>${rec_data[0][2]}</b> ClashCoins
    </div>
    <div id="avatar">
        <img src="../static/src/profile.jpg" alt="" class="">
    </div>
    <div id="usertitle">
        <h2>${rec_data[0][0]}</h2>
    </div>
    <div id="mail">
        <h4>${rec_data[0][1]}</h4>
    </div>`;
    document.getElementById("profiledata").innerHTML = html;
}
let data = JSON.stringify({});
xhr.send(data);