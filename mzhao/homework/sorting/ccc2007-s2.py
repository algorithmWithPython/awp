import glob
import time
import bisect

filelist = glob.glob('C:\\Users\\education\\Downloads\\2007\\stage1Marking\\WINDOWS\\s2\\s2.*.in')
for file in filelist:
    with open(file) as f:
        t1=time.time()
        boxNumber = int(input().strip())
        boxes = [] # [[4, 1 , 1 , 4], [8, 1, 2 4]]
        boxvol = []
        for i in range(boxNumber):
            size = [int(i) for i in input().split()] # list(map(int, input().split()))
            size.sort()
            vol = size[0]*size[1]*size[2]
            boxvol.append(vol)
            boxes.append([vol, size[0], size[1], size[2]])
        boxvol.sort()
        boxes.sort(key=lambda item: item[0])

        itemNumber = int(input().strip())
        items = []
        res=[]
        for i in range(itemNumber):
            size = [int(i) for i in input().split()]
            size.sort()
            pos = bisect.bisect_left(boxvol, size[0]*size[1]*size[2])
            while pos < boxNumber:
                if boxes[pos][1] >= size[0] and \
                   boxes[pos][2] >= size[1] and \
                   boxes[pos][3] >= size[2]:
                   res.append(str(boxes[pos][0]))
                   break
                pos+=1
            else:
                res.append("Item does not fit.")
        duration = time.time()-t1
        ofile = 'exp'.join(file.rsplit("in", 1))
        with open(ofile) as of:
            for i in range(itemNumber):
                exp = of.readline().strip()
                if res[i] != exp:
                    print("wrong for " + file + ". line {} exp {}, but {}".format(i, exp, res[i]) )
                    break
            else:
                print("correct for " + file )
        print("take {} seconds".format(duration))
