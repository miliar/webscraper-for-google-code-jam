'''
Created on 12 Apr, 2014

@author: Ye Tian
'''
from decimal import Decimal

input = """50
1
0.6
0.5
10
0.17 0.02 0.49 0.65 0.42 0.78 0.43 0.05 0.55 0.03
0.83 0.34 0.63 0.88 0.18 0.48 0.08 0.85 0.51 0.14
7
0.72 0.33 0.49 0.67 0.91 0.51 0.02
0.14 0.47 0.19 0.09 0.30 0.58 0.12
8
0.48 0.29 0.55 0.94 0.74 0.58 0.61 0.81
0.06 0.13 0.65 0.90 0.16 0.68 0.52 0.39
4
0.74 0.37 0.56 0.33
0.07 0.19 0.22 0.15
1
0.4
0.6
10
0.05 0.24 0.90 0.61 0.21 0.29 0.13 0.08 0.23 0.98
0.16 0.19 0.26 0.76 0.73 0.50 0.11 0.55 0.56 0.69
7
0.72 0.56 0.67 0.61 0.89 0.94 0.83
0.11 0.22 0.33 0.39 0.44 0.28 0.50
2
0.13 0.53
0.60 0.27
10
0.62 0.54 0.12 0.88 0.31 0.15 0.81 0.35 0.73 0.58
0.69 0.27 0.23 0.19 0.65 0.04 0.08 0.77 0.38 0.96
9
0.43 0.82 0.25 0.68 0.32 0.36 0.16 0.02 0.41
0.66 0.27 0.95 0.77 0.86 0.07 0.45 0.23 0.61
8
0.66 0.72 0.62 0.69 0.53 0.88 0.59 0.97
0.06 0.28 0.50 0.16 0.47 0.44 0.31 0.34
10
0.87 0.60 0.63 0.72 0.71 0.88 0.19 0.29 0.26 0.44
0.22 0.37 0.46 0.91 0.31 0.51 0.40 0.81 0.94 0.68
4
0.21 0.29 0.14 0.93
0.50 0.43 0.79 0.36
10
0.56 0.26 0.74 0.67 0.62 0.10 0.95 0.13 0.82 0.05
0.72 0.28 0.38 0.87 0.31 0.51 0.49 0.85 0.03 0.77
10
0.68 0.92 0.98 0.70 0.44 0.06 0.17 0.29 0.02 0.85
0.58 0.32 0.71 0.42 0.53 0.15 0.21 0.03 0.55 0.38
8
0.12 0.10 0.27 0.23 0.25 0.15 0.04 0.44
0.92 0.54 0.58 0.60 0.98 0.81 0.69 0.79
10
0.30 0.38 0.20 0.81 0.86 0.89 0.50 0.67 0.84 0.83
0.42 0.72 0.11 0.34 0.52 0.28 0.66 0.64 0.39 0.14
10
0.532 0.303 0.220 0.174 0.706 0.165 0.092 0.624 0.119 0.945
0.606 0.101 0.651 0.963 0.028 0.872 0.670 0.982 0.294 0.183
10
0.31 0.15 0.19 0.46 0.12 0.04 0.27 0.38 0.42 0.23
0.62 0.58 0.65 0.73 0.77 0.96 0.88 0.92 0.69 0.54
10
0.91 0.86 0.36 0.42 0.43 0.01 0.48 0.54 0.25 0.59
0.74 0.75 0.71 0.88 0.70 0.03 0.81 0.77 0.04 0.23
10
0.92 0.83 0.62 0.21 0.79 0.87 0.29 0.96 0.12 0.58
0.04 0.38 0.42 0.50 0.25 0.08 0.75 0.33 0.54 0.67
3
0.53 0.19 0.69
0.75 0.88 0.97
10
0.98 0.02 0.74 0.84 0.59 0.07 0.03 0.68 0.27 0.97
0.44 0.51 0.13 0.87 0.54 0.35 0.76 0.77 0.18 0.99
4
0.1 0.8 0.2 0.7
0.9 0.6 0.4 0.3
6
0.33 0.86 0.90 0.29 0.71 0.52
0.14 0.10 0.48 0.57 0.24 0.76
9
0.38 0.56 0.03 0.69 0.41 0.28 0.12 0.31 0.09
0.75 0.84 0.16 0.34 0.44 0.06 0.72 0.53 0.94
10
0.40 0.72 0.56 0.13 0.75 0.06 0.33 0.14 0.90 0.19
0.04 0.76 0.50 0.07 0.10 0.01 0.81 0.78 0.65 0.46
10
0.96 0.49 0.04 0.27 0.55 0.35 0.43 0.51 0.65 0.84
0.41 0.82 0.39 0.63 0.86 0.24 0.31 0.98 0.37 0.92
8
0.90 0.50 0.95 0.15 0.85 0.05 0.55 0.65
0.30 0.25 0.70 0.45 0.60 0.80 0.10 0.40
10
0.388 0.786 0.447 0.757 0.913 0.631 0.602 0.117 0.049 0.738
0.262 0.971 0.583 0.408 0.379 0.505 0.612 0.184 0.437 0.718
4
0.25 0.67 0.50 0.17
0.83 0.08 0.75 0.92
10
0.77 0.74 0.75 0.83 0.85 0.66 0.78 0.89 0.71 0.97
0.54 0.20 0.34 0.05 0.40 0.62 0.37 0.09 0.03 0.26
10
0.82 0.20 0.13 0.85 0.55 0.02 0.42 0.96 0.78 0.80
0.84 0.47 0.53 0.15 0.44 0.60 0.27 0.36 0.35 0.62
1
0.4
0.9
4
0.40 0.52 0.32 0.16
0.56 0.88 0.68 0.96
9
0.579 0.243 0.336 0.505 0.103 0.477 0.019 0.346 0.252
0.785 0.869 0.888 0.813 0.701 0.766 0.981 0.879 0.776
10
0.94 0.72 0.97 0.84 0.71 0.75 0.83 0.77 0.67 0.90
0.09 0.26 0.45 0.39 0.52 0.13 0.16 0.06 0.17 0.41
10
0.67 0.27 0.08 0.78 0.19 0.25 0.65 0.20 0.77 0.04
0.24 0.86 0.92 0.80 0.28 0.49 0.13 0.29 0.38 0.91
6
0.25 0.72 0.09 0.69 0.78 0.94
0.38 0.03 0.59 0.12 0.88 0.50
3
0.44 0.62 0.81
0.12 0.25 0.06
2
0.86 0.07
0.36 0.43
10
0.17 0.40 0.12 0.05 0.26 0.02 0.33 0.14 0.19 0.21
0.93 0.98 0.45 0.55 0.86 0.83 0.50 0.64 0.60 0.69
3
0.48 0.28 0.04
0.44 0.72 0.60
10
0.40 0.89 0.49 0.32 0.94 0.74 0.66 0.91 0.02 0.45
0.70 0.96 0.28 0.23 0.11 0.21 0.06 0.19 0.98 0.36
4
0.44 0.38 0.56 0.08
0.67 0.15 0.92 0.74
10
0.25 0.51 0.91 0.54 0.26 0.32 0.09 0.39 0.23 0.96
0.72 0.11 0.63 0.30 0.60 0.33 0.40 0.68 0.42 0.37
10
0.716 0.637 0.892 0.843 0.941 0.706 0.931 0.598 0.794 0.765
0.343 0.225 0.353 0.265 0.314 0.069 0.167 0.147 0.392 0.059
1
0.64
0.55
7
0.23 0.33 0.52 0.22 0.28 0.10 0.12
0.50 0.67 0.35 0.30 0.02 0.68 0.07
"""
def haslarger(b, ken):
    for k in ken:
        if k > b:
            return True;
    
    return False;

