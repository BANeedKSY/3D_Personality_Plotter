import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import math

# ==========================================
# 1. アプリケーション初期設定
# ==========================================
st.set_page_config(layout="wide", page_title="3D性格プロッター", page_icon="🌐")

st.title("3軸人間性プロッター（思考OS・相性診断システム） 0.03d")
st.write("人間の思考傾向を「X・Y・Zの3つの次元」で可視化し、ペルソナ間の相性やコミュニケーションエラーを予測するツールです。")

# デフォルトペルソナ・データベースの定義
default_personas = [
 # --- 動物グループ ---
    {"グループ": "動物", "名前": "女王蜂", "カテゴリ": "動物（象徴）", "X軸": -5.0, "Y軸": 5.0, "Z軸": 5.0, "説明": "存在そのものがシステムを統合する、究極の象徴（記号）生命体。"},
    {"グループ": "動物", "名前": "ボス猿", "カテゴリ": "動物（極限）", "X軸": -4.0, "Y軸": 5.0, "Z軸": 5.0, "説明": "利権にしがみつき、派閥工作で群れを統治する老ボス。"},
    {"グループ": "動物", "名前": "ライオン", "カテゴリ": "動物（極限）", "X軸": 5.0, "Y軸": -4.0, "Z軸": -5.0, "説明": "弱肉強食で圧倒的なパワーにより既存の群れを乗っ取る絶対的捕食者。"},   
    {"グループ": "動物", "名前": "一匹狼", "カテゴリ": "動物（極限）", "X軸": 5.0, "Y軸": -5.0, "Z軸": 5.0, "説明": "外部を完全遮断し、独自の掟（美学）のみで荒野を走る孤高の狂信者。"},
    {"グループ": "動物", "名前": "キツネ", "カテゴリ": "動物（日常）", "X軸": 2.0, "Y軸": 3.0, "Z軸": -3.0, "説明": "既存ルールの隙間を突き、要領の良さと知略で立ち回る策士型ハッカー。"},
    {"グループ": "動物", "名前": "ノラネコ", "カテゴリ": "動物（日常）", "X軸": 0.0, "Y軸": -5.0, "Z軸": -5.0, "説明": "他人に興味ゼロ。100%自分のペースと今ここの快適さを極める自由人。"},
    {"グループ": "動物", "名前": "飼いイヌ", "カテゴリ": "動物（日常）", "X軸": -4.0, "Y軸": 5.0, "Z軸": -2.0, "説明": "圧倒的なロイヤリティ（忠誠心）と絆でチームを支える最高のフォロワー。"},
    {"グループ": "動物", "名前": "タヌキ", "カテゴリ": "動物（日常）", "X軸": -2.0, "Y軸": 2.0, "Z軸": -4.0, "説明": "愛嬌とトボけ（狸寝入り）を使い、面倒な仕事や組織の嵐をやり過ごす世渡り上手。"},
# --- 芸能人グループ ---
    {"グループ": "芸能人", "名前": "大御所司会者", "カテゴリ": "タレント", "X軸": 4.0, "Y軸": 3.0, "Z軸": 2.0, "説明": "圧倒的な場番回しと権力でスタジオの空気を支配する。"},
    {"グループ": "芸能人", "名前": "ひな壇芸人", "カテゴリ": "芸人", "X軸": -2.0, "Y軸": -3.0, "Z軸": 4.0, "説明": "空気を機敏に察知し、求められた役割を完璧にこなして場を盛り上げる。"},
    {"グループ": "芸能人", "名前": "正統派俳優", "カテゴリ": "役者", "X軸": 1.0, "Y軸": 2.0, "Z軸": -3.0, "説明": "自己の軸を強く持ちながら、作品の世界観にストイックに没入する。"}
]

# データフレーム化と識別用タイプの付与
df_default = pd.DataFrame(default_personas)
df_default["タイプ"] = "デフォルト"

# ==========================================
# 2. セッション状態（ユーザー定義データ）の管理
# ==========================================
if "custom_personas" not in st.session_state:
    st.session_state.custom_personas = []

# ==========================================
# 3. サイドバー：コントロール層
# ==========================================
st.sidebar.title("🛠️ コントロールパネル")

# ② ユーザー定義枠（カスタム追加機能）
st.sidebar.header("👤 カスタムペルソナの追加")
# with st.sidebar.form(key="add_persona_form", clear_on_submit=True):
with st.sidebar.form(key="add_persona_form", clear_on_submit=False):
    name = st.text_input("ペルソナ名 / ターゲット名", placeholder="例：自分、上司A、プロジェクトX")
    
    st.markdown("**X軸：システム（ルールへのスタンス）**")
