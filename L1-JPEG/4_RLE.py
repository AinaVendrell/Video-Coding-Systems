# source https://wiki.multimedia.cx/index.php/Run_Length_Encoding

def RLE_1(data):
    out = ""
    count = 1
    i = 0
    n = len(data)
    while i < n - 1:
        if(data[i] == data[i+1]):
            count += 1
            if(i == n-2):
                out += str(count)
                out += data[i]
        else:
            out += str(count)
            out += data[i]
            count = 1
        i += 1
    if (data[n-2] != data[n-1]):
        out += '1'
        out += data[n-1]

    print('\nFirst encoding ', out)
    print('Len', len(out))
    return out


def RLE_2(data):
    out = ""
    aux = ""
    count = 0
    m = len(data)

    for i in range(0, m, 2):
        if(data[i] != '1'):
            if (count != 0):
                out = out + str(-count)
                out = out + aux
            out = out + data[i]
            out = out + data[i+1]
            aux = ""
            count = 0
        else:
            count += 1
            aux = aux + data[i+1]
    if (count != 0 and len(aux) > 0):
        out = out + str(-count)
        out = out + aux

    print('\nSecond encoding ', out)
    print('Len', len(out))
    return out


print('Enter a string')
data = str(input())
print('Original lenght', len(data))
rle1 = RLE_1(data)
rle2 = RLE_2(rle1)
