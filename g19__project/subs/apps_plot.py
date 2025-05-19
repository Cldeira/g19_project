import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from flask import render_template, session
from sqlalchemy import create_engine
from classes.author import Author

def apps_plot():
    engine = create_engine('sqlite:///data/' + 'Publishing.db')
    df_tabela = pd.read_sql_query("SELECT * FROM Author", con=engine)

    resultado = df_tabela.groupby('authors_id')['royalty_percentage'].sum()
    categorias = resultado.index
    ids = []
    for categoria in categorias:
        obj = Author.obj[categoria]
        ids.append(str(categoria))

    valores = resultado.values

    fig, ax = plt.subplots(figsize=(10, 6))
    x_index = range(len(ids))
    plt.bar(x_index, valores, width=0.4, label='Royalty Percentage')
    plt.xticks(ticks=x_index, labels=ids, rotation=45)
    plt.xlabel('Author ID')
    plt.ylabel('Royalty Percentage')
    plt.title('Gráfico de Royalties por Autor')
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)
    imagem_codificada = base64.b64encode(buf.getvalue()).decode('utf-8')

    return render_template("plot.html", image=imagem_codificada, ulogin=session.get("user"))