#    x_val = st.slider("[-5:保守・規律・秩序維持 ↔ +5:変革・破壊・ルールメイク]", -5.0, 5.0, 0.0, 1.0, key="slider_x")
    x_val = st.slider("[-5:保守・秩序維持 ↔ +5:変革・破壊・ルールメイク]", -5.0, 5.0, 0.0, 1.0, key="slider_x")
    
    st.markdown("**Y軸：動機（エネルギーの方向性）**")
    y_val = st.slider("[-5:自己完結・孤高 ↔ +5:外部接続・共感・全体調和]", -5.0, 5.0, 0.0, 1.0, key="slider_y")
    
    st.markdown("**Z軸：立脚点（価値基準）**")
#    z_val = st.slider("[-5:泥臭い実利・成果 ↔ +5:抽象大義・精神・理念]", -5.0, 5.0, 0.0, 1.0, key="slider_z")
    z_val = st.slider("[-5:分かりやすさ・成果 ↔ +5:正確さ・精神・理念]", -5.0, 5.0, 0.0, 1.0, key="slider_z")
   
    desc = st.text_area("説明（特徴や行動特性など）", placeholder="ターゲットの性格やプロトコルに関するメモ")
    
    submit_button = st.form_submit_button(label="空間へプロット追加")

# フォーム送信時の処理
if submit_button:
    if not name.strip():
        st.sidebar.error("⚠️ 名前を入力してください。")
    else:
        new_persona = {
            "名前": name.strip(),
            "カテゴリ": "カスタム",
            "X軸": x_val,
            "Y軸": y_val,
            "Z軸": z_val,
            "説明": desc.strip() if desc.strip() else "ユーザーが定義したカスタムペルソナです。",
            "タイプ": "カスタム"
        }
        st.session_state.custom_personas.append(new_persona)
        st.sidebar.success(f"🎉 「{name}」をプロット空間に登録しました！")

# カスタムペルソナのリセット機能
if st.sidebar.button("🗑️ カスタムペルソナを全消去"):
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
available_groups = df_all["グループ"].unique().tolist()

# マルチセレクトでグループを選択（初期値はすべてのグループを選択状態に）
selected_groups = st.sidebar.multiselect(
    "表示するグループを選択:",
    options=available_groups,
    default=available_groups
)

# 選択されたグループのデータだけに絞り込む（1次抽出）
df_group_filtered = df_all[df_all["グループ"].isin(selected_groups)]

# ==========================================
# 【修正】② 動的凡例チェックボックス（2次フィルタリング）
# ==========================================
st.sidebar.write("---")
st.sidebar.header("👁️ 個別ペルソナの表示切り替え")

# 絞り込まれたグループの中での全選択 / 全解除
select_all = st.sidebar.checkbox("グループ内のすべての対象を表示", value=True)

selected_names = []
# ループ対象を df_all から 「df_group_filtered」 に変更します
for idx, row in df_group_filtered.iterrows():
    # 選択されているグループのペルソナだけがここにチェックボックスとして並びます
    if st.sidebar.checkbox(row["名前"], value=select_all, key=f"cb_{row['名前']}_{idx}_{row['グループ']}"):
        selected_names.append(row["名前"])

# 最終的に3Dプロットに渡すデータ（最終抽出）
df_final = df_group_filtered[df_group_filtered["名前"].isin(selected_names)]



# ==========================================
# 4. メインレイアウト層
# ==========================================
col1, col2 = st.columns([3, 2])

# ------------------------------------------
# 左側カラム：③ Plotlyを用いた3D散布図
# ------------------------------------------
with col1:
    st.subheader("🌐 3D思考OS空間プロット")
    
