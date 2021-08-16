def main():
    buffer=512
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
            newname='ENCRYPTED_'+name
            invalid=False
        elif i == 'n' or i == 'N':
            newname='DECRYPTED_'+name
            invalid=False
            encrypt=-1
    r=open(name, 'rb')
    e=open(newname, 'wb')
    chars=r.read(buffer)
    while chars:
        data=b''
        for char in chars:
            seed=(seed*seed+1)%49
            byte=(int(char)+(encrypt*(seed%8)))
            while byte < 0:
                byte+=256
            while byte > 255:
                byte-=256
            data+=bytes([byte])
        e.write(data)
        chars=r.read(buffer)
    r.close()
    e.close()
    print('done')
    
if __name__ == '__main__':
    main()
