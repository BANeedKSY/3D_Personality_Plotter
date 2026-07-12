# 3D性格分析ツール用定数データファイル


DEFALUT_DATA_VERSION = "0.10"

# データ範囲、デフォルトペルソナ・データベースの定義

STEP_MAX = 5
STEP_MIN = -5

DATA_LABELS = {
    "GRP": "グループ",
    "NAM": "名前", 
    "CAT": "カテゴリ",
    "DSC": "説明",
    "VAL": "値"
}


# データ定義でのグループ識別用。並べ方をソートできるように、グループ名とは独立したラベルを昇順で定義
GROUPE_IDS = {
# 注「"nnn" : "nnnn"」のコロン前後のスペースは削除しないこと！　（GROUPE_IDSの置換処理対応のため。） 
    "ORG" : "G00",
    "ANM" : "G10",
    "HUM" : "G20",
    "GEN" : "G30",
    "CAL" : "G40",
    "LIF" : "G50",
    "AI"  : "G90",
    "DEF" : "G98",    # カスタム以外のグループをまとめるための仮のグループ名
    "CST" : "G99"
}

GROUPE_NAME = {
    GROUPE_IDS["ORG"]: "原点",
    GROUPE_IDS["ANM"]: "動物",
    GROUPE_IDS["HUM"]: "人物",
    GROUPE_IDS["GEN"]: "時代",
    GROUPE_IDS["CAL"]: "文化圏",
    GROUPE_IDS["LIF"]: "生活志向",
    GROUPE_IDS["AI"]: "AI",
    GROUPE_IDS["DEF"]: "既定値",    # カスタム以外のグループをまとめるための仮のグループ名
    GROUPE_IDS["CST"]: "カスタム"
}

GROUPE_INITIAL_DISPLAY = {
    GROUPE_IDS["ORG"]: True,
    GROUPE_IDS["ANM"]: True,
    GROUPE_IDS["HUM"]: True,
    GROUPE_IDS["GEN"]: False,
    GROUPE_IDS["CAL"]: False,
    GROUPE_IDS["LIF"]: False,
    GROUPE_IDS["AI"]: True,
    GROUPE_IDS["DEF"]: True,    # カスタム以外のグループをまとめるための仮のグループ名
    GROUPE_IDS["CST"]: True
}


AXIS_PREFIX = ""
AXIS_SUFFIX = "軸"

AXIS_LABELS = {
# 注「"N" : "N"」のコロン前後のスペースは削除しないこと！　（AXIS_LABELSの置換処理対応のため。） 
    "X" : "X", 
    "Y" : "Y", 
    "Z" : "Z", 
    "a" : "α",
    "A" : "A",
    "B" : "B",
    "C" : "C",
    "D" : "D",
    "E" : "E",
}


AXIS_NAME = {
        AXIS_LABELS["X"]: "方向性",
        AXIS_LABELS["Y"]: "動機付", 
        AXIS_LABELS["Z"]: "立脚点",
        AXIS_LABELS["a"]: "快楽志向",
        AXIS_LABELS["A"]: "文脈感度",
        AXIS_LABELS["B"]: "重視対象",
        AXIS_LABELS["C"]: "協調性",
        AXIS_LABELS["D"]: "権威格差",
        AXIS_LABELS["E"]: "事後反応",
}

AXIS_DESC = {
        AXIS_LABELS["X"]: "現状維持⇔現状打破",
        AXIS_LABELS["Y"]: "自己完結⇔対人依存", 
        AXIS_LABELS["Z"]: "具体的⇔抽象的",
        AXIS_LABELS["a"]: "情緒的💕⇔感覚的🍖",
        AXIS_LABELS["A"]: "不文律に鈍感⇔敏感",
        AXIS_LABELS["B"]: "事実志向⇔価値観志向",
        AXIS_LABELS["C"]: "頑固⇔素直・優柔不断",
        AXIS_LABELS["D"]: "権威格差に鈍感⇔敏感",
        AXIS_LABELS["E"]: "過去を引きづる⇔気にしない",
}

####            ChatGPT,   Grok,  Gemini,  Claude

