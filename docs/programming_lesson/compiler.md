# プログラミング・レッスン　コンパイラー編


## 手順１：

以下のような、４つのファイルを作ってください。  


📄 `./temp/lesson/hoge.json`  

```json
{
    "exports": {
        "hoge": "hooooooge"
    }
}
```


📄 `./temp/lesson/fuga.json`  

```json
{
    "exports": {
        "fuga": "fuuuuuuga"
    }
}
```


📄 `./temp/lesson/piyo.json`  

```json
{
    "imports": [
        "./temp/lesson/hoge.json"
    ],
    "piyo": {
        "imports": [
            "./temp/lesson/fuga.json"
        ]
    }
}
```


📄 `./temp/lesson/config.json`  

```json
{
    "builder": {

    },
    "compiler": {
        "objectFolder": "./temp/objects",
        "translationOrder": [
            "imports"
        ],
        "tlanslators": {
            "imports": {
                "enabled": true,
                "objectFile": {
                    "write": true,
                    "suffix": "after_imports"
                }
            }
        }
    }
}
```


## 手順２：

ターミナルに、以下のコマンドを打鍵してください。

```shell
py
```

👆　あるいは、`python` や `python3` といったコマンドかもしれません。環境に合わせてください。  
以降、インタープリターのモードに入ります。  

以下のスクリプトを打鍵してください。  

```py
import trelliswork as tl
tl.Trellis.compile(
    config='./temp/lesson/config.json',
    content='./temp/lesson/piyo.json')
```

👆 content で指定したファイルが読込、上書きの両方される。  
TODO 出力ファイルも指定したい
FIXME 動作しなかった
