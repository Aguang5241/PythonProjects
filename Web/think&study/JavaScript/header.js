$(document).ready(function() {
    setInterval(showTime, 1000);
    function showTime() {
        var t = new Date();
        $('#showTime').text(t.toLocaleString());
    }
})
