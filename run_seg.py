"""
Script to expose the command line interface (--input, --output, and --use-gpu)
and call the FakeSegmenter model.
"""

import sys
import argparse
from seg_pipeline import FakeSegmenter


def parse_args():
    p = argparse.ArgumentParser(description='Fake image segmentation')
    p.add_argument('--input', '-i', required=True, help='Path to input images directory')
    p.add_argument('--output', '-o', required=True, help='Path to output masks directory')
    p.add_argument('--use-gpu', action='store_true', help='Flag to simulate using GPU')

    return p.parse_args()


if __name__ == '__main__':
    args = parse_args()

    try:
        seg = FakeSegmenter(use_gpu=args.use_gpu)
        print(f'[INFO] Initiliazing segmentation. use_gpu={seg.use_gpu}')

        seg.segment(input_dir=args.input, output_dir=args.output)
        print('[INFO] Segmentation finished.')
    except Exception as e:
        print(f'[ERROR] {e}', file=sys.stderr)
        sys.exit(1)
