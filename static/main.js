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


socket.on('status', (data) => {
    const para = document.createElement("p");
    const node = document.createTextNode(data);
    para.appendChild(node);

    const element = document.getElementById('status');
    element.appendChild(para);

})
