# Package Generator
AviUtlプラグイン・スクリプトの解説とインストール手順をREADMEや解説URLから自動生成、`AviUtl Package Manager`により読み込み可能な形式にします。

Google Colabとお使いの大規模言語モデルを組み合わせて動きます。最良の結果を得るためには[ChatGPT](https://chat.openai.com/)の`Advanced Data Analysis`が必要ですが、無料で使用できる[GoogleのBard](https://bard.google.com/)でも動作します。

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mitosagi/package-generator/blob/main/apm.ipynb)

## 初期設定
```
pip install -r requirements.txt
playwright install-deps
playwright install webkit
```
