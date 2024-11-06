// Obtención de datos desde las etiquetas script
const edadData = JSON.parse(document.getElementById('edadData').textContent);
const generoData = JSON.parse(document.getElementById('generoData').textContent);
const probabilidadData = JSON.parse(document.getElementById('probabilidadData').textContent);

// Gráfico de Distribución de Edad
new Chart(document.getElementById('edadChart'), {
    type: 'bar',
    data: {
        labels: Array.from({ length: edadData.length }, (_, i) => i + 1),  // Etiquetas para las edades
        datasets: [{
            label: 'Distribución de Edad de Pacientes',
            data: edadData,
            backgroundColor: 'rgba(54, 162, 235, 0.5)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: { 
                beginAtZero: true,
                ticks: {
                    callback: function(value) {
                        return value + ' años';  // Añade 'años' a los valores en el eje y
                    }
                }
            }
        }
    }
});

// Gráfico de Probabilidad de Cáncer por Género (Histograma)
new Chart(document.getElementById('probabilidadHistogramaChart'), {
    type: 'bar',
    data: {
        labels: ['0-25%', '26-50%', '51-75%', '76-100%'],  // Intervalos de probabilidad
        datasets: [{
            label: 'Distribución de Probabilidad de Cáncer',
            data: probabilidadData,  // Datos de las probabilidades de cáncer
            backgroundColor: 'rgba(75, 192, 192, 0.5)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: { 
                beginAtZero: true,
                ticks: {
                    callback: function(value) {
                        return value + ' Pacientes';  // Añade 'Pacientes' a los valores en el eje y
                    }
                }
            }
        }
    }
});

// Gráfico de Distribución de Género y Probabilidad de Cáncer (Torta)
new Chart(document.getElementById('generoProbabilidadTortaChart'), {
    type: 'pie',
    data: {
        labels: ['Hombres', 'Mujeres'],  // Distribución por género
        datasets: [{
            label: 'Promedio de Probabilidad de Cáncer por Género',
            data: generoData,
            backgroundColor: ['rgba(75, 192, 192, 0.5)', 'rgba(255, 99, 132, 0.5)']
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                display: true,
                position: 'top',
            },
            tooltip: {
                callbacks: {
                    label: function(context) {
                        return context.label + ': ' + context.raw.toFixed(2) + '%'; // Mostrar porcentaje
                    }
                }
            }
        }
    }
});


