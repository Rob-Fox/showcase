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