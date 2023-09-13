---------------------------------------------------


    NVEnc.auo / NVEncC
     by rigaya

---------------------------------------------------

NVEnc.auo は、
NVIDIAのNVEncを使用してエンコードを行うAviutlの出力プラグインです。
NVEncによるハードウェア高速エンコードを目指します。

NVEncC は、上記のコマンドライン版です。
コマンドラインオプションについては、下記urlを参照ください。
https://github.com/rigaya/NVEnc/blob/master/NVEncC_Options.ja.md

【基本動作環境】
Windows 10 (x86/x64)
Aviutl 1.00 以降
NVEncが載ったハードウェア
  NVIDIA製 GPU GeForce Kepler世代以降 (GT/GTX 6xx 以降)
  ※GT 63x, 62x等はFermi世代のリネームであるため非対応なものがあります。
NVIDIA グラフィックドライバ 418.81以降 (x64版)
NVIDIA グラフィックドライバ 456.81以降 (x86版)

【NVEnc 使用にあたっての注意事項】
無保証です。自己責任で使用してください。
NVEncを使用したことによる、いかなる損害・トラブルについても責任を負いません。

【NVEnc 再配布(二次配布)について】
このファイル(NVEnc_readme.txt)と一緒に配布してください。念のため。
まあできればアーカイブまるごとで。

【導入方法】
※ 下記リンク先では図も使用して説明していますので、よりわかりやすいかもしれません。
   https://github.com/rigaya/NVEnc/blob/master/NVEnc_auo_readme.md#NVEnc-の-aviutl-への導入更新

1.
ダウンロードしたAviutl_NVEnc_6.xx.zipを開きます。

2.
zipファイル内のフォルダすべてをAviutlフォルダにコピーします。

3.
Aviutlを起動します。

4.
環境によっては、ウィンドウが表示され必要なモジュールのインストールが行われます。
その際、この不明な発行元のアプリがデバイスに変更を加えることを許可しますか? と出ることがありますが、
「はい」を選択してください。

5.
「その他」>「出力プラグイン情報」にNVEnc 6.xxがあるか確かめます。
ここでNVEncの表示がない場合、
- zipファイル内のフォルダすべてをコピーできていない
- 必要なモジュールのインストールに失敗した
  - この不明な発行元のアプリがデバイスに変更を加えることを許可しますか? で 「はい」を選択しなかった
  - (まれなケース) ウイルス対策ソフトにより、必要な実行ファイルが削除された
などの原因が考えられます。


【削除方法】
※ 下記リンク先では図も使用して説明していますので、よりわかりやすいかもしれません。
   https://github.com/rigaya/NVEnc/blob/master/NVEnc_auo_readme.md#NVEnc-の-aviutl-からの削除

・Aviutlのpulginsフォルダ内から下記フォルダとファイルを削除してください。
  - [フォルダ] NVEnc_stg
  - [ファイル] NVEnc.auo
  - [ファイル] NVEnc.conf (存在する場合)
  - [ファイル] NVEnc(.ini)
  - [ファイル] auo_setup.auf

【iniファイルによる拡張】
NVEnc.iniを書き換えることにより、
音声エンコーダやmuxerのコマンドラインを変更できます。
また音声エンコーダを追加することもできます。

デフォルトの設定では不十分だと思った場合は、
iniファイルの音声やmuxerのコマンドラインを調整してみてください。



コーディングが汚いとか言わないで。

【コンパイル環境】
VC++ 2019 Community

【NVIDIA CORPORATION CUDA SAMPLES EULA のライセンス規定の準拠表記】
本プログラムは、NVIDA CUDA Samplesをベースに作成されています。
すなわちサンプルコードをベースとする派生プログラムであり、サンプルコードを含みます。
“This software contains source code provided by NVIDIA Corporation.”

【dtlの使用表記】
本プログラムは、dtlライブラリを内部で使用しています。
https://github.com/cubicdaiya/dtl

【tinyxml2の使用表記】
本プログラムは、tinyxml2を内部で使用しています。
http://www.grinninglizard.com/tinyxml2/index.html


【検証環境 2014.03～】
Win7 x64
Intel Core i7 4770K + Asrock Z87 Extreme4
GeForce GTX 660
16GB 
NVIDIA グラフィックドライバ 335.23
NVIDIA グラフィックドライバ 347.09

【検証環境 2015.01～】
Win8.1 x64
Intel Core i7 5960X + ASUS X99 Deluxe
Geforce GTX 970
32GB RAM
NVIDIA グラフィックドライバ 347.25

【検証環境 2015.08～】
Win10 x64
Intel Core i7 5960X + ASUS X99 Deluxe
Geforce GTX 970
32GB RAM
NVIDIA グラフィックドライバ 353.62

【検証環境 2015.12～】
Win8.1 x64
Intel Core i3 4170 + Gigabyte Z97M-DS3H
Geforce GTX 970
8GB RAM
NVIDIA グラフィックドライバ 359.00

【検証環境 2015.12～】
Win10 x64
Intel Core i7 5960X + ASUS X99 Deluxe
Geforce GTX 960
32GB RAM
NVIDIA グラフィックドライバ 364.51


【検証環境 2016.07～】
Win10 x64
Intel Core i7 5960X + ASUS X99 Deluxe
Geforce GTX 1060
32GB 
NVIDIA グラフィックドライバ 368.81
NVIDIA グラフィックドライバ 372.70
NVIDIA グラフィックドライバ 375.95
NVIDIA グラフィックドライバ 382.33
NVIDIA グラフィックドライバ 385.41
NVIDIA グラフィックドライバ 385.69

【検証環境 2017.11～】
Win10 x64
Intel Core i9 7980XE +