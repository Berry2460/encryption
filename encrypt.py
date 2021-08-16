def main():
    buffer=64
    name=str(input('NAME: '))
    invalid=True
    while invalid:
        try:
            buffer=int(input('STEP (1-512): '))
            if buffer < 1 or buffer > 512:
                continue
            else:
                invalid=False
        except:
            pass
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
        seed=(seed*seed+1)%499
        byte=(int(chars[seed%len(chars)])+(encrypt*(seed%8)))
        while byte < 0:
            byte+=256
        while byte > 255:
            byte-=256
        data=chars[slice(0,seed%len(chars),1)]+bytes([byte])+chars[slice(seed%len(chars)+1,len(chars),1)]
        e.write(data)
        chars=r.read(buffer)
    r.close()
    e.close()
    print('done')
    
if __name__ == '__main__':
    main()
