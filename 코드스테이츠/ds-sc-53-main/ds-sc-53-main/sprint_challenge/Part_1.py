# SHA(Secure Hash Algorithm) : 고정값을 반환하는 함수로 Hashing 적용
# sha256개념을 이해하는 것이 아닌 결과값을 반환해주는 적절한 메소드를 활용하세요.

import hashlib

def sha_hash_function():
    # str = input("단어 입력 :")
    h = hashlib.sha256('Test Name'.encode())
    
    if [h.hexdigest()] == ['b19cfa3a0f7cef07dc1dd1604cee0a49c57d0e1a4f1baa864ba1c7c2229b147f']:
          print('true')
    else :
          print('false')
  
    return [h.hexdigest()]


if __name__ == '__main__':
    print(sha_hash_function())
