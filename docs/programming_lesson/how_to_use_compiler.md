# コンパイラーの使い方


## 手順１：　コンパイラーの動作確認

ターミナルに、以下のコマンドを打鍵してください。

```shell
py
```

👆　あるいは、`python` や `python3` といったコマンドかもしれません。環境に合わせてください。  
以降、インタープリターのモードに入ります。  

以下のスクリプトを打鍵してください。  

```py
import trelliswork as tl
tc = tl.Compiler()
tc.compile(
    config='./examples/configurations/compiler-tutorial-o1o0-empty.json',
    source='./examples/sources/compiler-tutorial-o1o0-empty.json')
```

次のような出力が表示されます。  

Output:  

```plaintext
🔧　read ./examples/configurations/compiler-tutorial-o1o0-empty.json config file.
🔧　read ./examples/sources/compiler-tutorial-o1o0-empty.json source file.
```

👆　２つのファイルを読み込んだことが分かります。  
動作確認はこれでＯｋです。  


## 手順２：　インポート機能の動作確認

コンパイラーは設定ファイルで機能を追加することで使っていきます。  

