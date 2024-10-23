csrf_token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

document.getElementById("eliminar").onclick = function () {
  let active = document.querySelector(".active");
  active.parentElement.removeChild(active);
  let new_ac = document.querySelector(".carousel-item");
  new_ac.classList += " active";
};

document.getElementById("añadir").onclick = function () {
  let container = document.createElement("div");
  let button = document.createElement("button");
  let img = document.createElement("img");
  img.classList += "dblock w-10";
  let filefield = document.createElement("input");
  filefield.type = "file";
  filefield.hidden = true;
  button.appendChild(img);
  container.appendChild(button);
  container.appendChild(filefield);
  container.classList += "carousel-item";

  let file = document.getElementById("files");
  file.appendChild(container);
};
function create_container() {
  let files = document.getElementById("files");
  let container = document.createElement("div");
  let delete_button = document.createElement("button");
  delete_button.innerHTML = "Eliminar";
  delete_button.onclick = function () {
    if (
      this.parentElement.previousElementSibling ||
      this.parentElement.nextElementSibling
    ) {
      this.parentElement.parentElement.removeChild(this.parentElement);
    }
  };
  let mover_arriba = document.createElement("button");
  mover_arriba.innerHTML = "Mover arriba";
  mover_arriba.onclick = function () {
    if (
      this.parentElement.previousElementSibling &&
      this.parentElement.previousElementSibling.id != "files"
    ) {
      this.parentElement.parentNode.insertBefore(
        this.parentElement,
        this.parentElement.previousElementSibling,
      );
    }
  };
  let mover_abajo = document.createElement("button");
  mover_abajo.innerHTML = "Mover abajo";
  mover_abajo.onclick = function () {
    if (
      this.parentElement.nextElementSibling &&
      this.parentElement.nextElementSibling.id != "enviar"
    ) {
      this.parentElement.parentNode.insertBefore(
        this.parentElement.nextElementSibling,
        this.parentElement,
      );
    }
  };
  let file = document.createElement("input");
  file.type = "file";
  file.classList.add("archivos");
  file.addEventListener("input", function (e) {
    console.log(
      this.parentElement.nextElementSibling,
      this.parentElement,
      this,
    );
    if (this.parentElement.nextElementSibling == null) {
      create_container();
    }
  });

  container.append(delete_button, mover_arriba, mover_abajo, file);
  files.appendChild(container);
}

document.getElementById("enviar").onclick = function () {
  let titulo = document.getElementById("titulo");
  let descripcion = document.getElementById("descripcion");
  let portada = document.getElementById("portada");
  let categorias = document.getElementById("categoria");
  let archivos = document.querySelectorAll('input[type="file"].archivos');
  let archivos_filtrados = Array();
  for (let i = 0; i < archivos.length; i++) {
    if (archivos[i].files.length > 0) {
      archivos_filtrados.push(archivos[i].files[0]);
    }
  }
  let categorias_filtradas = Array();
  for (let i = 0; i < categorias.options.length; i++) {
    console.log();
    if (categorias.options[i].selected) {
      categorias_filtradas.push(categorias.options[i].value);
    }
  }
  let form = new FormData();
  form.append("titulo", titulo.value);
  form.append("descripcion", descripcion.value);
  form.append("portada", portada.files[0]);
  form.append("categorias", categorias_filtradas);
  archivos_filtrados.forEach((a) => form.append("archivos[]", a));
  fetch("/publication", {
    method: "POST",
    cache: "no-cache",
    credentials: "same-origin",
    headers: { "X-CSRFToken": csrf_token },
    body: form,
  })
    .then((a) => {
      if (a.status != 404) {
        location.href = a.url;
      } else {
        console.log("ERROR");
      }
    })
    .catch((e) => console.log(e));
};
