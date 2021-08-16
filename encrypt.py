def main():
    name=str(input('NAME: '))
    seed=str(input('SEED: '))
    temp=0
    for c in seed:
        temp+=ord(c)
    seed=temp
    encrypt=1
    invalid=True
    while invalid:
        i=str(input('ENCRYPT (Y/N)?: '))
        if i == 'y' or i == 'Y':
            newname='E_'+name
            invalid=False
        elif i == 'n' or i == 'N':
            newname='D_'+name
            invalid=False
            encrypt=-1
    r=open(name, 'rb')
    e=open(newname, 'wb')
    char=r.read(1)
    while char:
        seed=(seed*seed+1)%49
        byte=(int(char[0])+(encrypt*(seed%8)))
        while byte < 0:
            byte+=256
        while byte > 255:
            byte-=256
        #print(char[0], byte, seed%8)
        e.write(bytes([byte]))
        char=r.read(1)
    r.close()
    e.close()
    print('done')
    
if __name__ == '__main__':
    main()
