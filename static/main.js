var socket = io();

function currTime() {
    socket.emit('ask-time')
}
socket.on('get-time', (data) => {
    document.getElementById('area1').innerHTML = data;
})


function clients() {
    socket.emit('ask-clients')
}
socket.on('get-clients', (data) => {
    document.getElementById('area2').innerHTML = data;
})


function age() {
    socket.emit('ask-age')
}
socket.on('get-age', (data) => {
    document.getElementById('area3').innerHTML = data;
})

socket.on('push-connect', (data) => {
    var val = document.getElementById('area1').innerHTML;
    document.getElementById('area1').innerHTML = val + data;
})

socket.on('get-time', (data) => {
    document.getElementById('area1').innerHTML = data;
})