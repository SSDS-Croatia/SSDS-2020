import numpy as np
from collections import defaultdict
import os
import sys
from math import log10

class OutputReader:
    '''
    '''
    def __init__(self, stream, offline_online, window_size, max_size, view='id', alpha=1, beta=1, gamma=1, save_occs=False):
        '''
        Load the output of the methods for analysis.
        '''
        file_prefix = '{}_window_size_{}_max_size_{}_exps_{}_{}_{}'.format(stream, window_size, max_size, alpha, beta, gamma)
        base_path = '../output/{}/{}/{}'.format(offline_online, view, file_prefix)
        # self.with_W = with_W
        self.load(file_prefix, base_path, save_occs)

    def load(self, file_prefix, base_path, save_occs):
        '''
        Loads the output.
        '''
        self.patterns = set()
        self.pattern_to_P = dict()
        with open('{}_out.txt'.format(base_path), 'r') as f:
            for line in f:
                pattern, P = line.strip().split(',')
                P = float(P)
                self.patterns.add(pattern)
                self.pattern_to_P[pattern] = P
        self.pattern_to_F = dict()
        with open('{}_freq_out.txt'.format(base_path), 'r') as f:
            for line in f:
                pattern, F = line.strip().split(',')
                F = float(F)
                self.pattern_to_F[pattern] = F
        self.lex_F = list()
        self.lex_P = list()
        self.sorted_F = sorted(self.pattern_to_F.items(), reverse=True, key=lambda it: it[1])
        self.sorted_P = sorted(self.pattern_to_P.items(), reverse=True, key=lambda it: it[1])
        self.rank_F = dict()
        self.rank_P = dict()
        for i, pattern_F in enumerate(self.sorted_F):
            self.rank_F[pattern_F[0]] = i + 1
        for i, pattern_P in enumerate(self.sorted_P):
            self.rank_P[pattern_P[0]] = i + 1
        for pattern in sorted(self.patterns):
            self.lex_F.append(self.pattern_to_F[pattern])
            self.lex_P.append(self.pattern_to_P[pattern])
        # if self.with_W:
        #     self.pattern_to_W = dict()
        #     with open('{}_coverage_out.txt'.format(base_path), 'r') as f:
        #         for line in f:
        #             pattern, W = line.strip().split(',')
        #             W = float(W)
        #             self.pattern_to_W[pattern] = W
        if save_occs:
            self.pattern_to_occs = dict()
            self.ts = 10000000000000000000000000
            self.te = -1
            with open('{}_occs.txt'.format(base_path), 'r') as f:
                for line in f:
                    line = line.strip().split(',')
                    pattern, occs = line[0], line[1:]
                    occs = list(int(t) for t in occs)
                    tl = max(occs)
                    if tl > self.te:
                        self.te = tl
                    tf = min(occs)
                    if tf < self.ts:
                        self.ts = tf
                    self.pattern_to_occs[pattern] = np.asarray(occs, dtype=int)
            for pattern in self.patterns:
                self.pattern_to_occs[pattern] -= self.ts - 1

    def P(self, pattern):
        return self.pattern_to_P[pattern]

    def F(self, pattern, _log=False):
        if _log:
            return log10(self.pattern_to_F[pattern] + 1)
        return self.pattern_to_F[pattern]

    def occs(self, pattern):
        return self.pattern_to_occs[pattern]
