document.addEventListener('DOMContentLoaded', function() {
    // 1. Récupérer les valeurs des cartes dynamiquement
    const redValue = parseInt(document.querySelector('.card.red .value').textContent);
    const greenValue = parseInt(document.querySelector('.card.green .value').textContent);
    const blueValue = parseInt(document.querySelector('.card.blue .value').textContent);
    const yellowValue = parseInt(document.querySelector('.card.yellow .value').textContent);

    const dataValues = [redValue, greenValue, blueValue, yellowValue];

    const ctx = document.getElementById('wasteHistogram').getContext('2d');

    // Assurez-vous que l'instance de Chart est détruite avant d'en créer une nouvelle si elle existe déjà
    // Ceci est important si vous aviez un mécanisme de re-création de chart ailleurs
    if (window.wasteChart instanceof Chart) {
        window.wasteChart.destroy();
    }

    window.wasteChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Red', 'Green', 'Blue', 'Yellow'],
            datasets: [{
                label: 'Waste Quantity',
                data: dataValues, // Utilise les valeurs récupérées dynamiquement
                backgroundColor: [
                    'rgba(220, 53, 69, 0.7)',   // Red (légèrement transparent pour mode clair)
                    'rgba(40, 167, 69, 0.7)',  // Green
                    'rgba(0, 123, 255, 0.7)',  // Blue
                    'rgba(255, 193, 7, 0.7)'   // Yellow
                ],
                borderColor: [
                    'rgba(220, 53, 69, 1)',
                    'rgba(40, 167, 69, 1)',
                    'rgba(0, 123, 255, 1)',
                    'rgba(255, 193, 7, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false, // Important pour contrôler la taille avec CSS
            scales: {
                y: {
                    beginAtZero: true,
                    // min: 0, // Optionnel, mais assure que ça commence à zéro
                    // max et ticks.stepSize sont gérés automatiquement par Chart.js
                    // Si vous voulez forcer un max, vous pouvez le définir ici,
                    // mais l'objectif est d'utiliser le plus grand nombre présent.
                    ticks: {
                        color: '#666666' // Ticks gris pour l'axe Y
                    },
                    grid: {
                        color: 'rgba(0, 0, 0, 0.1)' // Lignes de grille claires
                    }
                },
                x: {
                    ticks: {
                        color: '#666666' // Ticks gris pour l'axe X
                    },
                    grid: {
                        color: 'rgba(0, 0, 0, 0.1)' // Lignes de grille claires
                    }
                }
            },
            plugins: {
                legend: {
                    display: false
                },
                title: {
                    display: true,
                    text: 'Waste Quantity by Color',
                    color: '#333333', // Titre du graphique sombre
                    font: {
                        size: 18
                    }
                }
            }
        }
    });
});