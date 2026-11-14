class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        lst=[0]*n
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                lst[i-1]="FizzBuzz"
            elif i%3==0 :
                lst[i-1]="Fizz"
            elif i%5==0:
                lst[i-1]="Buzz"
             
            else:
                lst[i-1]=str(i) 
        return lst

        