#    if df_filtered.empty:
    if df_final.empty:

        st.warning("⚠️ 左側のサイドバーで対象を1つ以上選択してください。プロット空間が空集合（Empty）です。")
    else:
        fig = go.Figure()

        for group_name, group_df in df_final.groupby("グループ"):
            fig.add_trace(go.Scatter3d(
                x=group_df["X軸"],
                y=group_df["Y軸"],
                z=group_df["Z軸"],
                mode="markers+text",
                name=group_name, # 凡例にグループ名が表示されます
                text=group_df["名前"],
                hoverinfo="text"
            ))

        # 中心（0, 0, 0）のガイドライン（ゼロ線）を補助的に描画
        fig.add_trace(go.Scatter3d(x=[-5, 5], y=[0, 0], z=[0, 0], mode='lines', line=dict(color='rgba(255,255,255,0.3)', width=3), showlegend=False, hoverinfo='skip'))
        fig.add_trace(go.Scatter3d(x=[0, 0], y=[-5, 5], z=[0, 0], mode='lines', line=dict(color='rgba(255,255,255,0.3)', width=3), showlegend=False, hoverinfo='skip'))
        fig.add_trace(go.Scatter3d(x=[0, 0], y=[0, 0], z=[-5, 5], mode='lines', line=dict(color='rgba(255,255,255,0.3)', width=3), showlegend=False, hoverinfo='skip'))

        # A. デフォルトペルソナのプロット（丸型・グラデーション表示）
  #      df_f_default = df_filtered[df_filtered["タイプ"] == "デフォルト"]
        df_f_default = df_final[df_final["タイプ"] == "デフォルト"]
        if not df_f_default.empty:
            fig.add_trace(go.Scatter3d(
                x=df_f_default["X軸"],
                y=df_f_default["Y軸"],
                z=df_f_default["Z軸"],
                mode='markers+text',
                text=df_f_default["名前"],
                textposition="top center",
                marker=dict(
                    size=7,
                    color=df_f_default["Z軸"],  # Z軸の数値で色分け
                    colorscale='Viridis',
                    colorbar=dict(title="Z軸 (立脚点)", x=1.05),
                    symbol='circle',
                    line=dict(color='white', width=1)
                ),
                hovertemplate="<b>%{text}</b><br>カテゴリ: %{customdata[0]}<br>X (システム): %{x}<br>Y (動機): %{y}<br>Z (立脚点): %{z}<br>説明: %{customdata[1]}<extra></extra>",
                customdata=df_f_default[["カテゴリ", "説明"]],
                name="既存ペルソナ"
            ))

        # B. カスタムペルソナのプロット（星型・独立カラーで明確に視覚的区別）
#        df_f_custom = df_filtered[df_filtered["タイプ"] == "カスタム"]
        df_f_custom = df_final[df_final["タイプ"] == "カスタム"]
        if not df_f_custom.empty:
            fig.add_trace(go.Scatter3d(
                x=df_f_custom["X軸"],
                y=df_f_custom["Y軸"],
                z=df_f_custom["Z軸"],
                mode='markers+text',
                text=df_f_custom["名前"],
                textposition="top center",
                marker=dict(
                    size=12,
                    color='#FF4B4B',  # 強調用のカスタムカラー（赤）
#                    symbol='star',
                    symbol='circle',
                    line=dict(color='white', width=1)
                ),
                hovertemplate="<b>%{text}</b><br>カテゴリ: カスタム<br>X (システム): %{x}<br>Y (動機): %{y}<br>Z (立脚点): %{z}<br>説明: %{customdata[0]}<extra></extra>",
                customdata=df_f_custom[["説明"]],
                name="カスタムペルソナ"
            ))

        # 空間レイアウトの最適化（スタイリッシュなダークモードに適合）
        fig.update_layout(
            template='plotly_dark',
            # 👇 ここを追加！縦幅を 800ピクセル（好みに合わせて900などでも可）に引き上げ
            height=800, 
            # 👇 ここを追加！上下左右の無駄な余白（マージン）をゼロに削ってエリアを最大化
            margin=dict(l=0, r=0, b=0, t=30), 
            scene=dict(
                xaxis=dict(title='X: システム (保守 ↔ 変革)', range=[-5.5, 5.5], gridcolor='rgba(128,128,128,0.2)'),
                yaxis=dict(title='Y: 動機 (自己完結 ↔ 外部接続)', range=[-5.5, 5.5], gridcolor='rgba(128,128,128,0.2)'),
                zaxis=dict(title='Z: 立脚点 (実利 ↔ 抽象大義)', range=[-5.5, 5.5], gridcolor='rgba(128,128,128,0.2)'),
                aspectmode='cube' # 立方体の枠線を固定
            ),
#            margin=dict(l=0, r=0, b=0, t=30),
            legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
        )
        st.plotly_chart(fig, width='stretch')

