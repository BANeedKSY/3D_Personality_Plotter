import math
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from three_d_plot_constants import (
    AXIS_LABEL1_X, AXIS_LABEL1_Y, AXIS_LABEL1_Z, AXIS_LABEL1_A,
    AXIS_LABEL2_A, AXIS_LABEL2_B, AXIS_LABEL2_C, AXIS_LABEL2_D, AXIS_LABEL2_E,
    AXIS_NAME1_X, AXIS_NAME1_Y, AXIS_NAME1_Z, AXIS_NAME1_A,
    AXIS_NAME2_A, AXIS_NAME2_B, AXIS_NAME2_C, AXIS_NAME2_D, AXIS_NAME2_E,
    AXIS_PREFIX, AXIS_SUFFIX,
    DATA_CAT, DATA_DSC, DATA_GRP, DATA_NAM, DATA_VAL,
    DEFALUT_DATA_VERSION, DEFAULT_PERSONAS,
    GRP_CST_INDEX, GRP_HOVER, GRP_INIT_DISP, GRP_NAME_CST, GRP_NAME_DEF, GRP_NAMES,
    DEFAULT_PERSONAS,STEP_MAX, STEP_MIN, THRESHOLD )

# "ToDo: "

##############################################################################################################################
# 定数定義
##############################################################################################################################

APP_VER = "0.26d"  # アプリケーションバージョン
# セッション管理用
SESSION_DELETE_CUSTOM = "custom_personas"  ## 設定されていたら、デフォルト内データ内のサンプルカスタム削除


# データ範囲、デフォルトペルソナ・データベースの定義 inport

default_personas = DEFAULT_PERSONAS

# デフォルトデータフレーム化
df_default = pd.DataFrame(default_personas)
# df_default["タイプ"] = "デフォルト"

# データ検索関数

# 2. 条件に合う要素が含まれているか判定する関数
def contains_name(data_list, key_name, target_name):
    # any() は1つでも条件に合うものがあれば True を返します（見つかった時点で処理を打ち切るため効率的）
    return any(item.get(key_name) == target_name for item in data_list)


# 個性傾向判定関数
def check_personality_note(threshold, num_x, num_y, num_z, num_alfa, num_a, num_b, num_c, num_d, num_e,):
    return_msg = ""

    # 原則として、人格評価は行わないこと。

    # ===== 例外： ==================================
    #
    # 特異な領域（局地コーナー領域）に位置する場合
    # Y軸（動機）とZ軸（立脚点）の歪みだけを検知する
    # Z:-5$（生存実利） * Y:+5$（外部操作） = 他者ハック・搾取セクター（我儘）
    # Z:+5$（極限の抽象） * Y:-5$（自己完結・遮断） = 原理主義セクター（妄信、自己陶酔）
    # X軸は判定から除外。(保守・革新とは関係ない。要注意傾向の人物は左右両方に存在する。)
    # if (abs(row["Y軸"]) > 4.0 and abs(row["Z軸"]) > 4.0) or (abs(target_data["Y軸"]) > 4.0 and abs(target_data["Z軸"]) > 4.0):
    #   alert_logs.append("⚠️ **【空間配置注意】** 固有の強い特性（動機と立脚点の組み合わせ）により、一般的な社会（多数派の環境）や、多くの人との間で意見・利害の競合が予想される座標領域です。お互いの立ち位置を慎重にキャリブレーション（調整）してください。")
    if (num_y >= STEP_MAX and num_z <= STEP_MIN): 
        return_msg += "【Y+Z-】⚠️固有の強い特性（動機と立脚点の組み合わせ）により、一般的な社会（多数派の環境）や、多くの人との間で意見・利害の競合が予想されます。\n\n"
        
    if (num_y <= STEP_MIN and num_z >= STEP_MAX): 
        return_msg += "【Y-Z+】⚠️固有の強い特性（動機と立脚点の組み合わせ）により、一般的な社会（多数派の環境）や、多くの人との間で意見・利害の競合が予想されます。\n\n"


    # ===== 一般評価 ==================================
    #
    # ① 利用・支配型（相互利用リスク）
    #               Y＋（他人依存）    Z－（具体）
    # 起きやすいこと： 他人を問題解決手段として見やすい、人間関係が損得勘定になりやすい、短期利益を優先しやすい　－＞依存関係になりやすい
    # 相手側の感じ方： 利用されている、振り回される、境界線を越えられる
    # 距離を置く理由： 利害が一致している間は良いが、一致しなくなると摩擦が急激に増える。
    # リスク補足：　　　家族思いな人もいれば、利用的な人もいる。他責、攻撃性、嘘　が加わるとリスク大
    if (num_y >= threshold and num_z <= -threshold):
        return_msg += "【Y+Z-】依存関係になりやすく、短期利益優先の傾向があります。利害が一致している間は良いのですが、一致しなくなると摩擦が急激に増えることがあります。"
        return_msg += "境界線を越えたり、責任転嫁が見られる場合、注意が必要です。\n\n"


    # ③ 理念優先型
    # X＋（革新）     Y－（自己完結）   Z＋（抽象）
    # 起きやすいこと：理想社会を追求する、手段を正当化しやすい、現実より理念を優先する。極端になると カリスマ化、独善化、イデオロギー化
    # 距離を置く理由：理念が一致しない相手とは対立しやすい。
    # リスク補足：　　「一人で考える」だけなら、実害無し。他責、攻撃性、嘘　が加わるとリスク大
    if (num_x >= threshold and num_y <= -threshold and num_z >= threshold):
        return_msg += "【X-Y+Z+】自身の信念を重視するあまり手段を正当化し、現実よりも理念を優先するあまり、カリスマ化、独善化、イデオロギー化と見做される恐れがあります。"
        return_msg += "他責、攻撃性、が見られる場合、注意が必要です。\n\n"

    # ② 独善型
    #               Y－（自己完結）    Z＋（抽象）
    # 起きやすいこと: 自分の理論を重視する、他人の助言が入りにくい、現実とのズレが大きくなりやすい　
    # 相手側の感じ方：話が通じない、自分の世界に閉じこもる
    # 距離を置く理由：悪意はなくても意思疎通が成立しなくなる。
    # リスク補足：　　「一人で考える」だけなら、実害無し。他責、攻撃性、嘘　が加わるとリスク大
    elif (num_y <= -threshold and num_z >= threshold):
        return_msg += "【Y-Z+】自身の信念を重視するあまり現実とのズレが大きいことがあります。悪意はなくても意思疎通が成立しなくなる恐れがあります。\n\n"
        return_msg += "他責、攻撃性、が見られる場合、注意が必要です。\n\n"
        

    # ④ 現状依存型
    # X－（保守）   Y＋（他人依存）
    # 起きやすいこと：自分から改善しない、周囲に依存しやすい、「誰かがやってくれる」
    # 距離を置く理由：責任分担でストレスになりやすい。
    if (num_x <= -threshold and num_y >= threshold):
        return_msg += "【X-Y+】自身で改善しようとせず周囲に任せ（誰かがやってくれる）の傾向があります。責任分担でストレスとなる可能性があります。\n\n"


    # ⑥ 反権威型
    # A－
    # C－
    # D－（上下に無頓着）
    # 起きやすいこと：指示を嫌う、組織との相性が悪い、自己判断を優先
    # 距離を置く理由：共同作業でルールが共有しにくい。
    if (num_a <= -threshold and num_c <= -threshold and num_d <= threshold):
        return_msg += "【A-C-D-】指示を嫌う、組織との相性が悪い、自己判断を優先する傾向があります。共同作業でルールが共有しにくい可能性があります。\n\n"

    # ⑤ 配慮不足型
    # A－（無頓着）
    # C－（頑固）
    # 起きやすいこと：自分基準で判断する、他者感情を軽視しやすい、妥協しにくい
    # 距離を置く理由：小さな衝突が積み重なりやすい。
    elif (num_a <= -threshold and num_c <= -threshold):
        return_msg += "【A-C-】自分基準で判断する、他者感情を軽視しやすい、妥協しにくい傾向があります。小さな衝突が積み重なりやすい可能性があります。\n\n"

    # ⑧ 権威依存型
    # A＋
    # C＋
    # D＋（権威に敏感）
    # 起きやすいこと：権威を信頼する、自分で検証しない、所属集団へ同調
    # 距離を置く理由：意見が食い違うと対話が難しくなる。
    if (num_a >= threshold and num_c >= threshold and num_d >= threshold):
        return_msg += "【A+C+D+】権威を信頼する、自分で検証しない、所属集団へ同調する傾向があります。意見が食い違うと対話が難しくなる可能性があります。\n\n"

    # ⑨ 過去拘束型
    # A＋
    # C＋
    # E－（過去重視）
    # 起きやすいこと：過去の失敗を忘れにくい。傷ついた経験を保持しやすい
    # 距離を置く理由：古い対立が解消されにくい。
    elif (num_a >= threshold and num_c >= threshold and num_e <= -threshold):
        return_msg += "【A+C+E-】過去の失敗を忘れにくい。傷ついた経験を保持しやすい傾向があります。古い対立が解消されにくい可能性があります。\n\n"

    # ⑦ 承認依存型
    # A＋（神経過敏）
    # C＋（他人任せ）
    # 起きやすいこと：評価を気にする、自分で決められない、判断を委ねる
    # 距#離を置く理由：依存関係になりやすい。
    elif (num_a >= threshold and num_c >= threshold):
        return_msg += "【A+C+】評価を気にする、自分で決められない、判断を委ねる傾向があります。依存関係になりやすい可能性があります。\n\n"

    # ⑩ 孤立固定型
    # Y－
    # E－
    # 起きやすいこと：過去経験に閉じこもる 人との交流を避ける 修正が起きにくい
    # 距離を置く理由：歩み寄りが難しい。
    if (num_y <= -threshold and num_e <= -threshold):
        return_msg += "【Y-E-】過去経験に閉じこもる、人との交流を避ける、修正が起きにくい傾向があります。歩み寄りが難しい可能性があります。\n\n"


    # ⑪ 権威追従型
    # Y＋
    # D＋
    # 起きやすいこと：上位者の判断を優先 多数派へ流れやすい
    # 距離を置く理由：対等な議論になりにくい。
    if (num_y >= threshold and num_d >= threshold):
        return_msg += "【Y+D+】上位者の判断を優先 多数派へ流れやすい傾向があります。対等な議論になりにくい可能性があります。\n\n"


    # ⑫ 革命実行型
    # X＋ × Z－
    # 革新性は高いが、具体的成果を急ぐため、強引 短期成果重視 になりやすい。
    if (num_x >= threshold and num_z <= -threshold):
        return_msg += "【X+Z-】革新性は高いが、具体的成果を急ぐため、強引 短期成果重視 になりやすい傾向があります。\n\n"
    

    # ⑬ 保守理念型
    # X－ × Z＋
    # 理念として伝統を守ろうとする。相手によっては「変化を拒絶している」と受け取られる。
    if (num_x <= -threshold and num_z >= threshold):
        return_msg += "【X-Z+】保守的な考えを持つ傾向があります。相手によっては「変化を拒絶している」と受け取られる可能性があります。\n\n"


    # ⑭ 孤高型
    # Y－ × C－
    # 自分で決めたい。他人から指示されることを嫌う。協働では摩擦になりやすい。
    if (num_y <= -threshold and num_c <= -threshold):
        return_msg += "【Y-C-】自分で決めたい、他人から指示されることを嫌う傾向があります。協働では摩擦になりやすい可能性があります。\n\n"

    # ⑮ 空気優先型
    # Y＋ × A＋
    # 周囲に合わせる能力は高いが、自分の意思表示が弱くなりやすい。
    if (num_y >= threshold and num_a >= threshold):
        return_msg += "【Y+A+】周囲に合わせる能力は高いが、自分の意思表示が弱くなりやすい傾向があります。\n\n"

    #--------------------------
    # 介護向け
    #--------------------------

    # Y－（自己完結）が高かった人なら、
    # 「できることは本人に任せる方が安心しやすいかもしれません。」
    if (num_y <= -threshold ):
        return_msg += "【Y-】🧑‍🦽介護関係の場合：できることは本人に任せる方が安心しやすいかもしれません。\n\n"

    # Y＋（他人依存）が高かった人なら、
    # 「一緒に行うことが安心につながるかもしれません。」
    if (num_y >= threshold ):
        return_msg += "【Y+】🧑‍🦽介護関係の場合：一緒に行うことが安心につながるかもしれません。\n\n"

    # A＋（神経過敏）が高かった人なら、
    # 「急な環境変化を避け、落ち着いた説明を心がける。」
    if (num_a >= threshold ):
        return_msg += "【A+】🧑‍🦽介護関係の場合：急な環境変化を避け、落ち着いた説明を心がける方が良いでしょう。\n\n"

    # A－（無頓着）が高かった人なら、
    # 「細かな説明よりも、自然な流れで支援した方が受け入れられやすいことがあります。」
    if (num_a <= -threshold ):
        return_msg += "【A-】🧑‍🦽介護関係の場合：細かな説明よりも、自然な流れで支援した方が受け入れられやすいことがあります。\n\n"

    return return_msg


