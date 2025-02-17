# graph-for-b

RPGBakin の自作戦闘を設計するために勝手に作ったった設計図を出力するツール。ＧＵＩはまだ無い  


## 成果物

![成果物](./docs/img/[20250113-0140]フローチャート.png)  

👆　上記のようなフローチャートが描かれたワークシートを出力します。  
内容を確認するには、 Microsoft Excel が必要です。  

![ソースファイル](./docs/img/[20250113-0148]ソースファイル.png)  

👆　ソースファイルは JSON 形式です。  
仕様書はまだ書けていません。サンプルを解析してください。  


## Git Hub を見ている人向けの説明

Git Hub が何だか分からない人は、この節は読み飛ばしてください。  

* 📖 [Git Hub を見ている人向けの説明](./docs_dev/from_git_hub.md)
    * インストール方法、コマンド操作方法の説明など


## 説明

* 📖 [Trellis コンパイラーの使い方](./docs/programming_lesson/how_to_use_compiler.md)
* 📖 [プログラミング・レッスン１](./docs/programming_lesson/1/README.md)


## 更新履歴

* TODO
    * [ ] (2025-01-26) JSONを生成するコードのテンプレもJSONで用意したい。JSON構造の仕様変更時に対応しやすいように。
    * [ ] (2025-01-26) 影の色 auto も、コンパイル後は具体的なウェブセーフカラーを入れるようにしたい
    * [ ] (2025-01-26) varColor = `{darkness:1}` を実装したい


### [20250128.0.0] - 2025-01-28

#### Changed

* [x] (2025-01-27) Rectangle クラスを VarRectangle にリネームし、さらに Rectangle クラスを新規作成したい
    * [x] (2025-01-27) VarRectangle にリネームした


### [20250126.0.0] - 2025-01-26

#### Changed

* [x] (2025-01-26) shadowColorMappings の中に varColorDict を置きたい


### [20250125.0.0] - 2025-01-25

#### Changed

* [x] (2025-01-25) Pillar の baseColor を "#FFFF00" 形式にすると例外、 "xlPale.xlBlue" 形式なら Ok という不具合がある
    * `fill_rectangle` がエラーを起こす？ ---> PatternFill を返す関数で、ウェブセーフカラー文字列を返していた
* [x] (2025-01-25) Border, Font, Rectangle, Segments の color を varColor に変更したい


### [20250113.0.0] - 2025-01-13

#### Changed

* [x] (2025-01-13) Square クラスを、 InningsPitched にリネームしたい ---> (2025-01-13) Done


### [20250112.0.0] - 2025-01-12

#### Changed

* [x] (2025-01-12) 現状、 Terminal は start １つ、 end １つしか設定できない。複数設定できるようにしたい ---> (2025-01-12) Done
* [x] (2025-01-12) 現状、 Pillar に Id を付けているが、要らないのでは？ ---> (2025-01-12) Pillar の Id を廃止
* [x] (2025-01-12) 内部的には、柱と柱の隙間も柱として扱いたい ---> (2025-01-12) Done
* [x] (2025-01-12) Square, Rectangle オブジェクトを四則演算できるようにしたい ---> (2025-01-12) Done。cell_num, cell_th プロパティ追加
