import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

class Plotter:
    def __init__(self, fontsize=30, theme=None, backend=None):
        self.fontsize = fontsize
        if backend:
            plt.switch_backend(backend)
        return

    def plot(self,
             title,
             xlabel='X-axis',
             ylabel='Y-axis',
             size=(15,10),
             xscale=None,
             yscale=None,
             xlim=None,
             ylim=None,
             grid=True,
             top_line=True,
             background=(0.8588235294117647, 0.8588235294117647, 0.8588235294117647)):
        '''
        The main plot function. This is responsible for managing the plot.
        Every type of plot should call this function.

        :title: The title for the plot
        :xlabel: The xlabel for the plot
        :ylabel: The ylabel for the plot
        '''
        fig = plt.figure(figsize=size) 
        if xlim:
            plt.xlim(xlim)
        if ylim:
            plt.ylim(ylim)
        plt.title(title, fontsize=self.fontsize)
        plt.xlabel(xlabel, fontsize=self.fontsize)
        plt.ylabel(ylabel, fontsize=self.fontsize)
        if xscale:
            plt.xscale(xscale)
        if yscale:
            plt.yscale(yscale)

        plt.xticks(fontsize=self.fontsize)
        plt.yticks(fontsize=self.fontsize)
        if background != 'white':
            plt.rcParams['axes.facecolor'] = background
        if grid:
            plt.grid()
        if not top_line:
            ax = plt.gca()
            ax.spines['top'].set_visible(False)

    def save(self, path, dpi=500, sns_plot=None, transparent=False):
        if not path.endswith('.jpg') and not path.endswith('.png') and not path.endswith('.pdf'):
            print('Path to save should end in .jpg or .png or .pdf')
            return
        if sns_plot:
            sns_plot.savefig(path, format='jpg', dpi=dpi, bbox_inches='tight')
        else:
            plt.savefig(path, format=path.split('.')[-1], bbox_inches='tight', transparent=transparent)

    def x_vs_y(self,
               x,
               y,
               title='y = f(x)',
               xlabel='x',
               ylabel='f(x)',
               save_path=None,
               dpi=500,
               colors=None,
               labels=None,
               alpha=None,
               xlim=None,
               ylim=None,
               size=None,
               grid=True,
               background='white',
               linewidth=None,
               transparent=False,
               xticks=None,
               yticks=None,
               xscale=None,
               yscale=None):
        self.plot(title=title, xlabel=xlabel, ylabel=ylabel, xscale=xscale, yscale=yscale, xlim=xlim, ylim=ylim, grid=grid, background=background)
        scatter_plot = plt.scatter(x, y, color=colors, alpha=alpha, s=size)
        if xticks != None:
            plt.xticks(xticks)
        if yticks != None:
            plt.yticks(yticks)

        if save_path:
            self.save(save_path, dpi, transparent=transparent)
        plt.show()

    def timeline(self,
                 x,
                 t,
                 start=1,
                 title='Timeline',
                 xlabel='Time',
                 ylabel='',
                 save_path=None,
                 dpi=500,
                 color=None,
                 alpha=1.,
                 interval=10,
                 with_dots=False,
                 top_line=True,
                 with_last=True,
                 xlim=None,
                 xscale=None):
        if color == None:
            color = 'green'
        if with_dots:
            x_to_c = defaultdict(int)
            for _x in x:
                x_to_c[_x] += 1
            x = sorted(set(x))
            m = max(x_to_c.values())
            size = (t, m)
        else:
            size = (15, 1)

        self.plot(title=title, xlabel=xlabel, ylabel=ylabel, xscale=xscale, xlim=xlim, size=size, background='white', grid=False, top_line=top_line)
        
        xs = np.arange(start, t + 1)
        ys = [0] * len(xs)
        plt.plot(xs, ys, color='black')

        xticks = [1] + list(np.arange(start, t + 1, interval) - 1)[1:]
        if with_last and xticks[-1] != xs[-1]:
            xticks.append(xs[-1])
        plt.xticks(xticks)

        y = [0] * len(x)
        plt.scatter(x, y, marker='|', s=500, color=color)

        if with_dots:
            x_dots = list()
            y_dots = list()
            for _x in x:
                for c in range(1, x_to_c[_x] + 1):
                    x_dots.append(_x)
                    y_dots.append(c)
            plt.scatter(x_dots, y_dots, marker='o', s=40, color=color)

        plt.xlabel('Time')

        # remove yticks
        frame1 = plt.gca()
        frame1.axes.yaxis.set_ticklabels([])
        if save_path:
            self.save(save_path, dpi)
        plt.show()
