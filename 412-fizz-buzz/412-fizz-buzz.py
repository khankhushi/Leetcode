class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        i=1
        answer = []
        for i in range(1,n+1):
            if not i % 3 and not i % 5:
                answer.append("FizzBuzz")
            elif not i % 3 :
                answer.append("Fizz")
            elif not i % 5  :
                answer.append("Buzz")
            else :
                answer.append(str(i))
                
        return answer
                
        