# 性格色生成関数
def generate_personality_color(step_min, step_max, num_x, num_y, num_z):  
    # NaNや欠損値があれば安全なデフォルト値にフォールバック
    # ToDo: 将来はDF生成時に事前欠落チェック追加
    
    if any(v is None or (isinstance(v, float) and math.isnan(v)) for v in (num_x, num_y, num_z)):
        return "rgb(128, 128, 128)"  # グレー：座標未定義を示す
    
    # X軸、Y軸、Z軸の値を0〜1の範囲に正規化してRGB値に変換

    rate_x = (max(STEP_MAX, STEP_MIN) - num_x) / abs(STEP_MAX - STEP_MIN)  # -5 → 1.0, -4 → 0.1, ..., 
    rate_y = (max(STEP_MAX, STEP_MIN) - num_y) / abs(STEP_MAX - STEP_MIN)  # -5 → 1.0, -4 → 0.1, ..., 
    rate_z = (max(STEP_MAX, STEP_MIN) - num_z) / abs(STEP_MAX - STEP_MIN)  # -5 → 1.0, -4 → 0.1, ..., 
    
    if rate_x > 1: 
        rate_x = 1
    elif rate_x < 0:
        rate_x = 0
        
    if rate_y > 1: 
        rate_y = 1
    elif rate_y < 0:
        rate_y = 0
    
    if rate_z > 1: 
        rate_z = 1
    elif rate_z < 0:
        rate_z = 0  
    
    color = f"rgb({int(255 * rate_x)}, {int(255 * rate_y)}, {int(255 * rate_z)})"
    
    return color

# 情緒色生成関数
def generate_emotionality_color(step_min, step_max, num_a):  
    # NaNや欠損値があれば安全なデフォルト値にフォールバック
    # ToDo: 将来はDF生成時に事前欠落チェック追加
    
    if num_a is None:
        return "rgb(128, 128, 128)"  # グレー：座標未定義を示す
    
    # a軸の値を0〜1の範囲に正規化してRGB値に変換

    rate_a = (max(STEP_MAX, STEP_MIN) - num_a) / abs(STEP_MAX - STEP_MIN)  # -5 → 1.0, -4 → 0.1, ..., 
    
    if rate_a > 1.0: 
        rate_a = 1.0
    elif rate_a < 0.0:
        rate_a = 0.0

    # 緑(0,128,0) ⇔ ピンク(255,128,128)    
    color = f"rgb({int(255 * (1.0 - rate_a))}, {int(128.0)}, {int(128 * (1.0 - rate_a))})"

    return color


# ==========================================",
# 2. セッション状態（ユーザー定義データ）の管理
# ==========================================
if "custom_personas" not in st.session_state:
    st.session_state.custom_personas = []


####################################################################################################################
#  見出し、説明エリア　表示処理
####################################################################################################################
# ┏━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ 　  ┃　💡見出し、説明エリア💡　　　　　　 ┃
# ┃　　 ┣━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┫
# ┃ 　  ┃　　　　　　３Ｄプロット 　┃ スケール ┃
# ┃　設 ┃　　　　　　　　エリア　　 ┃　エリア　┃
# ┃　定 ┣━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━┫
# ┃　　 ┃　相性診断エリア　　　　　　　　　　　┃
# ┗━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

# ==========================================
# 1. アプリケーション初期設定
# ==========================================
st.set_page_config(layout="wide", page_title="3D性格プロッター", page_icon="🌐")

st.title("3D性格プロッター（思考傾向・相性推定システム） Ver:" + APP_VER + " / Data:" + DEFALUT_DATA_VERSION)

# ここでの言語指定は無意味。　StreamLit側が、<html lang="en">と書いている。
## JavaScriptで html lang を日本語に変更（ブラウザの翻訳提案を抑制）
#st.markdown("""
#<script>
#document.documentElement.lang = 'ja';
#</script>
#""", unsafe_allow_html=True)

# 💡【翻訳ポップアップ防止ハック】 ### 結果的には無意味?
#    components.html(
#        """
#        <script>
#            try {
#                // 1. 親ドキュメントのlang属性をjaに変更（念のため）
#                window.parent.document.documentElement.lang = 'ja';
#                
#                // 2. Google翻訳を強制的に無効化するメタタグを作成してheadに追加
#                var meta = window.parent.document.createElement('meta');
#                meta.name = 'google';
#                meta.content = 'notranslate';
#                window.parent.document.getElementsByTagName('head')[0].appendChild(meta);
#            } catch (e) {
#                console.log("iframeのセキュリティ制限によりブロックされました");
#            }
#        </script>
#        """,
#        width=0,
#        height=0
#    )

