
'''
Dynamic programming exercise 1
Problem statement:
    Given a array of numbers, find the number of k-subsequence defined as follows:
    (1) it is a subsequence of contiguous elements in the array
    (2) the sum of the subsequence is divisible by k
'''


#==========================================================================================
# idea1: calculate cumulative sum (module) k of the array, a
#        slice p ... q is a k-subsequence if S[p] == S[q]
# Example: k = 3, arr = 1,2,3,4,1
# The corresponding culmulative sum S (module k)is [0 1 0 0 1 2] (we append 0 in the beginning!)
# So all the possible k_subseq exist in slice S[0]:S[2], S[0]:S[3], S[2]:S[3], S[1]:S[4] (not take into account
# the first element in the slice)
# If we have x ele in S with the same value i, then for value i, we have x(x-1)/2 number of k-subseqence(combination problem
# math)


def kSub(k,nums):
    # nums : input array
    # k    : number to be divised

    # S is our culmulative sum
    S = [0 for i in xrange(len(nums) + 1)] # you need to add an additional zero before!
    cnt = [0 for i in xrange(k)]
    cnt[0] = 1
    ans = 0


    # construct culmulative sum
    tmp =[x % k for x in nums]
    for i in xrange(len(nums)):
        S[i+1] =  (S[i] + tmp[i]) % k
        cnt[S[i+1]] += 1

    for i in xrange(k):
        ans += (cnt[i] * (cnt[i]-1)) / 2

    # print out all possible k-subsequence
    def print_subseq(nums,S,cnt):
        k_list = []
        tmp = [-1000] + nums # -1000 is a special number
        arr = [i for i, k in enumerate(cnt) if k > 1]
        print arr
        for i in arr:
            idx = [j for j, k in enumerate(S) if k == i]
            for l1 in range(len(idx)):
                l2 = l1 + 1
                while l2 < len(idx):
                    k_list.append(tmp[idx[l1]+1:idx[l2]+1])
                    l2 += 1
        return k_list

    print print_subseq(nums,S,cnt)

    return ans


#print kSub(5,[4,5,0,-2,-3,1])


#==========================================================================================
#Idea2 : use dynamic programming (credit tp weige)
# We use two arrs in the code: dp and ndp
# Supoose that arr nums grows dynamically,say if nums = [1,2,3,4,1], then we continuously
# grow from 1, then 1,2, then 1,2,3, up to 1,2,3,4,1
# dp : everytime we add a new number i, we record the frequency of remainer that all the subsequence
#      contiguous to i(it can be i itself) modules k
# ndp: it stands for new dp, everytime we will first update ndp and then assign it dp for the next iteration
#

def kSub1(k,nums):
    ans = 0
    dp = [0 for x in xrange(k)]
    for num in nums:
        ndp = [0 for x in xrange(k)]
        for i in xrange(k):
            ndp[(i + num) % k] = dp[i]
        ndp[num % k] += 1
        dp = ndp[:]
        ans += dp[0]

        print 'num = %i,ndp = %s, dp = %s, ans = %i '%(num,ndp,dp,ans)
    return ans

print kSub1(3,[1,2,3,4,1])



