import requests
import json
from jinja2 import Template

# Función para obtener los datos de las aves de la API
def get_birds_data():
    response = requests.get('https://aves.ninjas.cl/api/birds')
    if response.status_code == 200:
        return response.json()
    else:
        return []

# Función para generar el HTML utilizando los datos de las aves
def generate_html(birds):
    # Cargar el contenido del template HTML desde un archivo
    with open('template.html') as file:
        template = Template(file.read())
        # Renderizar el template con los datos de las aves
        html_content = template.render(birds=birds)
        # Guardar el HTML generado en un archivo
        with open('aves_de_chile.html', 'w') as output_file:
            output_file.write(html_content)

if __name__ == "__main__":
    # Obtener los datos de las aves
    birds_data = get_birds_data()
    # Generar el HTML con los datos de las aves
    generate_html(birds_data)
