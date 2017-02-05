if __name__ == "__main__":
    import argparse
    import task2_files as task

    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", default="input.txt", help="Output file name")
    parser.add_argument("-n", "--numeric", action="store_true", help="Interpreted chars as the number")
    parser.add_argument("-f", "--field-count", type=int, default=1, help="Column's count in row")
    parser.add_argument("-t", "--field-separator", default="\t", help="Input the symbol to separate columns")
    parser.add_argument("-l", "--line-separator", default="\n", help="Input the symbol to separate rows")
    parser.add_argument("-c", "--count", type=int, default=100, help="Count of rows to generate")

    args = parser.parse_args()
    out_file = task.sys.stdout
    if args.output is not None:
        task.out_file = open(args.output, "w+b")
    res = task.GenFiles(out_file, args.numeric, args.field_count, args.field_separator, args.line_separator)
    res.generate(args.count)
    res.close()
