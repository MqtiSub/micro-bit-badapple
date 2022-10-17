# BadApple on microbit
これは多分microbitでbadappleする試みです

## 説明兼メモ
必要物

・microbit拡張module ・SD card拡張　・ssd1306のdisplay ・半田 ・ブレッドボード

## やり方
.microbitの中のhexファイルをmicrobitに投げましょう!!

## 詳細
binファイルはwindowsのcertutilコマンドを使いました。

SDcardのSPIモードは64byte単位じゃないと動作遅くなるらしいので注意!!

不親切にもほどがあるのですが、v1.xのvariant.hにはSPIpinのuint8_t定義があるのにv2にはないおかげで、SDカードのライブラリーのコンパイルが通らなくて萎えました()

ちなみにmicrobitでは検証していないので動かないかもです...(は?)
