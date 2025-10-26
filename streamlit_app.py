import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="수학 개념 퀴즈", layout="wide")

# 간단한 샘플 문제 은행 (실제 앱에서는 외부 JSON/DB로 분리)
QUESTION_BANK = {
    "중학교 1학년": {
        "유리수와 소수": [
            {"id": 1, "question": "0.25는 분수로?", "choices": ["1/2", "1/3", "1/4", "2/5"], "answer": "1/4", "concept": "소수→분수"},
            {"id": 2, "question": "-3과 2의 합은?", "choices": ["-5", "-1", "1", "5"], "answer": "-1", "concept": "정수 연산"}
        ],
        "문자와 식": [
            {"id": 3, "question": "2x = 8이면 x는?", "choices": ["2", "3", "4", "6"], "answer": "4", "concept": "일차방정식"},
            {"id": 4, "question": "식 3(a+2) 전개하면?", "choices": ["3a+6", "3a+2", "a+6", "9a+6"], "answer": "3a+6", "concept": "식의 전개"}
        ]
    },
    "고등학교 1학년": {
        "함수의 개념": [
            {"id": 5, "question": "함수 f(x)=x^2의 f(2)는?", "choices": ["2", "4", "8", "0"], "answer": "4", "concept": "함수값"},
            {"id": 6, "question": "일대일 함수의 성질은?", "choices": ["역함수 존재", "항상 증가", "항상 감소", "주기적"], "answer": "역함수 존재", "concept": "역함수"}
        ],
        "집합과 명제": [
            {"id": 7, "question": "공집합의 부분집합 개수는?", "choices": ["0", "1", "inf", "2"], "answer": "1", "concept": "부분집합"},
            {"id": 8, "question": "집합 A={1,2}와 B={2,3}의 교집합은?", "choices": ["{1}", "{2}", "{3}", "{}"], "answer": "{2}", "concept": "교집합"}
        ]
    }
}

def get_units(level):
    return list(QUESTION_BANK.get(level, {}).keys())

def generate_quiz(level, unit, n):
    bank = QUESTION_BANK[level][unit][:]
    random.shuffle(bank)
    return bank[:n]

# 세션 상태 초기화
if "quiz" not in st.session_state:
    st.session_state.quiz = []
if "index" not in st.session_state:
    st.session_state.index = 0
if "user_answers" not in st.session_state:
    st.session_state.user_answers = []
if "wrong_counts" not in st.session_state:
    st.session_state.wrong_counts = {}

st.title("수학 개념 퀴즈")
st.write("학년/단원별로 문제를 풀고 오답을 분석해 취약 개념을 알려드립니다.")

with st.sidebar:
    st.header("퀴즈 설정")
    level = st.selectbox("교육과정(학년군)", ["중학교 1학년", "고등학교 1학년"])
    units = get_units(level)
    unit = st.selectbox("단원 선택", units)
    qcount = st.slider("문제 수", min_value=1, max_value=min(5, len(QUESTION_BANK[level][unit])), value=3)
    if st.button("문제 생성"):
        st.session_state.quiz = generate_quiz(level, unit, qcount)
        st.session_state.index = 0
        st.session_state.user_answers = []
        st.session_state.wrong_counts = {}
        st.experimental_rerun()

col1, col2 = st.columns([3,1])

with col1:
    if not st.session_state.quiz:
        st.info("사이드바에서 학년과 단원을 선택하고 '문제 생성'을 눌러 시작하세요.")
    else:
        i = st.session_state.index
        q = st.session_state.quiz[i]
        st.markdown(f"### 문제 {i+1}/{len(st.session_state.quiz)}")
        st.write(q["question"])
        choice = st.radio("보기", q["choices"], key=f"q{i}")
        if st.button("제출", key=f"submit_{i}"):
            st.session_state.user_answers.append({"id": q["id"], "selected": choice, "answer": q["answer"], "concept": q["concept"]})
            if choice != q["answer"]:
                st.session_state.wrong_counts[q["concept"]] = st.session_state.wrong_counts.get(q["concept"], 0) + 1
            st.session_state.index += 1
            if st.session_state.index >= len(st.session_state.quiz):
                st.success("퀴즈 완료! 우측에서 결과를 확인하세요.")
            st.experimental_rerun()

with col2:
    st.header("진행/결과")
    if st.session_state.quiz:
        st.write(f"현재 문제: {st.session_state.index} / {len(st.session_state.quiz)}")
        if st.session_state.user_answers:
            correct = sum(1 for a in st.session_state.user_answers if a["selected"] == a["answer"])
            st.write(f"정답: {correct}  오답: {len(st.session_state.user_answers)-correct}")
        if st.session_state.index >= len(st.session_state.quiz) and st.session_state.quiz:
            total = len(st.session_state.quiz)
            correct = sum(1 for a in st.session_state.user_answers if a["selected"] == a["answer"])
            st.metric("총점", f"{correct} / {total}")
            st.subheader("오답 분석 (취약 개념)")
            if st.session_state.wrong_counts:
                df = pd.DataFrame.from_dict(st.session_state.wrong_counts, orient="index", columns=["오답수"])
                df = df.sort_values("오답수", ascending=False)
                st.table(df)
                st.bar_chart(df)
                st.subheader("추천 학습 단서")
                top_concepts = df.index.tolist()[:3]
                for c in top_concepts:
                    st.write(f"- {c}: 해당 개념의 기본 이론과 예제 문제 풀이를 반복하세요.")
            else:
                st.success("모든 문제 정답입니다. 잘하셨습니다!")
            if st.button("다시 풀기"):
                st.session_state.quiz = []
                st.session_state.index = 0
                st.session_state.user_answers = []
                st.session_state.wrong_counts = {}
                st.experimental_rerun()