def getlargerblock(b, ken):
    minmax = max(ken);
    for k in ken:
        if k > b and minmax > k:
            minmax = k
    return minmax;

def getlargerblock_n(b, naomi):
    minmax = max(naomi);
    for k in naomi:
        if k > b and minmax > k:
            minmax = k
    return minmax;

def war(naomi, ken):
    #not randomly
    result = {};
    result["naomi"] = 0;
    result["ken"] = 0;
    
    for b in naomi:
        # ken choose one that larger than it
        #print "naomi", b;
        if haslarger(b, ken):
            k = getlargerblock(b, ken);
            result["ken"] += 1;
            #print "ken", k;
            ken.remove(k);
        else:
            if b in ken:
                ken.remove(b);
            else:       
                result["naomi"] += 1;
                ken.remove(min(ken));
    
    return result;

def naomialwayswin(naomi, ken):
    s_naomi = sorted(list(naomi));
    s_ken = sorted(list(ken));
    
    r = [n - k for n, k in zip(s_naomi, s_ken)];
    
    #print s_naomi
    #print s_ken
    
    for i in r:
        if i < 0:
            
            return False;
    return True;

def d_war(naomi, ken):
    #not randomly
    result = {};
    result["naomi"] = 0;
    result["ken"] = 0;    
    
    if len(naomi) == 1:
        return war(naomi, ken);
    
    while len(naomi) != 0:
        min_n = min(naomi);
        max_n = max(naomi);
        max_k = max(ken);
        min_k = min(ken);
        
        told_min_n = max_k - Decimal(0.000001); 
        
        if naomialwayswin(naomi, ken):
            b = getlargerblock_n(max_k, naomi);
            #print b;
            if haslarger(b, ken):
                k = getlargerblock(b, ken);
                result["ken"] += 1;
                #print "ken1", k;
                ken.remove(k);
                naomi.remove(b);
            else:
                if b in ken:
                    ken.remove(b);
                    naomi.remove(b);
                else:       
                    result["naomi"] += 1;
                    ken.remove(max(ken));
                    naomi.remove(b);
        else:
            result["ken"] += 1;
            ken.remove(max_k);
            naomi.remove(min_n);          
                
    return result;
               

inputlist = input.split("\n");
#print inputlist;

task_number = int(inputlist[0]);

for i in range(0, task_number):
    task = i * 3 + 1;
    
    blocks = int(inputlist[task]);
    naomi = inputlist[task+1].split(" ");
    ken = inputlist[task+2].split(" ");
    
    naomi_v = [];
    ken_v = [];
    
    for b in range(0,blocks):
        naomi_v.append(Decimal(naomi[b]));
        ken_v.append(Decimal(ken[b]));
    
    r_war = war(naomi_v, ken_v);

    naomi_v = [];
    ken_v = [];
    for b in range(0,blocks):
        naomi_v.append(Decimal(naomi[b]));
        ken_v.append(Decimal(ken[b]));
        
    dr_war = d_war(naomi_v, ken_v);
    print "Case #%d: %d %d" % (i+1, dr_war["naomi"], r_war["naomi"]); 
    
