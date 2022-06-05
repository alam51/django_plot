import numpy as np
import matplotlib.pyplot as plt
from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    # return HttpResponse('U r in app1 homepage')
    return render(request, 'homepage.html')


def say_hello(request):
    # return HttpResponse('Hello')
    return render(request, 'hello.html')


def test_plot(request):
    import plotly.express as px
    import pandas as pd

    x = np.arange(0, 10, 0.001)
    y1 = np.sin(x)
    y2 = np.cos(x)
    # fig = px.line(x=["a", "b", "c"], y=[1, 3, 2], title="sample figure")
    fig = px.line(x=x, y=y1, title="Sample figure")
    fig.update_layout(
        # title="Plot Title",
        xaxis_title="x",
        yaxis_title="sin(x)",
        legend_title="Legend Title",
        font=dict(
            family="Times New Roman, monospace",
            size=28,
            color="RebeccaPurple"
        ),
        # hoverlabel=list(font=list(size=10))
    )
    print(fig)
    # fig.show()
    # fig is plotly figure object and graph_div the html code for displaying the graph
    import plotly as plotly

    graph_div = plotly.offline.plot(fig, auto_open=False, output_type="div")
    # pass the div to the template
    return render(request, 'plotly.html', {'graph_div': graph_div})
