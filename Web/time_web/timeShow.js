setInterval(timeShow, 1000);
function timeShow() {
    var t = new Date();
    
    document.getElementById('main').innerHTML = t.toLocaleString();
}