import os
import sys
from dotenv import load_dotenv

# Ensure 'src' is in the python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from translation_agent import translate

load_dotenv()

if __name__ == "__main__":
    source_text = "이 제품은 쑥 성분이 고농축으로 들어있어 피부 진정에 탁월합니다. 또한 미백 기능성 원료가 함유되어 칙칙한 피부를 환하게 밝혀주는 순한 화이트닝 앰플입니다."
    
    print("--- Source Text ---")
    print(source_text)
    print("\n--- Translating... ---")
    
    # Using 'USA' as country context, though the updated logic forces US K-Beauty persona regardless
    translation = translate(
        source_lang="Korean",
        target_lang="English",
        source_text=source_text,
        country="USA"
    )
    
    print("\n--- Result ---")
    print(translation)
