csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value
let button = document.createElement("button");
button.onclick = function (e) {
    fetch("/login", {
      method: "DELETE",
      cache: "no-cache",
      credentials: "same-origin",
      headers: { "X-CSRFToken": csrf_token },
      body:{
        csrfmiddlewaretoken: '{{ csrf_token }}'
      }
    }).then(() => {e.preventDefault(); location.reload()});
  };
  button.innerHTML = "LOGOUT";

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
  console.log("No esat iniciado sesion");
  
}).then((data) => data).catch((e) => console.log(e))
}

get_login().then((data) => {
  if (data){
  if (data.nombre) {
    document.getElementById("nombre").innerHTML = data.nombre;
    document.getElementById("container").appendChild(button);
  }
}
});
    
  

  