def is_sublist(s, t, idx_s, idx_t):
    idx_s_max = len(s)
    idx_t_max = len(t)

    while True:
        if idx_s == idx_s_max:
            return True
        
        elif idx_t == idx_t_max:
            return False
        
        elif s[idx_s] == t[idx_t]:
            idx_s += 1
            idx_t += 1
            
        else:
            idx_t += 1
            
while True:
    try:
        s, t = input().split()

        if is_sublist(s, t, 0, 0):
            print("Yes")
        else:
            print("No")
    except:
        break