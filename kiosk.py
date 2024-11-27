#메뉴를 입력받아서 커피의 당도 사이즈업 온도를 설정하여 가격을 계산하는 키오스크 프로그램

# 잔돈 계산함수
def change(total_price):
    print(f"총가격: {total_price}원\n")
    while True:
        try:
            pay_money=int(input("지불금액: "))                             #지불금액 입력받기
            if pay_money<10:                                              #10원미만이면 받지않기
                print("10원이상을 입력하세요")
                print(f"{total_price}원을 지불하세요!")

            elif pay_money%10!=0:                                         #1원단위면 받지않기
                print("1원 단위는 지불할 수 없습니다 ")
                print(f"{total_price}원을 지불하세요!")
            
            elif pay_money<total_price:                                   #지불할 금액보다 적은돈을 내면 계산 후 더 지불한 금액 입력받기
                print(f"{total_price-pay_money}원이 부족합니다.")
                print(f"추가로 {total_price-pay_money}원을 더 지불하세요!")
                total_price-=pay_money

            else:                                                         #올바르게 지불헀으면 거스름돈을 계산하고 while빠져나오기
                change_money=pay_money-total_price
                print(f"거스름돈: {change_money}원")
                print("-"*15)
                break

        except ValueError:                                                #정수가 아니면 다시 입력받기
            print("정수를 입력하세요")
            print(f"{total_price}원을 지불하세요!")

# 주문받은 정보를 txt파일에 저장하기
def order_list(menu,drink_set,price):
    with open("order_list.txt","a" ,encoding="utf8") as ol:
        ol.write(f"{menu}\n")
        ol.write(f"- 당도{drink_set['당도']}\n")
        if drink_set['사이즈업']==1000:
            ol.write("- 사이즈: L\n")
        else:
            ol.write("- 사이즈: m\n")
             
        
        if 'HOT/ICE' in drink_set:
            ol.write(f"- {drink_set['HOT/ICE']}\n")
        else:
            pass
        coffee_price=drink_set['사이즈업']+price
        ol.write(f"가격 : {coffee_price}원\n")
        ol.write(f'------------\n')   
    return coffee_price
    
def coffee():
    #커피 옵션을 넣는 딕셔너리
    #당도는 2차원딕셔너리로 당도 번호를 받아와서 설정
    #사이즈업은 사이즈업을 할꺼면 1000원 안할꺼면 0원으로 설정
    #온도는 HOT ICE중에 설정
    drink_set={"당도":{1:"0%",2:"25%",3:"50%",4:"75%",5:"100%"},"사이즈업":1000,"HOT/ICE":""}
    #당도번호 받아오기 당도값을 올바르게 입력했으면 빠져나오는 while문
    while True:
        try:
            for i in range(1,len(drink_set['당도'])+1):
                print(i,end=": ")
                print(drink_set['당도'][i])
            suger=int(input("당도를 입력해주세요:"))

            if 0<suger<6:
                break
            else:
                print("당도 번호를 정확하게 입력해주세요!")   
        except ValueError:
            print("정수인 숫자를 입력하세요!")
    #사이즈업 값을 올바르게 입력하면 빠져나오는 while문
    while True:
        try:
            sizeup=input("사이즈업 하시겠습니까 o or x:").lower()
            if sizeup=='o' or sizeup=='x':
                break
            else:
                print("o와x중에 골라주세요!")   
        except ValueError:
            print("o와x중에 골라주세요!")
    # 온도값을 올바르게 입력하면 빠져나오는 whlie문
    while True:
        try:
            temp=input("HOT/ICE 골라주세요: ").upper()
            if temp=='HOT' or temp=='ICE':
                break
            else:
                print("HOT과 ICE중에 골라주세요!")   
        except ValueError:
            print("HOT과 ICE중에 골라주세요!")   
    #당도값은 사용자로부터 받아오면 '당도' 의 value값을 번호에 맞는 당도로 설정
    drink_set["당도"]=drink_set["당도"][suger]
    #사이즈업을 했다면 사이즈업 value에 1000입력 아니면 0입력
    if sizeup=='o':
        drink_set["사이즈업"]=1000
    else:
        drink_set["사이즈업"]=0
    #온도설정
    drink_set["HOT/ICE"]=temp
    #사용자로부터 입력받은 커피 옵션값을 담은 딕셔너리 리턴
    return drink_set
       
