import numpy as np
import plotly.express as px
import pandas as pd
x = np.arange(0, 10, 0.001)
y1 = np.sin(x)
y2 = np.cos(x)
# fig = px.line(x=["a", "b", "c"], y=[1, 3, 2], title="sample figure")
fig = px.line(x=x, y=y1, title="sample figure")
print(fig)
fig.show()
# fig is plotly figure object and graph_div the html code for displaying the graph
import plotly as plotly

graph_div = plotly.offline.plot(fig, auto_open=False, output_type="div")
# pass the div to the template
