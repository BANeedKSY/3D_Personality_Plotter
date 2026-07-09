import streamlit as st
#import streamlit.components.v1 as components
import pandas as pd
import plotly.graph_objects as go
import math
from three_d_plot_constants import DEFALUT_DATA_VERSION, STEP_MAX, STEP_MIN, DEFAULT_PERSONAS
from three_d_plot_constants import GROUPES, AXIS_PREFIX, AXIS_SUFFIX, AXIS_LABELS, AXIS_NAME ,AXIS_DESC ,DATA_LABELS

# "ToDo: "

####################################################################################################################
# ┏━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃　　 ┃　💡見出し、説明エリア　　　　　　　  ┃
# ┃　　 ┣━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┫
# ┃  　 ┃　 　　　３次元プロット　 ┃　　グラデ　┃
# ┃  設 ┃　　　　　　　　　エリア　┃　　エリア　┃
# ┃　定 ┣━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━┫
# ┃  　 ┃　　　相性診断エリア　　　　　　　　　 ┃
# ┗━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

# ==========================================
# 1. アプリケーション初期設定
# ==========================================
st.set_page_config(layout="wide", page_title="3D性格プロッター", page_icon="🌐")

st.title("3D性格プロッター（思考傾向・相性診断システム） 0.08d12/Data:" + DEFALUT_DATA_VERSION)

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
val_html +=  "【目的】人間の思考傾向を「X・Y・Zの3つの次元」で可視化し、ペルソナ間の相性やコミュニケーションエラーを予測するツールです。</br>"
val_html +=  "【注意】思考傾向は気分や体調などで大きく変化します。またその変化傾向も人によって異なりますが、現版では考慮していません。（将来対応のつもりです。）</br>"
val_html +=  "【重要】<stong><A href='https://www.openrail.org/' target='_blank'>OpenRAIL（Open Responsible AI License）</A></stong>として公開しています。</br>"
val_html +=  "<ul style='margin-left: 4em;'>"
val_html +=  "<li><strong><font color='red'>他者の誹謗・中傷用などの悪用利用は厳格にお断りします。</font></strong></li>"
val_html +=  "<li><strong><font color='red'>本版は、まだ開発途中で、十分な動作検証も行っていませんが、学術研究資料として無償で公開しています。</font></strong></li>"
val_html +=  "<li>ご意見等は歓迎いたしますが、ご希望に添えるかなどを含め、お返事はしない場合があります。</li>"
val_html += "</ul>"
val_html += "</p></div>"
st.markdown(val_html, unsafe_allow_html=True)
# 💡 区切り線
st.divider()

##############################################################################################################################
# 定数定義
##############################################################################################################################

# セッション管理用
SESSION_DELETE_CUSTOM = "custom_personas"  ## 設定されていたら、デフォルト内データ内のサンプルカスタム削除


# データ範囲、デフォルトペルソナ・データベースの定義 inport

default_personas = DEFAULT_PERSONAS

# デフォルトデータフレーム化
df_default = pd.DataFrame(default_personas)
# df_default["タイプ"] = "デフォルト"


# 要注意傾向判定関数
def check_conflict(num_x, num_y, num_z):
    # Y軸（動機）とZ軸（立脚点）の歪みだけを検知する
    # Z:-5$（生存実利） × Y:+5$（外部操作） ＝ 他者ハック・搾取セクター（我儘）
    # Z:+5$（極限の抽象） × Y:-5$（自己完結・遮断） ＝ 原理主義セクター（妄信、自己陶酔）
    # X軸は判定から除外。(保守・革新とは関係ない。要注意傾向の人物は左右両方に存在する。)
    if (num_z <= STEP_MIN + 1 and num_y >= STEP_MAX - 1) or (num_z >= STEP_MAX - 1 and num_y <= STEP_MIN + 1):
        return True
    return False


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
    
