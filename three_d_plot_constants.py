# 3D性格分析ツール用定数データファイル


DEFALUT_DATA_VERSION = "0.05"

# データ範囲、デフォルトペルソナ・データベースの定義

STEP_MAX = 5
STEP_MIN = -5


GROUPES = {
    "ANM": "動物",
    "HUM": "人物",
    "AI": "AI",
    "GEN": "時代",
    "CAL": "文化圏",
    "DEF": "既定値",    # カスタム以外のグループをまとめるための仮のグループ名
    "CST": "カスタム"
}


DATA_LABELS = {
    "GRP": "グループ",
    "NAM": "名前", 
    "CAT": "カテゴリ",
    "DSC": "説明",
    "VAL": "値"
}

AXIS_PREFIX = ""
AXIS_SUFFIX = "軸"

AXIS_LABELS = {
    "X": "X", 
    "Y": "Y", 
    "Z": "Z", 
    "a": "α",
    "A": "A",
    "B": "B",
    "C": "C",
    "D": "D",
    "E": "E",
}

AXIS_NAME = {
    "X": "方向性",
    "Y": "動機付", 
    "Z": "立脚点",
    "a": "快楽志向",
    "A": "文脈感度",
    "B": "重視対象",
    "C": "協調性",
    "D": "権威格差",
    "E": "事後反応",
}

AXIS_DESC = {
    "X": "現状維持⇔現状打破",
    "Y": "自己完結⇔対人依存", 
    "Z": "具体的⇔抽象的",
    "a": "情緒的💕⇔感覚的🍖",
    "A": "不文律に鈍感⇔敏感",
    "B": "事実志向⇔価値観志向",
    "C": "頑固⇔素直・優柔不断",
    "D": "権威格差に鈍感⇔敏感",
    "E": "過去を引きづる⇔気にしない",
}


####     Copilot,   Grok,  Gemini,  Claude

