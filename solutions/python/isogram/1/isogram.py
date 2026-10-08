def is_isogram(phrase):
    myphrase = phrase.replace("-","")
    myphrase1 = myphrase.replace(" ", "")
    finalphrase = myphrase1.lower()
    
    n = len(finalphrase)

    if n==0 or n==1:
        return True

    for i in range(n):
        for j in range(i+1, n):
            if finalphrase[i] == finalphrase[j]:
                return False
            
    return True
            