#    print(  f"DEBUG: step_min={step_min}, step_max={step_max}, "
#            f"num_x={num_x}, num_y={num_y}, num_z={num_z}, color={color}"
#    )
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
    color = f"rgb({int(255 * (1.0 - rate_a))}, {int(128)}, {int(128 * (1.0 - rate_a))})"

#    )
    return color




# ==========================================
# 2. セッション状態（ユーザー定義データ）の管理
# ==========================================
if "custom_personas" not in st.session_state:
    st.session_state.custom_personas = []



####################################################################################################################
# ┏━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃　　 ┃　　 見出し、説明エリア　　　　　　　  ┃
# ┃　💡 ┣━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┫
# ┃  　 ┃　 　　　３次元プロット　 ┃　　グラデ　┃
# ┃  設 ┃　　　　　　　　　エリア　┃　　エリア　┃
# ┃　定 ┣━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━┫
# ┃  　 ┃　　　相性診断エリア　　　　　　　　　 ┃
# ┗━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

# ==========================================
# 3. サイドバー：コントロール層
# ==========================================
st.sidebar.title("🛠️ 設定")

# ② ユーザー定義枠（カスタム追加機能）
with st.sidebar.expander("👤 カスタムペルソナ定義", expanded=False):
    name = st.text_input(
        "ペルソナ名 / ターゲット名", placeholder="例：自分、上司A、企画X"
    )

    st.markdown("**" + AXIS_PREFIX + "X" + AXIS_SUFFIX + ":" + AXIS_NAME["X"]  + "**")
    x_val = st.slider(
        "[" + str(STEP_MIN) + ":" + AXIS_DESC["X"] + ":" + str(STEP_MAX) + "]",
        int(STEP_MIN),
        int(STEP_MAX),
        0,
        1,
        key="slider_x",
    )

    st.markdown("**" + AXIS_PREFIX + "Y" + AXIS_SUFFIX + ":" + AXIS_NAME["Y"]  + "**")
    y_val = st.slider(
        "[" + str(STEP_MIN) + ":" + AXIS_DESC["Y"] + ":" + str(STEP_MAX) + "]",
        int(STEP_MIN),
        int(STEP_MAX),
        0,
        1,
        key="slider_y",
    )

    st.markdown("**" + AXIS_PREFIX + "Z" + AXIS_SUFFIX + ":" + AXIS_NAME["Z"]  + "**")
    z_val = st.slider(
        "[" + str(STEP_MIN) + ":" + AXIS_DESC["Z"] + ":" + str(STEP_MAX) + "]",
        int(STEP_MIN),
        int(STEP_MAX),
        0,
        1,
        key="slider_z",
    )

    st.markdown("**" + AXIS_PREFIX + "a" + AXIS_SUFFIX + ":" + AXIS_NAME["a"]  + "**")
    alfa_val = st.slider(
        "[" + str(STEP_MIN) + ":" + AXIS_DESC["a"] + ":" + str(STEP_MAX) + "]",
        int(STEP_MIN),
        int(STEP_MAX),
        0,
        1,
        key="slider_alfa",
    )

    desc = st.text_area(
        "説明（特徴や行動特性など）",
        placeholder="ターゲットの性格や行動の特徴に関するメモ",
    )

    submit_button = st.button(label="空間へプロット追加")