val_html = "<div><p>"
val_html +=  "【目的】人間の思考傾向を「X・Y・Zの3つの次元」等で可視化し、ペルソナ間の相性やコミュニケーションエラーを予測・推定するツールです。</br>"
val_html +=  "【注意】思考傾向は気分や体調,時期などで大きく変化します。またその変化傾向も人によって異なりますが、現版ではそこまでは考慮していません。</br>"
val_html +=  "【重要】<stong><A href='https://www.openrail.org/' target='_blank'>OpenRAIL（Open Responsible AI License）</A></stong>として公開しています。</br>"
val_html +=  "<ul style='margin-left: 4em;'>"
val_html +=  "<li><strong><font color='red'>他者の誹謗・中傷用などの悪用利用は厳格にお断りします。</font></strong></li>"
val_html +=  "<li><strong>本版は、まだ開発途中で、十分な動作検証も行っていませんが、<font color='red'>研究資料用として無償で公開しています。</font></strong></li>"
val_html +=  "<li><strong>比較サンプルの特性値は作者の独断で仮設定したものです。<font color='red'>正確さは一切保証していません。</font></strong></li>"
val_html +=  "<li>ご意見等は歓迎いたしますが、ご希望に添えるかなどを含め、お返事はしない場合があります。</li>"
val_html += "</ul>"
val_html += "</p></div>"
st.markdown(val_html, unsafe_allow_html=True)
# 💡 区切り線
st.divider()


####################################################################################################################
#  設定側（左サイドバー）表示処理
####################################################################################################################

# ┏━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃ 　  ┃　　見出し、説明エリア　　　　　　　　┃
# ┃💡💡┣━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┫
# ┃ 　  ┃　　　　　　３Ｄプロット 　┃ スケール ┃
# ┃　設 ┃　　　　　　　　エリア　　 ┃　エリア　┃
# ┃　定 ┣━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━┫
# ┃　　 ┃　相性診断エリア　　　　　　　　　　　┃
# ┗━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

# ==========================================
# 3. サイドバー：コントロール層
# ==========================================
st.sidebar.title("🛠️ 設定")


# ② ユーザー定義枠（カスタム追加機能）
with st.sidebar.expander("👤 カスタムペルソナ定義", expanded=False):
    name = st.text_input(
        "ペルソナ名", placeholder="例：自分、上司A、企画X"
    )

    st.markdown("**" + AXIS_PREFIX + "X" + AXIS_SUFFIX + ":" + AXIS_NAME1_X + "**")
    val1_x = st.slider(
        "[" + str(STEP_MIN) + ":" + AXIS_NAME1_X + ":" + str(STEP_MAX) + "]",
        int(STEP_MIN),
        int(STEP_MAX),
        0,
        1,
        key="slider_x",
    )

    st.markdown("**" + AXIS_PREFIX + "Y" + AXIS_SUFFIX + ":" + AXIS_NAME1_Y + "**")
    val1_y = st.slider(
        "[" + str(STEP_MIN) + ":" + AXIS_NAME1_Y + ":" + str(STEP_MAX) + "]",
        int(STEP_MIN),
        int(STEP_MAX),
        0,
        1,
        key="slider_y",
    )

    st.markdown("**" + AXIS_PREFIX + "Z" + AXIS_SUFFIX + ":" + AXIS_NAME1_Z + "**")
    val1_z = st.slider(
        "[" + str(STEP_MIN) + ":" + AXIS_NAME1_Z + ":" + str(STEP_MAX) + "]",
        int(STEP_MIN),
        int(STEP_MAX),
        0,
        1,
        key="slider_z",
    )

    st.markdown("**" + AXIS_PREFIX + "α" + AXIS_SUFFIX + ":" + AXIS_NAME1_A + "**")
    val1_a = st.slider(
        "[" + str(STEP_MIN) + ":" + AXIS_NAME1_A + ":" + str(STEP_MAX) + "]",
        int(STEP_MIN),
        int(STEP_MAX),
        0,
        1,
        key="slider_alfa",
    )

    st.markdown("**" + AXIS_PREFIX + "A" + AXIS_SUFFIX + ":" + AXIS_NAME2_A + "**")
    val2_a = st.slider(
        "[" + str(STEP_MIN) + ":" + AXIS_NAME2_A + ":" + str(STEP_MAX) + "]",
        int(STEP_MIN),
        int(STEP_MAX),
        0,
        1,
        key="slider_a",
    )

    st.markdown("**" + AXIS_PREFIX + "B" + AXIS_SUFFIX + ":" + AXIS_NAME2_B + "**")
    val2_b = st.slider(
        "[" + str(STEP_MIN) + ":" + AXIS_NAME2_B + ":" + str(STEP_MAX) + "]",
        int(STEP_MIN),
        int(STEP_MAX),
        0,
        1,
        key="slider_b",
    )

    st.markdown("**" + AXIS_PREFIX + "C" + AXIS_SUFFIX + ":" + AXIS_NAME2_C + "**")
    val2_c = st.slider(
        "[" + str(STEP_MIN) + ":" + AXIS_NAME2_C + ":" + str(STEP_MAX) + "]",
        int(STEP_MIN),
        int(STEP_MAX),
        0,
        1,
        key="slider_c",
    )

    st.markdown("**" + AXIS_PREFIX + "D" + AXIS_SUFFIX + ":" + AXIS_NAME2_D + "**")
    val2_d = st.slider(
        "[" + str(STEP_MIN) + ":" + AXIS_NAME2_D + ":" + str(STEP_MAX) + "]",
        int(STEP_MIN),
        int(STEP_MAX),
        0,
        1,
        key="slider_d",
    )

    st.markdown("**" + AXIS_PREFIX + "E" + AXIS_SUFFIX + ":" + AXIS_NAME2_E + "**")
    val2_e = st.slider(
        "[" + str(STEP_MIN) + ":" + AXIS_NAME2_E + ":" + str(STEP_MAX) + "]",
        int(STEP_MIN),
        int(STEP_MAX),
        0,
        1,
        key="slider_e",
    )

    desc = st.text_area(
        "説明（特徴や行動特性など）",
        placeholder="ペルソナの性格や行動の特徴に関するメモ",
    )

    submit_button = st.button(label="ペルソナを追加")

# フォーム送信時の処理
if submit_button:
    if not name.strip():
        st.sidebar.error("⚠️ ペルソナ名を入力してください。")
    elif contains_name(st.session_state.custom_personas, DATA_NAM, name):
        st.sidebar.error("⚠️ ペルソナ名"+name+"は登録済です。")
    else:
        new_persona = {
            DATA_GRP: GRP_CST_INDEX,
            DATA_NAM: name.strip(),
            AXIS_LABEL1_X : val1_x,
            AXIS_LABEL1_Y : val1_y,
            AXIS_LABEL1_Z : val1_z,
            AXIS_LABEL1_A : val1_a,
            AXIS_LABEL2_A : val2_a,
            AXIS_LABEL2_B : val2_b,
            AXIS_LABEL2_C : val2_c,
            AXIS_LABEL2_D : val2_d,
            AXIS_LABEL2_E : val2_e,
            DATA_DSC: desc.strip()
                if desc.strip()
                else "ユーザーが定義したカスタムペルソナです。",
            DATA_CAT: "カスタムカテゴリ",
        }
        st.session_state.custom_personas.append(new_persona)
        st.sidebar.success(f"🎉 「{name}」をプロット空間に登録しました！")

# カスタムペルソナのリセット機能
if st.sidebar.button("🗑️ カスタムペルソナ全消去"):
    st.session_state.custom_personas = []
    st.sidebar.info("カスタムデータをクリアしました。")
    st.rerun()

# ==========================================
# データの統合処理（既存ロジック）
# ==========================================
if st.session_state.custom_personas:
    df_custom = pd.DataFrame(st.session_state.custom_personas)
    df_pre_all = pd.concat([df_default, df_custom], ignore_index=True)
else:
    df_pre_all = df_default.copy()

# DEBUG print(df_pre_all.head())

# グループID順にソート
df_all = df_pre_all.sort_values(by=DATA_GRP)

# ==========================================
# 【新規追加】① グループ選択メニュー（1次フィルタリング）
# ==========================================
st.sidebar.write("---")
st.sidebar.header("📁 グループの絞り込み")

# ID(DATA_GRP)をソートし、List化
available_groups_id_list = sorted(df_all[DATA_GRP].unique().tolist())

# グループリストを表示しながら、selected_groupsを作成
initial_group_display = GRP_INIT_DISP
selected_groups = []

for group_name in available_groups_id_list:
    
    default_checked = initial_group_display[group_name]
    if st.sidebar.checkbox(
        GRP_NAMES[group_name],
        value=default_checked,
        key=f"group_filter_{group_name}",
    ):
        selected_groups.append(group_name)

# 選択されたグループだけに絞り込む（1次抽出）
df_group_filtered = (
    df_all[df_all[DATA_GRP].isin(selected_groups)]
    if selected_groups
    else df_all.iloc[0:0]
)

# ==========================================
# 【修正】② 動的凡例チェックボックス（2次フィルタリング）
# ==========================================
st.sidebar.write("---")
st.sidebar.header("👁️ 個別表示切り替え")

# 絞り込まれたグループの中での全選択 / 全解除
select_all = st.sidebar.checkbox("すべてを表示", value=True)

