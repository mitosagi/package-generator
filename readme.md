# Package Generator
AviUtlプラグイン・スクリプトの解説とインストール手順をREADMEや解説URLから自動生成、`AviUtl Package Manager`により読み込み可能な形式にします。

Google ColabとChatGPTを組み合わせて動きます。実用的な結果を得るためにはGPT4相当のLLMが必要です。

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mitosagi/package-generator/blob/main/apm.ipynb)

## 初期設定
```
pip install -r requirements.txt
playwright install-deps
playwright install webkit
```