# フォーム送信時の処理
if submit_button:
    if not name.strip():
        st.sidebar.error("⚠️ 名前を入力してください。")
    else:
        new_persona = {
            DATA_LABELS["GRP"]: GROUPES["CST"],
            DATA_LABELS["NAM"]: name.strip(),
            AXIS_LABELS["X"]: x_val,
            AXIS_LABELS["Y"]: y_val,
            AXIS_LABELS["Z"]: z_val,
            AXIS_LABELS["a"]: alfa_val,
            AXIS_LABELS["A"]: 0,
            AXIS_LABELS["B"]: 0,
            AXIS_LABELS["C"]: 0,
            AXIS_LABELS["D"]: 0,
            AXIS_LABELS["E"]: 0,
            DATA_LABELS["DSC"]: desc.strip()
                if desc.strip()
                else "ユーザーが定義したカスタムペルソナです。",
            DATA_LABELS["CAT"]: "カスタムカテゴリ",
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
    df_all = pd.concat([df_default, df_custom], ignore_index=True)
else:
    df_all = df_default.copy()


# ==========================================
# 【新規追加】① グループ選択メニュー（1次フィルタリング）
# ==========================================
st.sidebar.write("---")
st.sidebar.header("📁 グループの絞り込み")

# 存在するユニークなグループ名の一覧を取得
available_groups = df_all[DATA_LABELS["GRP"]].unique().tolist()

# マルチセレクトでグループを選択（初期値はすべてのグループを選択状態に）
selected_groups = st.sidebar.multiselect(
    "表示するグループを選択:", options=available_groups, default=available_groups
)

# 選択されたグループのデータだけに絞り込む（1次抽出）
df_group_filtered = df_all[df_all[DATA_LABELS["GRP"]].isin(selected_groups)]

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
        # row[DATA_LABELS['NAM']], value=select_all, key=f"cb_{row[DATA_LABELS['NAM']]}_{idx}_{row[DATA_LABELS['GRP']]}"
        row[DATA_LABELS['GRP']] + "-" + row[DATA_LABELS['NAM']], value=select_all, key=f"cb_{row[DATA_LABELS['NAM']]}_{idx}_{row[DATA_LABELS['GRP']]}"
    ):
        selected_names.append(row[DATA_LABELS['NAM']])

# 最終的に3Dプロットに渡すデータ（最終抽出）
df_pre_final = df_group_filtered[df_group_filtered[DATA_LABELS['NAM']].isin(selected_names)]

# マーカーにXYZ,a属性に応じた色をする設定する
df_final = df_pre_final.copy()  # コピーを作成
if not df_final.empty:
    df_final["color"] = df_final.apply(
        lambda row: generate_personality_color(
            STEP_MIN,
            STEP_MAX,
            row[AXIS_LABELS["X"]],
            row[AXIS_LABELS["Y"]],
            row[AXIS_LABELS["Z"]],
        ),
        axis=1
    )
    
    df_final["color_e"] = df_final.apply(
        lambda row: generate_emotionality_color(
            STEP_MIN,
            STEP_MAX,
            row[AXIS_LABELS["a"]],
        ),
        axis=1
    )
    
    
### print("DEBUG colors:", df_final["color"].tolist())


####################################################################################################################

# ==========================================
# 4. メインレイアウト層
# ==========================================

fig = go.Figure()

# 💡 グラフエリア(5) と 右側インジケーター：グラデエリア (1) の比率で横並びに分割します
plot_col, grade_col = st.columns([5, 1], gap="small")


