from collections import Counter

if __name__ == '__main__':
    s = input()
    c = Counter(s)
    mc = c.most_common(3)
    mcl = len(mc)
    mc = list(mc)
    sort_till_index = -1
    for index, elem in enumerate(mc):
        if index <= sort_till_index:
            continue
        if index != mcl - 1:
            if mc[index+1][1] != elem[1]:
                print(f"{elem[0]} {elem[1]}")     
            else:
                sort_from_index = index
                sort_till_index = index
                while mc[sort_till_index][1] == elem[1]:
                    if sort_till_index == mcl - 1:
                        break
                    sort_till_index += 1
                temp = sorted(mc[sort_from_index:sort_till_index+1],key=lambda x: x[0])
                for i in temp:
                    print(f"{i[0]} {i[1]}")
        else:
            print(f"{elem[0]} {elem[1]}")
