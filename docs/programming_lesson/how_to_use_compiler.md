# コンパイラーの使い方


## 手順１：　コンパイラーの動作確認

ターミナルに、以下のコマンドを打鍵してください。

```shell
py
```

👆　あるいは、`python` や `python3` といったコマンドかもしれません。環境に合わせてください。  
以降、インタープリターのモードに入ります。  

インタープリターのモードで、以下のスクリプトを打鍵してください。  

```py
import trelliswork as tl
tc = tl.Compiler()
tc.compile(
    config='./examples/configurations/compiler-tutorial-o1o0-empty.json',
    source='./examples/sources/compiler-tutorial-o1o0-empty.json')
```

config と source のファイルの中身を確認しておいてください。  

以下のような出力が表示されます。  

Output:  

```plaintext
🔧　read ./examples/configurations/compiler-tutorial-o1o0-empty.json config file.
🔧　read ./examples/sources/compiler-tutorial-o1o0-empty.json source file.
```

👆　２つのファイルを読み込んだことが分かります。  
動作確認はこれでＯｋです。  


## 手順２：　インポート機能の動作確認

コンパイラーは設定ファイルで機能を追加することで使っていきます。  

インタープリターのモードで、以下のスクリプトを打鍵してください。  

```py
import trelliswork as tl
tc = tl.Compiler()
tc.compile(
    config='./examples/configurations/compiler-tutorial-o2o0-imports.json',
    source='./examples/sources/compiler-tutorial-o2o0-imports.json')
```

config と source のファイルの中身を確認しておいてください。  

以下のような出力が表示されます。  

Output:  

```plaintext
🔧　read ./examples/configurations/compiler-tutorial-o2o0-imports.json config file.
🔧　read ./examples/sources/compiler-tutorial-o2o0-imports.json source file.
🔧　import ./examples/sources/hoge.json file.
🔧　write ./temp/examples\compiler-tutorial-o2o0-imports__after_imports.json object file.
    comment='imports'
```

👆 📄 `./temp/examples\compiler-tutorial-o2o0-imports__after_imports.json` ファイルの中身を確認してください。  
以下のようになっていればＯｋです。  

```json
{
    "hoge": "hooooooge"
}
```
