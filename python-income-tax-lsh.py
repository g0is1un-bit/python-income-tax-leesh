# 소득과 세금 변수 선언
income = 4500  # 단위: 만원
tax = 0        # 세금 변수 초기화

# 소득 수준 분류
if income >= 10000:
    level = "고소득자"
    tax = income * 0.3
elif income >= 5000:
    level = "중소득자"
    tax = income * 0.2
else:
    level = "저소득자"
    tax = income * 0.1

# 결과 출력
print("소득 수준:", level)
print("소득 금액:", income, "만원")
print("납부할 세금:", int(tax), "만원")
