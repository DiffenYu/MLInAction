import kNN


def main():
    print("main function")
    ma, la = kNN.file2matrix('datingTestSet.txt')
    print ma
    print la[0:20]


if __name__ == "__main__":
    main()
