# Package Generator
AviUtlプラグイン・スクリプトの解説とインストール手順をREADMEや解説URLから自動生成、`AviUtl Package Manager`により読み込み可能な形式のデータとして出力します。

Google Colabとお使いの大規模言語モデル(LLM)を組み合わせて動きます。最良の結果を得るためにはpythonインタプリンタ付きの[ChatGPT](https://chat.openai.com/)`Advanced Data Analysis`が必要ですが、無料で使用できる[GoogleのBard](https://bard.google.com/)でも動作します。

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mitosagi/package-generator/blob/main/apm.ipynb)

## 例
使用しているLLMはGPT-4 ChatGPT(August 3, 2023)です。

<details open>
  <summary>L-SMASH Works</summary>
  
```
{
  "id": "MrOjii/LSMASHWorks",
  "name": "L-SMASH Works",
  "overview": "様々な機能を追加するプラグインセット",
  "description": "L-SMASH Worksはプラグインセットであり、様々な機能を追加します。これにはファイルの読み込み、muxing、dumping、カラースペースの変換などが含まれます。また、VFRからCFRへの変換やLW48と呼ばれる特定のカラースペースもサポートしています。",
  "developer": "Mr-Ojii",
  "latestVersion": "r1103",
  "files": [
    {
      "filename": "plugins/lwinput64.aui"
    },
    {
      "filename": "plugins/lwcolor.auc"
    },
    {
      "filename": "plugins/lwdumper.auf"
    },
    {
      "filename": "plugins/lwinput.aui"
    },
    {
      "filename": "plugins/lwmuxer.auf"
    }
  ],
  "dependencies": [],
  "pageURL": [
    "https://github.com/Mr-Ojii/L-SMASH-Works"
  ],
  "downloadURLs": [
    ""
  ],
  "releases": [
    {
      "version": "r1103",
      "integrity": {
        "archive": "sha384-ncGezyo8D/99dgQh8HkYARxqJMGXNLCkR7fNwvcksL5A5/plhNvm2BbfDkhv6aOy",
        "file": [
          {
            "target": "plugins/lwinput64.aui",
            "hash": "sha384-4cm/v8T585jKv0mzuYJLGZQoH8ryept+3mREZNL6r5rETR+ChTbPrmLe0nPkGZck"
          },
          {
            "target": "plugins/lwcolor.auc",
            "hash": "sha384-B6syiH8c6mZkuhFkBzgiE4FKAI/RqGBWGLh0OEC6hArFSSgNKNONQOP5yIN5IcOR"
          },
          {
            "target": "plugins/lwdumper.auf",
            "hash": "sha384-ZYvPz90T0E7HtaFFQB6ZiPZfcrtJ8X2hL0IPsvtVcbAfOqeoKEvpWVa0BuBQ3KTU"
          },
          {
            "target": "plugins/lwinput.aui",
            "hash": "sha384-am2zKCVUKTm1B5nehVSBZnbqcBuiDf7JoCKscpUA2jvHq3rv99Q7A8cW+WZr9xsu"
          },
          {
            "target": "plugins/lwmuxer.auf",
            "hash": "sha384-Bq1r1Wokz13nvYrVh5EAY6ImZYgEYqTJpXLuBJ7d53DCLJFrk2uW8vdEp02j3zpU"
          }
        ]
      }
    }
  ]
}
```

</details>

<details>
  <summary>JPEG 3点セット</summary>

```
{
  "id": "unknown/JPEG3PointSet",
  "name": "JPEG 3点セット",
  "overview": "JPEG入出力の3つのプラグインセット",
  "description": "JPEG入出力に関連する3つのプラグインセット。これらのプラグインはJPEGのYCbCrをAviUtlの内部形式YC48に直接スケーリングし、変換誤差を低減します。セットにはJPEG File Reader、連番JPEG出力、JPEGワンクリック保存の3つのプラグインが含まれています。AviUtlのバージョンはver 0.99k2以降が推奨されていますが、ver 0.99k2以前のバージョンでも動作可能です。",
  "developer": "unknown",
  "dependencies": [
    "aviutl0.99k2"
  ],
  "latestVersion": "0.3.1",
  "files": [
    {
      "filename": "plugins/jpeg_input.aui"
    },
    {
      "filename": "plugins/jpeg_output.auo"
    },
    {
      "filename": "plugins/jpeg_print.auf"
    }
  ],
  "pageURL": [
    "https://sosakubiyori.com/aviutl-jpegprint/"
  ],
  "downloadURLs": [
    ""
  ],
  "releases": [
    {
      "version": "0.3.1",
      "integrity": {
        "archive": "sha384-bNi1uWuBipTrshC4yyDAQxdLt20xSjQXWQVYkQw6t83Ihd8fHwWwij1AJAQ8xej+",
        "file": [
          {
            "target": "plugins/jpeg_input.aui",
            "hash": "sha384-4+eu6lFvloskhVux2gf70V8dNG9HYvMJz/EPyUcNE5vGuOeMXXPvLQw/R1lXBBBk"
          },
          {
            "target": "plugins/jpeg_output.auo",
            "hash": "sha384-Pu0RsNujkPFy886s2+vlqLcnwhbEkbV2EZ0M/prHfFoA9i+eiw2IZtDSuaF6JY/h"
          },
          {
            "target": "plugins/jpeg_print.auf",
            "hash": "sha384-+iNM0Uhd3uWvGx2dk1vm9DC0iOgf+QaJ0bjhfa6bP/6mP3llfNwJC82AzdY2BEKm"
          }
        ]
      }
    }
  ]
}

```

</details>

<details>
  <summary>花火</summary>
  
```
{
  "id": "YaseiNoMokuyaP/HanaBi",
  "description": "This package provides animation effects for Aviutl's extended editing. Please learn how to use it by feeling. For more details, refer to the distribution URL.",
  "overview": "Animation effects for extended edit",
  "name": "花火",
  "developer": "野生の木屋P",
  "dependencies": [],
  "latestVersion": "2012/02/08",
  "files": [
    {
      "filename": "script/YaseiNoMokuyaP/@花火.anm"
    }
  ],
  "pageURL": [
    "https://www.nicovideo.jp/watch/sm16915418"
  ],
  "downloadURLs": [
    ""
  ],
  "releases": [
    {
      "version": "2012/02/08",
      "integrity": {
        "archive": "sha384-TOIQ2fFZCzAYkISBNkLNZ1g5aVBeF6tGyvFqC4uGhjEHreqrXV1skZzFDnobUkOL",
        "file": [
          {
            "target": "script/YaseiNoMokuyaP/@花火.anm",
            "hash": "sha384-dhy/Ht5rKRGbXE2fhfossqGDxNNJgTe9kjs+SALlWCDz2dK48JOS2EnZzU1Gj3dy"
          }
        ]
      }
    }
  ]
}
```

</details>

## 初期設定
```
pip install -r requirements.txt
playwright install-deps
playwright install webkit
```
