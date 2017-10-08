$(function () {
    let ws_scheme = window.location.protocol === "https:" ? "wss" : "ws";
    let update_socket = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/dashboard" + window.location.pathname);

    let visit_template = [
        '<tr>',
        '<td>$ip</td>',
        '<td>$browser</td>',
        '<td>$os</td>',
        '<td>$date</td>',
        '</tr>',
    ]

    update_socket.onmessage = function (message) {
        let data = JSON.parse(message.data);
        console.log(data);
        if (data.type === 'view') {
            $('#placeholder').remove();

            let template = visit_template.join('')
                .replace('$ip', data.ip)
                .replace('$browser', data.browser)
                .replace('$os', data.os)
                .replace('$date', data.date);

            $('#visits').prepend(template);
        }
    }
});