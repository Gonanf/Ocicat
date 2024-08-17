function get_login() { return fetch("/login", {
    method: "GET",
    mode: "cors",
    cache: "no-cache",
    credentials: "same-origin",
    headers: {
      "Content-Type": "application/json",
    },
  }).then((a) => {
    if (a.status != 404){
      return a.json()
    }
    console.log("No esta iniciado sesion");
    
  }).then((data) => data).catch((e) => console.log(e))
  }

  csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value

console.log(location.href, location.origin, location.pathname)

function create_container(){
  let files = document.getElementById("files");
  let container = document.createElement("div");
  let delete_button = document.createElement("button");
  delete_button.innerHTML = "Eliminar";
  delete_button.onclick = function(){
    if (this.parentElement.previousElementSibling || this.parentElement.nextElementSibling){
      this.parentElement.parentElement.removeChild(this.parentElement);

    }
  }
  let mover_arriba = document.createElement("button");
  mover_arriba.innerHTML = "Mover arriba";
  mover_arriba.onclick = function(){
    if (this.parentElement.previousElementSibling && this.parentElement.previousElementSibling.id != "files"){
      this.parentElement.parentNode.insertBefore(this.parentElement, this.parentElement.previousElementSibling)
    }
  }
  let mover_abajo = document.createElement("button");
  mover_abajo.innerHTML = "Mover abajo";
  mover_abajo.onclick = function(){
    if (this.parentElement.nextElementSibling && this.parentElement.nextElementSibling.id != "enviar"){
      this.parentElement.parentNode.insertBefore(this.parentElement.nextElementSibling, this.parentElement)
    }
  }
  let file = document.createElement("input");
  file.type = "file";
  file.classList.add("archivos");
  file.addEventListener('input', function (e) {
    console.log(this.parentElement.nextElementSibling, this.parentElement, this);
    if (this.parentElement.nextElementSibling == null ){
      create_container();
    }
});

  container.append(delete_button,mover_arriba,mover_abajo,file);
  files.appendChild(container);
}
  create_container();

