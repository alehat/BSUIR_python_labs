if __name__ == "__main__":
    import argparse
    import task1_bigsort as task

    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--numeric", action="store_true", help="Interpreted chars as the number in files")
    parser.add_argument("-b", "--buffer-size", help="Memory buffer size to use for sorting", default="1048576")
    parser.add_argument("-k", "--keys", help="Rows using for sorting")
    parser.add_argument("-t", "--field-separator", default="\t", help="Input the symbol to separate columns")
    parser.add_argument("-l", "--line-separator", default="\n", help="Input the symbol to separate rows")
    parser.add_argument("-i", "--input", help="Input file name")
    parser.add_argument("-o", "--output", help="Output file name")
    parser.add_argument("-r", "--reverse", action="store_true", help="Activate reserse sorting")
    parser.add_argument("-c", "--checking", action="store_true", help="Cheking for sorted")
    args = parser.parse_args()
    buf_size = task.check_mem(args.buffer_size)
    sorter = task.Sorter(buf_size, args)
    in_file = task.sys.stdin
    if args.input is not None:
        in_file = open(args.input, "r")
    if not args.checking:
        out_file = task.sys.stdout
        if args.output is not None:
            out_file = open(args.output, "w+b")
        sorter.sort(in_file, out_file)
    else:
        print sorter.checking(in_file)

