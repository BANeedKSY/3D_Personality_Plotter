# 3D性格分析ツール用定数データファイル

DEFALUT_DATA_VERSION = "0.20B"

# ペルソナグループ定義

GRP_ORG_INDEX = "G00"
GRP_ANM_INDEX = "G01"
GRP_HUM_INDEX = "G02"
GRP_GEN_INDEX = "G03"
GRP_CAL_INDEX = "G04"
GRP_LIF_INDEX = "G05"
GRP_AI_INDEX = "G06"
GRP_TST_INDEX = "G90"
GRP_DEF_INDEX = "G98"
GRP_CST_INDEX = "G99"

GRP_NAME_ORG = "原点"
GRP_NAME_ANM = "動物"
GRP_NAME_HUM = "人物"
GRP_NAME_GEN = "時代"
GRP_NAME_CAL = "文化圏"
GRP_NAME_LIF = "生活志向"
GRP_NAME_AI = "AI"
GRP_NAME_TST = "テスト"
GRP_NAME_DEF = "既定値"  # カスタム以外のグループをまとめるための仮のグループ名
GRP_NAME_CST = "カスタム"

GRP_NAMES = {
    GRP_ORG_INDEX : GRP_NAME_ORG,
    GRP_ANM_INDEX : GRP_NAME_ANM,
    GRP_HUM_INDEX : GRP_NAME_HUM,
    GRP_GEN_INDEX : GRP_NAME_GEN,
    GRP_CAL_INDEX : GRP_NAME_CAL,
    GRP_LIF_INDEX : GRP_NAME_LIF,
    GRP_AI_INDEX : GRP_NAME_AI,
    GRP_TST_INDEX : GRP_NAME_TST,
    GRP_DEF_INDEX : GRP_NAME_DEF,
    GRP_CST_INDEX : GRP_NAME_CST,
}

GRP_INIT_DISP = {
    GRP_ORG_INDEX : True,
    GRP_ANM_INDEX : True,
    GRP_HUM_INDEX : True,
    GRP_GEN_INDEX : False,
    GRP_CAL_INDEX : False,
    GRP_LIF_INDEX : False,
    GRP_AI_INDEX : True,
    GRP_TST_INDEX : False,
    GRP_DEF_INDEX : True,
    GRP_CST_INDEX : True,
}

GRP_HOVER = "grp_hover"

# データ範囲、デフォルトペルソナ・データベースの定義

AXIS_LABEL1_X = "X"
AXIS_LABEL1_Y = "Y"
AXIS_LABEL1_Z = "Z"
AXIS_LABEL1_A = "α"
AXIS_LABEL2_A = "A"
AXIS_LABEL2_B = "B"
AXIS_LABEL2_C = "C"
AXIS_LABEL2_D = "D"
AXIS_LABEL2_E = "E"

AXIS_NAME1_X = "方向性"
AXIS_NAME1_Y = "動機付" 
AXIS_NAME1_Z = "立脚点"
AXIS_NAME1_A = "快楽志向"
AXIS_NAME2_A = "文脈感度"
AXIS_NAME2_B = "重視対象"
AXIS_NAME2_C = "協調性"
AXIS_NAME2_D = "権威格差"
AXIS_NAME2_E = "事後反応"

AXIS_DESC1_X = "現状維持⇔現状打破"
AXIS_DESC1_Y = "自己完結⇔対人依存" 
AXIS_DESC1_Z = "具体的⇔抽象的"
AXIS_DESC1_A = "情緒的💕⇔感覚的🍖"
AXIS_DESC2_A = "不文律に鈍感⇔敏感"
AXIS_DESC2_B = "事実志向⇔価値観志向"
AXIS_DESC2_C = "頑固⇔素直・優柔不断"
AXIS_DESC2_D = "権威格差に鈍感⇔敏感"
AXIS_DESC2_E = "過去を引きづる⇔気にしない"

AXIS_PREFIX = ""
AXIS_SUFFIX = "軸"

STEP_MAX = 5
STEP_MIN = -5

DATA_GRP="グループ"
DATA_NAM="名前"
DATA_CAT="カテゴリ"
DATA_DSC="説明"
DATA_VAL="値"

#    DATA_LABEL_GRP = "グループ",
#    DATA_LABEL_NAM = "名前", 
#    DATA_LABEL_CAT = "カテゴリ",
#    DATA_LABEL_DSC = "説明",
#    DATA_LABEL_VAL = "値"

####            ChatGPT,   Grok,  Gemini,  Claude

