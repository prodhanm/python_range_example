import sys

def comp_li():
    range_li = [num*2 for num in range(5,26)]
    return f"Range_list = {range_li}"

def main():
    print(comp_li())
    print(sys.getsizeof(comp_li()))

if __name__ == "__main__":
    main()