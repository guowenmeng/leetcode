class Solution:
    def reconstructQueue(self, people):
        people_dict={}
        for p in people:
            h,k=p[0],p[1]
            people_dict.setdefault(h,[])
            people_dict[h].append(k)

        result=[]
        for h in sorted(people_dict.keys(),reverse=True):
            people_dict[h].sort()
            for k in people_dict[h]:
                result.insert(k,[h,k])

        return result




if __name__ == '__main__':
    s = Solution()
    l =[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    print(s.reconstructQueue(l))