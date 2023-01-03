class Solution:
    def minDeletionSize(self, strng: List[str]) -> int:
        int_count, cnt = 0,0
        for col in range(0,len(strng[0])): 
            for row in range(1, len(strng)):
                if strng[row-1][col]> strng[row][col]:
                    int_count += 1
                    break
                    
        # cnt =  int_count //(len(strng[0])) 
            
        # if int_count:
        #     cnt += 1
            
                        
        return int_count
                
        