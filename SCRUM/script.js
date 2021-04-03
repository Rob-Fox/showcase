taskNum = 1;
function on_drag_start(e){
    e.dataTransfer.setData('text/plain', e.target.id);

    e.currentTarget.style.backgroundColor = 'white';
}
function on_dragover(e){
    e.preventDefault();
}
function on_drop(e){
    const id = e.dataTransfer.getData('text');
    console.log(e.dataTransfer);
    const draggableElement = document.getElementById(id);
    console.log(draggableElement);
    const dropzone = e.target;
    dropzone.appendChild(draggableElement);
    e.dataTransfer.clearData();
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
                    div.setAttribute('id', 'task'+taskNum);
                    taskNum++;
                    input.replaceWith(div);
                    button.style.display = "inline";
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