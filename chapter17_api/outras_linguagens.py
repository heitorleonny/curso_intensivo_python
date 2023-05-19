"""Outras linguagens: Modifique a chamada de API em python_repos.py
para que ela gere um gráfico mostrando os projetos mais populares em outras
linguagens. Experimente usar linguagens como JavaScript, Ruby, C, Java, Perl,
439
Haskell e Go"""


""" 1 - definirar a url usando requests.get e .json
2 - conferir se está pegando pelo status_code
3 - transformar em dicionairo através do ['items']
4 - criar listas vazias e acrescentar informações por meio do for
"""
import requests
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:C&sort=stars'

busca_url = requests.get(url)
url_certa = busca_url.json()
dict_projetos = url_certa['items']

names, informacoes = [], []

for projeto in dict_projetos[:30]:
   names.append(projeto['name'])
   informacao = {
       'value' : projeto['stargazers_count'],
        'label' :projeto['description'],
        'xlink' :projeto['html_url'],
   }
   informacoes.append(informacao)

my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000


chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred C Projects on GitHub'
chart.x_labels = names
chart.add('', informacoes)
chart.render_to_file('c_repos.svg')