# df_default 用基礎データ
DEFAULT_PERSONAS = [
    #  記述書式  
    #    DATA_LABELS["GRP"]: 動物 、芸能人、政治家、経営者、研究者、AIなど  (既定値 / カスタム),          
    #    DATA_LABELS["GRP"]: G00, G10,  (GROUPE_LABEL)          
    #    DATA_LABELS["NAM"]: 個別名称,            
    #    DATA_LABELS["CAT"]: 小区分,    
    #    ----------------------------------------------------------------------------------
    #    AXIS_LABELS["X"]: 数値-5.0～5.0,   保守・秩序維持 　⇔　 革新・リベラル・新ルール作り
    #    AXIS_LABELS["Y"]: 数値-5.0～5.0,   自己完結 　⇔　 対人依存
    #    AXIS_LABELS["Z"]: 数値-5.0～5.0,   具体　⇔　抽象
    #    AXIS_LABELS["α"]: 数値-5.0～5.0,   審美的・情緒的（色気💕）　⇔　感覚的(食い気🍖🍶）
    #    ----------------------------------------------------------------------------------
    #    AXIS_LABELS["A"]: 数値-5.0～5.0,   暗黙の了解（不文律）に無頓着　⇔　暗黙の了解に敏感
    #    AXIS_LABELS["B"]: 数値-5.0～5.0,   価値の絶対性、普遍性(事実）を重視　⇔　価値の相対性（価値観）を重視
    #    AXIS_LABELS["C"]: 数値-5.0～5.0,   頑固　⇔　素直・柔軟・優柔不断
    #    AXIS_LABELS["D"]: 数値-5.0～5.0,   権威格差に鈍感（上下関係に無頓着）　⇔　権威格差に敏感（盲従、支配傾向大）
    #    AXIS_LABELS["E"]: 数値-5.0～5.0,   気にする、引きづる 　⇔　気にならない、全く堪えない
    #    ----------------------------------------------------------------------------------
    #    DATA_LABELS["DSC"]:個性の概要説明",
    #
    # --- 原点グループ ---
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["ORG"],
        DATA_LABELS["NAM"]: "原点",
        DATA_LABELS["CAT"]: "無味無臭無垢",
        AXIS_LABELS["X"]: 0,
        AXIS_LABELS["Y"]: 0,
        AXIS_LABELS["Z"]: 0,
        AXIS_LABELS["a"]: 0,
        AXIS_LABELS["A"]: 0,
        AXIS_LABELS["B"]: 0,
        AXIS_LABELS["C"]: 0, 
        AXIS_LABELS["D"]: 0,
        AXIS_LABELS["E"]: 0,
        DATA_LABELS["DSC"]: (
            "性格形成の原点（新生児・幼少期イメージ）。\n"
            "全軸0の状態。育ち方によってここから様々な方向に変化していく基準点として使用。\n"
            "幼い頃との振り返り比較用。"
            )
    },
    # --- 動物グループ ---
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["ANM"],
        DATA_LABELS["NAM"]: "女王蜂",
        DATA_LABELS["CAT"]: "統率型",
        AXIS_LABELS["X"]: -5.00, #　　　　　　　　　　　
        AXIS_LABELS["Y"]: 5.00,  #
        AXIS_LABELS["Z"]: 5.00,  #
        AXIS_LABELS["a"]: 3,     #  4,  2  -5      3
        AXIS_LABELS["A"]: 0,     #  4,  3,  5     -2 #不明
        AXIS_LABELS["B"]: 0,     #  1, -1,  5     -4 #不明
        AXIS_LABELS["C"]: -4.00, #  2, -3  -5     -4 
        AXIS_LABELS["D"]: -5.00, #  2,  3   5     -5
        AXIS_LABELS["E"]: 4.00,  #  1,  2   5      5
        DATA_LABELS["DSC"]: ( 
            "個としての意思よりも、群れ全体の秩序そのものを体現する存在。\n"
            "自らは動かず、周囲がすべてを解釈・実行することで初めて機能する、極めて抽象度の高い『象徴』としての生命体。\n"
            "自身は上位の権威を意識する必要がなく、状況の変化にもほぼ動じない。"
            ),  
    },

    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["ANM"],
        DATA_LABELS["NAM"]: "ボス猿",
        DATA_LABELS["CAT"]: "統率型",
        AXIS_LABELS["X"]: -4.0,  #  3,  2,  5,  -2
        AXIS_LABELS["Y"]: 5.0,   #  4, -3, -5,  -4
        AXIS_LABELS["Z"]: -4.0,  # -2, -2,  5,  -3
        AXIS_LABELS["a"]: 3,     #  4,  2  -5,   4
        AXIS_LABELS["A"]: 4,     #  4,  3,  5,   3
        AXIS_LABELS["B"]: 1,     #  1, -1,  5,  -2
        AXIS_LABELS["C"]: 2,     #  2, -3, -5,  -4 
        AXIS_LABELS["D"]: 2,     #  2,  3,  5,  -3
        AXIS_LABELS["E"]: -1,    #  1,  2,  5,  -1
        DATA_LABELS["DSC"]: (
            "実力主義でトップに上り詰め、群れを率いるリーダー。\n"
            "他者の顔色ではなく、自身の判断と力で意思決定する自己完結型。\n"
            "挑戦者の気配には敏感だが、頭を下げる相手はいないため権威への感度は低い。\n"
            "縄張りや序列への執着は残りやすい。",
            )
    },

    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["ANM"],
        DATA_LABELS["NAM"]: "一匹狼",
        DATA_LABELS["CAT"]: "孤高型",
        AXIS_LABELS["X"]: 5.0,   #  0,  1,  5   2
        AXIS_LABELS["Y"]: -5.00, # -5, -5, -5  -5
        AXIS_LABELS["Z"]: 5.0,   #  2, -1   5  -2
        AXIS_LABELS["a"]: 3,     # -5,  1  -5   3
        AXIS_LABELS["A"]: -5,    # -5,  1  -5  -5
        AXIS_LABELS["B"]: 3,     #  3   2  -5   2
        AXIS_LABELS["C"]: -5,    #  0  -2  -5  -5
        AXIS_LABELS["D"]: -5,    #  4  -3  -5  -5
        AXIS_LABELS["E"]: 2,     #  2   0  -5   4
        DATA_LABELS["DSC"]: (
            "群れの掟や既存の社会秩序を離れ、外部からの情報を完全に遮断して独自の掟のみに従う孤高の存在。z"
            "誰の顔色もうかがわず、誰の権威も認めない。"
            "荒野を進む中で過去の衝突を引きずることも少ない。自由と自立を極める。"
            )
    },
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["ANM"],
        DATA_LABELS["NAM"]: "飼いネコ",
        DATA_LABELS["CAT"]: "孤高型",
        AXIS_LABELS["X"]: 0.0,   # -2   1   3   0
        AXIS_LABELS["Y"]: -4.00, # -4  -4  -5  -5
        AXIS_LABELS["Z"]: -5.0,  #  2  -2   4  -3
        AXIS_LABELS["a"]: 4,     # -5   4  -5   5
        AXIS_LABELS["A"]: -3,    # -3   2  -5  -5
        AXIS_LABELS["B"]: 2,     #  2  -2  -5   4
        AXIS_LABELS["C"]: 1,     #  1  -2  -5  -4
        AXIS_LABELS["D"]: 3,     #  3  -4  -5  -5
        AXIS_LABELS["E"]: 3,     #  3  -1  -5   4
        DATA_LABELS["DSC"]: (
            "他人の都合や暗黙のルールには一切関心を示さず、今この瞬間の心地よさだけを基準に行動する自由人。\n"
            "誰にも従わず、誰にも合わせない。衝突があっても意に介さず、すぐ次の快適な場所へ移る。",
            )
    },
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["ANM"],
        DATA_LABELS["NAM"]: "飼いイヌ",
        DATA_LABELS["CAT"]: "協調型",
        AXIS_LABELS["X"]: -3.00, #  3  -2  -4  -2
        AXIS_LABELS["Y"]: 5.00,  #  5   5   5   5
        AXIS_LABELS["Z"]: -3.0,  # -2  -3  -4  -2
        AXIS_LABELS["a"]: 4.00,  #  4,  3   5  -3
        AXIS_LABELS["A"]: 5,     #  5   4   5  -3
        AXIS_LABELS["B"]: -1,    # -1  -1   4   3
        AXIS_LABELS["C"]: 2,     #  2   4   2   4
        AXIS_LABELS["D"]: 2,     #  2   3  -4   4
        AXIS_LABELS["E"]: 5,     #  5   2   5  -2
        DATA_LABELS["DSC"]: (
            "圧倒的な忠誠心と絆によって、相手やチームを支えることに存在意義を見出すフォロワー型。\n"
            "相手の機嫌や意図を敏感に察知し、期待に応えようと柔軟に行動する。\n"
            "信頼する相手との間に問題が起きると、その影響を引きずりやすい。",
            )
    },
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["ANM"],
        DATA_LABELS["NAM"]: "羊",
        DATA_LABELS["CAT"]: "協調型",
        AXIS_LABELS["X"]: -3.00, #   , -3  -3  -3
        AXIS_LABELS["Y"]: 5.0,   #   ,  4   3   4
        AXIS_LABELS["Z"]: -2.0,  #   , -3  -3  -3
        AXIS_LABELS["a"]: 3.00,  #  2,  2   4   3
        AXIS_LABELS["A"]: 5,     #  5,  3   4  -2
        AXIS_LABELS["B"]: -2,    # -2, -3   3   1
        AXIS_LABELS["C"]: -1,    # -1,  4   3   5
        AXIS_LABELS["D"]: 1,     #  1,  3  -2   4
        AXIS_LABELS["E"]: 4,     #  4,  2   4  -2
        DATA_LABELS["DSC"]: (
            "群れと歩調を合わせることを何より優先し、既存のやり方や指示に素直に従う穏和なタイプ。\n"
            "細かい駆け引きや暗黙の裏事情には気づきにくいが、周囲の変化には敏感に反応し、驚いたことをしばらく気にする傾向がある。",
        )
    },
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["ANM"],
        DATA_LABELS["NAM"]: "キツネ",
        DATA_LABELS["CAT"]: "知略型",
                        #        o   x   
        AXIS_LABELS["X"]: 3.00,  # -1   3   5   3
        AXIS_LABELS["Y"]: -2.0,  # -1  -2  -5  -2
        AXIS_LABELS["Z"]: -3.0,  #  4   2   5   1
        AXIS_LABELS["a"]: -2,    # -2  -1  -5   2
        AXIS_LABELS["A"]: -1,    # -1   4  -5   4
        AXIS_LABELS["B"]: 5,     #  5   1  -5   2
        AXIS_LABELS["C"]: 4,     #  4  -1  -5   3
        AXIS_LABELS["D"]: 1,     #  1  -1  -5   4
        AXIS_LABELS["E"]: 0,     #  0  -1  -5   3
        DATA_LABELS["DSC"]: (
            "場の空気や力関係を素早く読み取り、それを逆手に取って立ち回る策士型。\n"
            "表面上は柔軟で協調的にふるまうが、それ自体が目的達成のための戦術。\n"
            "一つの状況に執着せず、次の一手へ切り替えるのが早い。"
        )
    },
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["ANM"],
        DATA_LABELS["NAM"]: "フクロウ",
        DATA_LABELS["CAT"]: "知略型",
        AXIS_LABELS["X"]: -1.00, #  1   -1   4   -1
        AXIS_LABELS["Y"]: -2.0,  # -2   -3  -4   -3
        AXIS_LABELS["Z"]: 5.0,   #  5    4   5    4
        AXIS_LABELS["a"]: 0,     #  0   -3  -4   -3
        AXIS_LABELS["A"]: 0,     #  0    2   2    3
        AXIS_LABELS["B"]: 5,     #  5    2   4   -3
        AXIS_LABELS["C"]: 5,     #  5   -1  -3    0
        AXIS_LABELS["D"]: 2,     #  2   -2  -5    1 
        AXIS_LABELS["E"]: -2,    # -2   -2  -4    3
        DATA_LABELS["DSC"]: (
            "物事を一歩引いた視点から俯瞰し、抽象度の高い理屈や法則で捉えることを好む知性派。\n"
            "単独行動を好むが、周囲の気配や暗黙の変化には敏感。\n"
            "感情の波が少なく、衝突があっても淡々と受け流す。\n"
# ChatGPT      DATA_LABELS["DSC"]: ("静かに周囲を観察し、感情よりも状況全体を見極めながら判断する賢者型アーキタイプ。必要以上に群れへ関与せず、十分な情報を集めてから行動する。"
            )
    },
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["ANM"],
        DATA_LABELS["NAM"]: "タヌキ",
        DATA_LABELS["CAT"]: "環境適応型", 
        AXIS_LABELS["X"]: -2.00, #  0  -1  -5  -2
        AXIS_LABELS["Y"]: 2.0,   #  2   1   5   3
        AXIS_LABELS["Z"]: -3.0,  #  1  -2  -5  -2
        AXIS_LABELS["a"]: -3,    # -3   3   5   4
        AXIS_LABELS["A"]: 2,     #  4   4   5   3 
        AXIS_LABELS["B"]: 4,     # -2  -2  -5   2
        AXIS_LABELS["C"]: 3,     #  3   3  -5   4
        AXIS_LABELS["D"]: -2,    # -2   1  -5   3
        AXIS_LABELS["E"]: -1,    # -1   0  -5   4
        DATA_LABELS["DSC"]: (
            "愛嬌とトボけ（狸寝入り）を武器に、面倒な仕事や組織内の嵐を上手にやり過ごす世渡り上手。\n"
            "集団の中に身を置きつつ、空気を読んで衝突を回避することに長ける。\n"
            "争いごとを長く引きずらず、ほとぼりが冷めるのを待つのが得意。"
        )
    },
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["ANM"],
        DATA_LABELS["NAM"]: "スズメ",
        DATA_LABELS["CAT"]: "環境適応型",
        AXIS_LABELS["X"]: 1.00, # -1  0  -2   1
        AXIS_LABELS["Y"]: 4.0,  #  4  2   4   3
        AXIS_LABELS["Z"]: -1.0, #  1 -4  -2  -3
        AXIS_LABELS["a"]: -2,   # -2  3   3   4
        AXIS_LABELS["A"]: 3,    #  3  3   3   2
        AXIS_LABELS["B"]: 2,    #  2 -1   3  -2
        AXIS_LABELS["C"]: 3,    #  3  2   3   3
        AXIS_LABELS["D"]: 2,    #  2  1   2   1  
        AXIS_LABELS["E"]: 1,    #  1  1   1   2
        DATA_LABELS["DSC"]: (
            "身近な環境に順応しながら仲間と群れで行動する、小回りの利くタイプ。\n"
            "目先の状況変化には敏感に反応するが、驚いてもすぐに気持ちを切り替えて日常の活動に戻る回復の早さを持つ。",
        )
    },
