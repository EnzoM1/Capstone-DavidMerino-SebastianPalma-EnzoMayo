
        
        document.addEventListener('DOMContentLoaded', function () {
            // 1. Gráfico de Distribución por Género
            // Extraer los datos de género y probabilidad promedio
            var labelsGenero = generoData.map(function(item) {
                return item.Genero;
            });
            var countGenero = generoData.map(function(item) {
                return item.count;
            });
            var avgProbGenero = generoData.map(function(item) {
                return item.avg_probabilidad;
            });

            // Crear gráfico de torta
            var ctx = document.getElementById('generoChart').getContext('2d');
            var generoChart = new Chart(ctx, {
                type: 'pie',  // Cambiar a 'pie' para gráfico de torta
                data: {
                    labels: labelsGenero,  // Género como etiquetas (H, M)
                    datasets: [{
                        label: 'Distribución por Género',
                        data: avgProbGenero,  // Usar la probabilidad promedio de cáncer
                        backgroundColor: ['rgba(75, 192, 192, 0.6)', 'rgba(153, 102, 255, 0.6)'],
                        borderColor: ['rgba(75, 192, 192, 1)', 'rgba(153, 102, 255, 1)'],
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            position: 'top', // Colocar la leyenda en la parte superior
                        },
                        tooltip: {
                            callbacks: {
                                label: function(tooltipItem) {
                                    var total = tooltipItem.dataset.data.reduce(function(previousValue, currentValue) {
                                        return previousValue + currentValue;
                                    });
                                    var currentValue = tooltipItem.raw;
                                    var percentage = Math.floor(((currentValue / total) * 100) + 0.5);         
                                    return tooltipItem.label + ': ' + percentage + '%';  // Mostrar el porcentaje en el tooltip
                                }
                            }
                        }
                    }
                }
            });

            // 2. Gráfico Promedio de Probabilidad por Edad
            var edadChart = new Chart(document.getElementById('edadChart'), {
                type: 'line',
                data: {
                    labels: edadData.map(function(item) { return item.Edad; }),
                    datasets: [{
                        label: 'Promedio de Probabilidad de Cáncer por Edad',
                        data: edadData.map(function(item) { return item.promedio_probabilidad; }),
                        borderColor: 'rgba(255, 99, 132, 1)',
                        fill: false
                    }]
                }
            });

            // 3. Gráfico de Relación entre Tabaquismo y Probabilidad
            var alcoholChart  = new Chart(document.getElementById('alcoholChart'), {
                type: 'scatter', // Cambiado a 'scatter' para un gráfico de puntos
                data: {
                    datasets: [{
                        label: 'Relación Consumo de alcohol y Probabilidad',
                        data: alcoholData.map(function(item) {
                            return { x: item.Consumo_de_alcohol, y: item.promedio_probabilidad }; // Eje X: Dedos_amarillos, Eje Y: promedio_probabilidad
                        }),
                        backgroundColor: 'rgba(54, 162, 235, 0.2)', // Color de los puntos
                        borderColor: 'rgba(54, 162, 235, 1)', // Color del borde de los puntos
                        borderWidth: 1,
                        pointRadius: 5 // Tamaño de los puntos
                    }]
                },
                options: {
                    scales: {
                        x: {
                            title: {
                                display: true,
                                text: 'Consumo de alcohol' // Etiqueta para el eje X
                            },
                            ticks: {
                                beginAtZero: true,
                                stepSize: 1 // Para que se vea de manera clara entre los valores 0 y 1
                            }
                        },
                        y: {
                            title: {
                                display: true,
                                text: 'Promedio de Probabilidad' // Etiqueta para el eje Y
                            }
                        }
                    }
                }
            });

            // 4. Gráfico de Pacientes con Tos y su Probabilidad
            var tosChart = new Chart(document.getElementById('tosChart'), {
                type: 'bar',
                data: {
                    labels: tosProbabilidadData.map(function(item) { return item.Tos == 1 ? 'Sí' : 'No'; }),
                    datasets: [{
                        label: 'Pacientes con Tos y su Probabilidad',
                        data: tosProbabilidadData.map(function(item) { return item.promedio_probabilidad; }),
                        backgroundColor: 'rgba(255, 159, 64, 0.2)',
                        borderColor: 'rgba(255, 159, 64, 1)',
                        borderWidth: 1
                    }]
                }
            });
        });