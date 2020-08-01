import sys
fr_len = int(input()) # The first line will contain a number 'N' that specifies the size of 'frequencies' array
fr_lst = list(map(int, input().split())) # The second line will contain N numbers that form the frequencies array
key_len = int(input()) # The third line contains a number 'K' that specifies the size of the 'keySize' array
key_lst = list(map(int, input().split())) # The fourth line contains K numbers that form the keySize array

fr_lst.sort(reverse=True)
key_lst.sort(reverse=True)
level = 1 # number of times need to type the key to display the letter
fr_idx = 0
key_idx = 0
res = 0
while fr_idx < fr_len:
    if not key_lst: # case that we have letter with frequency but no more available key
        print(-1)
        sys.exit(0)
    if level > key_lst[key_idx]: # if max number of pushes of the key is less than level  
        key_lst = key_lst[:key_idx] # remove the key and any keys after it in the list, remember key_lst is sorted in desent order
        key_idx = 0 # start next level
        level += 1
        continue
    res += fr_lst[fr_idx] * level
    fr_idx += 1
    key_idx += 1
    if key_idx == len(key_lst):
        key_idx = 0  # start next level
        level += 1
print(res)