selected_names = []
# ループ対象を df_all から 「df_group_filtered」 に変更します
for idx, row in df_group_filtered.iterrows():
    # 選択されているグループのペルソナだけがここにチェックボックスとして並びます
    if st.sidebar.checkbox(
        # row[DATA_LABELS['NAM']], value=select_all, key=f"cb_{row[DATA_LABELS['NAM']]}_{idx}_{row[DATA_GRP]}"
#        row[DATA_GRP] + "-" + row[DATA_NAM], value=select_all, key=f"cb_{row[DATA_NAM]}_{idx}_{row[DATA_GRP]}"
        GRP_NAMES[row[DATA_GRP]] + "-" + row[DATA_NAM], value=select_all, key=f"cb_{row[DATA_NAM]}_{idx}_{row[DATA_GRP]}"

        #GROUPE_MATRIX(GROUPE_MX_NAME, int(row[DATA_GRP])) + "-" + row[DATA_NAM], value=select_all, key=f"cb_{row[DATA_GRP]}_{idx}_{row[DATA_GRP]}"
    ):
        selected_names.append(row[DATA_NAM])

# ==========================================
# 最終的に3Dプロットに渡すデータ（最終抽出）
# ==========================================

df_pre_final = df_group_filtered[df_group_filtered[DATA_NAM].isin(selected_names)]

df_final = df_pre_final.copy()  # コピーを作成
if not df_final.empty:
    # マーカーで使用するXYZ,a属性に応じた色を追加する

    df_final["color"] = df_final.apply(
        lambda row: generate_personality_color(
            STEP_MIN,
            STEP_MAX,
            row[AXIS_LABEL1_X],
            row[AXIS_LABEL1_Y],
            row[AXIS_LABEL1_Z],
        ),
        axis=1
    )
    
    df_final["color_e"] = df_final.apply(
        lambda row: generate_emotionality_color(
            STEP_MIN,
            STEP_MAX,
             row[AXIS_LABEL1_A],
        ),
        axis=1
    )

    # グループ名を追加
#    df_final["groupe_name"] = GRP_NAMES[ df_final[DATA_GRP] ]
    #df_final["groupe_name"] = "TEST TEST"  #GRP_NAMES[ df_final[DATA_GRP] ]
    df_final[GRP_HOVER] = df_final.apply(
        lambda row: GRP_NAMES[ row[DATA_GRP] ], 
        axis=1
    )
    

####################################################################################################################
#  表示処理　（メインレイアウト層）
####################################################################################################################
fig = go.Figure()

# 💡 左側３次元プロット(5) と 右側グラデエリア (1) の比率で横並びす
plot_col, grade_col = st.columns([5, 1], gap="small")

# ┏━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃　　 ┃　　　見出し、説明エリア　　　　　　　 ┃
# ┃　　 ┣━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┫
# ┃  　 ┃　💡 　　３次元プロット　┃　　グラデ　┃
# ┃  設 ┃　　　　　　　　　エリア　┃　　エリア　┃
# ┃　定 ┣━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━┫
# ┃  　 ┃　　　相性診断エリア　　　　　　　　　 ┃
# ┗━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#

# ------------------------------------------
# 左：③ Plotlyを用いた3D散布図
# ------------------------------------------


# 🌐 公式リファレンス（詳細な設定を確認したい場合）
# 属性のすべての種類を網羅している公式サイトのページはこちらになります。
# ブラウザの翻訳機能（日本語翻訳）を有効にして眺めると、さらにマニアックな属性（ホバー時の挙動など）を調べることができます。
# 
# 3D散布図マーカー（Scatter3d.marker）公式リファレンス:
# https://plotly.com/python/reference/scatter3d/#scatter3d-marker
# 
# 2D散布図シンボル（形式）の一覧カタログ:
# https://plotly.com/python/marker-style/

