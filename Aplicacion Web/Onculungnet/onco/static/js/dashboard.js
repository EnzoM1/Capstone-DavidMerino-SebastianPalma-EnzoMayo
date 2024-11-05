// static/tu_app/js/dashboard.js

// Recoge los datos de edades y probabilidades desde el contexto Django
const edadData = JSON.parse(document.getElementById('edadData').textContent);
const probabilidadData = JSON.parse(document.getElementById('probabilidadData').textContent);

// Gráfico de Edades
const ctxEdad = document.getElementById('edadChart').getContext('2d');
new Chart(ctxEdad, {
    type: 'bar',
    data: {
        labels: Array.from({ length: edadData.length }, (_, i) => i + 1),
        datasets: [{
            label: 'Edad de Pacientes',
            data: edadData,
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: { beginAtZero: true }
        }
    }
});

// Gráfico de Probabilidades de Cáncer
const ctxProbabilidad = document.getElementById('probabilidadChart').getContext('2d');
new Chart(ctxProbabilidad, {
    type: 'line',
    data: {
        labels: Array.from({ length: probabilidadData.length }, (_, i) => i + 1),
        datasets: [{
            label: 'Probabilidad de Cáncer (%)',
            data: probabilidadData,
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: { beginAtZero: true, max: 100 }
        }
    }
});


// Gráfico de Torta para probabilidades por género
const promedioHombres = (edadData.length ? edadData.filter((_, index) => index % 2 === 0).reduce((a, b) => a + b, 0) / (edadData.length / 2) : 0);
const promedioMujeres = (edadData.length ? edadData.filter((_, index) => index % 2 !== 0).reduce((a, b) => a + b, 0) / (edadData.length / 2) : 0);

const ctxGenero = document.getElementById('generoChart').getContext('2d');
new Chart(ctxGenero, {
    type: 'pie',
    data: {
        labels: ['Hombres', 'Mujeres'],
        datasets: [{
            label: 'Promedio de Probabilidad de Cáncer de Pulmón',
            data: [promedioHombres, promedioMujeres],
            backgroundColor: ['rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)'],
            borderColor: ['rgba(255, 99, 132, 1)', 'rgba(54, 162, 235, 1)'],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            }
        }
    }
});