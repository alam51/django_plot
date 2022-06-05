import numpy as np
import matplotlib.pyplot as plt
import base64
from io import BytesIO

# fig = plt.figure()
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
x = np.arange(0, 10, 0.001)
y1 = np.sin(x)
y2 = np.cos(x)
ax1.plot(x, y1, 'g')
ax1.plot(x, y2, 'r--')
plt.grid(True)
# plot sth


tmpfile = BytesIO()
fig.savefig(tmpfile, format='png')
encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')

# html = 'Some html head' + '<img src=\'data:image/png;base64,{}\'>'.format(encoded) + 'Some more html'
html = '<H1>Heading 1 </H1>' + f'<img src=\'data:image/png;base64,{encoded}\'>' + '<H3>Heading 3</H3>'

with open('test.html', 'w') as f:
    f.write(html)
