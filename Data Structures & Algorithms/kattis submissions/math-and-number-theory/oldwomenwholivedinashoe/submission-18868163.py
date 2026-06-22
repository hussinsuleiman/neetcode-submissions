w_shoe = int(input())
l_shoe = int(input())
w_bed = int(input())

def N(w_s, l_s, w_bed):
    if w_bed > w_s or w_bed > l_s:
        return 0
    
    if 2*w_bed > w_s and 2*w_bed > l_s:
        return 0
    
    if 2*w_bed <= w_s:
        return 1 + N(w_s - 2*w_bed, l_s, w_bed) + N(2*w_bed, l_s - w_bed, w_bed)
    else:
        return 1 + N(w_s, l_s - 2*w_bed, w_bed) + N(w_s - w_bed, 2*w_bed, w_bed)

print(N(w_shoe, l_shoe, w_bed))