with plot_col:
    st.subheader("🌐 3D性格プロット - 性格・思考傾向分布把握用")

    # fig = go.Figure()

    # (既存のPlotly描画ロジックはそのまま使用)
    # ※ 混同を防ぐため、既存の fig.update_layout 内にあるカラーバー(colorbar)や
    #   colorscale の設定は無効化(削除)するか、単色設定にしておくのがおすすめです。

    if df_final.empty:
        st.warning(
            "⚠️ 左側のサイドバーで対象を1つ以上選択してください。プロット空間が空集合（Empty）です。"
        )
    else:
        fig = go.Figure()

        # 中心（0, 0, 0）のガイドライン（ゼロ線）を補助的に描画
        # X軸
        fig.add_trace(
            go.Scatter3d(
                x=[STEP_MIN, STEP_MAX],
                y=[0, 0],
                z=[0, 0],
                mode="lines",
                line={"color":"rgba(128,255,255,0.2)", "width":3},
                showlegend=False,
                hoverinfo="skip",
            )
        )
    
        # Y軸
        fig.add_trace(
            go.Scatter3d(
                x=[0, 0],
                y=[STEP_MIN, STEP_MAX],
                z=[0, 0],
                mode="lines",
                line={"color":"rgba(255,128,255,0.2)", "width":3},
                showlegend=False,
                hoverinfo="skip",
            )
        )
    
        # Z軸
        fig.add_trace(
            go.Scatter3d(
                x=[0, 0],
                y=[0, 0],
                z=[STEP_MIN, STEP_MAX],
                mode="lines",
                line={"color":"rgba(255,255,128,0.2)", "width":3},
                showlegend=False,
                hoverinfo="skip",
            )
        )

        ## 3D散布図の描画

        # ------------------------------------------
        # 3D散布図のマーカー描画関数
        # ------------------------------------------
        def draw_3d_markers(fig, df_draw, df_draw_type, legend_state=True):

            if not df_draw.empty:
                fig.add_trace(
                    go.Scatter3d(
                        x=group_df[AXIS_LABEL1_X],
                        y=group_df[AXIS_LABEL1_Y],
                        z=group_df[AXIS_LABEL1_Z],
                        mode="text",
                        name=group_name,  # 凡例にグループ名が表示されます
                        text=group_df[DATA_NAM],
                        hoverinfo="skip",
                        showlegend=False,                   # 凡例非表示 
                    )
                )

                # ペルソナのプロット（ぶりつぶし色は属性を反映）
                if df_draw_type != GRP_NAME_DEF:
                    # shadow_color='lightgray'            # 規定ペルソナは背景円示の色を薄い灰色にしてデフォルトペルソナを目立たせない
                    shadow_shape = 'circle'
                else:
                    # shadow_color='rgb(255,160,160)'     # カスタムペルソナは背景円示の色を薄赤にしてカスタムペルソナを強調
                    shadow_shape = 'square'
                
                # ①　マーカーの背景を描画                 # 枠線を太くして背景円を表示する    

                # DEBUG  print(df_draw.head())
                
                fig.add_trace(go.Scatter3d(

                    x=df_draw[AXIS_LABEL1_X],
                    y=df_draw[AXIS_LABEL1_Y],
                    z=df_draw[AXIS_LABEL1_Z],
                    
                    text=group_df[DATA_NAM],
                    #mode='markers+text',               # 名前も表示する場合は 'markers+text' に変更
                    mode='markers',                     # 名前も表示する場合は 'markers+text' に変更
                    
                    marker={    
                        "line": {"width": 0},             # 背景の枠線幅は０
                        "symbol": shadow_shape,
                        #symbol='diamond',
                        "size": 6,
                        "color": df_draw["color_e"],
                        "opacity": 0.7                     # 薄く透けさせる
                    },
                    # 吹き出し
                    hovertemplate = (
                        f"<b>%{{customdata[0]}}</b>  %{{customdata[1]}}  %{{customdata[2]}}<br><br>"
                        f"{AXIS_LABEL1_X}({AXIS_NAME1_X}): %{{x}}   {AXIS_LABEL1_Y}({AXIS_NAME1_Y}): %{{y}}   {AXIS_LABEL1_Z}({AXIS_NAME1_Z}): %{{z}}   "
                        f"{AXIS_LABEL1_A}({AXIS_NAME1_A}): %{{customdata[3]}}<br>"
                        f"{AXIS_LABEL2_A}({AXIS_NAME2_A}): %{{customdata[4]}}   {AXIS_LABEL2_B}({AXIS_NAME2_B}): %{{customdata[5]}}   {AXIS_LABEL2_C}({AXIS_NAME2_C}): %{{customdata[6]}}   "
                        f"{AXIS_LABEL2_D}({AXIS_NAME2_D}): %{{customdata[7]}}   {AXIS_LABEL2_E}({AXIS_NAME2_E}): %{{customdata[8]}}<br>"
                        f"<br>{DATA_DSC}:<br>%{{customdata[9]}}"
                    ), 
                    customdata = df_draw[[
                            DATA_NAM,     GRP_HOVER,    DATA_CAT,
                            AXIS_LABEL1_A, 
                            AXIS_LABEL2_A, AXIS_LABEL2_B, AXIS_LABEL2_C, AXIS_LABEL2_D, AXIS_LABEL2_E, 
                            DATA_DSC,
                            ]],

                    name=df_draw_type,
                    showlegend=not legend_state,        # 背景円を凡例として表状　 非表示だったら表示 

                ))
                
                # ② その上にマーカーを所定の外形でクッキリ描画

                fig.add_trace(go.Scatter3d(
                    x=df_draw[AXIS_LABEL1_X],
                    y=df_draw[AXIS_LABEL1_Y],
                    z=df_draw[AXIS_LABEL1_Z],
                    #a=df_draw[AXIS_MATRIX(AXIS_LABEL2_COL, AXIS_INDEX_2A)],

                    # mode='markers+text',              # 名前も表示する場合は 'markers+text' に変更
                    # mode='none',                      # 名前、マーカーも表示しない場合は 'none' に変更
                    # mode='markers',                   # 名前は出さずマーカーだけにする
                    mode='markers',                     # 名前は出さずマーカーだけにする

                    marker={
                        "line": {"width": 0},             # マーカー字体は輪郭線非表示
                        ###### 外形選択枝 #####
                        # ['circle', 'circle-open', 'cross', 'diamond',
                        #  'diamond-open', 'square', 'square-open', 'x']
                        # "symbol": "cross",               # ＋ 塗りつぶしなし　背景に円がつく。
                        "symbol": "square",                # 🔳 ■        背景に円がつく。
                        # "symbol": "diamond",             # 🔶 ひし形 　背景に円がつく。
                        # "symbol": "circle",              # 🔴 円
                        "size": 4,
                        "color": df_draw["color"],         # 予め計算しておいた色を設定
                        "opacity": 1.0
                    },
                    # hoverinfo='skip',                   # 吹き出し(ホバー情報)非表示の場合
                    # 吹き出し
                    hovertemplate = (
                        f"<b>%{{customdata[0]}}</b>  %{{customdata[1]}}  %{{customdata[2]}}<br><br>"
                        f"{AXIS_LABEL1_X}({AXIS_NAME1_X}): %{{x}}   {AXIS_LABEL1_Y}({AXIS_NAME1_Y}): %{{y}}   {AXIS_LABEL1_Z}({AXIS_NAME1_Z}): %{{z}}   "
                        f"{AXIS_LABEL1_A}({AXIS_NAME1_A}): %{{customdata[3]}}<br>"
                        f"{AXIS_LABEL2_A}({AXIS_NAME2_A}): %{{customdata[4]}}   {AXIS_LABEL2_B}({AXIS_NAME2_B}): %{{customdata[5]}}   {AXIS_LABEL2_C}({AXIS_NAME2_C}): %{{customdata[6]}}   "
                        f"{AXIS_LABEL2_D}({AXIS_NAME2_D}): %{{customdata[7]}}   {AXIS_LABEL2_E}({AXIS_NAME2_E}): %{{customdata[8]}}<br>"
                        f"<br>{DATA_DSC}:<br>%{{customdata[9]}}"
                    ), 
                    customdata = df_draw[[
                            DATA_NAM,     GRP_HOVER,    DATA_CAT,
                            AXIS_LABEL1_A, 
                            AXIS_LABEL2_A, AXIS_LABEL2_B, AXIS_LABEL2_C, AXIS_LABEL2_D, AXIS_LABEL2_E, 
                            DATA_DSC,
                            ]],

                    name=df_draw_type,
                    showlegend=False,                   # 凡例非表示 

                ))
        
        legend_displayed_flag = False  # 凡例表示のフラグ初期値を False に設定
        
        for group_name, group_df in df_final.groupby("グループ"):

            # A. デフォルトペルソナ(グループが、カスタム以外)のプロット
            draw_3d_markers(fig, 
                            df_final[df_final[DATA_GRP] != GRP_CST_INDEX].replace(r"\n","<br>", regex=True).copy(),
                            GRP_NAME_DEF,
                            legend_displayed_flag)

            # B. カスタムペルソナ(グループが、カスタム)のプロット

            draw_3d_markers(fig, 
                            df_final[df_final[DATA_GRP] == GRP_CST_INDEX].replace(r"\n","<br>", regex=True).copy(),
                            GRP_NAME_CST,
                            legend_displayed_flag)

            legend_displayed_flag = True  # 凡例表示済みフラグを True に設定

        # end of for group_name, group_df in df_final.groupby("グループ"):
        # ------------------------------------------------------------------------------------------------
        
        # 空間レイアウトの最適化 （軸の説明追加など）
        fig.update_layout(
            template="plotly_dark",
            # プロットエリア縦幅
            # 👇 ここを追加！縦幅を 800ピクセル（好みに合わせて900などでも可）に引き上げ
            height=800,
            
            # 3軸の説明
            # 👇 ここを追加！上下左右の無駄な余白（マージン）をゼロに削ってエリアを最大化
            margin={"l": 0, "r": 0, "b": 0, "t": 30},
            scene={
                "xaxis": {
#                    title=AXIS_LABEL1_X + ":" + AXIS_NAME1_X + "(" + AXIS_DESC1_X + ")",
                    "title":AXIS_LABEL1_X + ":" + AXIS_NAME1_X,
                    "range":[STEP_MIN - 0.5, STEP_MAX + 0.5],
                    "gridcolor":"rgba(128,128,128,0.2)",
                },
                "yaxis": {
#                   title=AXIS_LABEL1_X + ":" + AXIS_NAME1_Y + "(" + AXIS_DESC1_Y + ")",
                    "title":AXIS_LABEL1_Y + ":" + AXIS_NAME1_Y,
                    "range":[STEP_MIN - 0.5, STEP_MAX + 0.5],
                    "gridcolor":"rgba(128,128,128,0.2)",
                },
                "zaxis": {
#                    title=AXIS_LABEL1_X + ":" + AXIS_NAME1_Z + "(" + AXIS_DESC1_Z + ")",
                    "title":AXIS_LABEL1_Z + ":" + AXIS_NAME1_Z,
                    "range":[STEP_MIN - 0.5, STEP_MAX + 0.5],
                    "gridcolor":"rgba(128,128,128,0.2)",
                },
                "aspectmode": "cube",  # 立方体の枠線を固定
            },
            # ToDo: 凡例の表示方法を検討中。現在、重複表示される.また、背景もtrace n のように表示される
            # ペルソナ凡例の位置を左上に固定（右側のグラデエリアと重ならないように）
            legend={"yanchor": "top", "y": 0.99, "xanchor": "left", "x": 0.01},
        
        ) # end of fig.update_layout

        # chart 全体幅調整
        # chartを横幅いっぱいに広げ大画面で見やすくする。
        # st.plotly_chart(fig, width=500)
        st.plotly_chart(fig, width="stretch")

    # end of if df_final.empty:

####################################################################################################################

# 💡 プロットエリア全体のすぐ右に区切り線
# st.divider() 
# ToDo: 右側のグラデエリアとプロットエリアを分離するための区切り線追加方法検討中。

####################################################################################################################

# --- 右側：💡 4列構成・縦積み11段階インジケーター ---
# ┏━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃　　 ┃　　　見出し、説明エリア　　　　　　　 ┃
# ┃　　 ┣━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┫
# ┃  　 ┃　　　　　３次元プロット　┃　💡グラデ　┃
# ┃  設 ┃　　　　　　　　　エリア　┃　　エリア　┃
# ┃　定 ┣━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━┫
# ┃  　 ┃　　　相性診断エリア　　　　　　　　　 ┃
# ┗━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


