"""
요구사항:
조건에 적합하도록 예외사항을 해결하세요.

조건

함수, 변수를 적합하게 설계하여 코드를 전체적으로 재작성하세요.

커피는 총 5개, 커피 1개당 300원입니다.

자판기에 400원 이상의 돈을 넣은 경우, 넣은 금액으로 살 수 있는 최대한의 커피를 주고 잔돈을 거슬러주면 됩니다.

예를 들어, 1000원을 넣은 경우 3개의 커피를 주고 잔돈 100원을 반환하면 됩니다.
재작성된 코드에서도 아래의 예외사항과 주의사항을 지켜야 합니다.

코드를 수정하되, 전체적인 자판기 작동로직은 지켜야됩니다.

자판기 작동로직 예시

동전을 넣어주세요 -> 커피1개가 나옵니다. -> 사용자의 커피구매종료
예외사항

커피를 구매한 후 잔돈출력

커피자판기에 남은 커피갯수

돈 모자르는 경우

동전이 아닌 다른 것(특수문자, 음수값)이 입력된 경우

주의사항

위의 예외사항을 처리하기 위해 프로그램을 강제 종료시키면 안됩니다.

예를 들어 예외사항에 대해 'return 0' 와 같은 문법을 사용하여 종료하시면 안됩니다.



"""

def part3():
    money = 0
    coffee_machine = 5  # 커피자판기에 있는 전체 커피갯수, 총 5개, 구매가능한 총액 1500원
    remaining_coffee = 5 # 커피를 구매한 경우 커피자판기에 남은 커피갯수

    while remaining_coffee > 0:
        money = input("동전을 넣어주세요: ") # 커피를 구매하기 위한 돈의 액수
        try:
            money = int(money)
        except:
            print('정상적인 금액을 입력해주세요.')
            continue
        if money == 0:
            break

        if money < 0:
            print('정상적인 금액을 입력해주세요.')
            continue

        if money == 300:
            print("커피1개가 나옵니다.")
            remaining_coffee -= 1
            money -= 300
            print("남은 커피 %d개 입니다." % remaining_coffee)
            print('잔돈 %d원을 반환합니다.' % money)

        elif (money > 300) & (money <= remaining_coffee*300) :
            coffee = money // 300
            print('커피%d개가 나옵니다.' % coffee)
            
            remaining_coffee -= coffee
            print('남은 커피 %d개 입니다' % remaining_coffee)
            
            money -= 300 * coffee
            print('잔돈 %d원을 반환합니다.' % money)

        elif money > remaining_coffee*300:
            print('커피%d개가 나옵니다.' % remaining_coffee)
            money = money - remaining_coffee*300
            remaining_coffee = 0
            print('남은 커피 0개 입니다.')
            print('잔돈 %d원을 반환합니다.' % money)
     
        else:
            print("돈이 모자랍니다.")
            print("남은 커피 %d개 입니다." % coffee_machine)
            print('잔돈 %d원을 반환합니다.' % money)
    
    else:        
        print("커피자판기 영업종료")



if __name__ == "__main__":
    part3()