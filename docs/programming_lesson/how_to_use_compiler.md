# コンパイラーの使い方


## 手順１：

ターミナルに、以下のコマンドを打鍵してください。

```shell
py
```

👆　あるいは、`python` や `python3` といったコマンドかもしれません。環境に合わせてください。  
以降、インタープリターのモードに入ります。  

以下のスクリプトを打鍵してください。  

```shell
import trelliswork as tl
tl.Trellis.compile(
    config='./examples/configurations/compiler-tutorial-o1o0.json',
    source='./examples/sources/compiler-tutorial-o1o0-empty.json')
```

次のような出力が表示されます。  

Output:  

```plaintext
🔧　read ./examples/configurations/compiler-tutorial-o1o0.json config file
🔧　read ./examples/sources/compiler-tutorial-o1o0-empty.json source file
```

👆　２つのファイルを読み込んだことが分かります。  
動作確認はこれでＯｋです。  