#아이스는 온도 설정이 없으므로 온도설정을 뺀 함수 새로생성
def ice_blended():
    drink_set={"당도":{1:"0%",2:"25%",3:"50%",4:"75%",5:"100%"},"사이즈업":1000}
    while True:
        try:
            for i in range(1,len(drink_set['당도'])+1):
                print(i,end=": ")
                print(drink_set['당도'][i])
            suger=int(input("당도를 입력해주세요:"))
            if 0<suger<6:
                break
            else:
                print("당도 번호를 정확하게 입력해주세요!")   
        except ValueError:
            print("정수인 숫자를 입력하세요!")
    
    while True:
        try:
            sizeup=input("사이즈업 하시겠습니까 o or x:").lower()
            if sizeup=='o' or sizeup=='x':
                break
            else:
                print("o와x중에 골라주세요!")   
        except Exception:
            print("o와x중에 골라주세요!")
    
    drink_set["당도"]=drink_set["당도"][suger]
    if sizeup=='o':
        drink_set["사이즈업"]=1000
    else:
        drink_set["사이즈업"]=0
    
    return drink_set
    
#menus의 커피종류가 "ICE BLENDED" 면 ice_blended함수 실행 아니면 coffee함수실행
def menu_screen(order_num,menus):
    menu_name=menus[order_num]["메뉴"]
    if menus[order_num]["종류"]=="ICE BLENDED":
        print(f"{menu_name}을(를) 선택하셨습니다.")
        drink_set=ice_blended()
    else:
        
        print(f"{menu_name}을(를) 선택하셨습니다.")
        drink_set=coffee()
    return drink_set

# 메뉴화면 함수
def menus_screen():
#메뉴 2차원 딕셔너리생성 
    menus={
         0:"주문완료",
         1:{"메뉴":"아메리카노","가격":1500,"종류":"COFFEE"},
         2:{"메뉴":"카라멜 마끼야또","가격":4700,"종류":"COFFEE"},
         3:{"메뉴":"블랙밀크티","가격":3300,"종류":"MILK TEA"},
         4:{"메뉴":"제주말차밀크티","가격":3800,"종류":"MILK TEA"},
         5:{"메뉴":"자몽 블랙티","가격":3900,"종류":"FRUIT TEA"},
         6:{"메뉴":"자몽 그린티","가격":3900,"종류":"FURIT TEA"},
         7:{"메뉴":"요거트 스무디","가격":4500,"종류":"ICE BLENDED"},
         8:{"메뉴":"망고스무디","가격":4800,"종류":"ICE BLENDED"},
         9:{"메뉴":"카페라떼","가격":3800,"종류":"LATTE"},
         10:{"메뉴":"돌체라떼","가격":4600,"종류":"LATTE"}
    }
# menus중 메뉴번호 메뉴이름 메뉴 가격만 출력
    for i in range(1,len(menus)):
        print(i,end=" ")
        print( menus[i]["메뉴"],end=": ")
        print(menus[i]["가격"],end="원\n")
#사용자로부터 메뉴번호입력받기
    while True:

        try:
            order_num=int(input("메뉴를 골라서 번호를 입력하시오(0입력시 주문완료): "))
            
            if order_num<0 or order_num>len(menus): #메뉴번호가 0이하거나 없는메뉴의 번호일때 다시입력하라고출력 
                print("메뉴 번호를 정확하게 입력해주세요!")
            
            else:                                    # 올바른 번호입력하면 메뉴번호와 menus리턴하고 while문빠져나오기
                return order_num,menus
                break
    
        except ValueError:                           #정수타입 아닐 때 출력
            print("숫자를 입력해주세요")

def main():
    print("="*50)
    print(f"{'PALGONG TEA':^50}")
    print("="*50)
    with open("order_list.txt","w" ,encoding="utf8") as ol: #영수증파일 초기화
        ol.write(f"{'영수증':-^9}\n")

    try:
        total_price=0     #주문한 총금액을 저장하는 변수 처음 한번만 초기화 하면 되서 반복문 밖에 입력
        while True:
            order_num,menus=menus_screen()         #주문번호와 메뉴판을 받아오는 함수 실행
            if order_num==0:                       #0을 받아오면 주문 종료하고 while문빠져나오기
                print("\n주문이 완료되었습니다")
                break
            drink_set=menu_screen(order_num,menus) #주문번호를 입력받아서 그 번호에 맞는 주문메뉴의 옵션을 입력받는 함수 실행
            coffee_price=order_list(menus[order_num]["메뉴"],drink_set,menus[order_num]['가격']) # 옵션까지 입력받은 커피가격 받아오기
            total_price+=coffee_price              #총가격에 커피가격 더하기
    except Exception:
        print("오류")

    with open("order_list.txt","r" ,encoding="utf8") as ol: #영수증 읽어와서 출력
        content=ol.read()
        print(content)

    change(total_price)

if __name__=="__main__":
    main()