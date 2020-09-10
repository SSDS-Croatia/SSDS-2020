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

        if xscale:
            plt.xscale(xscale)
        if yscale:
            plt.yscale(yscale)

        if xlim:
            plt.xlim(xlim)
        if ylim:
            plt.ylim(ylim)
        plt.title(title, fontsize=self.fontsize)
        plt.xlabel(xlabel, fontsize=self.fontsize)
        plt.ylabel(ylabel, fontsize=self.fontsize)

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
               ytick_labels=None,
               xscale=None,
               yscale=None):
        self.plot(title=title, xlabel=xlabel, ylabel=ylabel, xscale=xscale, yscale=yscale, xlim=xlim, ylim=ylim, grid=grid, background=background)
        if linewidth != None:
            scatter_plot = plt.plot(x, y, '-o', color=colors[0], alpha=alpha, markersize=size, linewidth=linewidth)
        else:
            scatter_plot = plt.scatter(x, y, color=colors, alpha=alpha, s=size)
        if xticks != None:
            plt.xticks(xticks)
        if yticks != None:
            plt.yticks(yticks)
            if ytick_labels != None:
                plt.yticks(yticks, ytick_labels)

        if save_path:
            self.save(save_path, dpi, transparent=transparent)
        plt.show()

    def timeline(self,
                 x,
                 t,
                 ts,
                 te,
                 title='',
                 xlabel='Time',
                 ylabel='',
                 save_path=None,
                 dpi=500,
                 color=None,
                 alpha=1.,
                 interval='Y',
                 mute_ticks=False,
                 marker='line',
                 xticks_and_labels=None,
                 yticks=None,
                 top_line=False,
                 height=1,
                 anomaly_scores=None,
                 no_labels=False,
                 legend=True,
                 max_score=None,
                 tick_length=10,
                 timeticksize=None,
                 colors=None,
                 color_to_label=None,
                 size=None):
        if color == None:
            color = 'green'
        point_size = size
        size = (15, height)

        if interval == 'Y':
            xtick_gap = 31540000
        elif interval == 'M':
            xtick_gap = 2628000
        elif interval == 'W':
            xtick_gap = 604800
        elif interval == 'D':
            xtick_gap = 86400

        self.plot(title=title, xlabel=xlabel, ylabel=ylabel, xscale=None, xlim=None, size=size, background='white', grid=False, top_line=top_line)

        xs = [ts, te]
        ys = [0, 0]
        plt.plot(xs, ys, '-', color='black')

        if max_score != None:
            plt.plot(xs, [max_score, max_score], '-', color='gray', alpha=0)

        xticks = [ts]
        xticks_labels = ['ts'] if not mute_ticks else ['']
        i = 0
        while xticks[-1] + xtick_gap < te:
            i += 1
            xticks.append(xticks[-1] + xtick_gap)
            if xticks[-1] == te:
                xticks_labels.append('te')
            else:
                if mute_ticks:
                    xticks_labels.append('')
                else:
                    xticks_labels.append('{} {}'.format(interval, i))
        if xticks[-1] < te:
            xticks.append(te)
            if mute_ticks:
                xticks_labels.append('')
            else:
                xticks_labels.append('te')


        if xticks_and_labels:
            for tick, lab in zip(*xticks_and_labels):
                xticks.append(tick)
                xticks_labels.append(lab)

        plt.xticks(xticks, xticks_labels)

        x = list(filter(lambda it: ts <= it <= te, x))

        if marker == 'line':
            y = [0] * len(x)
            if timeticksize != None:
                plt.plot(x, y, '|', markersize=500, mew=timeticksize, color=color, alpha=alpha)
            else:
                plt.scatter(x, y, marker='|', s=500, color=color, alpha=alpha)
        elif marker == 'dot':
            y = [0] * len(x)
            plt.scatter(x, y, marker='o', s=10, color=color, alpha=alpha)

        plt.xlabel(xlabel)

        if anomaly_scores != None:
            ax = x[-len(anomaly_scores):]
            ay = anomaly_scores
            color_to_x = defaultdict(list)
            color_to_y = defaultdict(list)

            if not color_to_label:
                color_to_label = dict()
                for c in set(colors):
                    color_to_label[c] = c

            for _ax, _ay, _c in zip(ax, ay, colors):
                color_to_x[_c].append(_ax)
                color_to_y[_c].append(_ay)
            for c in set(colors):
                _ax = color_to_x[c]
                _ay = color_to_y[c]
                plt.scatter(_ax, _ay, color=c, alpha=alpha, s=point_size, label=color_to_label[c])
            plt.plot(ax, ay, '-', color=color, alpha=alpha)
            if legend:
                plt.legend(fontsize=self.fontsize)

        # remove yticks
        frame1 = plt.gca()
        frame1.tick_params('x', length=tick_length)
        frame1.tick_params('y', length=0)
        if anomaly_scores == None:
            frame1.axes.yaxis.set_ticklabels([])
        if yticks != None:
            frame1.axes.yaxis.set_ticklabels(yticks)
        if no_labels == True:
            frame1.axes.xaxis.set_ticklabels([])
        if save_path:
            self.save(save_path, dpi)
        plt.show()
