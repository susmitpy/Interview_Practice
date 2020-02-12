def process(filename):
    f = open(filename,"r")
    m, n = [int(i) for i in f.readline().split(" ")]
    slices = [int(i) for i in f.readline().split(" ")]
    f.close()

    #m, n = [int(i) for i in input().split(" ")]
    #slices = [int(i) for i in input().split(" ")]

    #print(f"Max slices: {m}")
    #print(f"Pizzas available: {n}")
    #print(f"slices: {slices}")

    pizza_index_to_order = []
    slices_remaining = m

    for i in range(-1,-(n+1),-1):
        if slices[i] <= slices_remaining:
            slices_remaining -= slices[i]
            pizza_index_to_order.append(n+i)
        
        if slices_remaining <= 0:
            break
            
    #print(f"Pizza index to order: {pizza_index_to_order}")
    pizza_index_to_order.reverse()
    #print(f"Pizza index to order in input sequence: {pizza_index_to_order}")

    print(len(pizza_index_to_order))
    ans = " ".join([str(i) for i in pizza_index_to_order])
    #print(ans)

    f = open(filename[:-3]+"_ans.txt","w")
    f.write(str(len(pizza_index_to_order))+"\n")
    f.write(ans)
    f.close()
    
filenames = ["a_example.in","b_small.in","c_medium.in","d_quite_big.in","e_also_big.in"]

for f in filenames:
    process(f)



