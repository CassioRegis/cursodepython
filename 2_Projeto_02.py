import plotly.graph_objs as graph_ob
import plotly.express as px
import pandas as pd
import dash 
import dash_bootstrap_components as dbc
from dash_bootstrap_templates
import ThemeSwitchAIO
from dash.dependencies
import Input, Output
from dash
import html , dcc, Input, Output
#configurando cores para os temas
dark_themes = 'darkly'
vapor_themes = 'vapor'
url_dark_thems = dbc.themes.DARKLY
url_vapor_thems = dbc.themes.VAPOR

#--------------------------------DADOS--------------------------------------------------

df = pd.read_csv('dataset_comp.csv')
df['dt_Venda'] = pd.todatetime(df['dt_Venda'])
df['Mes'] =df['dt_Venda'].dt.strftime('%b').str.upper()

#-------------------------------Listas---------------------------------------------------
#Criar listas de clientes
lista_clientes = []
for cliente in df['Cliente'].unique():
    lista_clientes.append({
        'label': cliente,
        'value': cliente
    })

lista_clientes.append({
    'label': 'Todos os clientes',
    'value': 'todos_clientes'
})

# Criando 

meses_br = dict(
    JAN ='JAN',
    FEB='FEV',
    MAR='MAR',
    APR='ABR',
    MAY='MAI',
    JUN='JUN',
    JUL='JUL',
    AUG='AGO',
    SEP='SET',
    OCT='OUT',
    NOV='NOV',
    DEC='DEZ'
    )

lista_meses = []
for mes in df['Mes'].unique():
    mes_pt = meses_br.get(mes, mes)

lista_meses.append({
    'label': mes_pt,
    'value': mes
})

lista_meses.append({
    'label': 'Ano Completo',
    'value': 'ano_completo'
})

#Criando as categorias
lista_categorias = []
for categoria in df['Categorias'].unique():
    lista_categorias.append({
        'label': 'Todas as Categorias',
        'value': 'todas_categorias'
    })
#Inicio do servidor
app = dash.Dash(__name__)
server = app.server

#------------------------------LAYOUT-------------------------------------------------------
#elelmento do select no superior esquerdo
layout_titulo = html.Div([
    html.Div(
        dcc.dropdown(
            id='dropdown_cliente',
            options=lista_clientes,
            placeholder= lista_clientes[-1]['label'],
            style={
                'backgroud-color': 'transparent',
                'border': 'nome',
                'color': 'black'
                }
        ), style={'width': '25%'}
    ),
    html.Div(
        html.legend(
            'SebraeMaranhão',
            style={
                'front-size': '150%',
                'text-align': 'center'
            }
        ), styler={'width': '50%'}
    ),
    html.Div(
        ThemeSwitchAIO(
            aio_id='theme',
            themes=[
                url_dark_thems,
                url_vapor_thems
            ]
        ), style={'width': '25%'}
    )
], style=(
    'text-align': 'center',
    'display': 'flex',
    'justify-content': 'space-around',
    'align-items': 'center',
    'font-family': 'Fire code',
    'margin-top': '20px'
))
layour_linha01 = html.Div([
    html.Div([
        html.H4(id='output_cliente'),
        dcc.Graph(id='visual01')
    ], style={
        'width': '65%',
        'text-align': 'center'}
    ), 
    html.Div([
        dbc.Checklist(
            id='radio_mes',
            options='lista_meses',
            inline=True
        ),
        dbc.RadioItems(
            id='radio_categorias',
            options=lista_categorias,
            inline=True
        )
    ], style={
        'width': '30%',
        'display': 'flex',
        'flex_direction': 'column',
        'justify-content': 'space-evenly'})
], style={
    'display': 'flex',
    'justify': 'space-around',
    'margin-top': '40px',
    'heigth': '300px'
})
layour_linha02 = html.Div([])
      html.Div([
           html.H4('Vendas por Mês e Loja/Cidade'),
           dcc.Graph(id='Visual02')    
      ], style={
          'width': '60%',
          'text-align':'center'
          }),
      html.Div(dcc.Graph(id='Visual03'), style={'width': '35%'})
      ], style={
          'display':'flex',
          'justify-content':'space-around',
          'margin-top': '40px',
          'height':'150px'
      })
#carregar o layout
app.layout = html.Div ([
   layout_titulo,
   layout_linha01,
   layout_linha02     
])

#------------------------------FUNÇÕES DE APOIO-------------------------------------------------------
def filtro_cliente(cliente_selecionado):
    if cliente_selecionado is Nome:
        return pd.Series(True, index=df.index)
    return df['Cliente'] == cliente_selecionado

#------------------------------CALLBACKS-------------------------------------------------------

#Subindo o servidor
if __name__ == '__neme__':
    app.run_server(debug=True)
