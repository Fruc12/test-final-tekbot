document.addEventListener('DOMContentLoaded', function () {
    const dataValues = [0, 0, 0, 0]; // [red, green, blue, yellow]
    const ctx = document.getElementById('wasteHistogram').getContext('2d');

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

    async function fetchAndUpdateWasteData() {
        try {
            const response = await fetch('/api/set');
            const result = await response.json();

            if (result.success && result.data) {
                const { red, green, blue, yellow } = result.data;

                // Met à jour les anciennes classes
                document.querySelector('.value').textContent = red;
                document.querySelector('.value1').textContent = green;
                document.querySelector('.value2').textContent = blue;
                document.querySelector('.value3').textContent = yellow;

                const total = red + green + blue + yellow;
                document.getElementById("total-count").textContent = total;

                window.wasteChart.data.datasets[0].data = [red, green, blue, yellow];
                window.wasteChart.update();
            }
        } catch (error) {
            console.error("Erreur API /api/set :", error);
        }
    }

    fetchAndUpdateWasteData();
    setInterval(fetchAndUpdateWasteData, 1000);

   // Mise à jour de la batterie
navigator.getBattery?.().then(battery => {
    const updateBattery = () => {
        const level = Math.round(battery.level * 100);
        const batteryIcon = document.querySelector('.battery-icon');
        const batteryLevel = document.querySelector('.battery-level');
        
        batteryLevel.textContent = `${level}%`;
        
        // Changement de couleur et d'icône selon le niveau
        if (level < 20) {
            batteryIcon.className = "fas fa-battery-quarter battery-icon";
            batteryIcon.style.color = '#dc3545'; /* Rouge */
        } else if (level < 50) {
            batteryIcon.className = "fas fa-battery-half battery-icon";
            batteryIcon.style.color = '#ffc107'; /* Jaune */
        } else if (level < 80) {
            batteryIcon.className = "fas fa-battery-three-quarters battery-icon";
            batteryIcon.style.color = '#28a745'; /* Vert */
        } else {
            batteryIcon.className = "fas fa-battery-full battery-icon";
            batteryIcon.style.color = '#28a745'; /* Vert */
        }
    };

    // Initialisation
    updateBattery();
    
    // Écouteurs d'événements
    battery.addEventListener('levelchange', updateBattery);
    battery.addEventListener('chargingchange', updateBattery);
});
});

// Fonction de rapport vocal
function lireRapport() {
    // const rouge = parseInt(document.getElementById("rouge-count")?.innerText || "0");
    // const bleu = parseInt(document.getElementById("bleu-count")?.innerText || "0");
    // const vert = parseInt(document.getElementById("vert-count")?.innerText || "0");
    // const jaune = parseInt(document.getElementById("jaune-count")?.innerText || "0");
    const red = parseInt(document.querySelector('.value')?.innerText || "0");
    const green = parseInt(document.querySelector('.value1')?.innerText || "0");
    const blue = parseInt(document.querySelector('.value2')?.innerText || "0");
    const yellow = parseInt(document.querySelector('.value3')?.innerText || "0");
    const total = red + green + blue + yellow;

    const message = `Il y a au total ${total} déchets; ${red} déchets rouges, ${blue} bleus, ${green} verts et ${yellow} jaunes.`;
    const synth = window.speechSynthesis;
    const utterance = new SpeechSynthesisUtterance(message);
    utterance.lang = "fr-FR";
    synth.speak(utterance);
}
