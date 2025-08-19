import streamlit as st

# 🎭 MBTI 궁합 데이터 (샘플)
compatibility = {
    "ENTP": ["INFJ 💡", "ENFP 🌈"],
    "INFJ": ["ENTP 🔥", "ENFP 🌟"],
    "ISTJ": ["ESFP 🎶", "ESTP ⚡"],
    "ENFP": ["INFJ 🌙", "ENTP 🚀"],
    "INTP": ["ENTJ 🧠", "ENFP 🌻"],
    "ESFP": ["ISTJ 🛠️", "ISFJ 💎"],
    # … 전체 16유형 채우기 가능
}

# 🎉 페이지 꾸미기
st.set_page_config(page_title="MBTI 궁합 진로 앱", page_icon="💫", layout="centered")

st.markdown("""
# 🌟 MBTI 궁합 기반 진로 교육 앱 🌟  
여러분의 **MBTI**를 입력하면  
✨ 가장 잘 맞는 MBTI ✨를 알려드립니다!  

💡 *진로 교육 & 협업 스타일 분석에도 활용해보세요!* 🚀  
""")

# 🔮 사용자 MBTI 선택
user_mbti = st.selectbox("당신의 MBTI를 선택해주세요 🧩", list(compatibility.keys()))

# 결과 출력
if user_mbti:
    st.subheader(f"🔮 {user_mbti}와 환상의 케미를 자랑하는 MBTI는?")
    matches = compatibility.get(user_mbti, [])
    if matches:
        st.success(" 💕 ".join(matches))
        st.markdown("🌈 함께하면 **최고의 팀워크**를 발휘할 수 있어요! ✨🤝")
    else:
        st.warning("😢 아직 이 MBTI의 궁합 데이터는 준비되지 않았어요.")

# 👥 두 사람 MBTI 궁합
st.markdown("---")
st.subheader("👥 두 사람의 MBTI 궁합 확인하기 💞")

col1, col2 = st.columns(2)
mbti1 = col1.selectbox("첫 번째 MBTI 선택 🎭", list(compatibility.keys()), key="mbti1")
mbti2 = col2.selectbox("두 번째 MBTI 선택 🎭", list(compatibility.keys()), key="mbti2")

if st.button("✨ 궁합 확인하기 ✨"):
    if mbti2 in compatibility.get(mbti1, []):
        st.balloons()
        st.success(f"🎉 {mbti1} 와(과) {mbti2}는 **찰떡궁합 케미**! 🌟🔥")
        st.markdown("🤝 함께라면 **완벽한 협업**이 가능해요! 🚀💡")
    else:
        st.error(f"⚡ {mbti1} 와(과) {mbti2}는 조금 다른 스타일 😅")
        st.markdown("💡 하지만 서로 배울 점이 많을 수 있어요! 🌱✨")
