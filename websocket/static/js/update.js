$(function() {
    var ws_scheme = window.location.protocol === "https:" ? "wss" : "ws";
    var update_socket = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/chat" + window.location.pathname);


    update_socket.onmessage = function(message) {
        let data =JSON.parse(message);
        console.log(data);
    }
});