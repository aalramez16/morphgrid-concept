
# coding: utf-8

# In[103]:


a1,a2,a3,a4 = [[0,-1,-2], [-2,0,-3], [1,-2,1], [-2,3,-4]]

x = [[a1,a2],[a3,a4]]

def get_avg_list(v1, v2):
    v3 = []
    for i in range(len(v1)):
        v3.append((v1[i]+v2[i])/2)
    return v3

def recursive_pop_v(l,i):
    if i > 0:
        avg_left = get_avg_list(l[0][0],l[-1][0])
        avg_right = get_avg_list(l[0][-1],l[-1][-1])
        
        l.insert(1,[avg_left,avg_right])
        
        halfway_length = (int)(len(l)/2)
        
        new_l = recursive_pop_v(l[0:halfway_length+1],i-1)[0:-1] + recursive_pop_v(l[halfway_length:len(l)],i-1)

        return new_l
    
    else:
        return l
    
def recursive_pop_h(l,i):  
    if i > 0:
        avg = get_avg_list(l[0],l[-1])
        l.insert(1,avg)

        halfway_length = (int)(len(l)/2)

        new_l = recursive_pop_h(l[0:halfway_length+1],i-1)[0:-1] + recursive_pop_h(l[halfway_length:len(l)],i-1)

        return new_l

    else:
        return l     
z = []    
y= recursive_pop_v(x,2)
for i in range(len(y)):
    print(recursive_pop_h(y[i],2))
             

