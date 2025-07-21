#!/bin/bash

# echo "🔧 Démarrage des services Apache2 et MySQL..."
# sudo systemctl start apache2 mysql

cd "$(dirname "$0")"

echo "🚀 Lancement du node ROS2 demo_tri..."
# cd ~/test-final-tekbot
source /opt/ros/humble/setup.bash
colcon build --symlink-install
source install/setup.bash
ros2 run demo_tri_pkg demo_tri &
ROS2_PID=$!

echo "🐍 Activation de l'environnement virtuel Flask..."
cd flask-app
source env/bin/activate

# Corriger le PATH si nécessaire
export PATH=$HOME/.local/bin:$PATH

# Vérifier si Flask est installé
if ! python -c "import flask" &> /dev/null; then
    echo "⚠️ Flask n'est pas installé. Installation en cours..."
    pip install flask
else
    echo "✅ Flask déjà installé."
fi

# --- Lancement de Flask ---
echo "🌐 Lancement de Flask TekBot..."
flask --app 'TekBot' run --debug --with-threads --host=0.0.0.0&
FLASK_PID=$!

# --- Gestion de l’arrêt ---
trap "echo '🛑 Arrêt des services...'; kill $ROS2_PID $FLASK_PID" SIGINT

# Boucle principale
wait

