def sequencia():
    seq=''
    for w in range(10,1000,10):
        seq+= str(w) + ', '
        final = '1000' +'.'
    return(f'{seq}{final}')
def main():
    print(sequencia())
if __name__=='__main__':
    main()
    
