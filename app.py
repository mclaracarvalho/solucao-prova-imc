from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def pagina_inicial():
        resultado = False #Criando uma variável resultado para controlar se o resultado do IMC deve ser exibido ou não. Inicialmente, ela é definida como False, indicando que o resultado não deve ser exibido.
    
    if request.method == 'POST':
        nome = request.form['nome']
        peso = request.form['peso']
        altura = request.form['altura']

        altura = float(altura)
        peso = float(peso)

        imc = peso / altura * altura

        if imc < 18.5:
            mensagem = '🔵 Abaixo do peso'
            cor='alert-info'
        elif imc >= 18.5 and imc < 25: #usando and os dois lados tem que estar certo. O or é utilizado para quando um dos lados estiver certo, o outro não importa
            mensagem = '🟢 Peso normal'
            cor = 'alert-success'
        elif imc < 30:
            mensagem = '🟡 Sobrepeso'
            cor = 'alert-warning'
        else:
            mensagem = '🔴 Obesidade'
            cor = 'alert-danger'

        resultado = True #Se o resultado do IMC for calculado, a variável resultado é definida como True, indicando que o resultado deve ser exibido.

        return render_template('index.html', nome=nome, peso=peso, altura=altura, imc=imc, mensagem=mensagem, cor=cor, resultado=resultado)
    return render_template('index.html', resultado=resultado)

@app.route('/equipe')
def equipe():
    return render_template('equipe.html')



if __name__ == '__main__':
    app.run(debug=True)
