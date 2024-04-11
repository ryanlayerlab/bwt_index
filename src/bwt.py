mport utils
from WaveletTree import WaveletTree
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-q',
                        '--query',
                        required=True,
                        type=str,
                        help='String to search')
    parser.add_argument('-r',
                        '--sample_rate',
                        type=int,
                        default=2,
                        help='Suffix array sampling rate')
    parser.add_argument('-s',
                        '--string',
                        type=str,
                        help='String to use')
    parser.add_argument('-f',
                        '--file',
                        type=str,
                        help='File to read')
    return parser.parse_args()


def bwt(s):
    return None

def get_skip_list(L):
    return None

def get_count(q, bwt, wt, sl):
    return None

def get_sampled_sa(s, n):
    return None

def get_offsets(top, bot, bwt, wt, sa):
    return None

def main():
    args = get_args()
    s = ''
    if args.string:
        s = args.string + '$'
    elif args.file:
        FA = utils.read_fasta(args.file)
        s = FA[0][1] + '$'
    else:
        print('Please provide a string or a file')
        return

    L = bwt(s) 
    wt = WaveletTree(L)
    sl = get_skip_list(L)
    sa = get_sampled_sa(s, args.sample_rate)
    top, bot = count(args.query, L, wt, sl)
    print(get_offsets(top, bot, L, wt, sl))

if __name__ == '__main__':
    main()
