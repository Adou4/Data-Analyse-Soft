import pandas as pd
import ipywidgets as widgets
from IPython.display import display

# Charger les données
data = pd.read_csv('https://media.githubusercontent.com/media/datablist/sample-csv-files/main/files/organizations/organizations-100.csv')

# Créer des widgets pour la sélection des colonnes et le filtrage
column_dropdown = widgets.Dropdown(options=list(data.columns), description='Colonnes:')
filter_text = widgets.Text(description='Filtrer:')
filter_button = widgets.Button(description='Filtrer')

# Fonction de filtrage
def filter_data(_):
    column = column_dropdown.value
    filter_value = filter_text.value
    filtered_data = data[data[column] == filter_value]
    display(filtered_data)

# Connecter la fonction de filtrage au bouton
filter_button.on_click(filter_data)

# Afficher les widgets
display(column_dropdown, filter_text, filter_button)
