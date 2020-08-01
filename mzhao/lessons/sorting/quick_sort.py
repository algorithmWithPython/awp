import random
class QuickSort:
    def __init__(self, l, acsent = True, use_partition2=False):
        self.lst = l
        self.acsent = acsent
        self.use_partition2 = use_partition2

    def _inOrder(self, a,b):
        if self.acsent:
            return a<=b
        else:
            return a>=b

    def _sort(self, s, e):
        # base cases
        if s>=e:
            return 
        
        # there will be at lease 2 elements in the list
        pivot = random.randint(s, e)
        if self.use_partition2:
            k = self._partition2(s, e, pivot)
        else:
            k = self._partition(s, e, pivot)
        self._sort(s, k-1)
        self._sort(k+1, e)

    def _partition(self, l, r, pivot):
        self.lst[pivot], self.lst[r] = self.lst[r], self.lst[pivot]
        i = l
        for j in range(l, r):
            if self._inOrder(self.lst[j], self.lst[r]):
                self.lst[i], self.lst[j] = self.lst[j], self.lst[i]
                i += 1
        self.lst[r], self.lst[i] = self.lst[i], self.lst[r]
        return i

    def _partition2(self, l, r, pivot):
        self.lst[l], self.lst[pivot] = self.lst[pivot], self.lst[l]
        i = l+1
        j = r
        while True:
            while i<=r and self._inOrder(self.lst[i], self.lst[l]):
                i+=1
            while j>l and self._inOrder(self.lst[l], self.lst[j]):
                j-=1
            if i>=j:
                break
            self.lst[i], self.lst[j] = self.lst[j], self.lst[i]
        self.lst[j], self.lst[l] = self.lst[l], self.lst[j]
        return j

    def sort(self):
        self._sort(0, len(self.lst)-1)
        return self.lst

if __name__ == "__main__":
    for _ in range(20):
        l=[]
        for i in range(20):        
            l.append(random.randint(0, 1000))
        print(l)
        res1 = QuickSort(l).sort()
        res2 = QuickSort(l, use_partition2=True).sort()
        print(res1)
        print(res2)
        print()
        assert( res1 == res2 )

