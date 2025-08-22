import streamlit as st

cat_breeds = {
    "샴(Siamese)": {
        "특징": "날씬한 체형, 큰 귀, 파란 눈 👀",
        "성격": "활발하고 수다쟁이, 사람과 교감 잘함 💬",
        "사진": "https://upload.wikimedia.org/wikipedia/commons/5/56/Siam_lilacpoint.jpg"
    },
    "페르시안(Persian)": {
        "특징": "풍성한 털, 납작한 얼굴, 우아한 외모 ✨",
        "성격": "온화하고 느긋하며 차분함 😴",
        "사진": "https://upload.wikimedia.org/wikipedia/commons/3/32/Persian_cat_by_Tomitheos.JPG"
    },
    "러시안 블루(Russian Blue)": {
        "특징": "은빛 푸른 털, 초록빛 눈 💎",
        "성격": "조용하고 차분, 낯가림 심함 🙈",
        "사진": "https://upload.wikimedia.org/wikipedia/commons/5/5f/Russian_Blue_003.jpg"
    },
    "메인쿤(Maine Coon)": {
        "특징": "대형묘, 갈기 같은 털, 튼튼한 체형 🦁",
        "성격": "사교적이고 충성심 강함 ❤️",
        "사진": "https://upload.wikimedia.org/wikipedia/commons/3/3a/Maine_Coon_cat_by_Tomitheos.JPG"
    },
    "아비시니안(Abyssinian)": {
        "특징": "짧은 갈색 털, 날씬하고 우아함 🐆",
        "성격": "활발하고 호기심 많음 🔍",
        "사진": "https://upload.wikimedia.org/wikipedia/commons/0/0b/TawnyAbyssinian.jpg"
    },
    "벵갈(Bengal)": {
        "특징": "야생 표범 같은 무늬 🐆",
        "성격": "에너지가 넘치고 장난꾸러기 😼",
        "사진": "https://upload.wikimedia.org/wikipedia/commons/e/e5/Bengal_Cat_%28Fia_Fia%29.jpg"
    },
    "스코티시 폴드(Scottish Fold)": {
        "특징": "귀가 접힌 독특한 외모 👂",
        "성격": "차분하고 애교 많음 💞",
        "사진": "https://upload.wikimedia.org/wikipedia/commons/6/68/Scottish_Fold_cat.jpg"
    },
    "스핑크스(Sphynx)": {
        "특징": "털이 거의 없음, 따뜻한 피부 🩶",
        "성격": "호기심 많고 장난기 있음 🎭",
        "사진": "https://upload.wikimedia.org/wikipedia/commons/c/c2/Sphinx2_July_2006.jpg"
    },
    "노르웨이 숲(Norwegian Forest Cat)": {
        "특징": "풍성한 털, 큰 체격, 추위 강함 ❄️",
        "성격": "온화하고 느긋함 🌲",
        "사진": "https://upload.wikimedia.org/wikipedia/commons/b/b3/Norwegian_Forest_Cat_3.jpg"
    },
    "터키시 앙고라(Turkish Angora)": {
        "특징": "흰색 긴 털, 푸른 눈 ✨",
        "성격": "우아하고 독립적 🕊",
        "사진": "https://upload.wikimedia.org/wikipedia/commons/7/75/Turkish_Angora_white_cat.jpg"
    },
    "터키시 반(Turkish Van)": {
        "특징": "흰색 털과 머리·꼬리 색, 수영 잘함 🏊",
        "성격": "활발하고 독립심 강함 🐾",
        "사진": "https://upload.wikimedia.org/wikipedia/commons/f/f2/Turkish_Van_Cat.jpg"
    },
    "오리엔탈 쇼트헤어(Oriental Shorthair)": {
        "특징": "샴과 비슷, 다양한 색의 털 🎨",
        "성격": "매우 수다스럽고 활발 💬",
        "사진": "https://upload.wikimedia.org/wikipedia/commons/f/f5/Oriental_Shorthair_tortie.jpg"
    },
    "브리티시 쇼트헤어(British Shorthair)": {
        "특징": "둥근 얼굴, 푸른 털, 단단한 체형 ⚪",
        "성격": "차분하고 느긋함 🛋",
        "사진": "https://upload.wikimedia.org/wikipedia/commons/9/9d/Britishblue.jpg"
    },
    "아메리칸 쇼트헤어(American Shorthair)": {
        "특징": "짧은 은색 털, 근육질 💪",
        "성격": "활발하지만 순종적 🤗",
        "사진": "https://upload.wikimedia.org/wikipedia/commons/5/59/American_Shorthair_-_brown_tabby.jpg"
    },
    "코리안 쇼트헤어(Korean Shorthair)": {
        "특징": "한국 길고양이, 무늬와 색 다양 🐾",
        "성격": "독립적이고 영리함 🧠",
        "사진": "https://upload.wikimedia.org/wikipedia/commons/2/23/Korean_shorthair_cat.jpg"
    },
    "랙돌(Ragdoll)": {
        "특징": "긴 털, 파란 눈, 인형처럼 늘어짐 🧸",
        "성격": "온순하고 사람 좋아함 🥰",
        "사진": "https://upload.wikimedia.org/wikipedia/commons/6/69/Ragdoll_from_Gatil_Ragbelas.jpg"
    },
    "버만(Birman)": {
        "특징": "푸른 눈, 흰 장갑 무늬 🧤",
        "성격": "차분하고 충성심 강함 💙",
        "사진": "https://upload.wikimedia.org/wikipedia/commons/b/b3/Birman_Cat.jpg"
    },
    "샤르트뢰(Chartreux)": {
        "특징": "푸른 회색 털, 미소 같은 얼굴 😊",
        "성격": "조용하고 충성심 강함 🐾",
        "사진": "https://upload.wikimedia.org/wikipedia/commons/d/dc/Chartreux_cat_France.jpg"
    },
    "싱가푸라(Singapura)": {
        "특징": "작은 체구, 크고 맑은 눈 👁️",
        "성격": "장난꾸러기, 사교적 💃",
        "사진": "https://upload.wikimedia.org/wikipedia/commons/9/9e/Singapura_cat.jpg"
    },
    "히말라얀(Himalayan)": {
        "특징": "페르시안+샴 혼합, 긴 털, 파란 눈 🏔",
        "성격": "온화하고 다정함 🌸",
        "사진": "https://upload.wikimedia.org/wikipedia/commons/8/8b/Himalayan_cat.jpg"
    },
    "라팜(LaPerm)": {
        "특징": "곱슬곱슬한 털 🎀",
        "성격": "애교 많고 활발함 💞",
        "사진": "https://upload.wikimedia.org/wikipedia/commons/4/4c/LaPerm_cat.jpg"
    },
    "맹크스(Manx)": {
        "특징": "꼬리가 짧거나 없음 🌀",
        "성격": "충성심 강하고 민첩함 🏃",
        "사진": "https://upload.wikimedia.org/wikipedia/commons/f/fb/Manx_cat.jpg"
    },
    "오시캣(Ocicat)": {
        "특징": "야생 같은 점박이 무늬 🐆",
        "성격": "활발하고 외향적 😸",
        "사진": "https://upload.wikimedia.org/wikipedia/commons/c/c0/Ocicat_Brown_Spotted.jpg"
    },
    "발리니즈(Balinese)": {
        "특징": "샴과 비슷하나 긴 털 🪶",
        "성격": "수다쟁이, 사교적 💬",
        "사진": "https://upload.wikimedia.org/wikipedia/commons/f/fb/Balinese-cat.jpg"
    },
    "데본 렉스(Devon Rex)": {
        "특징": "큰 귀, 곱슬 털, 독특한 외모 👂",
        "성격": "장난꾸러기, 활발 🤪",
        "사진": "https://upload.wikimedia.org/wikipedia/commons/b/b6/Devon_Rex_-_Black_tabby.jpg"
    },
    "코니시 렉스(Cornish Rex)": {
        "특징": "짧고 곱슬한 털, 날씬한 몸 ✨",
        "성격": "사교적이고 장난기 많음 🎉",
        "사진": "https://upload.wikimedia.org/wikipedia/commons/a/ab/Cornish_Rex_red_tabby.jpg"
    },
    "재패니즈 밥테일(Japanese Bobtail)": {
        "특징": "짧은 꼬리, 삼색 털(행운 상징) 🍀",
        "성격": "활발하고 친근함 😻",
        "사진": "https://upload.wikimedia.org/wikipedia/commons/7/7e/JapaneseBobtailBlueEyed.jpg"
    },
    "이집션 마우(Egyptian Mau)": {
        "특징": "점박이 무늬, 날렵한 체형 🐆",
        "성격": "활발하고 빠름 ⚡",
        "사진": "https://upload.wikimedia.org/wikipedia/commons/0/0b/Egyptian_Mau_Brown_Spotted.jpg"
    },
    "하바나 브라운(Havana Brown)": {
        "특징": "짙은 갈색 털, 초록 눈 🌿",
        "성격": "호기심 많고 장난꾸러기 🙃",
        "사진": "https://upload.wikimedia.org/wikipedia/commons/4/44/Havana_Brown_cat.jpg"
    }
}

# Streamlit UI
st.set_page_config(page_title="🐱 고양이 품종 도감", page_icon="🐾", layout="centered")

st.title("🐾 고양이 품종 특징 도감 🐾")
st.write("고양이 품종을 선택하면 사진과 특징을 확인할 수 있어요! 😻")

breed = st.selectbox("고양이 품종을 선택하세요:", list(cat_breeds.keys()))

if breed:
    st.subheader(f"✨ {breed} ✨")
    st.image(cat_breeds[breed]["사진"], width=350)
    st.write(f"**특징:** {cat_breeds[breed]['특징']}")
    st.write(f"**성격:** {cat_breeds[breed]['성격']}")
    st.success(f"🐱 {breed}는 정말 매력적인 고양이에요!")