# --- 左側：③ Plotlyを用いた3D散布図 ---

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
    st.subheader("🌐 3D性格プロット － 性格・思考傾向分布把握用")

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
                line=dict(color="rgba(128,255,255,0.2)", width=3),
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
                line=dict(color="rgba(255,128,255,0.2)", width=3),
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
                line=dict(color="rgba(255,255,128,0.2)", width=3),
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
                        x=group_df[AXIS_LABELS["X"]],
                        y=group_df[AXIS_LABELS["Y"]],
                        z=group_df[AXIS_LABELS["Z"]],
                        mode="text",
                        name=group_name,  # 凡例にグループ名が表示されます
                        text=group_df[DATA_LABELS["NAM"]],
                        hoverinfo="skip",
                        showlegend=False,                   # 凡例非表示 
                    )
                )

                # ペルソナのプロット（ぶりつぶし色は属性を反映）
                if df_draw_type != GROUPES["CST"]:
                    # shadow_color='lightgray'            # 規定ペルソナは背景円示の色を薄い灰色にしてデフォルトペルソナを目立たせない
                    shadow_shape = 'circle'
                else:
                    # shadow_color='rgb(255,160,160)'     # カスタムペルソナは背景円示の色を薄赤にしてカスタムペルソナを強調
                    shadow_shape = 'square'
                
                # ①　マーカーの背景を描画                 # 枠線を太くして背景円を表示する    

                # DEBUG  print(df_draw.head())
                
                fig.add_trace(go.Scatter3d(

                    x=df_draw[AXIS_LABELS["X"]],
                    y=df_draw[AXIS_LABELS["Y"]],
                    z=df_draw[AXIS_LABELS["Z"]],
                    
                    text=group_df[DATA_LABELS["NAM"]],
                    #mode='markers+text',               # 名前も表示する場合は 'markers+text' に変更
                    mode='markers',                     # 名前も表示する場合は 'markers+text' に変更
                    
                    marker=dict(
                        line=dict(width=0),             # 背景の枠線幅は０
                        symbol=shadow_shape,
                        #symbol='diamond',
                        size=6,
#                        color=generate_emotionality_color(STEP_MIN, STEP_MAX, f"{AXIS_NAME['Z']}"),
#                        color=generate_emotionality_color(STEP_MIN, STEP_MAX, df_draw[AXIS_LABELS['a']]),
                        color=df_draw["color_e"],
                        opacity=0.7                     # 薄く透けさせる
                    ),
                    hoverinfo='skip',                   # ホバー情報は表示しない
                    name=df_draw_type,
                    showlegend=not legend_state,        # 背景円を凡例として表状　 非表示だったら表示 
                ))
                
                # ② その上にマーカーを所定の外形でクッキリ描画

                fig.add_trace(go.Scatter3d(
                    x=df_draw[AXIS_LABELS["X"]],
                    y=df_draw[AXIS_LABELS["Y"]],
                    z=df_draw[AXIS_LABELS["Z"]],
                    #a=df_draw[AXIS_LABELS["a"]],

                    # mode='markers+text',              # 名前も表示する場合は 'markers+text' に変更
                    # mode='none',                      # 名前、マーカーも表示しない場合は 'none' に変更
                    # mode='markers',                   # 名前は出さずマーカーだけにする
                    mode='markers',                     # 名前は出さずマーカーだけにする

                    marker=dict(
                        line=dict(width=0),             # マーカー字体は輪郭線非表示
                        ###### 外形選択枝 #####
                        # ['circle', 'circle-open', 'cross', 'diamond',
                        #  'diamond-open', 'square', 'square-open', 'x']
                        # symbol="cross",               # ＋ 塗りつぶしなし　背景に円がつく。
                        symbol='square',                # 🔳 ■        背景に円がつく。
                        # symbol='diamond',             # 🔶 ひし形 　背景に円がつく。
                        # symbol='circle',              # 🔴 円
                        size=4,
                        color=df_draw["color"],         # 予め計算しておいた色を設定
                        opacity=1.0
                    ),

                    # 吹き出し
                    hovertemplate = (
                        f"<b>%{{customdata[0]}}</b><br>"
                        f"%{{customdata[1]}} %{{customdata[2]}}<br>"
                        f"X ({AXIS_NAME['X']}): %{{x}}<br>"
                        f"Y ({AXIS_NAME['Y']}): %{{y}}<br>"
                        f"Z ({AXIS_NAME['Z']}): %{{z}}<br>"
                        f"α ({AXIS_NAME['a']}): %{{customdata[3]}}<br>"
                        f"{DATA_LABELS['DSC']}:<br>%{{customdata[4]}}"
                    ), 
                    customdata=df_draw[[DATA_LABELS["NAM"], DATA_LABELS["GRP"], DATA_LABELS["CAT"], AXIS_LABELS["a"],
                                        DATA_LABELS["DSC"]]],

                    name=df_draw_type,
                    showlegend=False,                   # 凡例非表示 
                ))
        
        legend_displayed_flag = False  # 凡例表示のフラグ初期値を False に設定
        
        for group_name, group_df in df_final.groupby("グループ"):


