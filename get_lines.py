import sys
def count_lines(paht):
    if paht != '':
        text = open(paht).read().split('\n')
        return len(text)
    if __name__ == "__main__":
        text = open(paht).read().split('\n')
        return len(text)



def main(paht):
    print(count_lines(paht))


if __name__ == "__main__":
    try:
        main(sys.argv[2])
    except Exception:
        print(0)
