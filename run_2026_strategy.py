import translation_agent as ta
import os
from dotenv import load_dotenv

load_dotenv()

# 2026 마케팅 전략 보고서에 나온 핵심 사례 3가지
test_cases = [
    {
        "name": "Case 1: 쑥(Mugwort) 완전 제거 테스트",
        "text": "이 앰플은 고농축 쑥 추출물이 함유되어 붉은기를 빠르게 진정시킵니다.",
        "category": "skincare"
    },
    {
        "name": "Case 2: 엘로엘 '딸기우유' 선쿠션 (경험 번역)",
        "text": "단순한 톤업이 아니라, 바르는 순간 딸기우유처럼 생기 있는 핑크빛 피부를 연출해주는 선쿠션입니다.",
        "category": "makeup"
    },
    {
        "name": "Case 3: 에스네이처 '쌀뜨물' 세안 (친숙한 개념)",
        "text": "쌀뜨물로 세안한 듯, 칙칙한 피부를 뽀얗고 투명하게 만들어주는 미백 효소 세안제입니다.",
        "category": "body_hair"
    }
]

print("=== 2026 K-Beauty Strategy Agent Test ===\n")

for case in test_cases:
    print(f"▶ Testing {case['name']}...")
    print(f"[Original]: {case['text']}")
    
    # 에이전트 실행
    translation = ta.translate(
        source_lang="Korean",
        target_lang="English",
        source_text=case['text'],
        country="USA",
        category=case.get('category', 'general')
    )
    
    print(f"[Agent Result]: {translation}\n")
    print("-" * 60 + "\n")