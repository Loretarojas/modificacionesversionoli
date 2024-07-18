let submitButton = document.querySelector("#form-carga #crear-boton");

submitButton.addEventListener("click", (event) => {
    event.preventDefault();

    let mariposa_nueva = {
        'nombre': document.querySelector("#form-carga #nombre").value,
        'especie': document.querySelector("#form-carga #especie").value,
        'familia': document.querySelector("#form-carga #familia").value,
        'nombreCientifico': document.querySelector("#form-carga #nombreCientifico").value,
        'pais': document.querySelector("#form-carga #pais").value,
        'peligroExtincion': document.querySelector("#form-carga #peligroExtincion").checked,
        'migratoria': document.querySelector("#form-carga #migratoria").checked
    }

    fetchData("http://localhost:5000/api/mariposas/crear/", "POST", (data) => {
        document.querySelector("#form-carga").reset();
        window.location.replace("../gestionbutterflies.html");
    }, mariposa_nueva);
});
