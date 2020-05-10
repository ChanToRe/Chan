#11번, 18번 줄의 경로를 수정해서 사용
#fileD(X, Y).jpg -> D : 파일 번호 / X : 임계값1 / Y : 임계값2
import cv2

print("**임계값1 이하는 모두 제외**")       #임계값 입력
imgye1 = int(input("임계값 1 : "))
print("**임계값2 이상은 모두 간주**")
imgye2 = int(input("임계값 2 : "))

togi = cv2.imread("/Users/jch/Desktop/cvstudy/Images/togi.jpg", cv2.IMREAD_COLOR)       #이미지 로드

filecount = 1       #파일번호 카운트

for i in range(1, imgye1+1): 
    for j in range(1, imgye2+1):
        transtogi = cv2.Canny(togi, i, j)       #도면화
        filename = "/Users/jch/Desktop/cvstudy/file/file%d_(%d, %d).jpg" %(filecount, i, j)     #도면 이름 설정
        cv2.imwrite(filename, transtogi)        #도면 저장
        print("%d" %filecount)
        filecount += 1

print("작업이 종료되었습니다.")