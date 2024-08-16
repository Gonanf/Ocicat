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

fetch("/login", {
  method: "GET",
  mode: "cors",
  cache: "no-cache",
  credentials: "same-origin",
  headers: {
    "Content-Type": "application/json",
  },

})
  .then((a) => a.json())
  .then((result_json) => {
    if (result_json.nombre) {
      document.getElementById("nombre").innerHTML = result_json.nombre;
      document.getElementById("container").appendChild(button);
    }
  });

  