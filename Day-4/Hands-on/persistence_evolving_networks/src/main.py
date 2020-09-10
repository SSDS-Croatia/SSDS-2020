from sPENminer import sPENminer
from oPENminer import oPENminer
from stream import Stream
import argparse
import sys

def parse_args():
    def str2bool(v):
        if v.lower() in ('yes', 'true', 't', 'y', '1'):
            return True
        elif v.lower() in ('no', 'false', 'f', 'n', '0'):
            return False
        else:
            raise argparse.ArgumentTypeError('Boolean value expected.')

    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', type=str2bool, default=True, required=False, help="If True, then print on the fly.")
    parser.add_argument('--stream', '-s', type=str, required=True, help="Stream name.")
    parser.add_argument('--window_size', '-ws', type=int, default=1, required=False, help="Window size; equivalent to max duration (\delta_max).")
    parser.add_argument('--max_size', '-ms', type=int, default=1, required=False, help="Max snippet size (k_max).")
    parser.add_argument('--view', '-v', type=str, default='id', required=False, help="What view of nodes to use.")
    parser.add_argument('--alpha', '-alpha', type=float, default=1, required=False, help="What exponent to use for W().")
    parser.add_argument('--beta', '-beta', type=float, default=1, required=False, help="What exponent to use for F().")
    parser.add_argument('--gamma', '-gamma', type=float, default=1, required=False, help="What exponent to use for S().")
    parser.add_argument('--delimiter', '-d', type=str, default=',', required=False, help="Delimiter.")
    parser.add_argument('--offline', '-o', type=str2bool, default=False, required=False, help="If True, then run offline version.")
    parser.add_argument('--seed', '-seed', type=int, default=0, required=False, help="Seed for random cut forests.")
    parser.add_argument('--save_output', '-save', type=str2bool, default=True, required=False, help="If True, then save persistence scores.")
    parser.add_argument('--save_occs', '-so', type=str2bool, default=False, required=False, help="If True, then save occurrences (offline version only).")
    return parser.parse_args()

def main(args):
    stream = Stream(args.stream, delimiter=args.delimiter)
    print('Using view \"{}\"'.format(args.view))
    if not args.offline:
        if args.save_occs:
            print('\'save_occs = True\' is only an option for offline verions. Occurrences will not be saved')
        method = sPENminer(stream,
                           window_size=args.window_size,
                           max_size=args.max_size,
                           view=args.view,
                           alpha=args.alpha,
                           beta=args.beta,
                           gamma=args.gamma,
                           save_output=args.save_output)
    else:
        method = oPENminer(stream,
                           window_size=args.window_size,
                           max_size=args.max_size,
                           view=args.view,
                           alpha=args.alpha,
                           beta=args.beta,
                           gamma=args.gamma,
                           save_output=args.save_output,
                           save_occs=args.save_occs)
    method.mine(verbose=args.verbose)

if __name__ == "__main__":
    args = parse_args()
    main(args)
