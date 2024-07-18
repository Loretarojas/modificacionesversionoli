document.addEventListener("DOMContentLoaded", () => {
    const container = document.querySelector("#container-tabla-carga");
    let allButterflies = [];

    function showButterflies(butterflies) {
        container.innerHTML = `
            <tr id="encabezado-tabla">
                <th>Nombre</th>
                <th>Especie</th>
                <th>Familia</th>
                <th>Nombre Científico</th>
                <th>País</th>
                <th>Peligro de Extinción</th>
                <th>Especie Migratoria</th>
            </tr>
        `;

        butterflies.forEach((butterfly) => {
            const row = document.createElement("tr");

            row.innerHTML = `
                <td>${butterfly.nombre}</td>
                <td>${butterfly.especie}</td>
                <td>${butterfly.familia}</td>
                <td>${butterfly.nombreCientifico}</td>
                <td>${butterfly.pais}</td>
                <td>${butterfly.peligroExtincion ? "Sí" : "No"}</td>
                <td>${butterfly.migratoria ? "Sí" : "No"}</td>
            `;

            container.appendChild(row);
        });
    }

    fetch("http://localhost:5000/posts")
        .then(response => response.json())
        .then(data => {
            allButterflies = data;
            showButterflies(allButterflies);
        })
        .catch(error => console.error("Error cargando las mariposas:", error));
});
