#!/bin/bash

# Crear estructura de carpetas
mkdir -p menu/templates
mkdir -p menu/static/css
mkdir -p menu/static/img

# Crear archivos HTML
touch menu/templates/index.html
touch menu/templates/comidas.html
touch menu/templates/bebidas.html

# Crear archivo CSS
touch menu/static/css/estilos.css

echo "✅ Estructura creada correctamente"