# df_draw[DATA_LABELS["DSC"] + "_formatted"] = df_draw[DATA_LABELS["DSC"]].str.replace("。", "。<br>")
# customdata=df_draw[[DATA_LABELS["NAM"], ..., DATA_LABELS["DSC"] + "_formatted"]]


            # A. デフォルトペルソナ(グループが、カスタム以外)のプロット
            draw_3d_markers(fig, 
#                            df_final[df_final[DATA_LABELS["GRP"]] != GROUPES["CST"]].copy(),

                            df_final[df_final[DATA_LABELS["GRP"]] != GROUPES["CST"]].replace(r"\n","<br>", regex=True).copy(),


                            GROUPES["DEF"],
                            legend_displayed_flag)

            # B. カスタムペルソナ(グループが、カスタム)のプロット

            draw_3d_markers(fig, 
                            df_final[df_final[DATA_LABELS["GRP"]] == GROUPES["CST"]].replace(r"\n","<br>", regex=True).copy(),
                            GROUPES["CST"],
                            legend_displayed_flag)

            legend_displayed_flag = True  # 凡例表示済みフラグを True に設定

        # end of for group_name, group_df in df_final.groupby("グループ"):
        # ------------------------------------------------------------------------------------------------
        
        # 空間レイアウトの最適化 （軸の説明追加など）
        fig.update_layout(
            template="plotly_dark",     #
            # プロットエリア縦幅
            # 👇 ここを追加！縦幅を 800ピクセル（好みに合わせて900などでも可）に引き上げ
            height=800,
            
            # 3軸の説明
            # 👇 ここを追加！上下左右の無駄な余白（マージン）をゼロに削ってエリアを最大化
            margin=dict(l=0, r=0, b=0, t=30),
            scene=dict(
                xaxis=dict(
                    title=AXIS_LABELS["X"] + ":" + AXIS_NAME["X"] + "(" + AXIS_DESC["X"] + ")",
                    range=[STEP_MIN - 0.5, STEP_MAX + 0.5],
                    gridcolor="rgba(128,128,128,0.2)",
                ),
                yaxis=dict(
                    title=AXIS_LABELS["Y"] + ":" + AXIS_NAME["Y"] + "(" + AXIS_DESC["Y"] + ")",
                    range=[STEP_MIN - 0.5, STEP_MAX + 0.5],
                    gridcolor="rgba(128,128,128,0.2)",
                ),
                zaxis=dict(
                    title=AXIS_LABELS["Z"] + ":" + AXIS_NAME["Z"] + "(" + AXIS_DESC["Z"] + ")",
                    range=[STEP_MIN - 0.5, STEP_MAX + 0.5],
                    gridcolor="rgba(128,128,128,0.2)",
                ),
                aspectmode="cube",  # 立方体の枠線を固定
            ),
            # ToDo: 凡例の表示方法を検討中。現在、重複表示される.また、背景もtrace n のように表示される
            # ペルソナ凡例の位置を左上に固定（右側のグラデエリアと重ならないように）
            legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
        
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
        "<div style='text-align: center; font-weight: bold; margin-bottom: 10px;'>📊XYZ軸／α軸 表示色</div>",
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
            "<div style='text-align: center; font-size: 11px; font-weight: bold; color: #555555;'>" + DATA_LABELS["VAL"] + "</div>",
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
            "<div style='text-align: center; font-size: 11px; font-weight: bold; color: #008B8B;'>" + AXIS_LABELS["X"] + "</div>",
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
            "<div style='text-align: center; font-size: 11px; font-weight: bold; color: #8B008B;'>" + AXIS_LABELS["Y"] + "</div>",
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
            "<div style='text-align: center; font-size: 11px; font-weight: bold; color: #8B8B00;'>" + AXIS_LABELS["Z"] + "</div>",
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
            "<div style='text-align: center; font-size: 11px; font-weight: bold; color: #8B8B00;'>" + AXIS_LABELS["a"] + "</div>",
            unsafe_allow_html=True,
        )
        a_html = "<div style='display: flex; flex-direction: column; gap: 4px; align-items: center;'>"
        for v in steps_reverse:
            color = generate_emotionality_color(STEP_MIN, STEP_MAX, v)  # a軸の値に基づく色を生成
            a_html += f"<div style='background-color:{color}; border:1px solid #B0BEC5; {block_style}'></div>"
        a_html += "</div>"
        st.markdown(a_html, unsafe_allow_html=True)