# df_default 用基礎データ
DEFAULT_PERSONAS = [
    #  記述書式  
    #    DATA_GRP: GRP_ORG_INDEX, GRP_ANM_INDEX, .....          
    #    DATA_NAM: 個別名称,            
    #     DATA_CAT: 小区分,    
    #    ----------------------------------------------------------------------------------
    #    AXIS_LABEL1_X: 数値-5.0～5.0,   保守・秩序維持 ⇔ 革新・リベラル・新ルール作り
    #    AXIS_LABEL1_Y: 数値-5.0～5.0,   自己完結 ⇔ 対人依存
    #    AXIS_LABEL1_Z: 数値-5.0～5.0,   具体 ⇔ 抽象
    #    AXIS_LABEL1_A: 数値-5.0～5.0,   審美的・情緒的（色気💕） ⇔ 感覚的(食い気🍖🍶）
    #    ----------------------------------------------------------------------------------
    #    AXIS_LABEL2_A: 数値-5.0～5.0,   暗黙の了解（不文律）に無頓着 ⇔ 暗黙の了解に敏感
    #    AXIS_LABEL2_B: 数値-5.0～5.0,   価値の絶対性、普遍性(事実）を重視 ⇔ 価値の相対性（価値観）を重視
    #    AXIS_LABEL2_C: 数値-5.0～5.0,   頑固 ⇔ 素直・柔軟・優柔不断
    #    AXIS_LABEL2_D: 数値-5.0～5.0,   権威格差に鈍感（上下関係に無頓着） ⇔ 権威格差に敏感（盲従、支配傾向大）
    #    AXIS_LABEL2_E: 数値-5.0～5.0,   気にする、引きづる  ⇔ 気にならない、全く堪えない
    #    ----------------------------------------------------------------------------------
    #    DATA_DSC:  "個性の概要説明",
    #
    # --- 原点グループ ---
    {
        DATA_GRP: GRP_ORG_INDEX,
        DATA_NAM: "原点",
        DATA_CAT: "無味無臭無垢",
        AXIS_LABEL1_X: 0,
        AXIS_LABEL1_Y: 0,
        AXIS_LABEL1_Z: 0,
        AXIS_LABEL1_A: 0,
        AXIS_LABEL2_A: 0,
        AXIS_LABEL2_B: 0,
        AXIS_LABEL2_C: 0, 
        AXIS_LABEL2_D: 0,
        AXIS_LABEL2_E: 0,
        DATA_DSC: (
            "性格形成の原点（新生児・幼少期イメージ）。\n"
            "全軸0の状態。育ち方によってここから様々な方向に変化していく基準点として使用。\n"
            "幼い頃との振り返り比較用。"
            )
    },
    
    # --- 動物グループ ---
    {
        DATA_GRP: GRP_ANM_INDEX,
        DATA_NAM: "女王蜂",
        DATA_CAT: "統率型",
        AXIS_LABEL1_X: -5.00, #
        AXIS_LABEL1_Y: 5.00,  #
        AXIS_LABEL1_Z: 5.00,  #
        AXIS_LABEL1_A: 3,     #  4,  2  -5      3
        AXIS_LABEL2_A: 0,     #  4,  3,  5     -2 #不明
        AXIS_LABEL2_B: 0,     #  1, -1,  5     -4 #不明
        AXIS_LABEL2_C: -4.00, #  2, -3  -5     -4 
        AXIS_LABEL2_D: -5.00, #  2,  3   5     -5
        AXIS_LABEL2_E: 4.00,  #  1,  2   5      5
        DATA_DSC: ( 
            "個としての意思よりも、群れ全体の秩序そのものを体現する存在。\n"
            "自らは動かず、周囲がすべてを解釈・実行することで初めて機能する、極めて抽象度の高い『象徴』としての生命体。\n"
            "自身は上位の権威を意識する必要がなく、状況の変化にもほぼ動じない。"
            ),  
    },

    {
        DATA_GRP: GRP_ANM_INDEX,
        DATA_NAM: "ボス猿",
        DATA_CAT: "統率型",
        AXIS_LABEL1_X: -4.0,  #  3,  2,  5,  -2
        AXIS_LABEL1_Y: 5.0,   #  4, -3, -5,  -4
        AXIS_LABEL1_Z: -4.0,  # -2, -2,  5,  -3
        AXIS_LABEL1_A: 3,     #  4,  2  -5,   4
        AXIS_LABEL2_A: 4,     #  4,  3,  5,   3
        AXIS_LABEL2_B: 1,     #  1, -1,  5,  -2
        AXIS_LABEL2_C: 2,     #  2, -3, -5,  -4 
        AXIS_LABEL2_D: 2,     #  2,  3,  5,  -3
        AXIS_LABEL2_E: -1,    #  1,  2,  5,  -1
        DATA_DSC: (
            "実力主義でトップに上り詰め、群れを率いるリーダー。\n"
            "他者の顔色ではなく、自身の判断と力で意思決定する自己完結型。\n"
            "挑戦者の気配には敏感だが、頭を下げる相手はいないため権威への感度は低い。\n"
            "縄張りや序列への執着は残りやすい。",
            )
    },

    {
        DATA_GRP: GRP_ANM_INDEX,
        DATA_NAM: "一匹狼",
        DATA_CAT: "孤高型",
        AXIS_LABEL1_X: 5.0,   #  0,  1,  5   2
        AXIS_LABEL1_Y: -5.00, # -5, -5, -5  -5
        AXIS_LABEL1_Z: 5.0,   #  2, -1   5  -2
        AXIS_LABEL1_A: 3,     # -5,  1  -5   3
        AXIS_LABEL2_A: -5,    # -5,  1  -5  -5
        AXIS_LABEL2_B: 3,     #  3   2  -5   2
        AXIS_LABEL2_C: -5,    #  0  -2  -5  -5
        AXIS_LABEL2_D: -5,    #  4  -3  -5  -5
        AXIS_LABEL2_E: 2,     #  2   0  -5   4
        DATA_DSC: (
            "群れの掟や既存の社会秩序を離れ、外部からの情報を完全に遮断して独自の掟のみに従う孤高の存在。\n"
            "誰の顔色もうかがわず、誰の権威も認めない。\n"
            "荒野を進む中で過去の衝突を引きずることも少ない。自由と自立を極める。"
            )
    },
    {
        DATA_GRP: GRP_ANM_INDEX,
        DATA_NAM: "飼いネコ",
        DATA_CAT: "孤高型",
        AXIS_LABEL1_X: 0.0,   # -2   1   3   0
        AXIS_LABEL1_Y: -4.00, # -4  -4  -5  -5
        AXIS_LABEL1_Z: -5.0,  #  2  -2   4  -3
        AXIS_LABEL1_A: 4,     # -5   4  -5   5
        AXIS_LABEL2_A: -3,    # -3   2  -5  -5
        AXIS_LABEL2_B: 2,     #  2  -2  -5   4
        AXIS_LABEL2_C: 1,     #  1  -2  -5  -4
        AXIS_LABEL2_D: 3,     #  3  -4  -5  -5
        AXIS_LABEL2_E: 3,     #  3  -1  -5   4
        DATA_DSC: (
            "他人の都合や暗黙のルールには一切関心を示さず、今この瞬間の心地よさだけを基準に行動する自由人。\n"
            "誰にも従わず、誰にも合わせない。\n"
            "衝突があっても意に介さず、すぐ次の快適な場所へ移る。",
            )
    },
    {
        DATA_GRP: GRP_ANM_INDEX,
        DATA_NAM: "飼いイヌ",
        DATA_CAT: "協調型",
        AXIS_LABEL1_X: -3.00, #  3  -2  -4  -2
        AXIS_LABEL1_Y: 5.00,  #  5   5   5   5
        AXIS_LABEL1_Z: -3.0,  # -2  -3  -4  -2
        AXIS_LABEL1_A: 4.00,  #  4,  3   5  -3
        AXIS_LABEL2_A: 5,     #  5   4   5  -3
        AXIS_LABEL2_B: -1,    # -1  -1   4   3
        AXIS_LABEL2_C: 2,     #  2   4   2   4
        AXIS_LABEL2_D: 2,     #  2   3  -4   4
        AXIS_LABEL2_E: 5,     #  5   2   5  -2
        DATA_DSC: (
            "圧倒的な忠誠心と絆によって、相手やチームを支えることに存在意義を見出すフォロワー型。\n"
            "相手の機嫌や意図を敏感に察知し、期待に応えようと柔軟に行動する。\n"
            "信頼する相手との間に問題が起きると、その影響を引きずりやすい。",
            )
    },
    {
        DATA_GRP: GRP_ANM_INDEX,
        DATA_NAM: "羊",
        DATA_CAT: "協調型",
        AXIS_LABEL1_X: -3.00, #   , -3  -3  -3
        AXIS_LABEL1_Y: 5.0,   #   ,  4   3   4
        AXIS_LABEL1_Z: -2.0,  #   , -3  -3  -3
        AXIS_LABEL1_A: 3.00,  #  2,  2   4   3
        AXIS_LABEL2_A: 5,     #  5,  3   4  -2
        AXIS_LABEL2_B: -2,    # -2, -3   3   1
        AXIS_LABEL2_C: -1,    # -1,  4   3   5
        AXIS_LABEL2_D: 1,     #  1,  3  -2   4
        AXIS_LABEL2_E: 4,     #  4,  2   4  -2
        DATA_DSC: (
            "群れと歩調を合わせることを何より優先し、既存のやり方や指示に素直に従う穏和なタイプ。\n"
            "細かい駆け引きや暗黙の裏事情には気づきにくいが、周囲の変化には敏感に反応し、驚いたことをしばらく気にする傾向がある。",
        )
    },
    {
        DATA_GRP: GRP_ANM_INDEX,
        DATA_NAM: "キツネ",
        DATA_CAT: "知略型",
                        #        o   x   
        AXIS_LABEL1_X: 3.00,  # -1   3   5   3
        AXIS_LABEL1_Y: -2.0,  # -1  -2  -5  -2
        AXIS_LABEL1_Z: -3.0,  #  4   2   5   1
        AXIS_LABEL1_A: -2,    # -2  -1  -5   2
        AXIS_LABEL2_A: -1,    # -1   4  -5   4
        AXIS_LABEL2_B: 5,     #  5   1  -5   2
        AXIS_LABEL2_C: 4,     #  4  -1  -5   3
        AXIS_LABEL2_D: 1,     #  1  -1  -5   4
        AXIS_LABEL2_E: 0,     #  0  -1  -5   3
        DATA_DSC: (
            "場の空気や力関係を素早く読み取り、それを逆手に取って立ち回る策士型。\n"
            "表面上は柔軟で協調的にふるまうが、それ自体が目的達成のための戦術。\n"
            "一つの状況に執着せず、次の一手へ切り替えるのが早い。"
        )
    },
    {
        DATA_GRP: GRP_ANM_INDEX,
        DATA_NAM: "フクロウ",
        DATA_CAT: "知略型",
        AXIS_LABEL1_X: -1.00, #  1   -1   4   -1
        AXIS_LABEL1_Y: -2.0,  # -2   -3  -4   -3
        AXIS_LABEL1_Z: 5.0,   #  5    4   5    4
        AXIS_LABEL1_A: 0,     #  0   -3  -4   -3
        AXIS_LABEL2_A: 0,     #  0    2   2    3
        AXIS_LABEL2_B: 5,     #  5    2   4   -3
        AXIS_LABEL2_C: 5,     #  5   -1  -3    0
        AXIS_LABEL2_D: 2,     #  2   -2  -5    1 
        AXIS_LABEL2_E: -2,    # -2   -2  -4    3
        DATA_DSC: (
            "物事を一歩引いた視点から俯瞰し、抽象度の高い理屈や法則で捉えることを好む知性派。\n"
            "単独行動を好むが、周囲の気配や暗黙の変化には敏感。\n"
            "感情の波が少なく、衝突があっても淡々と受け流す。\n"
# ChatGPT      DATA_DSC: ("静かに周囲を観察し、感情よりも状況全体を見極めながら判断する賢者型タイプ。必要以上に群れへ関与せず、十分な情報を集めてから行動する。"
            )
    },
    {
        DATA_GRP: GRP_ANM_INDEX,
        DATA_NAM: "タヌキ",
        DATA_CAT: "環境適応型", 
        AXIS_LABEL1_X: -2.00, #  0  -1  -5  -2
        AXIS_LABEL1_Y: 2.0,   #  2   1   5   3
        AXIS_LABEL1_Z: -3.0,  #  1  -2  -5  -2
        AXIS_LABEL1_A: -3,    # -3   3   5   4
        AXIS_LABEL2_A: 2,     #  4   4   5   3 
        AXIS_LABEL2_B: 4,     # -2  -2  -5   2
        AXIS_LABEL2_C: 3,     #  3   3  -5   4
        AXIS_LABEL2_D: -2,    # -2   1  -5   3
        AXIS_LABEL2_E: -1,    # -1   0  -5   4
        DATA_DSC: (
            "愛嬌とトボけ（狸寝入り）を武器に、面倒な仕事や組織内の嵐を上手にやり過ごす世渡り上手。\n"
            "集団の中に身を置きつつ、空気を読んで衝突を回避することに長ける。\n"
            "争いごとを長く引きずらず、ほとぼりが冷めるのを待つのが得意。"
        )
    },
    {
        DATA_GRP: GRP_ANM_INDEX,
        DATA_NAM: "スズメ",
        DATA_CAT: "環境適応型",
        AXIS_LABEL1_X: 1.00, # -1  0  -2   1
        AXIS_LABEL1_Y: 4.0,  #  4  2   4   3
        AXIS_LABEL1_Z: -1.0, #  1 -4  -2  -3
        AXIS_LABEL1_A: -2,   # -2  3   3   4
        AXIS_LABEL2_A: 3,    #  3  3   3   2
        AXIS_LABEL2_B: 2,    #  2 -1   3  -2
        AXIS_LABEL2_C: 3,    #  3  2   3   3
        AXIS_LABEL2_D: 2,    #  2  1   2   1  
        AXIS_LABEL2_E: 1,    #  1  1   1   2
        DATA_DSC: (
            "身近な環境に順応しながら仲間と群れで行動する、小回りの利くタイプ。\n"
            "目先の状況変化には敏感に反応するが、驚いてもすぐに気持ちを切り替えて日常の活動に戻る回復の早さを持つ。",
        )
    },
### 追加候補：ワシ（大局を見る挑戦者）　イルカ（知的で協調的な探究者）　ジンベイ鮫



# --- AIグループ ---
    {
        DATA_GRP: GRP_AI_INDEX,
        DATA_NAM:"対話型AI",
        DATA_CAT: "",
        AXIS_LABEL1_X: 0,
        AXIS_LABEL1_Y: 4,
        AXIS_LABEL1_Z: 3,
        AXIS_LABEL1_A: 2,
        AXIS_LABEL2_A: 5,
        AXIS_LABEL2_B: 3,
        AXIS_LABEL2_C: 4,
        AXIS_LABEL2_D: 0,
        AXIS_LABEL2_E: 3,
        DATA_DSC: (
            "ChatGPT風 利用者との対話を重視し、幅広い話題に柔軟に対応するバランス型AI。"
        )
    },
    {
        DATA_GRP: GRP_AI_INDEX,
        DATA_NAM:"慎重型AI",
        DATA_CAT: "",
        AXIS_LABEL1_X: 2,
        AXIS_LABEL1_Y: 3,
        AXIS_LABEL1_Z: 4,
        AXIS_LABEL1_A: 4,
        AXIS_LABEL2_A: 5,
        AXIS_LABEL2_B: 2,
        AXIS_LABEL2_C: 4,
        AXIS_LABEL2_D:-2,
        AXIS_LABEL2_E: 2,
        DATA_DSC: ( 
            "Claude風 安全性や論理性を優先し、慎重な判断を行う堅実型AI。"
        )
    },
    {
        DATA_GRP: GRP_AI_INDEX,
        DATA_NAM:"実務支援AI",
        DATA_CAT: "",
        AXIS_LABEL1_X: 2,
        AXIS_LABEL1_Y: 5,
        AXIS_LABEL1_Z:-1,
        AXIS_LABEL1_A: 4,
        AXIS_LABEL2_A: 5,
        AXIS_LABEL2_B: 2,
        AXIS_LABEL2_C: 3,
        AXIS_LABEL2_D: 1,
        AXIS_LABEL2_E: 4,
        DATA_DSC: (
            "Copilot風 仕事の効率化や組織での利用を重視し、実務支援を得意とするAI。"
        )
    },
    {
        DATA_GRP: GRP_AI_INDEX,
        DATA_NAM:"エンタメ志向AI",
        DATA_CAT: "",
        AXIS_LABEL1_X: 2,
        AXIS_LABEL1_Y: 4,
        AXIS_LABEL1_Z: 1,
        AXIS_LABEL1_A:-2,
        AXIS_LABEL2_A: 2,
        AXIS_LABEL2_B: 5,
        AXIS_LABEL2_C: 3,
        AXIS_LABEL2_D: 1,
        AXIS_LABEL2_E:-1,
        DATA_DSC: (
            "Grok風 親しみや話題性を重視し、自由な発想とユーモアで利用者を楽しませるAI。"
        )
    },
    {
        DATA_GRP: GRP_AI_INDEX,
        DATA_NAM:"調査志向AI",
        DATA_CAT: "",
        AXIS_LABEL1_X: 1,
        AXIS_LABEL1_Y: 2,
        AXIS_LABEL1_Z: 5,
        AXIS_LABEL1_A: 3,
        AXIS_LABEL2_A: 4,
        AXIS_LABEL2_B: 5,
        AXIS_LABEL2_C: 5,
        AXIS_LABEL2_D: 0,
        AXIS_LABEL2_E: 1,
        DATA_DSC: (
            "Gemini風 情報収集・分析・比較を得意とし、客観的な調査を支援するAI。"
        )
    },

    {
        DATA_GRP: GRP_AI_INDEX,
        DATA_NAM:"平均的な生成AI（2026年版）",
        DATA_CAT: "",
        AXIS_LABEL1_X:1,
        AXIS_LABEL1_Y:4,
        AXIS_LABEL1_Z:3,
        AXIS_LABEL1_A:3,
        AXIS_LABEL2_A:5,
        AXIS_LABEL2_B:3,
        AXIS_LABEL2_C:4,
        AXIS_LABEL2_D:0,
        AXIS_LABEL2_E:3,
        DATA_DSC: (
            "多様な利用者への支援を目的とし、協調性・情報整理・中立性を重視する対話型AIの代表的イメージ。"
        )
    },

# --- GEN(世代)グループ ---


    {
        DATA_GRP: GRP_GEN_INDEX,
        DATA_NAM:"終戦直後（1945年）",
        DATA_CAT:"日本",
        AXIS_LABEL1_X:5,
        AXIS_LABEL1_Y:5,
        AXIS_LABEL1_Z:-4,
        AXIS_LABEL1_A:5,
        AXIS_LABEL2_A:5,
        AXIS_LABEL2_B:-4,
        AXIS_LABEL2_C:-1,
        AXIS_LABEL2_D:-2,
        AXIS_LABEL2_E:5,
        DATA_DSC: (
            "生き延びることが最優先。共同体への依存が極めて強く、秩序・上下関係・助け合いを重視する時代。"
        )
    },
    
    {
        DATA_GRP: GRP_GEN_INDEX,
        DATA_NAM:"高度経済成長（1960年頃）",
        DATA_CAT:"日本",
        AXIS_LABEL1_X:4,
        AXIS_LABEL1_Y:5,
        AXIS_LABEL1_Z:-3,
        AXIS_LABEL1_A:5,
        AXIS_LABEL2_A:5,
        AXIS_LABEL2_B:-2,
        AXIS_LABEL2_C:1,
        AXIS_LABEL2_D:1,
        AXIS_LABEL2_E:5,
        DATA_DSC: (
            "努力すれば豊かになれるという期待が社会全体を支え、会社・学校・地域社会への帰属意識が非常に強い時代。"
        )
    },
    
    {
        DATA_GRP: GRP_GEN_INDEX,
        DATA_NAM:"学生運動・大阪万博（1970年頃）",
        DATA_CAT:"日本",
        AXIS_LABEL1_X:3,
        AXIS_LABEL1_Y:4,
        AXIS_LABEL1_Z:1,
        AXIS_LABEL1_A:2,
        AXIS_LABEL2_A:3,
        AXIS_LABEL2_B:2,
        AXIS_LABEL2_C:3,
        AXIS_LABEL2_D:2,
        AXIS_LABEL2_E:2,
        DATA_DSC: (
            "伝統的価値観と新しい価値観がぶつかり合う転換期。\n"
            "組織への忠誠と権威への批判が同時に存在した時代。"
        )
    },


    {
        DATA_GRP: GRP_GEN_INDEX,
        DATA_NAM:"平均的な高校生（1970年頃）",
        DATA_CAT:"日本",
        AXIS_LABEL1_X:2,
        AXIS_LABEL1_Y:4,
        AXIS_LABEL1_Z:-2,
        AXIS_LABEL1_A:2,
        AXIS_LABEL2_A:3,
        AXIS_LABEL2_B:-1,
        AXIS_LABEL2_C:0,
        AXIS_LABEL2_D:0,
        AXIS_LABEL2_E:3,
        DATA_DSC: (
            "学校や家庭の影響を強く受け、集団との調和を重視する傾向が強い。\n"
            "当時の社会規範を比較的素直に受け入れる文化的イメージ。"
        )
    },
    {
        DATA_GRP: GRP_GEN_INDEX,
        DATA_NAM:"平均的な大学生（1970年頃）",
        DATA_CAT:"日本",
        AXIS_LABEL1_X:-1,
        AXIS_LABEL1_Y:2,
        AXIS_LABEL1_Z:3,
        AXIS_LABEL1_A:-1,
        AXIS_LABEL2_A:1,
        AXIS_LABEL2_B:3,
        AXIS_LABEL2_C:3,
        AXIS_LABEL2_D:2,
        AXIS_LABEL2_E:-1,
        DATA_DSC: (
            "社会や政治への関心が比較的高く、既存の価値観を問い直そうとする気風も残る時代の学生像。"
        )
    },
    {
        DATA_GRP: GRP_GEN_INDEX,
        DATA_NAM:"平均的な社会人（1970年頃）",
        DATA_CAT:"日本",
        AXIS_LABEL1_X:3,
        AXIS_LABEL1_Y:4,
        AXIS_LABEL1_Z:-2,
        AXIS_LABEL1_A:4,
        AXIS_LABEL2_A:5,
        AXIS_LABEL2_B:-1,
        AXIS_LABEL2_C:1,
        AXIS_LABEL2_D:1,
        AXIS_LABEL2_E:4,
        DATA_DSC: (
            "終身雇用や年功序列を前提に、会社への帰属意識と組織への忠誠を重視する企業人の文化的イメージ。"
        )
    },
    {
        DATA_GRP: GRP_GEN_INDEX,
        DATA_NAM:"平均的な高齢者（1970年頃）",
        DATA_CAT:"日本",
        AXIS_LABEL1_X:5,
        AXIS_LABEL1_Y:3,
        AXIS_LABEL1_Z:-3,
        AXIS_LABEL1_A:5,
        AXIS_LABEL2_A:4,
        AXIS_LABEL2_B:-2,
        AXIS_LABEL2_C:2,
        AXIS_LABEL2_D:2,
        AXIS_LABEL2_E:4,
        DATA_DSC: (
            "戦前・戦中を経験し、年長者や社会秩序への敬意を重視する傾向が強い文化的イメージ。\n"
            "価値観とのギャップ差への困惑・抵抗・期待感などの個人差は大"
        )
    },

    {
        DATA_GRP: GRP_GEN_INDEX,
        DATA_NAM:"バブル経済（1989年頃）",
        DATA_CAT:"日本",
        AXIS_LABEL1_X:2,
        AXIS_LABEL1_Y:3,
        AXIS_LABEL1_Z:1,
        AXIS_LABEL1_A:2,
        AXIS_LABEL2_A:3,
        AXIS_LABEL2_B:3,
        AXIS_LABEL2_C:3,
        AXIS_LABEL2_D:0,
        AXIS_LABEL2_E:2,
        DATA_DSC: (
            "豊かさへの自信が社会全体を覆い、消費・個性・自己実現への関心が高まった時代。"
        )
    },
    {
        DATA_GRP: GRP_GEN_INDEX,
        DATA_NAM:"失われた10年・Windows95（1995年頃）",
        DATA_CAT:"日本",
        AXIS_LABEL1_X:2,
        AXIS_LABEL1_Y:2,
        AXIS_LABEL1_Z:2,
        AXIS_LABEL1_A:1,
        AXIS_LABEL2_A:3,
        AXIS_LABEL2_B:3,
        AXIS_LABEL2_C:4,
        AXIS_LABEL2_D:-1,
        AXIS_LABEL2_E:1,
        DATA_DSC: (
            "経済への不安が広がる一方で、インターネットが個人の情報発信と価値観の多様化を後押しした時代。"
        )
    },

    {
        DATA_GRP: GRP_GEN_INDEX,
        DATA_NAM:"IT革命・就職氷河期（2000年頃）",
        DATA_CAT:"日本",
        AXIS_LABEL1_X:1,
        AXIS_LABEL1_Y:2,
        AXIS_LABEL1_Z:3,
        AXIS_LABEL1_A:1,
        AXIS_LABEL2_A:3,
        AXIS_LABEL2_B:4,
        AXIS_LABEL2_C:4,
        AXIS_LABEL2_D:-2,
        AXIS_LABEL2_E:1,
        DATA_DSC: (
            "終身雇用への信頼が揺らぎ、自分で生き方を選ぶという意識が強まり始めた時代。"
        )
    },
    {
        DATA_GRP: GRP_GEN_INDEX,
        DATA_NAM:"東日本大震災（2011年頃）",
        DATA_CAT:"日本",
        AXIS_LABEL1_X:2,
        AXIS_LABEL1_Y:3,
        AXIS_LABEL1_Z:2,
        AXIS_LABEL1_A:1,
        AXIS_LABEL2_A:5,
        AXIS_LABEL2_B:2,
        AXIS_LABEL2_C:4,
        AXIS_LABEL2_D:-1,
        AXIS_LABEL2_E:4,
        DATA_DSC: (
            "未曽有の災害を契機に、地域・家族・助け合いの価値が再認識される一方、SNSによる情報共有も急速に広がった時代。"
        )
    },
    {
        DATA_GRP: GRP_GEN_INDEX,
        DATA_NAM:"コロナ禍（2020年頃）",
        DATA_CAT:"日本",
        AXIS_LABEL1_X:1,
        AXIS_LABEL1_Y:1,
        AXIS_LABEL1_Z:4,
        AXIS_LABEL1_A:1,
        AXIS_LABEL2_A:4,
        AXIS_LABEL2_B:4,
        AXIS_LABEL2_C:5,
        AXIS_LABEL2_D:-2,
        AXIS_LABEL2_E:2,
        DATA_DSC: (
            "オンライン化が急速に進み、個人の生活様式や働き方が大きく変化した時代。\n"
            "科学的情報と多様な価値観の両方が重視された。"
        )
    },
    {
        DATA_GRP: GRP_GEN_INDEX,
        DATA_NAM:"生成AI時代（2025年頃）",
        DATA_CAT:"日本",
        AXIS_LABEL1_X:0,
        AXIS_LABEL1_Y:1,
        AXIS_LABEL1_Z:5,
        AXIS_LABEL1_A:0,
        AXIS_LABEL2_A:3,
        AXIS_LABEL2_B:5,
        AXIS_LABEL2_C:5,
        AXIS_LABEL2_D:-2,
        AXIS_LABEL2_E:1,
        DATA_DSC: (
            "知識へのアクセスが大きく変化し、人とAIが協働する社会への移行が始まった時代。\n"
            "専門知識よりも、問いを立てる力や情報を見極める力の重要性が高まる文化的イメージ。"
        )
    },
    
    {
        DATA_GRP: GRP_GEN_INDEX,
        DATA_NAM:"平均的な会社員（2026年版）",
        DATA_CAT:"日本",
        AXIS_LABEL1_X:2,
        AXIS_LABEL1_Y:3,
        AXIS_LABEL1_Z:-1,
        AXIS_LABEL1_A:3,
        AXIS_LABEL2_A:4,
        AXIS_LABEL2_B:0,
        AXIS_LABEL2_C:1,
        AXIS_LABEL2_D:0,
        AXIS_LABEL2_E:3,
        DATA_DSC: (
            "組織との協調を重視し、役割分担やルールに従って安定した成果を目指す一般的なビジネスパーソン。"
        )
    },
    {
        DATA_GRP: GRP_GEN_INDEX,
        DATA_NAM:"平均的な高校生（2026年版）",
        DATA_CAT:"日本",
        AXIS_LABEL1_X:-1,
        AXIS_LABEL1_Y:3,
        AXIS_LABEL1_Z:-2,
        AXIS_LABEL1_A:-1,
        AXIS_LABEL2_A:3,
        AXIS_LABEL2_B:1,
        AXIS_LABEL2_C:0,
        AXIS_LABEL2_D:-1,
        AXIS_LABEL2_E:1,
        DATA_DSC: (
            "友人関係や学校生活の影響を受けやすく、価値観を模索している成長途中のモデル。"
        )
    },
    {
        DATA_GRP: GRP_GEN_INDEX,
        DATA_NAM:"平均的な大学生（2026年版）",
        DATA_CAT:"日本",
        AXIS_LABEL1_X:-1,
        AXIS_LABEL1_Y:2,
        AXIS_LABEL1_Z:1,
        AXIS_LABEL1_A:-1,
        AXIS_LABEL2_A:2,
        AXIS_LABEL2_B:2,
        AXIS_LABEL2_C:2,
        AXIS_LABEL2_D:0,
        AXIS_LABEL2_E:0,
        DATA_DSC: (
            "行動範囲や価値観が広がり始め、自立と協調のバランスを模索している若年層モデル。"
        )
    },
    {
        DATA_GRP: GRP_GEN_INDEX,
        DATA_NAM:"平均的な高齢者（2026年版）",
        DATA_CAT:"日本",
        AXIS_LABEL1_X:3,
        AXIS_LABEL1_Y:2,
        AXIS_LABEL1_Z:-1,
        AXIS_LABEL1_A:2,
        AXIS_LABEL2_A:3,
        AXIS_LABEL2_B:-1,
        AXIS_LABEL2_C:2,
        AXIS_LABEL2_D:1,
        AXIS_LABEL2_E:2,
        DATA_DSC: (
            "長年の経験を重視し、安定や慣習を大切にする傾向を持つモデル。"
        )
    },
    
    {
        DATA_GRP: GRP_CAL_INDEX,
        DATA_NAM:"日本社会（2026）",
        DATA_CAT:"日本",
        AXIS_LABEL1_X:1,
        AXIS_LABEL1_Y:2,
        AXIS_LABEL1_Z:3,
        AXIS_LABEL1_A:1,
        AXIS_LABEL2_A:3,
        AXIS_LABEL2_B:3,
        AXIS_LABEL2_C:4,
        AXIS_LABEL2_D:-2,
        AXIS_LABEL2_E:2,
        DATA_DSC: (
            "協調を重視しながらも、個人の価値観が多様化している成熟社会。\n"
            "対立より調整を好む文化的イメージ。"
        )
    },
    

    {
        DATA_GRP: GRP_CAL_INDEX,
        DATA_NAM:"アメリカ社会（2026）",
        DATA_CAT:"米国",
        AXIS_LABEL1_X:-2,
        AXIS_LABEL1_Y:-3,
        AXIS_LABEL1_Z:2,
        AXIS_LABEL1_A:-3,
        AXIS_LABEL2_A:1,
        AXIS_LABEL2_B:4,
        AXIS_LABEL2_C:4,
        AXIS_LABEL2_D:4,
        AXIS_LABEL2_E:-2,
        DATA_DSC: (
            "個人の自由と自己責任を強く重視する文化。\n"
            "自ら主張し挑戦する姿勢が高く評価される傾向。"
        )
    },
    
    {
        DATA_GRP: GRP_CAL_INDEX,
        DATA_NAM:"EU社会（2026）",
        DATA_CAT:"EU",
        AXIS_LABEL1_X:-3,
        AXIS_LABEL1_Y:0,
        AXIS_LABEL1_Z:4,
        AXIS_LABEL1_A:-2,
        AXIS_LABEL2_A:4,
        AXIS_LABEL2_B:3,
        AXIS_LABEL2_C:4,
        AXIS_LABEL2_D:0,
        AXIS_LABEL2_E:0,
        DATA_DSC: (
            "多様性・対話・社会的合意を重視する文化。\n"
            "個人の自由と共同体の調和の両立を志向する傾向。"
        )
    },

    {
        DATA_GRP: GRP_CAL_INDEX,
        DATA_NAM:"中国大陸社会（2026）",
        DATA_CAT:"中国大陸",
        AXIS_LABEL1_X:4,
        AXIS_LABEL1_Y:4,
        AXIS_LABEL1_Z:0,
        AXIS_LABEL1_A:4,
        AXIS_LABEL2_A:4,
        AXIS_LABEL2_B:1,
        AXIS_LABEL2_C:3,
        AXIS_LABEL2_D:2,
        AXIS_LABEL2_E:4,
        DATA_DSC: (
            "集団・組織・国家との一体感を重視し、秩序や長期的な安定を重視する文化的イメージ。"
        )
    },
    
        {
        DATA_GRP: GRP_LIF_INDEX,
        DATA_NAM:"社交的な酒好き(非酒乱)",
        DATA_CAT:"",
        AXIS_LABEL1_X:0,
        AXIS_LABEL1_Y:3,
        AXIS_LABEL1_Z:-2,
        AXIS_LABEL1_A:0,
        AXIS_LABEL2_A:4,
        AXIS_LABEL2_B:1,
        AXIS_LABEL2_C:1,
        AXIS_LABEL2_D:-1,
        AXIS_LABEL2_E:2,
        DATA_DSC: (
            "飲酒を人との交流やリラックスの手段として楽しむライフスタイル。\n"
            "酒量そのものではなく、社交の場を好む文化的タイプ。"
        )
    },

    {
        DATA_GRP: GRP_LIF_INDEX,
        DATA_NAM:"ノンアルコール志向",
        DATA_CAT:"",
        AXIS_LABEL1_X:1,
        AXIS_LABEL1_Y:0,
        AXIS_LABEL1_Z:2,
        AXIS_LABEL1_A:0,
        AXIS_LABEL2_A:2,
        AXIS_LABEL2_B:2,
        AXIS_LABEL2_C:3,
        AXIS_LABEL2_D:2,
        AXIS_LABEL2_E:0,
        DATA_DSC: (
            "健康・価値観・体質・生活習慣など様々な理由から飲酒を選ばないライフスタイル。\n"
            "飲酒の有無を人格の優劣とは結び付けない。"
        )
    },

    {
        DATA_GRP: GRP_LIF_INDEX,
        DATA_NAM:"健康志向（運動・筋トレ）",
        DATA_CAT:"",
        AXIS_LABEL1_X:1,
        AXIS_LABEL1_Y:0,
        AXIS_LABEL1_Z:-1,
        AXIS_LABEL1_A:2,
        AXIS_LABEL2_A:2,
        AXIS_LABEL2_B:2,
        AXIS_LABEL2_C:4,
        AXIS_LABEL2_D:4,
        AXIS_LABEL2_E:-2,
        DATA_DSC: (
            "身体能力や健康維持を重視し、継続的なトレーニングを生活の中心に置く。"
        )
    },

    {
        DATA_GRP: GRP_LIF_INDEX,
        DATA_NAM:"アウトドア派",
        DATA_CAT:"",
        AXIS_LABEL1_X:0,
        AXIS_LABEL1_Y:-1,
        AXIS_LABEL1_Z:-1,
        AXIS_LABEL1_A:-1,
        AXIS_LABEL2_A:2,
        AXIS_LABEL2_B:2,
        AXIS_LABEL2_C:3,
        AXIS_LABEL2_D:4,
        AXIS_LABEL2_E:-2,
        DATA_DSC: (
            "自然との触れ合いや冒険を楽しみ、未知の場所や体験を求める行動派。"
        )
    },

    {
        DATA_GRP: GRP_LIF_INDEX,
        DATA_NAM:"園芸・自然派",
        DATA_CAT:"",
        AXIS_LABEL1_X:2,
        AXIS_LABEL1_Y:-2,
        AXIS_LABEL1_Z:1,
        AXIS_LABEL1_A:1,
        AXIS_LABEL2_A:4,
        AXIS_LABEL2_B:2,
        AXIS_LABEL2_C:3,
        AXIS_LABEL2_D:-1,
        AXIS_LABEL2_E:-3,
        DATA_DSC: (
            "植物や自然と向き合い、ゆったりとした時間を楽しむ穏やかなライフスタイル。"
        )
    },

    {
        DATA_GRP: GRP_LIF_INDEX,
        DATA_NAM:"読書・学習派",
        DATA_CAT:"",
        AXIS_LABEL1_X:0,
        AXIS_LABEL1_Y:-3,
        AXIS_LABEL1_Z:4,
        AXIS_LABEL1_A:0,
        AXIS_LABEL2_A:0,
        AXIS_LABEL2_B:5,
        AXIS_LABEL2_C:5,
        AXIS_LABEL2_D:0,
        AXIS_LABEL2_E:-2,
        DATA_DSC: (
            "知識や教養を深めることに喜びを感じ、一人で思索する時間を大切にする。"
        )
    },

    {
        DATA_GRP: GRP_LIF_INDEX,
        DATA_NAM:"創作・アート派",
        DATA_CAT:"",
        AXIS_LABEL1_X:-2,
        AXIS_LABEL1_Y:-2,
        AXIS_LABEL1_Z:5,
        AXIS_LABEL1_A:-2,
        AXIS_LABEL2_A:0,
        AXIS_LABEL2_B:5,
        AXIS_LABEL2_C:4,
        AXIS_LABEL2_D:2,
        AXIS_LABEL2_E:-1,
        DATA_DSC: (
            "芸術や創作活動を通じて自己表現を行い、新しい価値を生み出すことを楽しむ。"
        )
    },

    {
        DATA_GRP: GRP_LIF_INDEX,
        DATA_NAM:"ゲーム・デジタル派",
        DATA_CAT:"",
        AXIS_LABEL1_X:-1,
        AXIS_LABEL1_Y:-2,
        AXIS_LABEL1_Z:2,
        AXIS_LABEL1_A:-2,
        AXIS_LABEL2_A:0,
        AXIS_LABEL2_B:4,
        AXIS_LABEL2_C:3,
        AXIS_LABEL2_D:2,
        AXIS_LABEL2_E:-1,
        DATA_DSC: (
            "デジタル空間を生活の一部とし、ゲームやオンラインコミュニティを楽しむ。"
        )
    },

    {
        DATA_GRP: GRP_LIF_INDEX,
        DATA_NAM:"旅行・冒険派",
        DATA_CAT:"",
        AXIS_LABEL1_X:-2,
        AXIS_LABEL1_Y:-1,
        AXIS_LABEL1_Z:2,
        AXIS_LABEL1_A:-2,
        AXIS_LABEL2_A:1,
        AXIS_LABEL2_B:4,
        AXIS_LABEL2_C:3,
        AXIS_LABEL2_D:5,
        AXIS_LABEL2_E:-3,
        DATA_DSC: (
            "未知の土地や文化との出会いを求め、新しい経験を積極的に楽しむ。"
        )
    },

    {
        DATA_GRP: GRP_LIF_INDEX,
        DATA_NAM:"瞑想・精神世界派",
        DATA_CAT:"",
        AXIS_LABEL1_X:-1,
        AXIS_LABEL1_Y:-4,
        AXIS_LABEL1_Z:5,
        AXIS_LABEL1_A:-2,
        AXIS_LABEL2_A:3,
        AXIS_LABEL2_B:4,
        AXIS_LABEL2_C:5,
        AXIS_LABEL2_D:-2,
        AXIS_LABEL2_E:-4,
        DATA_DSC: (
            "内省や精神性を重視し、自分自身との対話や心の安定を大切にする。"
        )
    },

    {
        DATA_GRP: GRP_LIF_INDEX,
        DATA_NAM:"家族中心派",
        DATA_CAT:"",
        AXIS_LABEL1_X:2,
        AXIS_LABEL1_Y:4,
        AXIS_LABEL1_Z:-2,
        AXIS_LABEL1_A:2,
        AXIS_LABEL2_A:5,
        AXIS_LABEL2_B:0,
        AXIS_LABEL2_C:2,
        AXIS_LABEL2_D:-1,
        AXIS_LABEL2_E:4,
        DATA_DSC: (
            "家族との時間や身近な人との絆を最優先に考えるライフスタイル。"
        )
    },

    {
        DATA_GRP: GRP_LIF_INDEX,
        DATA_NAM:"仕事中心派",
        DATA_CAT:"",
        AXIS_LABEL1_X:2,
        AXIS_LABEL1_Y:2,
        AXIS_LABEL1_Z:1,
        AXIS_LABEL1_A:3,
        AXIS_LABEL2_A:2,
        AXIS_LABEL2_B:3,
        AXIS_LABEL2_C:4,
        AXIS_LABEL2_D:5,
        AXIS_LABEL2_E:1,
        DATA_DSC: (
            "仕事や社会的成果を自己実現の中心に据え、高い目標へ挑戦し続ける。"
        )
    },

    {
        DATA_GRP: GRP_LIF_INDEX,
        DATA_NAM:"ミニマリスト",
        DATA_CAT:"",
        AXIS_LABEL1_X:0,
        AXIS_LABEL1_Y:-3,
        AXIS_LABEL1_Z:3,
        AXIS_LABEL1_A:-1,
        AXIS_LABEL2_A:1,
        AXIS_LABEL2_B:3,
        AXIS_LABEL2_C:4,
        AXIS_LABEL2_D:1,
        AXIS_LABEL2_E:-3,
        DATA_DSC: (
            "所有物や人間関係を必要最小限に整理し、本当に大切なものに集中する。"
        )
    },


    {
        DATA_GRP: GRP_HUM_INDEX,
        DATA_NAM:"孤高の天才専門医",
        DATA_CAT:"",
        AXIS_LABEL1_X:-2,
        AXIS_LABEL1_Y:-5,
        AXIS_LABEL1_Z:3,
        AXIS_LABEL1_A:-4,
        AXIS_LABEL2_A:-3,
        AXIS_LABEL2_B:5,
        AXIS_LABEL2_C:5,
        AXIS_LABEL2_D:1,
        AXIS_LABEL2_E:-2,
        DATA_DSC: (
            "専門能力を最優先し、組織や慣習より合理性と結果を重視するスペシャリスト。"
        )
    },
    {
        DATA_GRP: GRP_HUM_INDEX,
        DATA_NAM:"食べ歩き営業マン",
        DATA_CAT:"",
        AXIS_LABEL1_X:0,
        AXIS_LABEL1_Y:2,
        AXIS_LABEL1_Z:-2,
        AXIS_LABEL1_A:-3,
        AXIS_LABEL2_A:2,
        AXIS_LABEL2_B:3,
        AXIS_LABEL2_C:2,
        AXIS_LABEL2_D:-2,
        AXIS_LABEL2_E:0,
        DATA_DSC: (
            "現場を歩き、人との距離感を保ちながら自分のペースで行動する実務派。\n"
            "食べることが生きがい。"
        )
    },
    {
        DATA_GRP: GRP_HUM_INDEX,
        DATA_NAM:"理想派グルメ評論家",
        DATA_CAT:"",
        AXIS_LABEL1_X:-1,
        AXIS_LABEL1_Y:-2,
        AXIS_LABEL1_Z:4,
        AXIS_LABEL1_A:-2,
        AXIS_LABEL2_A:-2,
        AXIS_LABEL2_B:5,
        AXIS_LABEL2_C:5,
        AXIS_LABEL2_D:1,
        AXIS_LABEL2_E:-1,
        DATA_DSC: (
            "理想と哲学を重視し、本質を追求する評論家タイプ。\n"
            "自分の満足できる味を求め料亭を主催。"
        )
    },
    {
        DATA_GRP: GRP_HUM_INDEX,
        DATA_NAM:"極限の食いしん坊",
        DATA_CAT:"",
        AXIS_LABEL1_X:3,
        AXIS_LABEL1_Y:-2,
        AXIS_LABEL1_Z:5,
        AXIS_LABEL1_A:2,
        AXIS_LABEL2_A:-2,
        AXIS_LABEL2_B:5,
        AXIS_LABEL2_C:4,
        AXIS_LABEL2_D:3,
        AXIS_LABEL2_E:-2,
        DATA_DSC: (
            "圧倒的な審美眼を持ち、自らの理想を妥協なく追求する芸術家肌。\n"
            "但し本業の仕事はグータラ。"
        )
    },
    {
        DATA_GRP: GRP_HUM_INDEX,
        DATA_NAM:"放浪の人情家",
        DATA_CAT:"",
        AXIS_LABEL1_X:-2,
        AXIS_LABEL1_Y:4,
        AXIS_LABEL1_Z:1,
        AXIS_LABEL1_A:-5,
        AXIS_LABEL2_A:3,
        AXIS_LABEL2_B:2,
        AXIS_LABEL2_C:2,
        AXIS_LABEL2_D:0,
        AXIS_LABEL2_E:4,
        DATA_DSC: (
            "組織には属さず、人との縁を大切にしながら自由に生きる情の厚い風来坊。"
        )
    },
    {
        DATA_GRP: GRP_HUM_INDEX,
        DATA_NAM:"組織内改革者",
        DATA_CAT:"",
        AXIS_LABEL1_X:2,
        AXIS_LABEL1_Y:3,
        AXIS_LABEL1_Z:2,
        AXIS_LABEL1_A:3,
        AXIS_LABEL2_A:2,
        AXIS_LABEL2_B:4,
        AXIS_LABEL2_C:4,
        AXIS_LABEL2_D:5,
        AXIS_LABEL2_E:3,
        DATA_DSC: (
            "組織を守りながらも、不正や矛盾には真正面から立ち向かう企業社員"
        )
    },
    {
        DATA_GRP: GRP_HUM_INDEX,
        DATA_NAM:"正義感の強い船乗り",
        DATA_CAT:"",
        AXIS_LABEL1_X:1,
        AXIS_LABEL1_Y:3,
        AXIS_LABEL1_Z:-2,
        AXIS_LABEL1_A:1,
        AXIS_LABEL2_A:4,
        AXIS_LABEL2_B:-1,
        AXIS_LABEL2_C:2,
        AXIS_LABEL2_D:5,
        AXIS_LABEL2_E:2,
        DATA_DSC: (
            "困っている相手を放っておけず、強い信念で行動するヒーロー型。"
        )
    },
    {
        DATA_GRP: GRP_HUM_INDEX,
        DATA_NAM:"自由を愛する放浪詩人",
        DATA_CAT:"",
        AXIS_LABEL1_X:-3,
        AXIS_LABEL1_Y:-4,
        AXIS_LABEL1_Z:5,
        AXIS_LABEL1_A:-5,
        AXIS_LABEL2_A:-2,
        AXIS_LABEL2_B:5,
        AXIS_LABEL2_C:3,
        AXIS_LABEL2_D:0,
        AXIS_LABEL2_E:-3,
        DATA_DSC: (
            "組織や権威に縛られず、自然や芸術を愛し、自分らしい生き方を貫く自由人。\n"
            "ごくまれに限界を超えると周りも目を見張る行動を起こす。"
        )
    },

    ## 成長・変化前後比較

    {
        # おしん
        DATA_GRP: GRP_HUM_INDEX,
        DATA_NAM:"🌾逆境克服型努力家（若年期）",
        DATA_CAT:"",
        AXIS_LABEL1_X:3,
        AXIS_LABEL1_Y:3,
        AXIS_LABEL1_Z:-2,
        AXIS_LABEL1_A:2,
        AXIS_LABEL2_A:4,
        AXIS_LABEL2_B:-2,
        AXIS_LABEL2_C:2,
        AXIS_LABEL2_D:4,
        AXIS_LABEL2_E:3,
        DATA_DSC: (
            "厳しい環境の中で忍耐と努力を積み重ね、周囲との協調を保ちながら逆境を乗り越えようとするタイプ。"
        )
    },
    {
        # おしん
        DATA_GRP: GRP_HUM_INDEX,
        DATA_NAM:"🌾共生型経営者（成熟期）",
        DATA_CAT:"",
        AXIS_LABEL1_X:3,
        AXIS_LABEL1_Y:2,
        AXIS_LABEL1_Z:1,
        AXIS_LABEL1_A:4,
        AXIS_LABEL2_A:5,
        AXIS_LABEL2_B:2,
        AXIS_LABEL2_C:3,
        AXIS_LABEL2_D:3,
        AXIS_LABEL2_E:2,
        DATA_DSC: (
            "豊富な経験を基盤に組織を率い、現場感覚と経営感覚を兼ね備えた実務型リーダー。"
        )
    },

    {
        # ダメオヤジ
        DATA_GRP: GRP_HUM_INDEX,
        DATA_NAM:"👔忍耐型家庭人（初期）",
        DATA_CAT:"",
        AXIS_LABEL1_X:-3,
        AXIS_LABEL1_Y:4,
        AXIS_LABEL1_Z:-3,
        AXIS_LABEL1_A:0,
        AXIS_LABEL2_A:4,
        AXIS_LABEL2_B:-2,
        AXIS_LABEL2_C:-3,
        AXIS_LABEL2_D:-4,
        AXIS_LABEL2_E:4,
        DATA_DSC: (
            "周囲との衝突を極力避け、自分の主張よりもその場の空気を優先する受動型タイプ\n"
            "自己評価が低く、困難な状況でも耐え続ける傾向がある。\n"
            "大切にしているもの:家庭の平穏\n"
            "苦手なもの:対立・自己主張を迫られる場面"
        )
    },

    {
        # ダメオヤジ
        DATA_GRP: GRP_HUM_INDEX,
        DATA_NAM:"👔成熟型家庭人（後期）",
        DATA_CAT:"",
        AXIS_LABEL1_X:0,
        AXIS_LABEL1_Y:1,
        AXIS_LABEL1_Z:1,
        AXIS_LABEL1_A:1,
        AXIS_LABEL2_A:3,
        AXIS_LABEL2_B:1,
        AXIS_LABEL2_C:2,
        AXIS_LABEL2_D:2,
        AXIS_LABEL2_E:1,
        DATA_DSC: (
            "経験を積むことで自信を取り戻し、必要な場面では自分の考えを穏やかに伝えられる成熟型タイプ。\n"
            "協調性を保ちながらも、自分の軸を持つようになった。\n"
            "大切にしているもの:家族と自尊心の両立\n"
            "苦手なもの:理不尽な支配"
        )
    },
    {
        # クリスマスキャロル
        DATA_GRP: GRP_HUM_INDEX,
        DATA_NAM:"💰利益最優先経営者（クリスマス前）",
        DATA_CAT:"",
        AXIS_LABEL1_X:4,
        AXIS_LABEL1_Y:-5,
        AXIS_LABEL1_Z:0,
        AXIS_LABEL1_A:4,
        AXIS_LABEL2_A:-5,
        AXIS_LABEL2_B:0,
        AXIS_LABEL2_C:2,
        AXIS_LABEL2_D:3,
        AXIS_LABEL2_E:3,
        DATA_DSC: (
            "利益と自己防衛を最優先し、人との関わりを極力避ける孤立型タイプ。\n"
            "効率と所有を重視する一方、他者への共感は乏しい。\n"
            "大切にしているもの:財産と自己防衛\n"
            "苦手なもの:他人への依存"
        )
    },

    {
        # クリスマスキャロル
        DATA_GRP: GRP_HUM_INDEX,
        DATA_NAM:"💰慈善・共生型経営者（クリスマス後）",
        DATA_CAT:"",
        AXIS_LABEL1_X:1,
        AXIS_LABEL1_Y:3,
        AXIS_LABEL1_Z:1,
        AXIS_LABEL1_A:1,
        AXIS_LABEL2_A:5,
        AXIS_LABEL2_B:2,
        AXIS_LABEL2_C:3,
        AXIS_LABEL2_D:2,
        AXIS_LABEL2_E:-1,
        DATA_DSC: (
            "人生観が大きく変わり、人とのつながりや思いやりに価値を見いだすようになった共生型タイプ。\n"
            "豊かさを分かち合う喜びを知る。\n"
            "大切にしているもの:人との絆\n"
            "苦手なもの:孤独と利己主義"
        )
    },

    {
        # アイアンマン
        DATA_GRP: GRP_HUM_INDEX,
        DATA_NAM:"⚙️孤高のイノベーター（初期）",
        DATA_CAT:"",
        AXIS_LABEL1_X:-2,
        AXIS_LABEL1_Y:-3,
        AXIS_LABEL1_Z:3,
        AXIS_LABEL1_A:-2,
        AXIS_LABEL2_A:-2,
        AXIS_LABEL2_B:5,
        AXIS_LABEL2_C:4,
        AXIS_LABEL2_D:5,
        AXIS_LABEL2_E:-2,
        DATA_DSC: (
            "卓越した才能と創造性を持ち、自分の能力への強い自信を原動力に行動する革新型タイプ。\n"
            "組織よりも自らの判断を優先する。\n"
            "大切にしているもの:自由な創造\n"
            "苦手なもの:束縛と無能"
        )
    },

    {
        # アイアンマン
        DATA_GRP: GRP_HUM_INDEX,
        DATA_NAM:"⚙️社会を支えるイノベータ（後期）",
        DATA_CAT:"",
        AXIS_LABEL1_X:0,
        AXIS_LABEL1_Y:1,
        AXIS_LABEL1_Z:4,
        AXIS_LABEL1_A:0,
        AXIS_LABEL2_A:3,
        AXIS_LABEL2_B:5,
        AXIS_LABEL2_C:4,
        AXIS_LABEL2_D:5,
        AXIS_LABEL2_E:1,
        DATA_DSC: (
            "高い創造力を維持しながら、その才能を仲間や社会のために生かそうとする成熟型タイプ。\n"
            "責任感と自己犠牲の精神が加わる。\n"
            "大切にしているもの:未来への責任\n"
            "苦手なもの:仲間を失うこと"
        )
    },

    # --- テスト用分析対象者（自分など） ---
    {
        DATA_GRP: GRP_TST_INDEX,
        DATA_NAM: "蛮苦恣意（現在）",
        DATA_CAT: "厄介者・要注意",
        AXIS_LABEL1_X: -2,
        AXIS_LABEL1_Y: -4, 
        AXIS_LABEL1_Z: -3,
        AXIS_LABEL1_A: 3, 
        AXIS_LABEL2_A: -3,    
        AXIS_LABEL2_B: -3,     
        AXIS_LABEL2_C: -3,     
        AXIS_LABEL2_D: -3,    
        AXIS_LABEL2_E: -4,   
        DATA_DSC: ( 
            "作家や芸術家になれず落書きで暇つぶししている、もとITエンジニア。\n"
            "テクノストレスになりかけたがアウトドアレジャーで回避。以降、晴耕兼落書き、雨落書き。\n"
            "X軸：伝統志向だが、料理は新作も好き。落語は古典の方がいい。ロックも最近は苦手。K-Popにも興味なし。\n"
            "Y軸：基本ゴーイングマイウェイだが、所帯をもってから多少連れ合いのことも意識。\n"
            "Z軸：口下手だが、話しだすと長話。\n"
            "α軸：どちらかといえば食い気。自炊好き。\n"
            "A軸：わがままに育ってきたため、場の雰囲気を読むことが苦手。\n"
            "B軸：理系なのでやや事実志向寄りかも。\n"
            "C軸：かなり頑固だが、相手次第で妥協することもある。\n"
            "D軸：相手の社会的立場などの権威には無頓着。（権威を笠に着る人を嫌うこともあるので極値ではない。）\n"
            "E軸：結構ひきずられる。根に持つ。\n"
            "大切にしているもの:（後日記載）\n"
            "苦手なもの:（後日記載）"
            ),
    },

    {
        DATA_GRP: GRP_TST_INDEX,
        DATA_NAM: "蛮苦恣意（若年期）",
        DATA_CAT: "厄介者・要注意",
        AXIS_LABEL1_X: 3,
        AXIS_LABEL1_Y: -5,
        AXIS_LABEL1_Z: 0,
        AXIS_LABEL1_A: -2, 
        AXIS_LABEL2_A: -3,   
        AXIS_LABEL2_B: -3,    
        AXIS_LABEL2_C: -4,      
        AXIS_LABEL2_D: -3,     
        AXIS_LABEL2_E: -4,   
        DATA_DSC: ( 
            "サンダーバードを見て育ち、秘密基地ごっこ遊びをしながら技術屋を夢見る田舎者。オラ、東京さ行ぐだ。\n"
            "X軸：ほとんど外食しなかったため、目新しいものに憧れ大。叙情派フォークもいいが、ヒュージョン系音楽も好き。\n"
            "Y軸：我儘。ゴーイングマイウェイ。\n"
            "Z軸：具体、抽象傾向はまだ不明確か？\n"
            "α軸：色気づいてはいるが晩生。\n"
            "A軸：わがままに育ってきたため、場の雰囲気を読むことが苦手。\n"
            "B軸：理系なのでやや事実志向寄りかも。\n"
            "C軸：わがままなのでかなり頑固。\n"
            "D軸：相手の社会的立場などの権威に、一応気づいてはいるが、ほとんど重視していない。\n"
            "E軸：結構ひきずられる。根に持つ。\n"
            "大切にしているもの:（後日記載）\n"
            "苦手なもの:（後日記載）"
            ),
    },

    {
        DATA_GRP: GRP_TST_INDEX,
        DATA_NAM: "テスト１",
        DATA_CAT: "",
        AXIS_LABEL1_X: -4,
        AXIS_LABEL1_Y: 4, 
        AXIS_LABEL1_Z: -4,
        AXIS_LABEL1_A: -4, 
        AXIS_LABEL2_A: 3,     
        AXIS_LABEL2_B: 4,  
        AXIS_LABEL2_C: -4,     
        AXIS_LABEL2_D: -3,
        AXIS_LABEL2_E: -4,  
        DATA_DSC: ( 
            "新しいことを覚える気力が薄れ、対人関係も少なく、家に閉じこもり気味。\n"
            "X軸：伝統志向。音楽はクラシックに興味はないが、幼少期、若年時代に聞いたものが今も好き。新しいものにはあまり興味がない。近代的な街も苦手。\n"
            "Y軸：かなり対人依存。\n"
            "Z軸：長話が好き。数値化などは苦手。\n"
            "α軸：地味なものより派手なものが好き。食事は美味しければうれしいが、基本、食べれればそれでいい。自炊は苦手。\n"
            "A軸：場の雰囲気には気づくほう。価値観の異なる人ともそれなりの会話は続けられる。\n"
            "B軸：文系､主観的判断が多い｡\n"
            "C軸：かなり頑固。\n"
            "D軸：相手の社会的立場などの権威には無頓着。（権威を笠に着る人を嫌うこともあるので極値ではない。）\n"
            "E軸：結構ひきずられる。根に持つ。\n"
            "大切にしているもの:（後日記載）\n"
            "苦手なもの:（後日記載）"
            ),
    },

    {
        DATA_GRP: GRP_TST_INDEX,
        DATA_NAM: "テスト２",
        DATA_CAT: "",
        AXIS_LABEL1_X: 0, # 仮
        AXIS_LABEL1_Y: -4, 
        AXIS_LABEL1_Z: -4,
        AXIS_LABEL1_A: 3, 
        AXIS_LABEL2_A: 3,     
        AXIS_LABEL2_B: 4,  
        AXIS_LABEL2_C: -4,     
        AXIS_LABEL2_D: -3,
        AXIS_LABEL2_E: -4,  
        DATA_DSC: ( 
            "甘やかされて育った（？）趣味人。対人関係は限定的。\n"
            "X軸：どちらかといえば伝統志向。音楽はクラシックがメイン。演歌、ロックは嫌い。新しいものには結構興味がある。街中は苦手。\n"
            "Y軸：殆ど依存しない。もしスキーをするならノルディック。\n"
            "Z軸：長話が好き。時としてくどい。\n"
            "α軸：芸術、食べ物、酒にはそうとう拘るが、贅沢はできないので、普段は我慢。ここ一番のときには遠慮しない。自炊もする。\n"
            "A軸：場の雰囲気にはそれなりに気づく。ただし、合わない人とはすぐ距離をおく。\n"
            "B軸：文系､主観的判断が多い｡\n"
            "C軸：かなり頑固。\n"
            "D軸：相手の社会的立場などの権威には無頓着。（権威を笠に着る人を嫌うこともあるので極値ではない。）\n"
            "E軸：結構ひきずられる。\n"
            "大切にしているもの:（後日記載）\n"
            "苦手なもの:（後日記載）"
        ),
    },

]