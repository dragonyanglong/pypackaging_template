import os
from argparse import ArgumentParser, RawTextHelpFormatter
from pkgname.hello import add

def main():
    _BANNER = """
    This is the Billinge Group python packaging format.
    
    This helps people set up their git repo correctly for releasing.
    """
    parser = ArgumentParser(prog = 'pkgname',
                            description = _BANNER, formatter_class = RawTextHelpFormatter)
    # required args
    parser.add_argument("x", type = float,
                        help = "x")
    # required args
    parser.add_argument("y", type = float,
                        help = "y")
    # optional args
    parser.add_argument("--opt", dest="opt", type = str,
                        help = "option")

    args = parser.parse_args()
    print(add(args.x,args.y))

if __name__ == "__main__":
    main()