# ------------------------------------------
# 右側カラム：④ 衝突判定アルゴリズム（相性診断）
# ------------------------------------------
with col2:
    st.subheader("💥 衝突判定＆相性診断")
    
    if not st.session_state.custom_personas:
        st.info("💡 左側のサイドバーから「カスタムペルソナ」を登録すると、既存データベースや他のカスタムデータとの距離測定・相性バグの予測自動シミュレーションがここに展開されます。")
    else:
        # ユーザー定義ペルソナからベースを選択
        custom_names = [p["名前"] for p in st.session_state.custom_personas]
        target_name = st.selectbox("診断の基準軸にするペルソナを選択:", custom_names)
        
        # ターゲット対象のデータ取得
        target_data = next(p for p in st.session_state.custom_personas if p["名前"] == target_name)
        
        st.markdown(f"### 🎯 「{target_name}」の相性診断レポート")
        st.write(f"**現在座標**: X: {target_data['X軸']} / Y: {target_data['Y軸']} / Z: {target_data['Z軸']}")
        st.caption(f"プロファイル情報: {target_data['説明']}")
        st.write("---")
        
        st.write("#### 🔍 各ペルソナとの通信シミュレーション")
        
        # 選択されたペルソナと他の全ペルソナを比較
        for idx, row in df_all.iterrows():
            # 自分自身（同じ名前かつ同じタイプ）との比較はスキップ
            if row["名前"] == target_name and row["タイプ"] == "カスタム":
                continue
                
            # 1. 3次元ユークリッド距離の計算
            dist = math.sqrt(
                (target_data["X軸"] - row["X軸"]) ** 2 +
                (target_data["Y軸"] - row["Y軸"]) ** 2 +
                (target_data["Z軸"] - row["Z軸"]) ** 2
            )
            
            # バグ・相性判定配列の生成
            alert_logs = []
            
            # 距離基準の判定
 #           if dist < 2.0:
 #               alert_logs.append("🟢 **【思考OS酷似】** 思考アルゴリズムがほぼ同一です。言葉を尽くさずとも理解し合える最高の相性ですが、互いの短所も鏡写しになるため「同族嫌悪」のループに注意してください。")
 #           elif dist >= 7.0:
 #               alert_logs.append("👽 **【宇宙人レベル】** 根本的な前提コードが違いすぎて、お互いの意図が全く翻訳できません。普通に話すと致命的なバグが起きるため、割り切ったプロトコル接続が必要です。")
            
            # 2. X軸反転（変革vs守護）の検出
 #           if (target_data["X軸"] >= 4.0 and row["X軸"] <= -4.0) or (target_data["X軸"] <= -4.0 and row["X軸"] >= 4.0):
 #               alert_logs.append("⚔️ **【X軸バグ：システム衝突】** ルールを破壊して新システムを作りたい変革者と、既存の秩序・規律を死守したい守護者の正面衝突。真っ向からの権力闘争が勃発しやすいアーキテクチャです。")
                
            # 3. Y軸反転（共感vs自己完結）の検出
 #           if (target_data["Y軸"] >= 4.0 and row["Y軸"] <= -4.0) or (target_data["Y軸"] <= -4.0 and row["Y軸"] >= 4.0):
 #               alert_logs.append("📡 **【Y軸バグ：通信エラー】** 片方は外部への共感や接続を求めますが、片方はデバッグパケットを完全遮断したスタンドプレー型。連絡無視や過剰な干渉によるシステムエラーを誘発します。")
                
            # 4. Z軸反転（大義vs実利）の検出
  #          if (target_data["Z軸"] >= 4.0 and row["Z軸"] <= -4.0) or (target_data["Z軸"] <= -4.0 and row["Z軸"] >= 4.0):
  #              alert_logs.append("💎 **【Z軸バグ：価値観の断絶】** 片方は綺麗な理念や大義名分（記号）に命を懸け、片方は目先の生存・経済合理性（具体）を最優先します。互いに「詐欺師」「冷酷人間」と罵り合う最恐のバグ領域です。")
            
            # アコーディオンパネルで綺麗に出力
   #         icon = "🦊" if row["タイプ"] == "デフォルト" else "👤"
            icon = "👤" # if row["タイプ"] == "デフォルト" else "👤"
            with st.expander(f"{icon} {row['名前']}（空間距離: {dist:.2f}）"):
                st.write(f"**システム座標**: X:{row['X軸']} / Y:{row['Y軸']} / Z:{row['Z軸']} ({row['カテゴリ']})")
                st.markdown(f"*特性記述*: {row['説明']}")
                st.write("---")
                
                if alert_logs:
                    for log in alert_logs:
                        st.write(log)
                else:
  #                  st.write("🔵 **【通常通信可能】** 致命的な反転構造はなく、標準的なプロトコルによる安定したコミュニケーションが可能な関係性です。")
                    st.write("🔵 **【相性診断】** 将来対応するかもしれません。")
  