####################################################################################################################

# 💡 プロットエリア全体のすぐ下に区切り線
st.divider()

####################################################################################################################
# --- 左側：③ Plotlyを用いた3D散布図 ---
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

st.subheader("💥 衝突判定＆相性診断 💕")

if not st.session_state.custom_personas:
    st.info(
        "💡 左側のサイドバーから「カスタムペルソナ」を登録すると、既存データベースや他のカスタムデータとの距離測定・相性バグの予測自動シミュレーションがここに展開されます。"
    )
else:
    # ユーザー定義ペルソナからベースを選択
    custom_names = [p["名前"] for p in st.session_state.custom_personas]
    target_name = st.selectbox("診断の基準軸にするペルソナを選択:", custom_names)

    # ターゲット対象のデータ取得
    target_data = next(
        p for p in st.session_state.custom_personas if p[DATA_LABELS["NAM"]] == target_name
    )

    st.markdown(f"### 🎯 「{target_name}」の相性診断レポート")
    st.write(
        f"**現在座標**: X: {target_data[AXIS_LABELS['X']]} / Y: {target_data[AXIS_LABELS['Y']]} / Z: {target_data[AXIS_LABELS['Z']]}"
    )
    # ToDo # st.caption(f"プロファイル情報: {target_data[DATA_LABELS["DSC"]]}")

    # ユーザー定義ペルソナの要注意判定
    if check_conflict(target_data[AXIS_LABELS["X"]], target_data[AXIS_LABELS["Y"]], target_data[AXIS_LABELS["Z"]]):
        st.warning(
            "⚠️ **【注意】** 強い個性の組み合わせ。一般的な社会（多数派前提の環境）や、多くの人との意見・利害の対立が予想される。"
        )
    st.write("---")

    st.write("#### 🔍 各ペルソナとの相性シミュレーション")

    # 選択されたペルソナと他の全ペルソナを比較
    for idx, row in df_all.iterrows():
        # 自分自身（同じ名前かつ同じタイプ）との比較はスキップ
        if row[DATA_LABELS["NAM"]] == target_name and row[DATA_LABELS["GRP"]] == GROUPES["CST"]:
            continue

        # 1. 3次元ユークリッド距離の計算
        dist = math.sqrt(
            (target_data[AXIS_LABELS["X"]] - row[AXIS_LABELS["X"]]) ** 2
            + (target_data[AXIS_LABELS["Y"]] - row[AXIS_LABELS["Y"]]) ** 2
            + (target_data[AXIS_LABELS["Z"]] - row[AXIS_LABELS["Z"]]) ** 2
        )

        # バグ・相性判定配列の生成
        alert_logs = []

        # 【新規追加】複数極値の重複検知（多くの人との競合リスク）
        # 自身、または比較対象のいずれかが特異な領域（コーナー）に位置する場合
        #            if (abs(row["Y軸"]) >= 4.0 and abs(row["Z軸"]) >= 4.0) or (abs(target_data["Y軸"]) >= 4.0 and abs(target_data["Z軸"]) >= 4.0):
        #                alert_logs.append("⚠️ **【空間配置注意】** 固有の強い特性（動機と立脚点の組み合わせ）により、一般的な社会（多数派の環境）や、多くの人との間で意見・利害の競合が予想される座標領域です。お互いの立ち位置を慎重にキャリブレーション（調整）してください。")

        if check_conflict(target_data[AXIS_LABELS["X"]], target_data[AXIS_LABELS["Y"]], target_data[AXIS_LABELS["Z"]]):
            alert_logs.append(
                "⚠️ **【注意】** 強い個性の組み合わせ。一般的な社会（多数派前提の環境）や、多くの人との意見・利害の対立が予想される。"
            )

        # 距離基準の判定
        if dist < 2.0:
            alert_logs.append(
                "🟢 **【思考OSの近接】** 思考アルゴリズムの親和性が非常に高い配置です。非言語的な相互理解が期待できる一方、課題や死角（短所）も共通化しやすいため、補完関係というよりは同質的な共鳴としてのバランスに留意が必要です。"
            )
        elif dist >= 7.0:
            alert_logs.append(
                "🌐 **【独立プロトコル】** 思考の前提となる基礎コード（3軸の距離）が大きく離れています。直感的な通信にはノイズが乗りやすいため、感情的な反発を排し、お互いの特性を切り分けた客観的なプロトコル（割り切ったルール設定）による接続が有効です。"
            )

        # 2. X軸反転（変革vs守護）の検出
        if (target_data[AXIS_LABELS["X"]] >= 4.0 and row[AXIS_LABELS["X"]] <= -4.0) or (
            target_data[AXIS_LABELS["X"]] <= -4.0 and row[AXIS_LABELS["X"]] >= 4.0
        ):
            alert_logs.append(
                "⚔️ **【X軸：システム運用の非対称性】** 既存システムの改変・再構築を志向するエネルギーと、伝統・秩序の維持・安定を志向するエネルギーの乖離です。共同作業において、意思決定の手順やルールの扱いを巡る調整コストが高まりやすい関係性です。"
            )

        # 3. Y軸反転（外部接続vs自己完結）の検出
        if (target_data[AXIS_LABELS["Y"]] >= 4.0 and row[AXIS_LABELS["Y"]] <= -4.0) or (
            target_data[AXIS_LABELS["Y"]] <= -4.0 and row[AXIS_LABELS["Y"]] >= 4.0
        ):
            alert_logs.append(
                "📡 **【Y軸：通信プロトコルの不整合】** 外部との柔軟なパケット交換・協調を重視する側と、外部からの通信を制限して自己完結的に稼働する側の対比です。連絡の頻度や、関与の度合いに対する認識のズレ（過干渉または通信遮断）が生じやすい配置です。"
            )

        # 4. Z軸反転（概念抽象vs生存実利）の検出
        if (target_data[AXIS_LABELS["Z"]] >= 4.0 and row[AXIS_LABELS["Z"]] <= -4.0) or (
            target_data[AXIS_LABELS["Z"]] <= -4.0 and row[AXIS_LABELS["Z"]] >= 4.0
        ):
            alert_logs.append(
                "💎 **【Z軸：価値基準・立脚点の断絶】** 抽象的な理念・システム全体の美しさを優先する思考OSと、具体的な成果・物理的現実・経済合理性を優先する思考OSの衝突です。目的設定において根本的なすれ違いが発生しやすいため、互いの評価基準を明文化する必要があります。"
            )

        # アコーディオンパネルで綺麗に出力
        # ToDo: グループのアイコン変更？
        icon = "🦊" if row[DATA_LABELS["GRP"]] == GROUPES["CST"] else "👤"
        with st.expander(f"{icon} {row[DATA_LABELS['NAM']]}（空間距離: {dist:.2f}）"):
            #
            st.write(
            #    f"**システム座標**: X:{row['X軸']} / Y:{row['Y軸']} / Z:{row['Z軸']} ({row['カテゴリ']})"
                f"**システム座標**: X:{row[AXIS_LABELS['X']]} / Y:{row[AXIS_LABELS['Y']]} / Z:{row[AXIS_LABELS['Z']]} ({row[DATA_LABELS['CAT']]})"
            )
            st.markdown(f"*特性記述*: {row[DATA_LABELS['DSC']]}")
            st.write("---")

            if alert_logs:
                for log in alert_logs:
                    st.write(log)
            else:
                st.write(
                    "🔵 **【標準通信圏内】** 決定的な反転・乖離構造はなく、共通のプロトコルによる安定的かつ予測可能なコミュニケーションが維持しやすい関係性です。"
                )
