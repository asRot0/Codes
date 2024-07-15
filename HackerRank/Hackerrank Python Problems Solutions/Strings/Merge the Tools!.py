import textwrap
def merge_the_tools(string, k):
    li = textwrap.wrap(string, k)
    for i in li:
        print(''.join(sorted(set(i), key=i.index)))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
