document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("formularioCarga");
    const mariposaId = new URLSearchParams(window.location.search).get('id');
    
    if (mariposaId) {
        document.querySelector(".title-carga").textContent = "Editar mariposa";
        fetchData(`/api/mariposas/${mariposaId}`, "GET", (data) => {
            document.getElementById("nombre").value = data.nombre;
            document.getElementById("especie").value = data.especie;
            document.getElementById("familia").value = data.familia;
            document.getElementById("nombreCientifico").value = data.nombreCientifico;
            document.getElementById("pais").value = data.pais;
            document.getElementById("peligroExtincion").checked = data.peligroExtincion;
            document.getElementById("migratoria").checked = data.migratoria;
        });
    }

    form.addEventListener("submit", (event) => {
        event.preventDefault();
        const formData = {
            nombre: document.getElementById("nombre").value,
            especie: document.getElementById("especie").value,
            familia: document.getElementById("familia").value,
            nombreCientifico: document.getElementById("nombreCientifico").value,
            pais: document.getElementById("pais").value,
            peligroExtincion: document.getElementById("peligroExtincion").checked,
            migratoria: document.getElementById("migratoria").checked
        };

        if (mariposaId) {
            fetchData(`/api/mariposas/${mariposaId}`, "PUT", (data) => {
                alert("Mariposa actualizada correctamente!");
                window.location.href = "gestionbutterflies.html";
            }, formData);
        } else {
            fetchData("/api/mariposas/crear/", "POST", (data) => {
                alert("Mariposa creada correctamente!");
                window.location.href = "gestionbutterflies.html";
            }, formData);
        }
    });
});
