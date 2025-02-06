"""
白紙に柱の頭を追加
"""

import json
import trelliswork as tl


# 設定ファイル（JSON形式）
file_path_of_config_doc = './examples/data_of_config/trellis_config_of_example2.json'

print(f"""\
example 2: pillars""")

# 設定ファイル（JSON形式）を読込
print(f"""\
    🔧　read {file_path_of_config_doc} file""")
with open(file_path_of_config_doc, encoding='utf-8') as f:
    config_doc = json.load(f)


# 設定ファイルを加工
config_doc['compiler']['objectFilePrefix'] = 'no2'


# ビルド
tl.build(
        config_doc=config_doc)
