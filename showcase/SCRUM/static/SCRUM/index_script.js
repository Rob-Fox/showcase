// taskNum = 1;
const wSocket = new WebSocket(
    'ws://127.0.0.1:8000/SCRUM'
    // + window.location.host
    // + '/SCRUM'
);

wSocket.onmessage = function(e){
    alert(e.data);
    return(e.data);
}

wSocket.onclose = function(e){
    console.error('Web Socket Closed');
    console.error(e);
}


window.onload = function(){

    
    function add_item(id, button){
            wSocket.send(JSON.stringify({
                    'column': backlog,
                    'name': input.value,
                    'new': true,
                }))
                var rec = wSocket.onmessage()
    }
}