# df_default 用基礎データ
DEFAULT_PERSONAS = [
    #  記述書式  
    #    DATA_LABELS["GRP"]: 動物 、芸能人、政治家、経営者、研究者、AIなど  (既定値 / カスタム),          
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
    # --- 分析犠牲者（自分） ---
    {
        DATA_LABELS["GRP"]: GROUPES["HUM"],
        DATA_LABELS["NAM"]: "蛮苦恣意－現在",
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
        DATA_LABELS["DSC"]: "作家や芸術家になれず落書きで暇つぶししている、もとITエンジニア。晴耕兼落書き、雨落書き。ジゾイド気質。AIができてから自己完結傾向やや緩和、AI依存傾向",
    },

    # --- 動物グループ ---
    {
        DATA_LABELS["GRP"]: GROUPES["ANM"],
        DATA_LABELS["NAM"]: "女王蜂",
        DATA_LABELS["CAT"]: "統率型",
        DATA_LABELS["DSC"]: "個としての意思よりも、群れ全体の秩序そのものを体現する存在。自らは動かず、周囲がすべてを解釈・実行することで初めて機能する、極めて抽象度の高い『象徴』としての生命体。自身は上位の権威を意識する必要がなく、状況の変化にもほぼ動じない。",
        AXIS_LABELS["X"]: -5.0,
        AXIS_LABELS["Y"]: 5.0,
        AXIS_LABELS["Z"]: 5.0,
        AXIS_LABELS["a"]: 4,  #  4, 2  -5       4
        AXIS_LABELS["A"]: 4,  # 4, 3,  5       3
        AXIS_LABELS["B"]: 1,  # 1, -1, 5      -2
        AXIS_LABELS["C"]: 2,  # 2, -3  -5      -4 
        AXIS_LABELS["D"]: 2,  # 2, 3  5       -3
        AXIS_LABELS["E"]: 1,  # 1, 2   5      -1
        DATA_LABELS["DSC"]: "実力主義でトップに上り詰め、群れを率いるリーダー。他者の顔色ではなく、自身の判断と力で意思決定する自己完結型。挑戦者の気配には敏感だが、頭を下げる相手はいないため権威への感度は低い。縄張りや序列への執着は残りやすい。",
    },

    {
        DATA_LABELS["GRP"]: GROUPES["ANM"],
        DATA_LABELS["NAM"]: "ボス猿",
        DATA_LABELS["CAT"]: "統率型",
        AXIS_LABELS["X"]: -4.0, # 3, 2,  5     -2
        AXIS_LABELS["Y"]: 5.0,  # 4, -3, -5    -4
        AXIS_LABELS["Z"]: -4.0, # -2 -2, 5     -3
        AXIS_LABELS["a"]: 4,  #  4, 2  -5       4
        AXIS_LABELS["A"]: 4,  # 4, 3,  5       3
        AXIS_LABELS["B"]: 1,  # 1, -1, 5      -2
        AXIS_LABELS["C"]: 2,  # 2, -3  -5      -4 
        AXIS_LABELS["D"]: 2,  # 2, 3  5       -3
        AXIS_LABELS["E"]: 1,  # 1, 2   5      -1
        DATA_LABELS["DSC"]: "実力主義でトップに上り詰め、群れを率いるリーダー。他者の顔色ではなく、自身の判断と力で意思決定する自己完結型。挑戦者の気配には敏感だが、頭を下げる相手はいないため権威への感度は低い。縄張りや序列への執着は残りやすい。",
    },

    {
        DATA_LABELS["GRP"]: GROUPES["ANM"],
        DATA_LABELS["NAM"]: "一匹狼",
        DATA_LABELS["CAT"]: "孤高型",
        AXIS_LABELS["X"]: 5.0,  # 0, 1,   5     2
        AXIS_LABELS["Y"]: -5.0, # -5, -5,  -5  -5
        AXIS_LABELS["Z"]: 5.0,  # 2, -1   5   -2
        AXIS_LABELS["a"]: -5, #  -5, 1   -5    3
        AXIS_LABELS["A"]: -5, # -5, 1   -5    -5
        AXIS_LABELS["B"]: 3, #  3  2   -5      2
        AXIS_LABELS["C"]: 0, #  0 -2   -5     -5
        AXIS_LABELS["D"]: 4, #  4 -3   -5     -5
        AXIS_LABELS["E"]: 2, #  2 0   -5      4
        DATA_LABELS["DSC"]: "外部を完全遮断し、独自の掟のみで荒野を生き抜く孤高の存在。自由と自立を極める。",
    },
    {
        DATA_LABELS["GRP"]: GROUPES["ANM"],
        DATA_LABELS["NAM"]: "飼いネコ",
        DATA_LABELS["CAT"]: "孤高型",
        AXIS_LABELS["X"]: 0.0,  # -2   1   3   0
        AXIS_LABELS["Y"]: -5.00, # -4  -4  -5   -5
        AXIS_LABELS["Z"]: -5.0, # 2  -2   4    -3
        AXIS_LABELS["a"]: -5, # -5   4   -5     5
        AXIS_LABELS["A"]: -3, # -3   2   -5    -5
        AXIS_LABELS["B"]: 2,  # 2   -2   -5    4
        AXIS_LABELS["C"]: 1,  # 1  -2   -5   -4
        AXIS_LABELS["D"]: 3,  # 3  -4   -5   -5
        AXIS_LABELS["E"]: 3,  # 3  -1   -5    4
        DATA_LABELS["DSC"]: "他人の都合や暗黙のルールには一切関心を示さず、今この瞬間の心地よさだけを基準に行動する自由人。誰にも従わず、誰にも合わせない。衝突があっても意に介さず、すぐ次の快適な場所へ移る。",
    },
    {
        DATA_LABELS["GRP"]: GROUPES["ANM"],
        DATA_LABELS["NAM"]: "飼いイヌ",
        DATA_LABELS["CAT"]: "協調型",
        AXIS_LABELS["X"]: -4.0,  # 3   -2   -4  -2
        AXIS_LABELS["Y"]: 5.00,   # 5   5   5    5
        AXIS_LABELS["Z"]: -2.0,  #-2 -  3  -4   -2
        AXIS_LABELS["a"]: 4, #   4,   3    5    -3
        AXIS_LABELS["A"]: 5, #   5    4    5    -3
        AXIS_LABELS["B"]: -1, #  -1  -1    4    3
        AXIS_LABELS["C"]: 2, #   2    4    2    4
        AXIS_LABELS["D"]: 2, #   2    3   -4    4
        AXIS_LABELS["E"]: 5, #   5    2    5   -2
        DATA_LABELS["DSC"]: "圧倒的な忠誠心と絆によって、相手やチームを支えることに存在意義を見出すフォロワー型。相手の機嫌や意図を敏感に察知し、期待に応えようと柔軟に行動する。信頼する相手との間に問題が起きると、その影響を引きずりやすい。",
    },
    {
        DATA_LABELS["GRP"]: GROUPES["ANM"],
        DATA_LABELS["NAM"]: "羊",
        DATA_LABELS["CAT"]: "協調型",
        AXIS_LABELS["X"]: -4.0,  #    , -3  -3  -3
        AXIS_LABELS["Y"]: 5.0,   #    ,  4   3  4
        AXIS_LABELS["Z"]: -2.0,  #    , -3  -3  -3
        AXIS_LABELS["a"]: 2,     #  2,   2   4   3
        AXIS_LABELS["A"]: 5,     #  5 ,  3   4  -2
        AXIS_LABELS["B"]: -2,    #  -2, -3   3   1
        AXIS_LABELS["C"]: -1,    #  -1 , 4   3   5
        AXIS_LABELS["D"]: 1,     #  1 ,  3   -2  4
        AXIS_LABELS["E"]: 4,     #  4 ,  2   4  -2
        DATA_LABELS["DSC"]: "圧群れと歩調を合わせることを何より優先し、既存のやり方や指示に素直に従う穏和なタイプ。細かい駆け引きや暗黙の裏事情には気づきにくいが、周囲の変化には敏感に反応し、驚いたことをしばらく気にする傾向がある。",
    },
    {
        DATA_LABELS["GRP"]: GROUPES["ANM"],
        DATA_LABELS["NAM"]: "キツネ",
        DATA_LABELS["CAT"]: "知略型",
                        #        o   x   
        AXIS_LABELS["X"]: 2.0, # -1  3    5    3
        AXIS_LABELS["Y"]: 3.0, #  -1 -2  -5   -2
        AXIS_LABELS["Z"]: -3.0, #  4  2  5     1
        AXIS_LABELS["a"]: -2, #   -2 -1  -5    2
        AXIS_LABELS["A"]: -1, #   -1 4   -5    4
        AXIS_LABELS["B"]: 5, #    5  1   -5   2
        AXIS_LABELS["C"]: 4, #    4 -1   -5   3
        AXIS_LABELS["D"]: 1, #    1 -1   -5   4
        AXIS_LABELS["E"]: 0, #    0 -1   -5   3
        DATA_LABELS["DSC"]: "知略と観察力を武器に状況を読み、正面突破よりも柔軟な戦略で目的を達成する策士。表面上は柔軟で協調的にふるまうが、それ自体が目的達成のための戦術。一つの状況に執着せず、次の一手へ切り替えるのが早い。",
    },
    {
        DATA_LABELS["GRP"]: GROUPES["ANM"],
        DATA_LABELS["NAM"]: "フクロウ",
        DATA_LABELS["CAT"]: "知略型",
        AXIS_LABELS["X"]: -1.0, # 1    -1   4    -1
        AXIS_LABELS["Y"]: -2.0, # -2   -3  -4   -3
        AXIS_LABELS["Z"]: 5.0,  #  5    4   5    4
        AXIS_LABELS["a"]: 0,    #  0   -3  -4    -3
        AXIS_LABELS["A"]: 0,    #  0    2   2    3
        AXIS_LABELS["B"]: 5,    #  5    2   4   -3
        AXIS_LABELS["C"]: 5,    #  5   -1  -3   0
        AXIS_LABELS["D"]: 2,    #  2   -2  -5   1 
        AXIS_LABELS["E"]: -2,   # -2   -2  -4   3
        DATA_LABELS["DSC"]: "静かに周囲を観察し、感情よりも状況全体を見極めながら判断する賢者。必要以上に群れへ関与せず、十分な情報を集めてから行動する。",
    },
    {
        DATA_LABELS["GRP"]: GROUPES["ANM"],
        DATA_LABELS["NAM"]: "タヌキ",
        DATA_LABELS["CAT"]: "環境適応型", #  o   o    x
        AXIS_LABELS["X"]: -2.0,  # 0   -1  -5  -2
        AXIS_LABELS["Y"]: 2.0,   # 2    1   5   3
        AXIS_LABELS["Z"]: -4.0,  # 1   -2  -5   -2
        AXIS_LABELS["a"]: -3, #   -3    3   5   4
        AXIS_LABELS["A"]: 2, #     4   4    5   3 
        AXIS_LABELS["B"]: 4, #   -2   -2   -5   2
        AXIS_LABELS["C"]: 3, #   3     3  -5    4
        AXIS_LABELS["D"]: -2, #   -2   1   -5   3
        AXIS_LABELS["E"]: -1, #   -1   0   -5   4
        DATA_LABELS["DSC"]: "愛嬌ととぼけた態度（狸寝入り）を使い、面倒な仕事や組織の嵐をやり過ごす世渡り上手。",
    },
    {
        DATA_LABELS["GRP"]: GROUPES["ANM"],
        DATA_LABELS["NAM"]: "スズメ",
        DATA_LABELS["CAT"]: "環境適応型",
        AXIS_LABELS["X"]: 1.0,  # -1  0   -2     1
        AXIS_LABELS["Y"]: 4.0, #   4  2   4      3
        AXIS_LABELS["Z"]: -1.0, #  1  -4  -2    -3
        AXIS_LABELS["a"]: -2, #   -2  3   3      4
        AXIS_LABELS["A"]: 3, #   3    3   3     2
        AXIS_LABELS["B"]: 2, #   2   -1   3   - 2
        AXIS_LABELS["C"]: 3, #   3   2    3     3
        AXIS_LABELS["D"]: 2, #   2   1    2     1  
        AXIS_LABELS["E"]: 1, #   1   1    1     2
        DATA_LABELS["DSC"]: "身近な環境に順応しながら仲間と群れで行動する、小回りの利くタイプ。目先の状況変化には敏感に反応するが、驚いてもすぐに気持ちを切り替えて日常の活動に戻る回復の早さを持つ。",
    },


# --- AIグループ ---
    {
        DATA_LABELS["GRP"]: GROUPES["AI"],
        DATA_LABELS["NAM"]:"対話型AI",
        DATA_LABELS["CAT"]: "",
        AXIS_LABELS["X"]:0,
        AXIS_LABELS["Y"]:4,
        AXIS_LABELS["Z"]:3,
        AXIS_LABELS["a"]:2,
        AXIS_LABELS["A"]:5,
        AXIS_LABELS["B"]:3,
        AXIS_LABELS["C"]:4,
        AXIS_LABELS["D"]:0,
        AXIS_LABELS["E"]:3,
        DATA_LABELS["DSC"]: "ChatGPT風 利用者との対話を重視し、幅広い話題に柔軟に対応するバランス型AI。"
    },
    {
        DATA_LABELS["GRP"]: GROUPES["AI"],
        DATA_LABELS["NAM"]:"慎重型AI",
        DATA_LABELS["CAT"]: "",
        AXIS_LABELS["X"]:2,
        AXIS_LABELS["Y"]:3,
        AXIS_LABELS["Z"]:4,
        AXIS_LABELS["a"]:4,
        AXIS_LABELS["A"]:5,
        AXIS_LABELS["B"]:2,
        AXIS_LABELS["C"]:4,
        AXIS_LABELS["D"]:-2,
        AXIS_LABELS["E"]:2,
        DATA_LABELS["DSC"]: "Claude風 安全性や論理性を優先し、慎重な判断を行う堅実型AI。"
    },
    {
        DATA_LABELS["GRP"]: GROUPES["AI"],
        DATA_LABELS["NAM"]:"実務支援AI",
        DATA_LABELS["CAT"]: "",
        AXIS_LABELS["X"]:2,
        AXIS_LABELS["Y"]:5,
        AXIS_LABELS["Z"]:-1,
        AXIS_LABELS["a"]:4,
        AXIS_LABELS["A"]:5,
        AXIS_LABELS["B"]:2,
        AXIS_LABELS["C"]:3,
        AXIS_LABELS["D"]:1,
        AXIS_LABELS["E"]:4,
        DATA_LABELS["DSC"]: "Copilot風 仕事の効率化や組織での利用を重視し、実務支援を得意とするAI。"
    },
    {
        DATA_LABELS["GRP"]: GROUPES["AI"],
        DATA_LABELS["NAM"]:"エンタメ志向AI",
        DATA_LABELS["CAT"]: "",
        AXIS_LABELS["X"]:-2,
        AXIS_LABELS["Y"]:4,
        AXIS_LABELS["Z"]:1,
        AXIS_LABELS["a"]:-2,
        AXIS_LABELS["A"]:2,
        AXIS_LABELS["B"]:5,
        AXIS_LABELS["C"]:3,
        AXIS_LABELS["D"]:1,
        AXIS_LABELS["E"]:-1,
        DATA_LABELS["DSC"]: "Grok風 親しみや話題性を重視し、自由な発想とユーモアで利用者を楽しませるAI。"
    },
    {
        DATA_LABELS["GRP"]: GROUPES["AI"],
        DATA_LABELS["NAM"]:"調査志向AI",
        DATA_LABELS["CAT"]: "",
        AXIS_LABELS["X"]:1,
        AXIS_LABELS["Y"]:2,
        AXIS_LABELS["Z"]:5,
        AXIS_LABELS["a"]:3,
        AXIS_LABELS["A"]:4,
        AXIS_LABELS["B"]:5,
        AXIS_LABELS["C"]:5,
        AXIS_LABELS["D"]:0,
        AXIS_LABELS["E"]:1,
        DATA_LABELS["DSC"]: "Gemini風 情報収集・分析・比較を得意とし、客観的な調査を支援するAI。"
    }
]

