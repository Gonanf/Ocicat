csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value
let button = document.getElementById('logout');
if (button){
  button.onclick = function (e) {
    fetch("/login", {
      method: "DELETE",
      cache: "no-cache",
      credentials: "same-origin",
      headers: { "X-CSRFToken": csrf_token },
    }).then(() => {e.preventDefault(); location.reload()});
  };

}

let publicaciones = document.getElementsByClassName('publicacion');
for (var i = 0; i < publicaciones.length; i++){
  publicaciones[i].onclick = function(a){
    location.href = (location.origin + "/publication_page/view/" + this.id);
  }
}

let buscador = document.getElementById('buscador')
let buscar = document.getElementById('buscar')

buscar.onclick = function(){
  location = (location.origin + "/publication_page/filter/1/title/" + buscador.value + "/recent");
}