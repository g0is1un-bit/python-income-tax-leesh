import streamlit as st

st.set_page_config(page_title="소득·세금 계산기", page_icon="💸", layout="centered")

# -----------------------------
# 설정
# -----------------------------
st.title("💸 소득 수준 분류 & 세금 계산기")
st.caption("기본 예시: 저·중·고 소득 구간에 따라 단일세율 적용 (예: 10%/20%/30%)")

with st.expander("⚙️ 세율/구간 설정 보기(열어서 수정 가능)"):
    col_a, col_b = st.columns(2)
    with col_a:
        t_low = st.number_input("저소득 세율(%)", min_value=0.0, max_value=100.0, value=10.0, step=0.5)
        t_mid = st.number_input("중소득 세율(%)", min_value=0.0, max_value=100.0, value=20.0, step=0.5)
        t_high = st.number_input("고소득 세율(%)", min_value=0.0, max_value=100.0, value=30.0, step=0.5)
    with col_b:
        thr_mid = st.number_input("중소득 하한 (만원)", min_value=0.0, value=5000.0, step=100.0, help="이 값 이상이면 중소득")
        thr_high = st.number_input("고소득 하한 (만원)", min_value=0.0, value=10000.0, step=100.0, help="이 값 이상이면 고소득")

st.divider()

# -----------------------------
# 입력
# -----------------------------
income = st.number_input("소득 (만원)", min_value=0.0, value=4500.0, step=50.0, format="%.0f")
calc_btn = st.button("계산하기", type="primary")

# -----------------------------
# 로직
# -----------------------------
def classify_and_tax(income_amt: float):
    if income_amt >= thr_high:
        level = "고소득자"
        rate = t_high / 100.0
    elif income_amt >= thr_mid:
        level = "중소득자"
        rate = t_mid / 100.0
    else:
        level = "저소득자"
        rate = t_low / 100.0
    tax = income_amt * rate
    return level, rate, tax

# -----------------------------
# 출력
# -----------------------------
if calc_btn or "auto_run" not in st.session_state:
    st.session_state["auto_run"] = True
    level, rate, tax = classify_and_tax(income)

    st.subheader("결과")
    col1, col2, col3 = st.columns(3)
    col1.metric("소득 수준", level)
    col2.metric("소득 금액(만원)", f"{income:,.0f}")
    col3.metric("세율(%)", f"{rate*100:.1f}")

    st.success(f"납부할 세금: **{tax:,.0f} 만원**")

    st.info(
        "이 예시는 간단한 ‘단일세율’ 적용 예시입니다. 실제 과세는 누진세/공제 등 제도에 따라 다릅니다.",
        icon="ℹ️",
    )

st.caption("© 예시 앱 — Streamlit로 배포 가능")
