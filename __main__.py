import argparse
import os

# Create argument parser
parser = argparse.ArgumentParser(description="A script that demonstrates adding arguments.")

# Add arguments
parser.add_argument("--name", "-n", type=str, default='', help="function name")
parser.add_argument('--module', '-m', type=str, default='', help='Module name')

# Parse arguments
args = parser.parse_args()

filepath = f'{args.module}/{args.name}.py'
test_filepath = f'tests/{args.module}/test_{args.name}.py'
cmd = f'touch  {filepath} {test_filepath}'
os.system(cmd)