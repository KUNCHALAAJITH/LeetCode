class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        l=[]
        k=[]
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr2[i]==arr1[j]:
                    l.append(arr1[j])
        for i in arr1:
            if i not in l:
                k.append(i)
        
        l.extend(sorted(k))
        return l
        