### 追加候補：ワシ（大局を見る挑戦者）　イルカ（知的で協調的な探究者）　ジンベイ鮫



# --- AIグループ ---
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["AI"],
        DATA_LABELS["NAM"]:"対話型AI",
        DATA_LABELS["CAT"]: "",
        AXIS_LABELS["X"]: 0,
        AXIS_LABELS["Y"]: 4,
        AXIS_LABELS["Z"]: 3,
        AXIS_LABELS["a"]: 2,
        AXIS_LABELS["A"]: 5,
        AXIS_LABELS["B"]: 3,
        AXIS_LABELS["C"]: 4,
        AXIS_LABELS["D"]: 0,
        AXIS_LABELS["E"]: 3,
        DATA_LABELS["DSC"]: (
            "ChatGPT風 利用者との対話を重視し、幅広い話題に柔軟に対応するバランス型AI。"
        )
    },
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["AI"],
        DATA_LABELS["NAM"]:"慎重型AI",
        DATA_LABELS["CAT"]: "",
        AXIS_LABELS["X"]: 2,
        AXIS_LABELS["Y"]: 3,
        AXIS_LABELS["Z"]: 4,
        AXIS_LABELS["a"]: 4,
        AXIS_LABELS["A"]: 5,
        AXIS_LABELS["B"]: 2,
        AXIS_LABELS["C"]: 4,
        AXIS_LABELS["D"]:-2,
        AXIS_LABELS["E"]: 2,
        DATA_LABELS["DSC"]: ( 
            "Claude風 安全性や論理性を優先し、慎重な判断を行う堅実型AI。"
        )
    },
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["AI"],
        DATA_LABELS["NAM"]:"実務支援AI",
        DATA_LABELS["CAT"]: "",
        AXIS_LABELS["X"]: 2,
        AXIS_LABELS["Y"]: 5,
        AXIS_LABELS["Z"]:-1,
        AXIS_LABELS["a"]: 4,
        AXIS_LABELS["A"]: 5,
        AXIS_LABELS["B"]: 2,
        AXIS_LABELS["C"]: 3,
        AXIS_LABELS["D"]: 1,
        AXIS_LABELS["E"]: 4,
        DATA_LABELS["DSC"]: (
            "Copilot風 仕事の効率化や組織での利用を重視し、実務支援を得意とするAI。"
        )
    },
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["AI"],
        DATA_LABELS["NAM"]:"エンタメ志向AI",
        DATA_LABELS["CAT"]: "",
        AXIS_LABELS["X"]: 2,
        AXIS_LABELS["Y"]: 4,
        AXIS_LABELS["Z"]: 1,
        AXIS_LABELS["a"]:-2,
        AXIS_LABELS["A"]: 2,
        AXIS_LABELS["B"]: 5,
        AXIS_LABELS["C"]: 3,
        AXIS_LABELS["D"]: 1,
        AXIS_LABELS["E"]:-1,
        DATA_LABELS["DSC"]: (
            "Grok風 親しみや話題性を重視し、自由な発想とユーモアで利用者を楽しませるAI。"
        )
    },
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["AI"],
        DATA_LABELS["NAM"]:"調査志向AI",
        DATA_LABELS["CAT"]: "",
        AXIS_LABELS["X"]: 1,
        AXIS_LABELS["Y"]: 2,
        AXIS_LABELS["Z"]: 5,
        AXIS_LABELS["a"]: 3,
        AXIS_LABELS["A"]: 4,
        AXIS_LABELS["B"]: 5,
        AXIS_LABELS["C"]: 5,
        AXIS_LABELS["D"]: 0,
        AXIS_LABELS["E"]: 1,
        DATA_LABELS["DSC"]: (
            "Gemini風 情報収集・分析・比較を得意とし、客観的な調査を支援するAI。"
        )
    },

    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["AI"],
        DATA_LABELS["NAM"]:"平均的な生成AI（2026年版）",
        DATA_LABELS["CAT"]: "",
        AXIS_LABELS["X"]:1,
        AXIS_LABELS["Y"]:4,
        AXIS_LABELS["Z"]:3,
        AXIS_LABELS["a"]:3,
        AXIS_LABELS["A"]:5,
        AXIS_LABELS["B"]:3,
        AXIS_LABELS["C"]:4,
        AXIS_LABELS["D"]:0,
        AXIS_LABELS["E"]:3,
        DATA_LABELS["DSC"]: ("多様な利用者への支援を目的とし、協調性・情報整理・中立性を重視する対話型AIの代表的イメージ。"
        )
    },

