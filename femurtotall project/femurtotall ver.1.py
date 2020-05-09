#대퇴골의 길이로 인간의 신장을 주정하는 프로그램

print("="*30)
print("="*13 + "tall" + "="*13)
print("="*30)
print(" ")

while True :
    print("남성 : 1\n여성 : 2\n종료 : 3")
    print(" ")
    MorF = input(">>> ")
    print(" ")

    if MorF == '1' : #남성
        print("남성을 입력받았습니다.")
        print("Pearson식, Trotter&Glaser식, 藤井식을 사용하여 신장을 추정합니다.")
        print("'0'을 입력하면 초기 메뉴로 돌아갑니다.")
        print(" ")
        while True :
            femur = float(input("대퇴골의 길이를 입력해주세요 >>> "))
            if femur != 0 :
                pearson_result = 81.306 + 1.880 * femur
                trotter_result = 2.15 * femur + 72.57
                huzii_result = (2.47 * (femur*10) + 549.01)/10
            
                print("- Pearson식 : %0.2fcm" % pearson_result)
                print("- Trotter&Glaser식 : %0.2fcm" % trotter_result)
                print("- 藤井식 : %0.2fcm" % huzii_result)
                print(" ")
            elif femur == 0 :
                print(" ")
                print("=" * 30)
                print("=" * 4 + "초기 메뉴로 돌아갑니다" + "=" * 4)
                print("=" * 30)
                print(" ")
                break
            
    elif MorF == '2' : #여성
        print("여성을 입력받았습니다.")
        print("Pearson식, 藤井식을 사용하여 신장을 추정합니다.")
        print("'0'을 입력하면 초기 메뉴로 돌아갑니다.")
        print(" ")
        while True :
            femur = float(input("대퇴골의 길이를 입력해주세요 >>> "))
            if femur != 0 :
                pearson_result = 72.844 + 1.945 * femur
                huzii_result = (2.24 * (femur*10) + 610.43)/10
            
                print("- Pearson식 : %0.2fcm"  % pearson_result)
                print("- 藤井식 : %0.2fcm" % huzii_result)
                print(" ")
            elif femur == 0 :
                print(" ")
                print("=" * 30)
                print("=" * 4 + "초기 메뉴로 돌아갑니다" + "=" * 4)
                print("=" * 30)
                print(" ")
                break

    elif MorF == '3' : #종료
        print("="*30)
        print("="*10 + "종료합니다" + "="*10)
        print("="*30)
        print(" ")
        break
    
    else : #오류
        print(" ")
        print("오류입니다. 다시 입력해주세요.")
        print(" ")