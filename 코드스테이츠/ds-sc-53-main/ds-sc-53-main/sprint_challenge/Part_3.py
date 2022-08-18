# 아래 코드는 변경하지 마세요!
class counter:
    def __init__(self, function):
        self.function = function
        self.cnt = 0

    def __call__(self, *args, **kwargs):
        self.cnt += 1
        return self.function(*args, **kwargs)

# 3 - 1
@counter
def fibonacci(n):
    ##### 소스코드 작성 #####
    return pass

# 3 - 2
@counter
def coin_exchange(, , ): 
  
    way_of_number = [0 for temp in range(total_price + 1)] 
  
    way_of_number[0] = 1
    ##### 소스코드 작성 #####
    
    return 


if __name__ == "__main__":
    # for i in range(0, 30):
    #     print(f'{i} -> {fibonacci(i)}')
    print('### 3 - 1 ###')
    print(fibonacci(5))

    print('### 3 - 2 ###')
    total_price = '교환할 동전금액을 입력하세요(단위 : 원) : '
    piece_price = '얼마짜리 동전으로 교환하시겠습니까?(단위 : 원) '
    piece_price_len = pass

    exchange_way = coin_exchange(, , ) 
    print('교환할 수 있는 방법은',exchange_way,'가지 입니다.') 
