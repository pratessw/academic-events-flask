from flask import Flask, render_template
from models import Evento, Palestrante, Categoria

app = Flask(__name__)

palestrante1 = Palestrante(1, 'João Pedro Araújo', 'palestrante1.jpg', 'Especialista em IA e Big Data.')
palestrante2 = Palestrante(2, 'Milena Carvalho', 'palestrante2.jpg', 'Psicóloga com foco em saúde mental estudantil.')

evento1 = Evento(
    1, 'Semana da Tecnologia', '13/05/2025', '09:00 - 17:00', 'banner.jpg',
    'Centro de Convenções',
    'Conferência sobre as últimas tendências em IA e desenvolvimento de software.',
    'Tecnologia'
)

evento2 = Evento(
    2, 'Saúde Mental na Universidade', '20/05/2025', '14:00 - 18:00', 'banner2.jpg',
    'Auditório',
    'Seminário sobre bem-estar emocional e autocuidado no ambiente acadêmico.',
    'Saúde'
)

evento1.adicionar_palestrante(palestrante1)
evento2.adicionar_palestrante(palestrante2)

eventos = [evento1, evento2]
palestrantes = [palestrante1, palestrante2]
categorias = list(set(e.categoria for e in eventos))

@app.route('/')
def index():
    return render_template('index.html', eventos=eventos)

@app.route('/evento/<int:evento_id>')
def evento_view(evento_id):
    evento = next((e for e in eventos if e.id == evento_id), None)
    if evento:
        return render_template('evento.html', evento=evento)
    return "<h1>Evento não encontrado</h1>"

@app.route('/palestrantes')
def palestrantes_view():
    return render_template('palestrantes.html', palestrantes=palestrantes)

@app.route('/palestrante/<int:id>')
def palestrante_view(id):
    palestrante = next((p for p in palestrantes if p.id == id), None)
    if palestrante:
        eventos_do_palestrante = [e for e in eventos if palestrante in e.palestrantes]
        return render_template('palestrante.html', palestrante=palestrante, eventos=eventos_do_palestrante)
    return "<h1>Palestrante não encontrado</h1>"


@app.route('/categorias')
def categorias_view():
    return render_template('categorias.html', categorias=categorias)

@app.route('/categoria/<categoria>')
def eventos_por_categoria(categoria):
    eventos_filtrados = [e for e in eventos if e.categoria == categoria]
    return render_template('categorias.html', categorias=categorias, eventos_filtrados=eventos_filtrados)