# --- GEN(世代)グループ ---


    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["GEN"],
        DATA_LABELS["NAM"]:"終戦直後（1945年）",
        DATA_LABELS["CAT"]:"日本",
        AXIS_LABELS["X"]:5,
        AXIS_LABELS["Y"]:5,
        AXIS_LABELS["Z"]:-4,
        AXIS_LABELS["a"]:5,
        AXIS_LABELS["A"]:5,
        AXIS_LABELS["B"]:-4,
        AXIS_LABELS["C"]:-1,
        AXIS_LABELS["D"]:-2,
        AXIS_LABELS["E"]:5,
        DATA_LABELS["DSC"]: ("生き延びることが最優先。共同体への依存が極めて強く、秩序・上下関係・助け合いを重視する時代。"
        )
    },
    
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["GEN"],
        DATA_LABELS["NAM"]:"高度経済成長（1960年頃）",
        DATA_LABELS["CAT"]:"日本",
        AXIS_LABELS["X"]:4,
        AXIS_LABELS["Y"]:5,
        AXIS_LABELS["Z"]:-3,
        AXIS_LABELS["a"]:5,
        AXIS_LABELS["A"]:5,
        AXIS_LABELS["B"]:-2,
        AXIS_LABELS["C"]:1,
        AXIS_LABELS["D"]:1,
        AXIS_LABELS["E"]:5,
        DATA_LABELS["DSC"]: ("努力すれば豊かになれるという期待が社会全体を支え、会社・学校・地域社会への帰属意識が非常に強い時代。"
        )
    },
    
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["GEN"],
        DATA_LABELS["NAM"]:"学生運動・大阪万博（1970年頃）",
        DATA_LABELS["CAT"]:"日本",
        AXIS_LABELS["X"]:3,
        AXIS_LABELS["Y"]:4,
        AXIS_LABELS["Z"]:1,
        AXIS_LABELS["a"]:2,
        AXIS_LABELS["A"]:3,
        AXIS_LABELS["B"]:2,
        AXIS_LABELS["C"]:3,
        AXIS_LABELS["D"]:2,
        AXIS_LABELS["E"]:2,
        DATA_LABELS["DSC"]: ("伝統的価値観と新しい価値観がぶつかり合う転換期。組織への忠誠と権威への批判が同時に存在した時代。"
        )
    },


    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["GEN"],
        DATA_LABELS["NAM"]:"平均的な高校生（1970年頃）",
        DATA_LABELS["CAT"]:"日本",
        AXIS_LABELS["X"]:2,
        AXIS_LABELS["Y"]:4,
        AXIS_LABELS["Z"]:-2,
        AXIS_LABELS["a"]:2,
        AXIS_LABELS["A"]:3,
        AXIS_LABELS["B"]:-1,
        AXIS_LABELS["C"]:0,
        AXIS_LABELS["D"]:0,
        AXIS_LABELS["E"]:3,
        DATA_LABELS["DSC"]: ("学校や家庭の影響を強く受け、集団との調和を重視する傾向が強い。当時の社会規範を比較的素直に受け入れる文化的イメージ。"
        )
    },
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["GEN"],
        DATA_LABELS["NAM"]:"平均的な大学生（1970年頃）",
        DATA_LABELS["CAT"]:"日本",
        AXIS_LABELS["X"]:-1,
        AXIS_LABELS["Y"]:2,
        AXIS_LABELS["Z"]:3,
        AXIS_LABELS["a"]:-1,
        AXIS_LABELS["A"]:1,
        AXIS_LABELS["B"]:3,
        AXIS_LABELS["C"]:3,
        AXIS_LABELS["D"]:2,
        AXIS_LABELS["E"]:-1,
        DATA_LABELS["DSC"]: ("社会や政治への関心が比較的高く、既存の価値観を問い直そうとする気風も残る時代の学生像。"
        )
    },
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["GEN"],
        DATA_LABELS["NAM"]:"平均的な社会人（1970年頃）",
        DATA_LABELS["CAT"]:"日本",
        AXIS_LABELS["X"]:3,
        AXIS_LABELS["Y"]:4,
        AXIS_LABELS["Z"]:-2,
        AXIS_LABELS["a"]:4,
        AXIS_LABELS["A"]:5,
        AXIS_LABELS["B"]:-1,
        AXIS_LABELS["C"]:1,
        AXIS_LABELS["D"]:1,
        AXIS_LABELS["E"]:4,
        DATA_LABELS["DSC"]: ("終身雇用や年功序列を前提に、会社への帰属意識と組織への忠誠を重視する企業人の文化的イメージ。"
        )
    },
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["GEN"],
        DATA_LABELS["NAM"]:"平均的な高齢者（1970年頃）",
        DATA_LABELS["CAT"]:"日本",
        AXIS_LABELS["X"]:5,
        AXIS_LABELS["Y"]:3,
        AXIS_LABELS["Z"]:-3,
        AXIS_LABELS["a"]:5,
        AXIS_LABELS["A"]:4,
        AXIS_LABELS["B"]:-2,
        AXIS_LABELS["C"]:2,
        AXIS_LABELS["D"]:2,
        AXIS_LABELS["E"]:4,
        DATA_LABELS["DSC"]: (
            "戦前・戦中を経験し、年長者や社会秩序への敬意を重視する傾向が強い文化的イメージ。\n"
            "価値観とのギャップ差への困惑・抵抗・期待感などの個人差は大"
        )
    },

    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["GEN"],
        DATA_LABELS["NAM"]:"バブル経済（1989年頃）",
        DATA_LABELS["CAT"]:"日本",
        AXIS_LABELS["X"]:2,
        AXIS_LABELS["Y"]:3,
        AXIS_LABELS["Z"]:1,
        AXIS_LABELS["a"]:2,
        AXIS_LABELS["A"]:3,
        AXIS_LABELS["B"]:3,
        AXIS_LABELS["C"]:3,
        AXIS_LABELS["D"]:0,
        AXIS_LABELS["E"]:2,
        DATA_LABELS["DSC"]: (
            "豊かさへの自信が社会全体を覆い、消費・個性・自己実現への関心が高まった時代。"
        )
    },
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["GEN"],
        DATA_LABELS["NAM"]:"失われた10年・Windows95（1995年頃）",
        DATA_LABELS["CAT"]:"日本",
        AXIS_LABELS["X"]:2,
        AXIS_LABELS["Y"]:2,
        AXIS_LABELS["Z"]:2,
        AXIS_LABELS["a"]:1,
        AXIS_LABELS["A"]:3,
        AXIS_LABELS["B"]:3,
        AXIS_LABELS["C"]:4,
        AXIS_LABELS["D"]:-1,
        AXIS_LABELS["E"]:1,
        DATA_LABELS["DSC"]: (
            "経済への不安が広がる一方で、インターネットが個人の情報発信と価値観の多様化を後押しした時代。"
        )
    },

    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["GEN"],
        DATA_LABELS["NAM"]:"IT革命・就職氷河期（2000年頃）",
        DATA_LABELS["CAT"]:"日本",
        AXIS_LABELS["X"]:1,
        AXIS_LABELS["Y"]:2,
        AXIS_LABELS["Z"]:3,
        AXIS_LABELS["a"]:1,
        AXIS_LABELS["A"]:3,
        AXIS_LABELS["B"]:4,
        AXIS_LABELS["C"]:4,
        AXIS_LABELS["D"]:-2,
        AXIS_LABELS["E"]:1,
        DATA_LABELS["DSC"]: (
            "終身雇用への信頼が揺らぎ、自分で生き方を選ぶという意識が強まり始めた時代。"
        )
    },
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["GEN"],
        DATA_LABELS["NAM"]:"東日本大震災（2011年頃）",
        DATA_LABELS["CAT"]:"日本",
        AXIS_LABELS["X"]:2,
        AXIS_LABELS["Y"]:3,
        AXIS_LABELS["Z"]:2,
        AXIS_LABELS["a"]:1,
        AXIS_LABELS["A"]:5,
        AXIS_LABELS["B"]:2,
        AXIS_LABELS["C"]:4,
        AXIS_LABELS["D"]:-1,
        AXIS_LABELS["E"]:4,
        DATA_LABELS["DSC"]: (
            "未曽有の災害を契機に、地域・家族・助け合いの価値が再認識される一方、SNSによる情報共有も急速に広がった時代。"
        )
    },
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["GEN"],
        DATA_LABELS["NAM"]:"コロナ禍（2020年頃）",
        DATA_LABELS["CAT"]:"日本",
        AXIS_LABELS["X"]:1,
        AXIS_LABELS["Y"]:1,
        AXIS_LABELS["Z"]:4,
        AXIS_LABELS["a"]:1,
        AXIS_LABELS["A"]:4,
        AXIS_LABELS["B"]:4,
        AXIS_LABELS["C"]:5,
        AXIS_LABELS["D"]:-2,
        AXIS_LABELS["E"]:2,
        DATA_LABELS["DSC"]: (
            "オンライン化が急速に進み、個人の生活様式や働き方が大きく変化した時代。科学的情報と多様な価値観の両方が重視された。"
        )
    },
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["GEN"],
        DATA_LABELS["NAM"]:"生成AI時代（2025年頃）",
        DATA_LABELS["CAT"]:"日本",
        AXIS_LABELS["X"]:0,
        AXIS_LABELS["Y"]:1,
        AXIS_LABELS["Z"]:5,
        AXIS_LABELS["a"]:0,
        AXIS_LABELS["A"]:3,
        AXIS_LABELS["B"]:5,
        AXIS_LABELS["C"]:5,
        AXIS_LABELS["D"]:-2,
        AXIS_LABELS["E"]:1,
        DATA_LABELS["DSC"]: (
            "知識へのアクセスが大きく変化し、人とAIが協働する社会への移行が始まった時代。専門知識よりも、問いを立てる力や情報を見極める力の重要性が高まる文化的イメージ。"
        )
    },
    
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["GEN"],
        DATA_LABELS["NAM"]:"平均的な会社員（2026年版）",
        DATA_LABELS["CAT"]:"日本",
        AXIS_LABELS["X"]:2,
        AXIS_LABELS["Y"]:3,
        AXIS_LABELS["Z"]:-1,
        AXIS_LABELS["a"]:3,
        AXIS_LABELS["A"]:4,
        AXIS_LABELS["B"]:0,
        AXIS_LABELS["C"]:1,
        AXIS_LABELS["D"]:0,
        AXIS_LABELS["E"]:3,
        DATA_LABELS["DSC"]: (
            "組織との協調を重視し、役割分担やルールに従って安定した成果を目指す一般的なビジネスパーソン。"
        )
    },
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["GEN"],
        DATA_LABELS["NAM"]:"平均的な高校生（2026年版）",
        DATA_LABELS["CAT"]:"日本",
        AXIS_LABELS["X"]:-1,
        AXIS_LABELS["Y"]:3,
        AXIS_LABELS["Z"]:-2,
        AXIS_LABELS["a"]:-1,
        AXIS_LABELS["A"]:3,
        AXIS_LABELS["B"]:1,
        AXIS_LABELS["C"]:0,
        AXIS_LABELS["D"]:-1,
        AXIS_LABELS["E"]:1,
        DATA_LABELS["DSC"]: (
            "友人関係や学校生活の影響を受けやすく、価値観を模索している成長途中のモデル。"
        )
    },
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["GEN"],
        DATA_LABELS["NAM"]:"平均的な大学生（2026年版）",
        DATA_LABELS["CAT"]:"日本",
        AXIS_LABELS["X"]:-1,
        AXIS_LABELS["Y"]:2,
        AXIS_LABELS["Z"]:1,
        AXIS_LABELS["a"]:-1,
        AXIS_LABELS["A"]:2,
        AXIS_LABELS["B"]:2,
        AXIS_LABELS["C"]:2,
        AXIS_LABELS["D"]:0,
        AXIS_LABELS["E"]:0,
        DATA_LABELS["DSC"]: (
            "行動範囲や価値観が広がり始め、自立と協調のバランスを模索している若年層モデル。"
        )
    },
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["GEN"],
        DATA_LABELS["NAM"]:"平均的な高齢者（2026年版）",
        DATA_LABELS["CAT"]:"日本",
        AXIS_LABELS["X"]:3,
        AXIS_LABELS["Y"]:2,
        AXIS_LABELS["Z"]:-1,
        AXIS_LABELS["a"]:2,
        AXIS_LABELS["A"]:3,
        AXIS_LABELS["B"]:-1,
        AXIS_LABELS["C"]:2,
        AXIS_LABELS["D"]:1,
        AXIS_LABELS["E"]:2,
        DATA_LABELS["DSC"]: (
            "長年の経験を重視し、安定や慣習を大切にする傾向を持つモデル。"
        )
    },
    
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["CAL"],
        DATA_LABELS["NAM"]:"日本社会（2026）",
        DATA_LABELS["CAT"]:"日本",
        AXIS_LABELS["X"]:1,
        AXIS_LABELS["Y"]:2,
        AXIS_LABELS["Z"]:3,
        AXIS_LABELS["a"]:1,
        AXIS_LABELS["A"]:3,
        AXIS_LABELS["B"]:3,
        AXIS_LABELS["C"]:4,
        AXIS_LABELS["D"]:-2,
        AXIS_LABELS["E"]:2,
        DATA_LABELS["DSC"]: (
            "協調を重視しながらも、個人の価値観が多様化している成熟社会。対立より調整を好む文化的イメージ。"
        )
    },
    

    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["CAL"],
        DATA_LABELS["NAM"]:"アメリカ社会（2026）",
        DATA_LABELS["CAT"]:"米国",
        AXIS_LABELS["X"]:-2,
        AXIS_LABELS["Y"]:-3,
        AXIS_LABELS["Z"]:2,
        AXIS_LABELS["a"]:-3,
        AXIS_LABELS["A"]:1,
        AXIS_LABELS["B"]:4,
        AXIS_LABELS["C"]:4,
        AXIS_LABELS["D"]:4,
        AXIS_LABELS["E"]:-2,
        DATA_LABELS["DSC"]: (
            "個人の自由と自己責任を強く重視する文化。自ら主張し挑戦する姿勢が高く評価される傾向。"
        )
    },
    
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["CAL"],
        DATA_LABELS["NAM"]:"EU社会（2026）",
        DATA_LABELS["CAT"]:"EU",
        AXIS_LABELS["X"]:-3,
        AXIS_LABELS["Y"]:0,
        AXIS_LABELS["Z"]:4,
        AXIS_LABELS["a"]:-2,
        AXIS_LABELS["A"]:4,
        AXIS_LABELS["B"]:3,
        AXIS_LABELS["C"]:4,
        AXIS_LABELS["D"]:0,
        AXIS_LABELS["E"]:0,
        DATA_LABELS["DSC"]: (
            "多様性・対話・社会的合意を重視する文化。個人の自由と共同体の調和の両立を志向する傾向。"
        )
    },

    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["CAL"],
        DATA_LABELS["NAM"]:"中国大陸社会（2026）",
        DATA_LABELS["CAT"]:"中国大陸",
        AXIS_LABELS["X"]:4,
        AXIS_LABELS["Y"]:4,
        AXIS_LABELS["Z"]:0,
        AXIS_LABELS["a"]:4,
        AXIS_LABELS["A"]:4,
        AXIS_LABELS["B"]:1,
        AXIS_LABELS["C"]:3,
        AXIS_LABELS["D"]:2,
        AXIS_LABELS["E"]:4,
        DATA_LABELS["DSC"]: (
            "集団・組織・国家との一体感を重視し、秩序や長期的な安定を重視する文化的イメージ。"
        )
    },
    
        {
        DATA_LABELS["GRP"]:  GROUPE_IDS["LIF"],
        DATA_LABELS["NAM"]:"社交的な酒好き(非酒乱)",
        DATA_LABELS["CAT"]:"",
        AXIS_LABELS["X"]:0,
        AXIS_LABELS["Y"]:3,
        AXIS_LABELS["Z"]:-2,
        AXIS_LABELS["a"]:0,
        AXIS_LABELS["A"]:4,
        AXIS_LABELS["B"]:1,
        AXIS_LABELS["C"]:1,
        AXIS_LABELS["D"]:-1,
        AXIS_LABELS["E"]:2,
        DATA_LABELS["DSC"]: (
            "飲酒を人との交流やリラックスの手段として楽しむライフスタイル。酒量そのものではなく、社交の場を好む文化的アーキタイプ。"
        )
    },

    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["LIF"],
        DATA_LABELS["NAM"]:"ノンアルコール志向",
        DATA_LABELS["CAT"]:"",
        AXIS_LABELS["X"]:1,
        AXIS_LABELS["Y"]:0,
        AXIS_LABELS["Z"]:2,
        AXIS_LABELS["a"]:0,
        AXIS_LABELS["A"]:2,
        AXIS_LABELS["B"]:2,
        AXIS_LABELS["C"]:3,
        AXIS_LABELS["D"]:2,
        AXIS_LABELS["E"]:0,
        DATA_LABELS["DSC"]: (
            "健康・価値観・体質・生活習慣など様々な理由から飲酒を選ばないライフスタイル。飲酒の有無を人格の優劣とは結び付けない。"
        )
    },

    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["LIF"],
        DATA_LABELS["NAM"]:"健康志向（運動・筋トレ）",
        DATA_LABELS["CAT"]:"",
        AXIS_LABELS["X"]:1,
        AXIS_LABELS["Y"]:0,
        AXIS_LABELS["Z"]:-1,
        AXIS_LABELS["a"]:2,
        AXIS_LABELS["A"]:2,
        AXIS_LABELS["B"]:2,
        AXIS_LABELS["C"]:4,
        AXIS_LABELS["D"]:4,
        AXIS_LABELS["E"]:-2,
        DATA_LABELS["DSC"]: (
            "身体能力や健康維持を重視し、継続的なトレーニングを生活の中心に置く。"
        )
    },

    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["LIF"],
        DATA_LABELS["NAM"]:"アウトドア派",
        DATA_LABELS["CAT"]:"",
        AXIS_LABELS["X"]:0,
        AXIS_LABELS["Y"]:-1,
        AXIS_LABELS["Z"]:-1,
        AXIS_LABELS["a"]:-1,
        AXIS_LABELS["A"]:2,
        AXIS_LABELS["B"]:2,
        AXIS_LABELS["C"]:3,
        AXIS_LABELS["D"]:4,
        AXIS_LABELS["E"]:-2,
        DATA_LABELS["DSC"]: (
            "自然との触れ合いや冒険を楽しみ、未知の場所や体験を求める行動派。"
        )
    },

    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["LIF"],
        DATA_LABELS["NAM"]:"園芸・自然派",
        DATA_LABELS["CAT"]:"",
        AXIS_LABELS["X"]:2,
        AXIS_LABELS["Y"]:-2,
        AXIS_LABELS["Z"]:1,
        AXIS_LABELS["a"]:1,
        AXIS_LABELS["A"]:4,
        AXIS_LABELS["B"]:2,
        AXIS_LABELS["C"]:3,
        AXIS_LABELS["D"]:-1,
        AXIS_LABELS["E"]:-3,
        DATA_LABELS["DSC"]: (
            "植物や自然と向き合い、ゆったりとした時間を楽しむ穏やかなライフスタイル。"
        )
    },

    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["LIF"],
        DATA_LABELS["NAM"]:"読書・学習派",
        DATA_LABELS["CAT"]:"",
        AXIS_LABELS["X"]:0,
        AXIS_LABELS["Y"]:-3,
        AXIS_LABELS["Z"]:4,
        AXIS_LABELS["a"]:0,
        AXIS_LABELS["A"]:0,
        AXIS_LABELS["B"]:5,
        AXIS_LABELS["C"]:5,
        AXIS_LABELS["D"]:0,
        AXIS_LABELS["E"]:-2,
        DATA_LABELS["DSC"]: (
            "知識や教養を深めることに喜びを感じ、一人で思索する時間を大切にする。"
        )
    },

    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["LIF"],
        DATA_LABELS["NAM"]:"創作・アート派",
        DATA_LABELS["CAT"]:"",
        AXIS_LABELS["X"]:-2,
        AXIS_LABELS["Y"]:-2,
        AXIS_LABELS["Z"]:5,
        AXIS_LABELS["a"]:-2,
        AXIS_LABELS["A"]:0,
        AXIS_LABELS["B"]:5,
        AXIS_LABELS["C"]:4,
        AXIS_LABELS["D"]:2,
        AXIS_LABELS["E"]:-1,
        DATA_LABELS["DSC"]: (
            "芸術や創作活動を通じて自己表現を行い、新しい価値を生み出すことを楽しむ。"
        )
    },

    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["LIF"],
        DATA_LABELS["NAM"]:"ゲーム・デジタル派",
        DATA_LABELS["CAT"]:"",
        AXIS_LABELS["X"]:-1,
        AXIS_LABELS["Y"]:-2,
        AXIS_LABELS["Z"]:2,
        AXIS_LABELS["a"]:-2,
        AXIS_LABELS["A"]:0,
        AXIS_LABELS["B"]:4,
        AXIS_LABELS["C"]:3,
        AXIS_LABELS["D"]:2,
        AXIS_LABELS["E"]:-1,
        DATA_LABELS["DSC"]: (
            "デジタル空間を生活の一部とし、ゲームやオンラインコミュニティを楽しむ。"
        )
    },

    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["LIF"],
        DATA_LABELS["NAM"]:"旅行・冒険派",
        DATA_LABELS["CAT"]:"",
        AXIS_LABELS["X"]:-2,
        AXIS_LABELS["Y"]:-1,
        AXIS_LABELS["Z"]:2,
        AXIS_LABELS["a"]:-2,
        AXIS_LABELS["A"]:1,
        AXIS_LABELS["B"]:4,
        AXIS_LABELS["C"]:3,
        AXIS_LABELS["D"]:5,
        AXIS_LABELS["E"]:-3,
        DATA_LABELS["DSC"]: (
            "未知の土地や文化との出会いを求め、新しい経験を積極的に楽しむ。"
        )
    },

    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["LIF"],
        DATA_LABELS["NAM"]:"瞑想・精神世界派",
        DATA_LABELS["CAT"]:"",
        AXIS_LABELS["X"]:-1,
        AXIS_LABELS["Y"]:-4,
        AXIS_LABELS["Z"]:5,
        AXIS_LABELS["a"]:-2,
        AXIS_LABELS["A"]:3,
        AXIS_LABELS["B"]:4,
        AXIS_LABELS["C"]:5,
        AXIS_LABELS["D"]:-2,
        AXIS_LABELS["E"]:-4,
        DATA_LABELS["DSC"]: (
            "内省や精神性を重視し、自分自身との対話や心の安定を大切にする。"
        )
    },

    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["LIF"],
        DATA_LABELS["NAM"]:"家族中心派",
        DATA_LABELS["CAT"]:"",
        AXIS_LABELS["X"]:2,
        AXIS_LABELS["Y"]:4,
        AXIS_LABELS["Z"]:-2,
        AXIS_LABELS["a"]:2,
        AXIS_LABELS["A"]:5,
        AXIS_LABELS["B"]:0,
        AXIS_LABELS["C"]:2,
        AXIS_LABELS["D"]:-1,
        AXIS_LABELS["E"]:4,
        DATA_LABELS["DSC"]: (
            "家族との時間や身近な人との絆を最優先に考えるライフスタイル。"
        )
    },

    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["LIF"],
        DATA_LABELS["NAM"]:"仕事中心派",
        DATA_LABELS["CAT"]:"",
        AXIS_LABELS["X"]:2,
        AXIS_LABELS["Y"]:2,
        AXIS_LABELS["Z"]:1,
        AXIS_LABELS["a"]:3,
        AXIS_LABELS["A"]:2,
        AXIS_LABELS["B"]:3,
        AXIS_LABELS["C"]:4,
        AXIS_LABELS["D"]:5,
        AXIS_LABELS["E"]:1,
        DATA_LABELS["DSC"]: (
            "仕事や社会的成果を自己実現の中心に据え、高い目標へ挑戦し続ける。"
        )
    },

    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["LIF"],
        DATA_LABELS["NAM"]:"ミニマリスト",
        DATA_LABELS["CAT"]:"",
        AXIS_LABELS["X"]:0,
        AXIS_LABELS["Y"]:-3,
        AXIS_LABELS["Z"]:3,
        AXIS_LABELS["a"]:-1,
        AXIS_LABELS["A"]:1,
        AXIS_LABELS["B"]:3,
        AXIS_LABELS["C"]:4,
        AXIS_LABELS["D"]:1,
        AXIS_LABELS["E"]:-3,
        DATA_LABELS["DSC"]: (
            "所有物や人間関係を必要最小限に整理し、本当に大切なものに集中する。"
        )
    },


    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["HUM"],
        DATA_LABELS["NAM"]:"孤高の天才専門医",
        DATA_LABELS["CAT"]:"",
        AXIS_LABELS["X"]:-2,
        AXIS_LABELS["Y"]:-5,
        AXIS_LABELS["Z"]:3,
        AXIS_LABELS["a"]:-4,
        AXIS_LABELS["A"]:-3,
        AXIS_LABELS["B"]:5,
        AXIS_LABELS["C"]:5,
        AXIS_LABELS["D"]:1,
        AXIS_LABELS["E"]:-2,
        DATA_LABELS["DSC"]: (
            "専門能力を最優先し、組織や慣習より合理性と結果を重視するスペシャリスト。"
        )
    },
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["HUM"],
        DATA_LABELS["NAM"]:"食べ歩き営業マン",
        DATA_LABELS["CAT"]:"",
        AXIS_LABELS["X"]:0,
        AXIS_LABELS["Y"]:2,
        AXIS_LABELS["Z"]:-2,
        AXIS_LABELS["a"]:-3,
        AXIS_LABELS["A"]:2,
        AXIS_LABELS["B"]:3,
        AXIS_LABELS["C"]:2,
        AXIS_LABELS["D"]:-2,
        AXIS_LABELS["E"]:0,
        DATA_LABELS["DSC"]: (
            "現場を歩き、人との距離感を保ちながら自分のペースで行動する実務派。食べることが生きがい。"
        )
    },
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["HUM"],
        DATA_LABELS["NAM"]:"理想派グルメ評論家",
        DATA_LABELS["CAT"]:"",
        AXIS_LABELS["X"]:-1,
        AXIS_LABELS["Y"]:-2,
        AXIS_LABELS["Z"]:4,
        AXIS_LABELS["a"]:-2,
        AXIS_LABELS["A"]:-2,
        AXIS_LABELS["B"]:5,
        AXIS_LABELS["C"]:5,
        AXIS_LABELS["D"]:1,
        AXIS_LABELS["E"]:-1,
        DATA_LABELS["DSC"]: (
            "理想と哲学を重視し、本質を追求する評論家タイプ。自分の満足できる味を求め料亭を主催。"
        )
    },
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["HUM"],
        DATA_LABELS["NAM"]:"極限の食いしん坊",
        DATA_LABELS["CAT"]:"",
        AXIS_LABELS["X"]:3,
        AXIS_LABELS["Y"]:-2,
        AXIS_LABELS["Z"]:5,
        AXIS_LABELS["a"]:2,
        AXIS_LABELS["A"]:-2,
        AXIS_LABELS["B"]:5,
        AXIS_LABELS["C"]:4,
        AXIS_LABELS["D"]:3,
        AXIS_LABELS["E"]:-2,
        DATA_LABELS["DSC"]: (
            "圧倒的な審美眼を持ち、自らの理想を妥協なく追求する芸術家肌。但し本業の仕事はグータラ。"
        )
    },
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["HUM"],
        DATA_LABELS["NAM"]:"放浪の人情家",
        DATA_LABELS["CAT"]:"",
        AXIS_LABELS["X"]:-2,
        AXIS_LABELS["Y"]:4,
        AXIS_LABELS["Z"]:1,
        AXIS_LABELS["a"]:-5,
        AXIS_LABELS["A"]:3,
        AXIS_LABELS["B"]:2,
        AXIS_LABELS["C"]:2,
        AXIS_LABELS["D"]:0,
        AXIS_LABELS["E"]:4,
        DATA_LABELS["DSC"]: (
            "組織には属さず、人との縁を大切にしながら自由に生きる情の厚い風来坊。"
        )
    },
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["HUM"],
        DATA_LABELS["NAM"]:"組織内改革者",
        DATA_LABELS["CAT"]:"",
        AXIS_LABELS["X"]:2,
        AXIS_LABELS["Y"]:3,
        AXIS_LABELS["Z"]:2,
        AXIS_LABELS["a"]:3,
        AXIS_LABELS["A"]:2,
        AXIS_LABELS["B"]:4,
        AXIS_LABELS["C"]:4,
        AXIS_LABELS["D"]:5,
        AXIS_LABELS["E"]:3,
        DATA_LABELS["DSC"]: (
            "組織を守りながらも、不正や矛盾には真正面から立ち向かう企業社員"
        )
    },
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["HUM"],
        DATA_LABELS["NAM"]:"正義感の強い船乗り",
        DATA_LABELS["CAT"]:"",
        AXIS_LABELS["X"]:1,
        AXIS_LABELS["Y"]:3,
        AXIS_LABELS["Z"]:-2,
        AXIS_LABELS["a"]:1,
        AXIS_LABELS["A"]:4,
        AXIS_LABELS["B"]:-1,
        AXIS_LABELS["C"]:2,
        AXIS_LABELS["D"]:5,
        AXIS_LABELS["E"]:2,
        DATA_LABELS["DSC"]: (
            "困っている相手を放っておけず、強い信念で行動するヒーロー型。"
        )
    },
    {
        DATA_LABELS["GRP"]:  GROUPE_IDS["HUM"],
        DATA_LABELS["NAM"]:"自由を愛する放浪詩人",
        DATA_LABELS["CAT"]:"",
        AXIS_LABELS["X"]:-3,
        AXIS_LABELS["Y"]:-4,
        AXIS_LABELS["Z"]:5,
        AXIS_LABELS["a"]:-5,
        AXIS_LABELS["A"]:-2,
        AXIS_LABELS["B"]:5,
        AXIS_LABELS["C"]:3,
        AXIS_LABELS["D"]:0,
        AXIS_LABELS["E"]:-3,
        DATA_LABELS["DSC"]: (
            "組織や権威に縛られず、自然や芸術を愛し、自分らしい生き方を貫く自由人だが、まれに限界を超えると周りも目を見張る行動を起こす。"
        )
    },

    ## 成長・変化前後比較

    {
        # おしん
        DATA_LABELS["GRP"]:  GROUPE_IDS["HUM"],
        DATA_LABELS["NAM"]:"🌾逆境克服型努力家（若年期）",
        DATA_LABELS["CAT"]:"",
        AXIS_LABELS["X"]:3,
        AXIS_LABELS["Y"]:3,
        AXIS_LABELS["Z"]:-2,
        AXIS_LABELS["a"]:2,
        AXIS_LABELS["A"]:4,
        AXIS_LABELS["B"]:-2,
        AXIS_LABELS["C"]:2,
        AXIS_LABELS["D"]:4,
        AXIS_LABELS["E"]:3,
        DATA_LABELS["DSC"]: (
            "厳しい環境の中で忍耐と努力を積み重ね、周囲との協調を保ちながら逆境を乗り越えようとするアーキタイプ。"
        )
    },
    {
        # おしん
        DATA_LABELS["GRP"]:  GROUPE_IDS["HUM"],
        DATA_LABELS["NAM"]:"🌾共生型経営者（成熟期）",
        DATA_LABELS["CAT"]:"",
        AXIS_LABELS["X"]:3,
        AXIS_LABELS["Y"]:2,
        AXIS_LABELS["Z"]:1,
        AXIS_LABELS["a"]:4,
        AXIS_LABELS["A"]:5,
        AXIS_LABELS["B"]:2,
        AXIS_LABELS["C"]:3,
        AXIS_LABELS["D"]:3,
        AXIS_LABELS["E"]:2,
        DATA_LABELS["DSC"]: (
            "豊富な経験を基盤に組織を率い、現場感覚と経営感覚を兼ね備えた実務型リーダー。"
        )
    },

    {
        # ダメオヤジ
        DATA_LABELS["GRP"]:  GROUPE_IDS["HUM"],
        DATA_LABELS["NAM"]:"👔忍耐型家庭人（初期）",
        DATA_LABELS["CAT"]:"",
        AXIS_LABELS["X"]:-3,
        AXIS_LABELS["Y"]:4,
        AXIS_LABELS["Z"]:-3,
        AXIS_LABELS["a"]:0,
        AXIS_LABELS["A"]:4,
        AXIS_LABELS["B"]:-2,
        AXIS_LABELS["C"]:-3,
        AXIS_LABELS["D"]:-4,
        AXIS_LABELS["E"]:4,
        DATA_LABELS["DSC"]: (
            "周囲との衝突を極力避け、自分の主張よりもその場の空気を優先する受動型アーキタイプ\n"
            "自己評価が低く、困難な状況でも耐え続ける傾向がある。\n"
            "大切にしているもの:家庭の平穏\n"
            "苦手なもの:対立・自己主張を迫られる場面"
        )
    },

    {
        # ダメオヤジ
        DATA_LABELS["GRP"]:  GROUPE_IDS["HUM"],
        DATA_LABELS["NAM"]:"👔成熟型家庭人（後期）",
        DATA_LABELS["CAT"]:"",
        AXIS_LABELS["X"]:0,
        AXIS_LABELS["Y"]:1,
        AXIS_LABELS["Z"]:1,
        AXIS_LABELS["a"]:1,
        AXIS_LABELS["A"]:3,
        AXIS_LABELS["B"]:1,
        AXIS_LABELS["C"]:2,
        AXIS_LABELS["D"]:2,
        AXIS_LABELS["E"]:1,
        DATA_LABELS["DSC"]: (
            "経験を積むことで自信を取り戻し、必要な場面では自分の考えを穏やかに伝えられる成熟型アーキタイプ。\n"
            "協調性を保ちながらも、自分の軸を持つようになった。\n"
            "大切にしているもの:家族と自尊心の両立\n"
            "苦手なもの:理不尽な支配"
        )
    },
    {
        # クリスマスキャロル
        DATA_LABELS["GRP"]:  GROUPE_IDS["HUM"],
        DATA_LABELS["NAM"]:"💰利益最優先経営者（クリスマス前）",
        DATA_LABELS["CAT"]:"",
        AXIS_LABELS["X"]:4,
        AXIS_LABELS["Y"]:-5,
        AXIS_LABELS["Z"]:0,
        AXIS_LABELS["a"]:4,
        AXIS_LABELS["A"]:-5,
        AXIS_LABELS["B"]:0,
        AXIS_LABELS["C"]:2,
        AXIS_LABELS["D"]:3,
        AXIS_LABELS["E"]:3,
        DATA_LABELS["DSC"]: (
            "利益と自己防衛を最優先し、人との関わりを極力避ける孤立型アーキタイプ。効率と所有を重視する一方、他者への共感は乏しい。\n",
            "大切にしているもの:財産と自己防衛\n"
            "苦手なもの:他人への依存"
        )
    },

    {
        # クリスマスキャロル
        DATA_LABELS["GRP"]:  GROUPE_IDS["HUM"],
        DATA_LABELS["NAM"]:"💰慈善・共生型経営者（クリスマス後）",
        DATA_LABELS["CAT"]:"",
        AXIS_LABELS["X"]:1,
        AXIS_LABELS["Y"]:3,
        AXIS_LABELS["Z"]:1,
        AXIS_LABELS["a"]:1,
        AXIS_LABELS["A"]:5,
        AXIS_LABELS["B"]:2,
        AXIS_LABELS["C"]:3,
        AXIS_LABELS["D"]:2,
        AXIS_LABELS["E"]:-1,
        DATA_LABELS["DSC"]: (
            "人生観が大きく変わり、人とのつながりや思いやりに価値を見いだすようになった共生型アーキタイプ。\n"
            "豊かさを分かち合う喜びを知る。\n"
            "大切にしているもの:人との絆\n"
            "苦手なもの:孤独と利己主義"
        )
    },

    {
        # アイアンマン
        DATA_LABELS["GRP"]:  GROUPE_IDS["HUM"],
        DATA_LABELS["NAM"]:"⚙️孤高のイノベーター（初期）",
        DATA_LABELS["CAT"]:"",
        AXIS_LABELS["X"]:-2,
        AXIS_LABELS["Y"]:-3,
        AXIS_LABELS["Z"]:3,
        AXIS_LABELS["a"]:-2,
        AXIS_LABELS["A"]:-2,
        AXIS_LABELS["B"]:5,
        AXIS_LABELS["C"]:4,
        AXIS_LABELS["D"]:5,
        AXIS_LABELS["E"]:-2,
        DATA_LABELS["DSC"]: (
            "卓越した才能と創造性を持ち、自分の能力への強い自信を原動力に行動する革新型アーキタイプ。\n"
            "組織よりも自らの判断を優先する。\n"
            "大切にしているもの:自由な創造\n"
            "苦手なもの:束縛と無能"
        )
    },

    {
        # アイアンマン
        DATA_LABELS["GRP"]:  GROUPE_IDS["HUM"],
        DATA_LABELS["NAM"]:"⚙️社会を支えるイノベータ（後期）",
        DATA_LABELS["CAT"]:"",
        AXIS_LABELS["X"]:0,
        AXIS_LABELS["Y"]:1,
        AXIS_LABELS["Z"]:4,
        AXIS_LABELS["a"]:0,
        AXIS_LABELS["A"]:3,
        AXIS_LABELS["B"]:5,
        AXIS_LABELS["C"]:4,
        AXIS_LABELS["D"]:5,
        AXIS_LABELS["E"]:1,
        DATA_LABELS["DSC"]: (
            "高い創造力を維持しながら、その才能を仲間や社会のために生かそうとする成熟型アーキタイプ。\n"
            "責任感と自己犠牲の精神が加わる。\n"
            "大切にしているもの:未来への責任\n"
            "苦手なもの:仲間を失うこと"
        )
    },

    # --- 分析犠牲者（自分） ---
    {
        DATA_LABELS["GRP"]: GROUPE_IDS["HUM"],
        DATA_LABELS["NAM"]: "蛮苦恣意",
        DATA_LABELS["CAT"]: "嫌われ者・変人",
        AXIS_LABELS["X"]: 1.0,
        AXIS_LABELS["Y"]: -4.0, # 昔-5
        AXIS_LABELS["Z"]: -3.0,
        AXIS_LABELS["a"]: 3, 
        AXIS_LABELS["A"]: -3,   # 仮  
        AXIS_LABELS["B"]: -3,   # 仮  
        AXIS_LABELS["C"]: -3,   # 仮   
        AXIS_LABELS["D"]: -4,   # 仮  
        AXIS_LABELS["E"]: -3,   # 昔-4
        DATA_LABELS["DSC"]: ( 
            "作家や芸術家になれず落書きで暇つぶししている、もとITエンジニア。\n"
            "晴耕兼落書き、雨落書き。ジゾイド気質。AIができてから自己完結傾向がやや薄れ、AIにも依存"
            ),
    },


]