with grade_col:
    st.markdown(
        "<div style='text-align: center; font-weight: bold; margin-bottom: 10px;'>📊XYZ軸(内側)／α軸(周囲) 表示色</div>",
        unsafe_allow_html=True,
    )

    # 上から下へ向かう11段階の数値リスト（+5 から -5）
    steps_reverse = list(range(STEP_MAX, STEP_MIN-1, -1))
    
    # 💡 5列（数値用、X軸、Y軸、Z軸、a軸）に小さく均等分割します
    c_val, c_x, c_y, c_z, c_a = st.columns(5)

    # 共通のバーグラフ用タイルのブロックサイズ設定
    block_style = (
        "width:22px; height:22px; display:flex; align-items:center;" 
        "justify-content:center; border-radius:3px; font-size:10px; font-weight:bold; font-family:monospace;"
        )
    
    # --- 1列目：数値表示（左端・単色グレー） ---
    with c_val:
        st.markdown(
            "<div style='text-align: center; font-size: 11px; font-weight: bold; color: #555555;'>" + DATA_VAL + "</div>",
            unsafe_allow_html=True,
        )
        val_html = "<div style='display: flex; flex-direction: column; gap: 4px; align-items: center;'>"
        for v in steps_reverse:
            # 左端の数値は、見やすさを最優先に淡いグレーの単色背景に固定します
            bg_color = "#ECEFF1"
            text_color = "#37474F"
            val_str = f"{v:+d}" if v > 0 else f"{v:d}"  # +5, 0, -5 のような表記
            val_html += f"<div style='background-color:{bg_color}; color:{text_color}; {block_style}'>{val_str}</div>"
        val_html += "</div>"
        st.markdown(val_html, unsafe_allow_html=True)

    # --- 2列目：X軸（シアン） ---
    with c_x:
        st.markdown(
            "<div style='text-align: center; font-size: 11px; font-weight: bold; color: #008B8B;'>" + AXIS_LABEL1_X + "</div>",
            unsafe_allow_html=True,
        )
        x_html = "<div style='display: flex; flex-direction: column; gap: 4px; align-items: center;'>"
        for v in steps_reverse:
            color = generate_personality_color(STEP_MIN, STEP_MAX, v, STEP_MIN, STEP_MIN)  # X軸の値に基づく色を生成
            x_html += f"<div style='background-color:{color}; border:1px solid #B0BEC5; {block_style}'></div>"
        x_html += "</div>"
        st.markdown(x_html, unsafe_allow_html=True)

    # --- 3列目：Y軸（マゼンタ） ---
    with c_y:
        st.markdown(
            "<div style='text-align: center; font-size: 11px; font-weight: bold; color: #8B008B;'>" + AXIS_LABEL1_Y + "</div>",
            unsafe_allow_html=True,
        )
        y_html = "<div style='display: flex; flex-direction: column; gap: 4px; align-items: center;'>"
        for v in steps_reverse:
            color = generate_personality_color(STEP_MIN, STEP_MAX, STEP_MIN, v, STEP_MIN)  # y軸の値に基づく色を生成
            y_html += f"<div style='background-color:{color}; border:1px solid #B0BEC5; {block_style}'></div>"
        y_html += "</div>"
        st.markdown(y_html, unsafe_allow_html=True)

    # --- 4列目：Z軸（イエロー） ---
    with c_z:
        st.markdown(
            "<div style='text-align: center; font-size: 11px; font-weight: bold; color: #8B8B00;'>" + AXIS_LABEL1_Z + "</div>",
            unsafe_allow_html=True,
        )
        z_html = "<div style='display: flex; flex-direction: column; gap: 4px; align-items: center;'>"
        for v in steps_reverse:
            color = generate_personality_color(STEP_MIN, STEP_MAX, STEP_MIN, STEP_MIN, v)  # Z軸の値に基づく色を生成
            z_html += f"<div style='background-color:{color}; border:1px solid #B0BEC5; {block_style}'></div>"
        z_html += "</div>"
        st.markdown(z_html, unsafe_allow_html=True)

    # --- 5列目：a軸（緑⇔ピンク） ---
    with c_a:
        st.markdown(
            "<div style='text-align: center; font-size: 11px; font-weight: bold; color: #8B8B00;'>" + AXIS_LABEL1_A + "</div>",
            unsafe_allow_html=True,
        )
        a_html = "<div style='display: flex; flex-direction: column; gap: 4px; align-items: center;'>"
        for v in steps_reverse:
            color = generate_emotionality_color(STEP_MIN, STEP_MAX, v)  # a軸の値に基づく色を生成
            a_html += (
##                    f"<div style='background-color:{color}; border:1px solid #B0BEC5; {block_style}'>"
##                    f"<p >●●</p></div>"
#                    f"<p style='color:{color};'>●■</p>"

                    f"<div style='color:{color}; {block_style}'>●■</div>"

            )
            
        a_html += "</div>"
        st.markdown(a_html, unsafe_allow_html=True)


####################################################################################################################

# 💡 プロットエリア全体のすぐ下に区切り線
st.divider()

####################################################################################################################

# ┏━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃　　 ┃　　　見出し、説明エリア　　　　　　　 ┃
# ┃　　 ┣━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┫
# ┃  　 ┃　　　  　３次元プロット　┃　　グラデ　┃
# ┃  設 ┃　　　　　　　　　エリア　┃　　エリア　┃
# ┃　定 ┣━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━┫
# ┃  　 ┃　　💥　相性診断エリア　💕　　　　　 ┃
# ┗━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
#
# ------------------------------------------
# ④ 下段　衝突判定アルゴリズム（相性診断）
# ------------------------------------------

st.subheader("💥 衝突推定 ＆ 相性推定 💕")

if not st.session_state.custom_personas:
    st.info(
        "💡 左側の設定から「カスタムペルソナ」を登録すると、既定ペルソナや他のカスタムペルソナとの距離測定・相性問題の予測シミュレーションがここに展開されます。"
    )
else:
    # ユーザー定義ペルソナからベースを選択
    custom_names = [p["名前"] for p in st.session_state.custom_personas]
    target_name = st.selectbox("診断の基準側とするペルソナを選択:", custom_names)

    # ターゲット対象のデータ取得
    target_data = next(
        p for p in st.session_state.custom_personas if p[DATA_NAM] == target_name
    )

    target_data_1x = target_data[AXIS_LABEL1_X]
    target_data_1y = target_data[AXIS_LABEL1_Y]
    target_data_1z = target_data[AXIS_LABEL1_Z]
    target_data_1a = target_data[AXIS_LABEL1_A]
    target_data_2a = target_data[AXIS_LABEL2_A]
    target_data_2b = target_data[AXIS_LABEL2_B]
    target_data_2c = target_data[AXIS_LABEL2_C]
    target_data_2d = target_data[AXIS_LABEL2_D]
    target_data_2e = target_data[AXIS_LABEL2_E]


    st.markdown(f"### 🎯 「{target_name}」の性格推定")
