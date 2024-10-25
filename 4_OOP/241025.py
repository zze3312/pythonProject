from random import randint

#test

# 성적표
class Student():

    def __init__(self, name):
        self.student = dict()
        self.student["name"] = name
        self.student["korean"] = self.student_grade()
        self.student["english"] = self.student_grade()
        self.student["math"] = self.student_grade()
        self.student["python"] = self.student_grade()
        self.student["stdAvg"] = self.student_avg(self.student)

    def student_sum(self, std):
        return std["korean"] + std["english"] + std["math"] + std["python"]

    def student_avg(self, std):
        return self.student_sum(std) / 4

    def toString(self):
        print(f"{self.student["name"]}\t{self.student["korean"]}\t\t{self.student["english"]}\t\t{self.student["math"]}\t\t{self.student["python"]}\t\t\t{self.student["stdAvg"]}")

    def student_grade(self):
        return randint( 0, 100)

def grade_cell(student_list):
    student_cnt = len(student_list)
    korean_sum = 0
    english_sum = 0
    math_sum = 0
    python_sum = 0
    student_avg_sum = 0

    print(f"{'성적표':^50}")
    print("-" * 50)
    print("이름", "국어", "영어", "수학", "파이썬", "평균", sep="\t\t")
    print("-" * 50)
    for std in student_list:
        Student.toString(std)
        korean_sum += std.student["korean"]
        english_sum += std.student["english"]
        math_sum += std.student["math"]
        python_sum += std.student["python"]
        student_avg_sum += std.student["stdAvg"]
    print("-" * 50)
    print(
        f"평균\t\t{korean_sum / student_cnt}\t{english_sum / student_cnt}\t{math_sum / student_cnt}\t{python_sum / student_cnt}\t\t{student_avg_sum / student_cnt}")


students = list()
students.append(Student("박선후"))
students.append(Student("황은비"))
students.append(Student("김승수"))
students.append(Student("조세빈"))

grade_cell(students)
print("")

from random import randint

# 로또 판매기
class Lotto:
    def __init__(self, cnt, auto_yn):
        self.cnt = cnt
        self.autoYn = auto_yn


    # 로또 구매 프로세스
    def buy(self):
        buy_cnt = 0
        lotto_list = list()

        # 구매한 장수만큼 반복
        while buy_cnt < self.cnt:
            # 자동구매
            if self.autoYn.upper() == 'Y':
                lotto = []
                num_cnt = 0
                #랜덤으로 같지 않은 숫자 6개 뽑음
                while num_cnt < 6:
                    num = randint(1, 45)
                    if num in lotto:
                        continue
                    else:
                        lotto.append(num)
                    num_cnt += 1
            # 수동구매
            else :
                lotto = input("구매하실 로또 번호를 입력해주세요(띄어쓰기로 구분) : ").split()
                # 입력한 숫자가 유효값인지 체크(정상 : True/불량 :False가 나오므로 reverse해줌)
                if not self.lottoCheck(lotto):
                    continue
            # 구매한 숫자를 오름차순으로 정렬
            lotto.sort()
            # 로또 한장으로 리스트에 저장
            lotto_list.append(lotto)
            buy_cnt += 1

        print("=" * 60)
        print(f"{'구매한 로또':^60}")
        print("=" * 60)
        for lotto in lotto_list:
            print(lotto)
        print("=" * 60)

        return lotto_list

    # 수동 입력 시 유효성 체크
    def lottoCheck(self, lotto):
        if len(lotto) != 6:
            print("숫자를 6개 선택해 주세요")
            return False

        for i in range(len(lotto)):
            try:
                num = int(lotto[i])
            except ValueError:
                print("숫자가 아닌 값이 입력 되었습니다. 다시 입력해 주세요")
                return False

            if num > 45 or num < 1 :
                print("선택하실 수 있는 숫자는 1~45 입니다. 다시 입력해 주세요")
                return False

            for j in range(len(lotto)):
                if lotto[i] == lotto[j] and i != j:
                    print("중복된 숫자가 있습니다. 다시 입력해주세요")
                    return False

        return True

# 사용자 입력값 체크
def inputCheck(cnt, money, autoYn):
    if cnt > 5 or cnt < 1:
        print("로또는 1~5장 구매하실 수 있습니다.")
        return False

    if money < cnt * 1000:
        print("금액이 부족합니다. 금액을 확인해 주세요")
        return False

    if autoYn.upper() != 'Y' and autoYn.upper() != 'N':
        print("자동 여부에 입렫된 값이 잘못된 값입니다")
        return False

    return True

# 당첨번호 확인
def result(lotto_list):
    success_lotto = list()
    cnt = 0
    # 당첨번호 + 보너스번호 랜덤으로 받기
    while cnt < 7:
        num = randint(1, 45)
        if num in success_lotto:
            continue
        else:
            success_lotto.append(num)
        cnt += 1

    print("당첨 번호 : ", success_lotto[0], success_lotto[1], success_lotto[2], success_lotto[3], success_lotto[4], success_lotto[5], "/ 보너스 번호 : ", success_lotto[6], sep="\t")

    # 사용자가 구매한 로또랑 당첨번호랑 비교
    for lotto in lotto_list:
        scs_cnt = 0
        bonusYn = False
        for lotto_num in lotto:
            if lotto_num in success_lotto and lotto_num != success_lotto[6]:
                scs_cnt += 1
            if lotto_num == success_lotto[6]:
                bonusYn = True

        if scs_cnt == 6:
            print("로또 결과 : 축하합니다! 1등 당첨입니다")
        elif scs_cnt == 5 and bonusYn:
            print("로또 결과 : 축하합니다! 2등 당첨입니다")
        elif scs_cnt == 5:
            print("로또 결과 : 축하합니다! 3등 당첨입니다")
        elif scs_cnt == 4:
            print("로또 결과 : 축하합니다! 4등 당첨입니다")
        elif scs_cnt == 3:
            print("로또 결과 : 축하합니다! 5등 당첨입니다")
        else:
            print("로또 결과 : 아쉽지만 당첨되지 않으셨습니다")

    print("=" * 60)




lotto_list = list()

try :
    lottoCnt = int(input("구매하실 로또의 개수를 입력하세요(최대 5장) : "))
    userPay = int(input("지불하실 금액을 입력하세요(장당 1000원) : "))
    autoYn = input("로또를 자동으로 구매하시겠습니까? (자동:y,수동:n) : ")
except ValueError:
        print("숫자가 아닌 다른 문자가 입력되었습니다. 입력을 확인해 주세요")
        exit()

if inputCheck(lottoCnt, userPay, autoYn):
    print(f"거스름돈 {userPay - (lottoCnt * 1000)}원과 로또 {lottoCnt}장을 받으셨습니다")

    lotto = Lotto(lottoCnt, autoYn)
    lotto_list = lotto.buy()



go_game = True
while go_game:
    user_go_yn = input("번호를 다시 선택 하시겠습니까? (예:y,아니오:n) : ")
    if user_go_yn.upper() == 'N':
        go_game = False
    else:
        lotto_list = lotto.buy()


if len(lotto_list) > 0 :
    result(lotto_list)
else:
    print("구매한 로또가 없습니다")