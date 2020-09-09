import numpy as np
from collections import defaultdict
import os
import sys
from math import log10

class OutputReader:
    '''
    '''
    def __init__(self, stream, offline_online, window_size, max_size, view='id', alpha=1, beta=1, gamma=1):
        '''
        Load the output of the methods for analysis.
        '''
        file_prefix = '{}_window_size_{}_max_size_{}_exps_{}_{}_{}'.format(stream, window_size, max_size, alpha, beta, gamma)
        self.base_path = '../output/{}/{}/{}'.format(offline_online, view, file_prefix)
        self.load(file_prefix)

    def load(self, file_prefix):
        '''
        Loads the output.
        '''
        self.patterns = set()
        self.pattern_to_P = dict()
        with open('{}_out.txt'.format(self.base_path), 'r') as f:
            for line in f:
                pattern, P = line.strip().split(',')
                P = float(P)
                self.patterns.add(pattern)
                self.pattern_to_P[pattern] = P
        self.pattern_to_F = dict()
        with open('{}_freq_out.txt'.format(self.base_path), 'r') as f:
            for line in f:
                pattern, F = line.strip().split(',')
                F = float(F)
                self.pattern_to_F[pattern] = F

    def load_occs(self, snippets):
        self.pattern_to_occs = dict()
        self.ts = 10000000000000000000000000
        self.te = -1
        with open('{}_occs.txt'.format(self.base_path), 'r') as f:
            for line in f:
                line = line.strip().split(',')
                pattern, occs = line[0], line[1:]
                if pattern in snippets:
                    occs = list(int(t) for t in occs)
                    tl = max(occs)
                    if tl > self.te:
                        self.te = tl
                    tf = min(occs)
                    if tf < self.ts:
                        self.ts = tf
                    self.pattern_to_occs[pattern] = np.asarray(occs, dtype=int)
            for pattern in sorted(self.pattern_to_occs.keys()):
                self.pattern_to_occs[pattern] -= self.ts - 1

    def P(self, pattern):
        return self.pattern_to_P[pattern]

    def F(self, pattern, _log=False):
        if _log:
            return log10(self.pattern_to_F[pattern] + 1)
        return self.pattern_to_F[pattern]

    def occs(self, pattern):
        return self.pattern_to_occs[pattern]