#    st.write(
#        f"**性格・思考傾向座標**: X:{target_data_1x} / Y:{target_data_1y} / Z:{target_data_1z}   "
#        f"**快楽志向座標**: α:{target_data_1a}   "
#        f"**相性診断用座標**: A:{target_data_1a} / B:{target_data_1b]} / C:{target_data_2c} / D:{target_data_2d} / E:{target_data_2e} "
#    )
 
    st.write(
        f"**性格・思考傾向座標**: X:{target_data_1x} / Y:{target_data_1y} / Z:{target_data_1z}   "
        f"**快楽志向座標**: α:{target_data_1a}   "
        f"**相性診断用座標**: A:{target_data_2a} / B:{target_data_2b} / C:{target_data_2c} / D:{target_data_2d} / E:{target_data_2e} "
    )



    # ユーザー定義ペルソナ（基準側）の正確傾向判定
    check_result_ref = check_personality_note(
                THRESHOLD, target_data_1x, target_data_1y, target_data_1z, target_data_1a, 
                target_data_2a, target_data_2b, target_data_2c, target_data_2d, target_data_2e)


    if (check_result_ref != "") :
        st.warning(
            "⚠️【注意】場合により他人と衝突する可能性がありえます。\n\n" + check_result_ref
        )
    st.write("---")

    st.write("#### 🔍 各ペルソナとの相性シミュレーション")

    # 選択されたペルソナと他の全ペルソナを比較
    for idx, row in df_final.iterrows():
        # 自分自身（同じ名前かつ同じタイプ）との比較はスキップ
        if row[DATA_NAM] == target_name and row[DATA_GRP] == GRP_CST_INDEX:
            continue
        
        
        row_data_1x = row[AXIS_LABEL1_X]
        row_data_1y = row[AXIS_LABEL1_Y]
        row_data_1z = row[AXIS_LABEL1_Z]
        row_data_1a = row[AXIS_LABEL1_A]
        row_data_2a = row[AXIS_LABEL2_A]
        row_data_2b = row[AXIS_LABEL2_B]
        row_data_2c = row[AXIS_LABEL2_C]
        row_data_2d = row[AXIS_LABEL2_D]
        row_data_2e = row[AXIS_LABEL2_E]
        
        # 1. 3次元ユークリッド距離の計算
        dist = math.sqrt(
            (target_data_1x - row_data_1x) ** 2
            + (target_data_1y - row_data_1y) ** 2
            + (target_data_1z - row_data_1z) ** 2
        )

        # アコーディオンパネルで綺麗に出力
        # ToDo: グループのアイコン変更？
        icon = "🦊" if row[DATA_GRP] == GRP_NAME_DEF else "👤"
        with st.expander(f"{icon} {row[DATA_NAM]}（空間距離: {dist:.2f}）"):
            st.write(
            #    f"**システム座標**: X:{row['X軸']} / Y:{row['Y軸']} / Z:{row['Z軸']} ({row['カテゴリ']})"
                f"**性格・思考傾向座標**: X:{row_data_1x} / Y:{row_data_1y} / Z:{row_data_1z} "
                f"**快楽志向座標**: α:{row_data_1a} "
                f"**相性診断用座標**: A:{row_data_2a} / B:{row_data_2b} / C:{row_data_2c} / D:{row_data_2d} / E:{row_data_2e} "
                f"({row[DATA_CAT]})"
            )
            st.markdown(f"**特性**: {row[DATA_DSC]}")

            st.write("---")
            
            
            # 💡 左側XYZa(1) と 右側ABCDE (1) の比率で横並びす
            xyza_col, abcde_col = st.columns([1, 1], gap="small")
            


            #----------------------
            # レーダーチャートを表示
            #----------------------

            with xyza_col:
                radar_categories = [
                    "X: " + AXIS_NAME1_X,
                    "Y: " + AXIS_NAME1_Y,
                    "Z: " + AXIS_NAME1_Z,
                    "α: " + AXIS_NAME1_A,
                ]
                radar_values_target = [
                    target_data_1x,
                    target_data_1y,
                    target_data_1z,
                    target_data_1a,
                ]
                radar_values_row = [
                    row_data_1x,
                    row_data_1y,
                    row_data_1z,
                    row_data_1a,
                ]

                radar_fig = go.Figure()
                radar_fig.add_trace(
                    go.Scatterpolar(
                        r=radar_values_target + [radar_values_target[0]],
                        theta=radar_categories + [radar_categories[0]],
                        fill="toself",
                        name=f"{target_name}",
                        line={"color":"rgba(31, 120, 180, 0.9)", "width":2},
                        fillcolor="rgba(31, 120, 180, 0.25)",
                    )
                )
                radar_fig.add_trace(
                    go.Scatterpolar(
                        r=radar_values_row + [radar_values_row[0]],
                        theta=radar_categories + [radar_categories[0]],
                        fill="toself",
                        name=f"{row[DATA_NAM]}",
                        line={"color":"rgba(227, 26, 28, 0.9)", "width":2},
                        fillcolor="rgba(227, 26, 28, 0.2)",
                    )
                )
                radar_fig.update_layout(
                    title="相性推定 レーダーチャート（X,Y,Z,α軸）",
                    polar={
                        "angularaxis":{"direction":"clockwise", "rotation":90},
                        "radialaxis":{"visible":True, "range":[-5, 5]},
                    },
                    showlegend=True,
                    margin={"l":40, "r":40, "t":60, "b":40},
                )
                st.plotly_chart(radar_fig, use_container_width=True)



            with abcde_col:
                radar_categories = [
                    "A: " + AXIS_NAME2_A,
                    "B: " + AXIS_NAME2_B,
                    "C: " + AXIS_NAME2_C,
                    "D: " + AXIS_NAME2_D,
                    "E: " + AXIS_NAME2_E,
                ]
                radar_values_target = [
                    target_data_2a,
                    target_data_2b,
                    target_data_2c,
                    target_data_2d,
                    target_data_2e,
                ]
                radar_values_row = [
                    row_data_2a,
                    row_data_2b,
                    row_data_2c,
                    row_data_2d,
                    row_data_2e,
                ]

                radar_fig = go.Figure()
                radar_fig.add_trace(
                    go.Scatterpolar(
                        r=radar_values_target + [radar_values_target[0]],
                        theta=radar_categories + [radar_categories[0]],
                        fill="toself",
                        name=f"{target_name}",
                        line={"color":"rgba(31, 120, 180, 0.9)", "width":2},
                        fillcolor="rgba(31, 120, 180, 0.25)",
                    )
                )
                radar_fig.add_trace(
                    go.Scatterpolar(
                        r=radar_values_row + [radar_values_row[0]],
                        theta=radar_categories + [radar_categories[0]],
                        fill="toself",
                        name=f"{row[DATA_NAM]}",
                        line={"color":"rgba(227, 26, 28, 0.9)", "width":2},
                        fillcolor="rgba(227, 26, 28, 0.2)",
                    )
                )
                radar_fig.update_layout(
                    title="相性推定 レーダーチャート（A〜E軸）",
                    polar={
                        "angularaxis":{"direction":"clockwise", "rotation":90},
                        "radialaxis":{"visible":True, "range":[-5, 5]},
                    },
                    showlegend=True,
                    margin={"l":40, "r":40, "t":60, "b":40},
                )
                st.plotly_chart(radar_fig, use_container_width=True)
            
            st.write("---")
            #----------------------
            # ペルソナ側正確推定結果表示
            #----------------------


            check_result_row = check_personality_note(
                THRESHOLD, row_data_1x, row_data_1y, row_data_1z, row_data_1a, 
                row_data_2a, row_data_2b, row_data_2c, row_data_2d, row_data_2e)
            st.markdown(f"#### 🎯 「"+row[DATA_NAM]+"」の性格推定")

            if (check_result_row != "") :
                st.warning(
                    check_result_row
                )
                st.write("---")
            else:   
                st.success("✅ このペルソナは多数派閥との衝突の可能性は高くはありません。")
                st.write("---")
                
            #----------------------
            # 相性推定
            #----------------------

            st.markdown(f"#### 🎯 「"+row[DATA_NAM]+"」との相性推定")
                
            general_logs = ""
            alert_logs = ""
            synagy_logs = ""

            # 距離基準の判定
            if dist < 2.0:
                general_logs += "🟢 **【思考傾向の近接】**\n\n"
                general_logs += "思考傾向の親和性が非常に高い（非常に近い）配置です。"
                general_logs += "非言語的な相互理解が期待できる一方、課題や死角（短所）も共通化しやすいため、補完関係というよりは同質的な共鳴としてのバランスに留意が必要です。\n\n"
            
            elif dist >= 7.0:
                ## ToDo: 距離がはなれていてもよい、補完関係の場合の対応。
                general_logs += "🌐 **【価値観の乖離】**\n\n"
                general_logs += "思考の前提となる基礎データ（3軸の距離）が離れていますが、離れていることそのものは悪いことではありません。\n\n"
                general_logs += "ただし直感的な対話にはノイズが乗りやすいため、感情的な反発を排し、お互いの特性を切り分けた客観的な会話・連絡方法（割り切ったルール設定）による関係性維持が有効です。\n\n"
                general_logs += "他の注意警告がなければ、良好な補完関係である場合もあります。 \n\n"

            # 簡易相性推定
            #-----------------------------------------------------
            # 複数極値の重複検知（競合リスク）
            #-----------------------------------------------------

            # 自身、または比較対象のいずれかが特異な領域（コーナー）に位置する場合
            #            if (abs(row["Y軸"]) > 4.0 and abs(row["Z軸"]) > 4.0) or (abs(target_data["Y軸"]) > 4.0 and abs(target_data["Z軸"]) > 4.0):
            #                alert_logs.append("⚠️ **【空間配置注意】** 固有の強い特性（動機と立脚点の組み合わせ）により、一般的な社会（多数派の環境）や、多くの人との間で意見・利害の競合が予想される座標領域です。お互いの立ち位置を慎重にキャリブレーション（調整）してください。")



            
            # 2. X軸反転（変革vs守護）の検出　（要注意）
            if ((target_data_1x >= STEP_MAX and row_data_1x <= STEP_MIN) or 
                (target_data_1x <= STEP_MIN and row_data_1x >= STEP_MAX)) :
                alert_logs += "【X軸】⚔️ **競合リスク：システム運用の非対称性**\n\n"
                alert_logs += "既存システムの改変・再構築を志向するエネルギーと、伝統・秩序の維持・安定を志向するエネルギーの乖離です。"
                alert_logs += "共同作業では意思決定の手順やルールの扱いを巡る調整に手間取りやすい関係性です。\n\n"

            # 3. Y軸反転（外部接続vs自己完結）の検出　（相性）
            if ((target_data_1y >= STEP_MAX and row_data_1y <= STEP_MIN) or 
                (target_data_1y <= STEP_MIN and row_data_1y >= STEP_MAX)) :
                alert_logs += "【Y軸】⚔️ **競合リスク：対話傾向の不整合**\n\n"
                alert_logs += "外部との柔軟な意見交換・協調を重視する側と、外部からの通信を制限して自己完結的な考え方の側との組み合わせです。"
                alert_logs += "連絡の頻度や、関与の度合いに対する認識のズレ（過干渉または通信遮断）が生じやすい配置です。\n\n"

            # 4. Z軸反転（概念抽象vs生存実利）の検出　（相性）
            if ((target_data_1z >= STEP_MAX and row_data_1z <= STEP_MIN) or 
                (target_data_1z <= STEP_MIN and row_data_1z >= STEP_MAX)):
                alert_logs += "【Z軸】⚔️ **競合リスク：価値基準・立脚点の断絶**\n\n"
                alert_logs += " 抽象的な理念・システム全体の美しさを優先する価値観と、具体的な成果・物理的現実・経済合理性を優先する価値観の衝突です。"
                alert_logs += "目的設定において根本的なすれ違いが発生しやすいため、互いの評価基準を明文化する必要があります。\n\n"

            #-----------------------------------------------------
            # **  AからE 軸の差異分析など
            #-----------------------------------------------------

            # 関係性（友人・夫婦・介護・上司部下など）　敵対者：論外
            # パワーバランス
            # 接触頻度
            # 離脱のしやすさ    親戚、友人→ 合わなければ距離を置ける。　会社→ 転職できる。　夫婦→ 最悪離婚できる。　介護→ 離れられない。
            
            #衝突リスクはこの4つでかなり説明できる気がします。

            #例えば 夫婦 価値観差★★★★ 毎日★★★★★ 離脱★★★
            #↓疲れやすい

            #会社 価値観差★★★★ 毎日★★★★★ 離脱★★
            #↓転職できる

            #親戚 価値観差★★★★★ 年一回★
            #↓問題なし

            #介護 価値観差★★★ 毎日★★★★★ 離脱★★★★★
            #↓ 最も疲れやすい


            #-----------------------------------------------------
            # **  介護モード。
            # 注意点 認知症などになっても、基本的な性格軸の方向性は従来通り。
            # 価値観の違いそのものが負担を生むのではありません。負担が大きくなりやすいのは、一方の価値観を、もう一方が継続的に支え続ける必要がある場合です。
            #-----------------------------------------------------

            judge_level = THRESHOLD
            Judge_hi = judge_level
            Judge_lo = -judge_level
            

            # 介護者が Y−（自己完結） C−（自分で決めたい） だったとします。
            # 一方、介護される側が Y＋（人との関わりを求める） E−（昔の話を繰り返す） だった場合、
            # 介護者は「何度も同じ話をされる」「常に呼ばれる」「自分の時間がない」


            if ((row_data_1y <= Judge_lo and row_data_2c <= Judge_lo and  target_data_1y >= Judge_hi and target_data_2e <= Judge_lo) or
                (target_data_1y <= Judge_lo and target_data_2c <= Judge_lo and  row_data_1y >= Judge_hi and row_data_2e <= Judge_lo)):
                alert_logs += "【Ȳ-C-・Y+E-】⚠️🧑‍🦽 **介護関係の場合**：一方的な依存関係です。介護者は「何度も同じ話をされる」「常に呼ばれる」「自分の時間がない」という状況に陥るかもしれません。\n\n"
                
                

            # ④ Y（自己完結⇔他者依存）
            # 介護者 Y− 「自分でできることはやってほしい。」
            # 被介護者 Y＋ 「ずっと一緒にいて。」
            # 介護者は疲れます。
            # 💎シナジーが起きやすい組み合わせ
            # Y－ × Y＋ 
            # 自立 + 協調
            # 適度なら 非常に良い。
            elif (
                (row_data_1y <= Judge_lo and target_data_1y >= Judge_hi ) or
                (target_data_1y <= Judge_lo and row_data_1y >= Judge_hi )
                ):
                alert_logs += "【Y+↔️Y-】⚠️🧑‍🦽 **介護関係の場合**：一方的な依存関係です。介護者は「自分でできることはやってほしい。」のに「ずっと一緒にいて。」という状況に陥るかもしれません。\n\n"
                synagy_logs += "【Y+↔️Y-】💎 自立+協調の関係です。適度なら 非常に良い組み合わせです。\n\n"

            # ⑤ C（主体性⇔委任）
            # 介護者 C− 「今日はこれをしましょう。」
            # 被介護者 C＋ 「どうすればいい？」
            # これは一見問題ないようで、介護者は「全部決める役」になります。これも疲労します。
            # 💎シナジーが起きやすい組み合わせ
            # C＋ × C－
            # 相談 ＋ 決断
            # 役割分担になります。
            elif (
                (row_data_2c <= Judge_lo and target_data_2c >= Judge_hi ) or
                (target_data_2c <= Judge_lo and row_data_2c >= Judge_hi )
                ):
                alert_logs += "【C+↔️C-】⚠️🧑‍🦽 **介護関係の場合**：一方的な依存関係です。一見問題ないようで、介護者は「全部決める役」という、疲労が溜まる状況に陥るかもしれません。\n\n"
                synagy_logs += "【C+↔️C-】💎主体性+委任の関係です。適度なら相談＋決断の役割分担になります。\n\n"

            # ③ E（未来⇔過去）
            # 介護者 E＋ 「来週デイサービスがあります。」
            # 被介護者 E− 「今日は昭和○年だ。」
            # 未来を前提に話すほど 会話が成立しにくいことがあります。
            # 💎シナジーが起きやすい組み合わせ
            # E＋ × E－
            # 未来 ＋ 過去
            # 長期と経験が融合します。
            
            elif (
                (row_data_2e <= Judge_lo and target_data_2e >= Judge_hi ) or
                (target_data_2e <= Judge_lo and row[AXIS_LABEL2_E  ] >= Judge_hi )
                ):
                alert_logs += "【E+↔️E-】⚠️🧑‍🦽 **介護関係の場合**：一方的な依存関係です。一見問題ないようで、介護者は「全部決める役」という、疲労が溜まる状況に陥るかもしれません。\n\n"
                synagy_logs += "【E+↔️E-】💎未来重視＋過去重視関係です。適度なら長期と経験が融合する良い組み合わせです。\n\n"

            # 両方E-なら昔話で盛り上がります。
            elif (row_data_2e <= Judge_lo and target_data_2e <= Judge_lo ):
                synagy_logs = "【E-↔️E-】💎🦽 **介護関係の場合**：昔話で盛り上がる、よい組み合わせの可能性があります。\n\n"


            # ① X（革新⇔保守）
            # 介護者 X＋ 「新しい介護用品を使おう。」
            # 被介護者 X− 「昔からこれで十分。」
            # これは非常によくあります。
            # 両方 x− なら「昔からのやり方」で一致します。
            # 💎シナジーが起きやすい組み合わせ
            # X＋ × X－
            # 革新 ＋ 保守
            # 適度なら 暴走を止められる。

            if (
                (row_data_1x <= Judge_lo and target_data_1x >= Judge_hi ) or
                (target_data_1x <= Judge_lo and row_data_1x >= Judge_hi )
                ):
                alert_logs += "【X+↔️X-】⚠️🧑‍🦽 **介護関係の場合**：衝突リスクがあります。例えば、介護者「新しい介護用品を使おう。」、被介護者「昔からこれで十分。」というような状況です。\n\n"

                synagy_logs += "【X+↔️X-】💎革新＋保守の関係です。適度ならお互いの暴走を止められます。\n\n"


            # ② Z（抽象⇔具体）
            # 介護者 Z＋ 「今日はリハビリのために歩きましょう。」
            # 被介護者 Z− 「寒い。」
            # 介護者は 「目的」を説明しています。被介護者は 「今」を見ています。ここですれ違います。
            # 両方 Z− なら具体的な話だけで済みます。
            # 💎シナジーが起きやすい組み合わせ
            # Z＋ × Z－
            # 抽象 ＋ 具体
            # 企画と実行になります。


            if (
                (row_data_1z <= Judge_lo and target_data_1z >= Judge_hi ) or
                (target_data_1z <= Judge_lo and row_data_1z >= Judge_hi )
                ):
                alert_logs += "【Z+↔️Z-】⚠️🧑‍🦽 **介護関係の場合**：衝突リスクがあります。例えば、介護者「今日はリハビリのために歩きましょう。」、被介護者「寒い。」というような状況です。"
                alert_logs += "介護者は 「目的」を説明していますが、被介護者は 「今」を見ています。ここですれ違います。\n\n"

                synagy_logs += "【Z+↔️Z-】💎抽象＋具体の関係です。適度なら企画役と実行役の組み合わせになります。\n\n"



            # ⑥ A（神経過敏⇔無頓着）
            # 介護者 A＋ 「床が汚れている。」
            # 被介護者 A− 「そんなこと気にしなくていい。」
            # 掃除だけで 毎日衝突します。
            # 💎シナジーが起きやすい組み合わせ
            # A＋ × A－
            # 慎重 ＋ 大胆
            # リスク管理になります。

            if (
                (row_data_2a <= Judge_lo and target_data_1a >= Judge_hi ) or
                (target_data_1a <= Judge_lo and row_data_2a >= Judge_hi )
                ):
                alert_logs += "【A+↔️A-】⚠️🧑‍🦽 **介護関係の場合**：衝突リスクがあります。例えば、介護者「床が汚れている。」、被介護者「そんなこと気にしなくていい。」という、衝突状況に陥るかもしれません。\n\n"


            # @軸 際の大きさが問題
            # 高い人 気になるもの（－か？）
            # 清潔 整理 品質 見た目
            # 低い人 気になるもの(＋か？）
            # 節約 実用品 思い出 まだ使える
            if (
                (row_data_1a <= Judge_lo and target_data_1a >= Judge_hi ) or
                (target_data_1a <= Judge_lo and row_data_1a >= Judge_hi )
                ):
                alert_logs += "【α+↔️α-】⚠️🧑‍🦽 **介護関係の場合**：衝突リスクがあります。例えば、介護者「清潔 整理 品質 見た目」、被介護者「節約 実用品 思い出 まだ使える」という、衝突状況に陥るかもしれません。\n\n"

            # 「反対側だから疲れる」というより、**「反対側にいる介護者が、毎日“翻訳役”を担うことになると疲れやすい」**という表現の方が、より正確だと思います。
            #  極端同士が問題。
            # 介護では「正しい人」が疲れます。
            # 介護者 A＋ きれい好き 
            # 被介護者 A− 気にしない
            # 毎日 掃除 注意 掃除 注意になります。
            # つまり 価値観が正しいから 疲れる。

            # カサンドラ症候群の問題
            # 介護疲れ  バーンアウト（燃え尽き） 孤立感  抑うつ

            #----------------------
            # 相性推定結果表示
            #----------------------

            if general_logs:
                st.markdown(general_logs)

            if alert_logs:
                st.warning(alert_logs)
            else:
                st.markdown(
                    "🔵 **【標準通信圏内】**\n\n"
                    "決定的な反転・乖離構造はなく、共通のプロトコルによる安定的かつ予測可能なコミュニケーションが維持しやすい関係性です。\n\n"
                )

            if synagy_logs:
                st.success(synagy_logs)

        # end of expander
    # end of for loop over df_final
