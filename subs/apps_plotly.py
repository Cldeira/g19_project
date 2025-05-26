from flask import render_template, session
from classes.product import Product
from datafile import filename

import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

def apps_plotly():
    # Creates a pandas dataframe with the orderproduct table data
    engine = create_engine('sqlite:///' + filename + 'business.db')
    df_orderproduct = pd.read_sql('OrderProduct', con=engine)
    # Uses groupby to obtain the total quantity order by product id
    result = df_orderproduct.groupby('product_id')['quantity'].sum()
    # From the product class get the product id names
    p_ids = result.index
    p_names = []
    for p_id in p_ids:
        p_obj = Product.obj[p_id]
        p_names.append(p_obj.name)
    quantities = result.values

    # Create interactive plot with Plotly
    fig = px.bar(x=p_names, y=quantities, labels={'x': 'Product ID', 'y': 'Quantity'}, title='Total quantity ordered by product')

    plot_div = fig.to_html(full_html=False, div_id='my-plot')

    return render_template("plotly.html", plot_div=plot_div, ulogin=session.get("user"))
