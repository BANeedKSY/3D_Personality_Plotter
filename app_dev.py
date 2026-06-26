import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout="wide")  # 画面を広く使って3Dを見やすくします
st.title("3軸人間性プロッター（視界デバッグ・修正版4：動的凡例フィルタ搭載）")

# 1. データの準備
data = {
    "対象名": [
        "蛮苦恣意", "金満実業家", "中華系左派政治家", "金満保守系大統領", "左派記者（身バレ引退）", 

        "尼僧(出家前)","尼僧(出家後)", "匿名落書き芸術家", "左派知事", "保守系女性首相",

        "初代・創業者(職人・芸人)", "何代目・後継者(看板の継承者)",  # ← 概念サンプルを追加
        "宗教・精神的巨頭","排他的孤独型巨塔","排他的カリスマ型巨塔","世襲マフィア型恐怖巨塔"
    ],
    "X_方向性(保守/リベ)":  [-3, -2, 4, -4, 5,    3,  4,  5, 4, -4,   -4, -4, -5, -5, +5, -5],
    "Y_動機(自己完結/名誉)":[-5, -5, 4,  5, 5,    4, -5, -5, 3,  3,   -5, +4, +5, -5, -5, +5], # 自立(-5) ↔ 依存(+4)
    "Z_立脚点(具体/抽象)":  [-4, -5, 4, -2, 5,   -4,  4, -3, 5,  2,   -4, +3, +5, +5, +5, -5]  # 具体(-4) ↔ 抽象(+3)
}

df = pd.DataFrame(data)

# ==============================================================================
# 【新規】 2. コントロール層：サイドバーへの「動的凡例チェックボックス」の実装
# ==============================================================================
st.sidebar.title("凡例 / 表示切り替え")
st.sidebar.write("チェックボックスのON/OFFで、3D空間へのプロット表示・非表示をリアルタイムに切り替えます。")

# 一括操作用のマスタースイッチ
select_all = st.sidebar.checkbox("すべての対象を表示（全選択 / 全解除）", value=True)

# ループ処理による動的チェックボックスの生成と、選択状態の配列化
selected_names = []
for name in data["対象名"]:
    # マスタースイッチの状態を初期値にバインド
    if st.sidebar.checkbox(name, value=select_all, key=f"cb_{name}"):
        selected_names.append(name)

# データ層のフィルタリング処理（選択された対象名のみを抽出）
df_filtered = df[df["対象名"].isin(selected_names)]

# ==============================================================================

# 表示対象が「空（0件選択）」の場合の例外処理（エラーハンドリング）
if df_filtered.empty:
    st.warning("⚠️ 左側のサイドバーで対象を1つ以上選択してください。プロット空間が空集合（Empty）です。")
else:
    # 3. ベースとなる3D散布図（フィルタリング済みの df_filtered を投入）
    fig = px.scatter_3d(
        df_filtered, 
        x="X_方向性(保守/リベ)", 
        y="Y_動機(自己完結/名誉)", 
        z="Z_立脚点(具体/抽象)",
        text="対象名",
        color="Y_動機(自己完結/名誉)",  # 動機の数値で色分け
        color_continuous_scale="Viridis",
        range_color=[-5, 5],            # 【デバッグ】絞り込み時も色の評価基準（スケール）を固定
        range_x=[-5, 5], range_y=[-5, 5], range_z=[-5, 5]
    )

    # 4. 対人依存度ベクトルの追加（非社交の極から社交の極へ貫くライン）
    vector_x = [-5, 5]
    vector_y = [-5, 5]
    vector_z = [-5, 5]

    fig.add_trace(go.Scatter3d(
        x=vector_x,
        y=vector_y,
        z=vector_z,
        mode="lines+markers",
        line=dict(color="rgba(255, 0, 0, 0.6)", width=4, dash="dash"),  # 赤い破線
        marker=dict(size=[0, 4], color="red"),  # 終点に小さな目印
        name="社交性・対人依存度ベクトル"
    ))

    # 5. ベクトルの先端に「3Dの矢印（円錐）」を配置
    fig.add_trace(go.Cone(
        x=[5], y=[5], z=[5],       # 矢印を配置する座標（終点）
        u=[2], v=[2], w=[2],       # 矢印が向く方向ベクトル
        sizemode="absolute",
        sizeref=1.2,               # 矢印の大きさ
        showscale=False, 
        colorscale=[[0, 'red'], [1, 'red']], 
        name="ベクトル先端"
    ))

    # 6. 極点のテキストラベルを追加
    fig.add_trace(go.Scatter3d(
        x=[-5, 5], y=[-5, 5], z=[-5, 5],
        mode="text",
        text=["極限の自立（スタンドアロン）", "極限の対人依存（外部接続必須）"],
        textposition=["top center", "bottom center"],
        showlegend=False
    ))

    # 7. 赤いベクトルの中ほど（原点）にラベル「（社交性）」を表示
    fig.add_trace(go.Scatter3d(
        x=[0], y=[0], z=[0],                              # 中点（原点）の座標
        mode="text",
        text=["（社交性）"],
        textposition="top center",                         # 各軸の交点と被らないよう、少し上に浮かせます
        textfont=dict(color="rgba(255, 0, 0, 0.9)", size=13),  # ベクトル線と同期した赤色で強調
        showlegend=False
    ))

    # 8. グラフのレイアウト・カメラ視点・余白の最適化
    fig.update_layout(
        scene=dict(
            aspectmode='cube',
            xaxis_title="X: 方向性 (左:保守 / 右:リベ)",
            yaxis_title="Y: 動機 (手前:自己完結 / 奥:名誉)",
            zaxis_title="Z: 立脚点 (下:具体 / 上:抽象)",
            
            # 3D空間のカメラ視野のデバッグ
            camera=dict(
                eye=dict(x=1.0, y=1.0, z=1.0),
                projection=dict(type="perspective")
            )
        ),
        margin=dict(l=5, r=5, b=5, t=5),
        height=850,  # 画面上でグラフ自体をさらに大きく表示
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
    )

    # 9. 画面への表示
    st.plotly_chart(fig, use_container_width=True)