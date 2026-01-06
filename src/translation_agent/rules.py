"""
K-Beauty Localization Rules Module
Defines the strict rules, banned terms, and marketing strategies for the US market.
"""

# Base Persona for the Agent
PERSONA = "You are a specialized Senior Copywriter & Localizer for the US Beauty Market (Sephora/Amazon) with 10 years of experience."

# 1. HSK Category Mapping
HSK_CATEGORIES = {
    "skincare": {
        "code": "3304.99",
        "name": "Skincare (기초화장용)",
        "strategy": "Focus on 'Skin Barrier', 'Clinical Results', and 'Microbiome Friendly'. Avoid listing ingredients without explaining the benefit.",
        "replacements": {
            "미백": "Brightening, Radiance, Glow, Even Tone",
            "순한": "Barrier Repair, Microbiome Friendly, Hypoallergenic",
            "쑥": "Artemisia, Nature-derived Soothing, K-Herb Complex",
            "한방": "Hanbang, Traditional Korean Herbal, Clean Beauty",
            "모공": "Pore Clarifying, Texturizing"
        }
    },
    "makeup": {
        "code": "3304.10-91",
        "name": "Makeup (색조화장용)",
        "strategy": "Focus on 'Flawless Finish', 'Long-wear', and 'Transfer-proof'. Avoid 'Natural' as it implies weak coverage.",
        "replacements": {
            "자연스러운": "Flawless, Seamless, Second-skin Finish",
            "착붙": "Long-wear, Transfer-proof, Crease-resistant",
            "지속력": "All-day Wear, Fade-proof",
            "물광": "Dewy Glow, Glass Skin, Luminous Finish",
            "딸기우유": "Vitalizing Pink Glow, Rosy Radiance"
        }
    },
    "body_hair": {
        "code": "3401/3305",
        "name": "Body & Hair (세정/두발용)",
        "strategy": "Focus on 'pH-balanced', 'Scalp Health', and 'Sulfate-free'. Avoid 'Squeaky Clean' or medical hair loss claims.",
        "replacements": {
            "뽀득뽀득": "pH-balanced, Sulfate-free, Hydrating Cleanse",
            "탈모": "Scalp Revitalizing, Volumizing, Root Fortifying",
            "한방샴푸": "Herbal Scalp Care, Root Enhancing Complex"
        }
    },
    "general": {
        "code": "General",
        "name": "General Beauty",
        "strategy": "Transcreate for US Consumer Psychology: Verification (Proof) > Experience > Specs.",
        "replacements": {
            "미백": "Brightening, Radiance, Even Tone",
            "화이트닝": "Brightening, Radiance",
            "약용": "Functional, Potent, Corrective, Clinical Grade",
            "트러블": "Blemish-prone, Clarifying, Breakout Care",
            "판매 1위": "Best-seller, Award-winning, Cult-favorite",
            "영양": "Potent Formula, Revitalizing, Clinical Grade"
        }
    }
}

# 2. Strict Ban List (Applies globally unless overridden)
GLOBAL_BAN_LIST = {
    "Whitening": "Brightening, Radiance, Glow",
    "Mugwort": "Artemisia, Nature-derived Soothing",
    "Gentle": "Barrier Repair, Hypoallergenic, Dermatologist Tested",
    "Oriental": "Hanbang, K-Herb",
    "Strawberry Milk": "Vitalizing Pink Glow, Rosy Radiance"
}

def get_rules_for_category(category_key: str = "general") -> str:
    """
    Returns a formatted string of rules for a specific category.
    
    Args:
        category_key (str): The HSK category or product type (e.g., 'skincare', 'makeup').
                          If the key is not found, defaults to 'general'.
    
    Returns:
        str: A comprehensive rule string including Strategy context, Mandatory Replacements, and the Global Ban List.
    """
    # Fallback logic: Default to 'general' if category is unknown or empty
    if not category_key or category_key not in HSK_CATEGORIES:
        category_key = "general"
        
    cat = HSK_CATEGORIES[category_key]
    
    rule_str = f"""
### [Target Category: {cat['name']} (HSK {cat['code']})]
**Strategic Intent**: {cat['strategy']}
*Why this matters?* In this category, US consumers prioritize {cat['strategy'].split('.')[0]}. 
We must shift from "Listing Specs" to "Verifying Benefits".

#### [Mandatory Replacements for {cat['name']}]
"""
    for kr, en in cat['replacements'].items():
        rule_str += f"- **{kr}** -> **{en}**\n"
        
    rule_str += "\n#### [Global Strict Ban List (CRITICAL FAILURE IF USED)]\n"
    for forbidden, replacement in GLOBAL_BAN_LIST.items():
        rule_str += f"- 🚫 **{forbidden}** -> 🟢 **{replacement}**\n"
        
    rule_str += """
#### [2026 Verification Strategy]
- **Abstract Adjectives** (e.g., Gentle, Good, Mild) -> **MUST BE CHANGED** to Verification Terms (e.g., Dermatologist Tested, Barrier Repair, Clinical Grade).
- **Prohibited**: Do not literally translate 'Water Glow' (Mul-gwang). Use 'Glass Skin' or 'Dewy Finish'.
"""
        
    return rule_str
