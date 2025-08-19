import streamlit as st

# MBTI 궁합 데이터 (샘플)
compatibility = {
    "ENTP": ["INFJ", "ENFP"],
    "INFJ": ["ENTP", "ENFP"],
    "ISTJ": ["ESFP", "ESTP"],
    "ENFP": ["INFJ", "ENTP"],
    # ... 전체 16유형 데이터 작성
}

# 페이지 제목
st.title("🌟 MBTI 궁합 기반 진로 교육 앱")

# 사용자 MBTI 입력
user_mbti = st.selectbox("당신의 MBTI를 선택하세요:", list(compatibility.keys()))

# 결과 출력
if user_mbti:
    st.subheader(f"🔮 {user_mbti}와 잘 맞는 MBTI 유형은?")
    matches = compatibility.get(user_mbti, [])
    if matches:
        st.success(", ".join(matches))
    else:
        st.warning("아직 데이터가 준비되지 않았습니다.")

# 추가 기능 (예: 두 사람 MBTI 궁합 보기)
st.subheader("👥 두 사람의 MBTI 궁합 보기")
col1, col2 = st.columns(2)
mbti1 = col1.selectbox("첫 번째 MBTI", list(compatibility.keys()), key="mbti1")
mbti2 = col2.selectbox("두 번째 MBTI", list(compatibility.keys()), key="mbti2")

if st.button("궁합 확인"):
    if mbti2 in compatibility.get(mbti1, []):
        st.success(f"{mbti1} 와(과) {mbti2}는 잘 맞는 조합이에요! 🤝")
    else:
        st.error(f"{mbti1} 와(과) {mbti2}는 서로 다른 스타일이 많아요. 협력 시 주의가 필요합니다 ⚡")
