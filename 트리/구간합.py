import sys

input = lambda : sys.stdin.readline().rstrip()

# f = open('./main.txt', 'r')
# input = lambda : f.readline().rstrip()

MAX = 100002
class Hap:
    def __init__(self, arr, size):
        self.arr = arr
        self.size = size
        self.values = [0] * (size*4)
        self.init(arr, 0, size-1, 1)
    
    def init(self, arr, left, right, node):
        if left == right :
            self.values[node] = arr[left]
            return self.values[node]

        mid = (left+right)//2
        leftValue = self.init(arr, left, mid, node*2)
        rightValue = self.init(arr, mid+1, right, node*2+1)
        self.values[node] = leftValue + rightValue
        return self.values[node]

    def _find(self,left, right):
        ans = self.find(left, right, 0, self.size-1, 1)
        print(ans)
        return ans
    
    def find(self, left, right, nodeLeft, nodeRight, node):
        if left <= nodeLeft and nodeRight <= right:
            return self.values[node]
        if nodeRight < left or right < nodeLeft:
            return 0 

        mid = (nodeLeft + nodeRight) // 2
        leftValue = self.find(left, right, nodeLeft, mid,node*2)
        rightValue = self.find(left,right,mid+1, nodeRight, node*2+1)
        return leftValue + rightValue
        

N, M = map(int, input().split())
arr = list(map(int, input().split()))
hap = Hap(arr, N)

for i in range(M):
    left, right =  map(int, input().split())
    hap._find(left-1, right-1)
