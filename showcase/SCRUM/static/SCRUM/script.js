// taskNum = 1;
const wSocket = new WebSocket(
    'ws://127.0.0.1:8000/SCRUM'
    // + window.location.host
    // + '/SCRUM'
);
function on_drag_start(e){
    e.dataTransfer.setData('text/plain', e.target.id);

    e.currentTarget.style.backgroundColor = 'white';
    e.currentTarget.style.border = 'thick solid aqua';
}
function on_dragover(e){
    e.preventDefault();
}
function on_drop(e){
    const id = e.dataTransfer.getData('text');
    const draggableElement = document.getElementById(id);
    draggableElement.style.border = '';
    const dropzone = e.target;
    console.log(e.dataTransfer.getData('text'));
    wSocket.send(JSON.stringify({
        'column': dropzone.id,
        'task': id,
        'new': false,
    }));
    dropzone.appendChild(draggableElement);
    e.dataTransfer.clearData();
}



wSocket.onmessage = function(e){
    alert(e.data);
    return(e.data);
}

wSocket.onclose = function(e){
    console.error('Web Socket Closed');
    console.error(e);
}


window.onload = function(){
    var list = document.getElementsByClassName('add');

    
    function add_item(id, button){
            let item = document.createElement("textarea");
            button.style.display = "none";
            item.setAttribute('id', "t-area")
            let parent = document.getElementById(id);
            item.innerHTML = "added item";
            parent.appendChild(item);
            let input = document.getElementById('t-area');
            input.addEventListener('keypress', function(e){
                if(e.key === 'Enter' && !e.shiftKey){
                    e.preventDefault();
                    var div = document.createElement('div');
                    div.innerHTML = input.value;
                    div.setAttribute('class', 'task');
                    div.setAttribute('draggable', 'true');
                    div.setAttribute('ondragstart', 'on_drag_start(event)');
                    // div.setAttribute('id', 'task'+taskNum);
                    // taskNum++;
                    input.replaceWith(div);
                    button.style.display = "inline";
                    wSocket.send(JSON.stringify({
                        'column': backlog,
                        'name': input.value,
                        'new': true,
                    }))
                    var rec = wSocket.onmessage()
                    div.setAttribute('id', rec);


                    alert(rec)
                }
            })
    }
    for(var i = 0; i < list.length; i++){
        let item = list[i];
        item.onclick = function(){
            flag = add_item(item.parentElement.id, item);
        }
    }
}