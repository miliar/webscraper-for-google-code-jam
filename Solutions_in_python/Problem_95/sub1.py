

v = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm','\n' : '\n','q':'z', 'z': 'q'}

re = open('A-small-attempt6.in','r')
wr = open('A-Output.out','w')

numlines = int(re.readline())

p = ''
for lin in re:
    p += lin
p.strip()

def translate(s):
    r = ''
    for i in s:
        try:
            r += v[i]
        except Exception:
            print i
    r.strip()
    return r

l = p.split('\n')
out = ''
for i in range(len(l)-1):
    #out += 'Case #' + str(i+1) + ': ' + translate(l[i]) + '\n'
    wr.write('Case #' + str(i+1) + ': ' + translate(l[i]) + '\n')
    
wr.close()


p = '''30
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
hello i am the google code jam test data
how are you
aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny iynny aynny ieeeeeeeee
y n f i c w l b k u o m x s e v z p d r j g a t h a q set k oset xa ynfd
schr rkxc tesr aej dksl tkrb xc
njww rpasiyxcpc ysi yxjxj
aej oset aej tysr re
aej tysr dcmm rbksld yr xc neksl qeeex
eb seeeee lellymep kd bcyici wep rbc epvbysylc
eb xa lei mcrd xyoc ejr
lpccrksld fbccdc vevdkfmc rbc sjxncp aej bygc ikymci kd fjppcsrma ejr ew vepofbevd
k bygc ncdrci wpjkr dvkoc ysi xees set k dbymm ncdr aej rbc lja
tbeeeeeeeeeeeeeeeeeeeyyyyyyyyy k oset f vmjd vmjd
wpkcsid iesr mcr wpkcsid mcr dfkcsrkwkf vpelpcdd le nekso
bet ypc aej bemiksl jv ncfyjdc kx y veryre
wep rbedc tbe dvcyo ks y resljc ie ser dvcyo re erbcp vcevmc
seneia jsicpdrysid rbcx dksfc rbca ypc dvcyoksl xadrcpkcd ks rbc dvkpkr
na rbc vpkfoksl ew xa rbjxnd dexcrbksl tkfoci rbkd tya fexcd
ks y tepmi ew ikpctemgcd ysi mkesd dexcrkxcd rbc pypcdr fpcyrjpc kd y wpkcsi
w ew rte czjymd w ew esc czjymd esc
wep k ncrtccs rbpcc ysi s w ew k czjymd w ew k xksjd esc vmjd w ew k xksjd rte
mcr mkvd ie tbyr bysid ie
eb byk kx ks jp fexvjrcp cyrksl aejp fbccqnjplcpd ysi leelmcpcdksl aejp rchrq
tba ie vpelpyxxcpd ymtyad xkh jv bymmetccs ysi fbpkdrxyd
aej ncrrcp fjr rbc vkqqy ks wejp vkcfcd ncfyjdc kx ser bjslpa csejlb re cyr dkh
kx fexxysicp dbcvypi ysi rbkd kd xa wygepkrc vpenmcx es rbc leelmc feic uyx
ys cac wep ys cac ysi y vklces wep y vklces
'''

