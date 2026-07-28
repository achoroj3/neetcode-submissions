class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #not quite sure what to do here
        # initial thought was define a priority queue with a custom comparator
        #then i realize you cant modify existing elements in the priority queue
        #so that simply wouldn't work.
        #ok i have an idea after writing that out
        #create a hashmap containing the number and frequency of the number
        #then iterate through the map, and manage a priority queue of the top k numbers
        #after that, return the priority queues numbers.
        
        frequency_table = {} # number:frequency
        for elem in nums:
            if elem not in frequency_table:
                frequency_table[elem] = 1
            else:
                frequency_table[elem]+= 1
        pq = []
        heapq.heapify_max(pq)
        for key,value in frequency_table.items():
            if len(pq) < k:
                heapq.heappush_max(pq, (value, key)) # value is the priority
            else:
                pq_temp = pq.copy()
                pq = []
                heapq.heapify_max(pq)
                while (len(pq_temp) > 1):
                    heapq.heappush_max(pq, heapq.heappop_max(pq_temp))
                if pq_temp[0][0] < value:
                    heapq.heappush_max(pq, (value, key))
                else:
                    heapq.heappush_max(pq, heapq.heappop_max(pq_temp))

        answer=[]
        while (len(pq) > 0):
            answer.append(heapq.heappop_max(pq)[1])
        return answer
            # ok this problem would've been much easier
            #with a min heap
            #instead of forcing the pq to be of size k,
            #allow the pq to grow greater than k, and just pop 
            #the smallest




