import plotly.plotly as py
from plotly.graph_objs import *
import sys
from IPython.display import IFrame

def main(args):
    trace0 = Scatter(
      x=[1, 2, 3, 4],
      y=[10, 15, 13, 17]
    )
    trace1 = Scatter(
      x=[1, 2, 3, 4],
      y=[16, 5, 11, 9]
    )
    data = Data([trace0, trace1])

    py.sign_in('karanjeet', 'ffe9iyynsp')
    url = py.iplot(data)
    print url.resource
    #IFrame(url.data, width=700, height=350)
    #py.iplot(data, filename = 'basic-line')

if __name__ == '__main__':
    main(sys.argv)