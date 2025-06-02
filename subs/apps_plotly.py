from flask import render_template, session
from classes.book import Books
from datafile import filename

import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

def apps_plotly():
    # Creates a pandas dataframe with the orderproduct table data
    engine = create_engine('sqlite:///' + filename + 'Publishing.db')
    df_book = pd.read_sql('Books', con=engine)
    # Uses groupby to obtain the total quantity order by product id
    resultado = df_book.groupby('genre').size()
   


    # Create interactive plot with Plotly
    fig = px.bar(x=resultado.index, y=resultado.values, labels={'x': 'Genre', 'y': 'Books'}, title='Total books by genre')

    plot_div = fig.to_html(full_html=False, div_id='my-plot')

    return render_template("plotly.html", plot_div=plot_div, ulogin=session.get("user"))
