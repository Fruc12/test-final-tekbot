document.addEventListener('DOMContentLoaded', function () {
    // Initialisation des données à 0
    const dataValues = [0, 0, 0, 0]; // [red, green, blue, yellow]

    const ctx = document.getElementById('wasteHistogram').getContext('2d');

    // Création du graphique une seule fois
    window.wasteChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Red', 'Green', 'Blue', 'Yellow'],
            datasets: [{
                label: 'Waste Quantity',
                data: dataValues,
                backgroundColor: [
                    'rgba(220, 53, 69, 0.7)',
                    'rgba(40, 167, 69, 0.7)',
                    'rgba(0, 123, 255, 0.7)',
                    'rgba(255, 193, 7, 0.7)'
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
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: { color: '#666666' },
                    grid: { color: 'rgba(0, 0, 0, 0.1)' }
                },
                x: {
                    ticks: { color: '#666666' },
                    grid: { color: 'rgba(0, 0, 0, 0.1)' }
                }
            },
            plugins: {
                legend: { display: false },
                title: {
                    display: true,
                    text: 'Waste Quantity by Color',
                    color: '#333333',
                    font: { size: 18 }
                }
            }
        }
    });

    // Fonction de mise à jour toutes les secondes
    async function fetchAndUpdateWasteData() {
        try {
            const response = await fetch('/api/set');
            const result = await response.json();

            if (result.success && result.data) {
                const { red, green, blue, yellow } = result.data;

                // MAJ des éléments HTML
                document.querySelector('.value').textContent = red;
                document.querySelector('.value1').textContent = green;
                document.querySelector('.value2').textContent = blue;
                document.querySelector('.value3').textContent = yellow;

                // MAJ des données du graphique
                window.wasteChart.data.datasets[0].data = [red, green, blue, yellow];
                window.wasteChart.update();
            }
        } catch (error) {
            console.error("Erreur API /api/set :", error);
        }
    }

    // Appel initial puis toutes les secondes
    fetchAndUpdateWasteData();
    setInterval(fetchAndUpdateWasteData, 1000);
});
