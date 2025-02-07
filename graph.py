import argparse
import datetime
import json
import os
import traceback
import trelliswork as tl


def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("command", help="コマンド名")
        parser.add_argument("-c", "--config", help="設定であるJSON形式ファイルへのパス")
        parser.add_argument("-s", "--source", help="描画の指示であるJSON形式ファイルへのパス")
        parser.add_argument("-o", "--output", help="書出し先となるExcelワークブック・ファイルへのパス")
        parser.add_argument("-t", "--temp", help="テンポラリー・ディレクトリー。削除してもよいファイルを置けるディレクトリーへのパス")
        args = parser.parse_args()

        if args.command == 'init':
            tl.init()

        elif args.command == 'build':
            build_by_command(
                    config_doc_path_to_read=args.config,    # json path
                    contents_doc_path_to_read=args.source,  # json path
                    wb_path_to_write=args.output,
                    temporary_directory_path=args.temp)

        else:
            raise ValueError(f'unsupported command: {args.command}')


    except Exception as err:
        print(f"""\
[{datetime.datetime.now()}] おお、残念！　例外が投げられてしまった！
{type(err)=}  {err=}

以下はスタックトレース表示じゃ。
{traceback.format_exc()}
""")


def build_by_command(
        config_doc_path_to_read,
        contents_doc_path_to_read,
        wb_path_to_write,
        temporary_directory_path):

    if not config_doc_path_to_read:
        print(f"""ERROR: build コマンドには --config オプションを付けて、トレリスの設定が書かれた JSON ファイルへのパスを指定してください""")
        return

    if not contents_doc_path_to_read:
        print(f"""ERROR: build コマンドには --source オプションを付けて、描画の設定が書かれた JSON ファイルへのパスを指定してください""")
        return

    if not temporary_directory_path:
        print(f"""ERROR: build コマンドには --temp オプションを付けて、（消えても構わないファイルを入れておくための）テンポラリー・ディレクトリーのパスを指定してください""")
        return


    # ソースファイル（JSON形式）を読込
    print(f"🔧　read {config_doc_path_to_read} file")
    with open(config_doc_path_to_read, encoding='utf-8') as f:
        config_doc = json.load(f)


    # コマンドライン引数で設定を上書き
    if 'builder' not in config_doc:
        config_doc['builder'] = {}
    
    config_doc['builder']['--source'] = contents_doc_path_to_read

    if 'compiler' not in config_doc:
        config_doc['compiler'] = {}

    if 'renderer' not in config_doc:
        config_doc['renderer'] = {}

    config_doc['renderer']['--output'] = wb_path_to_write


    # ビルド
    tl.build_by_config_doc(
            config_doc=config_doc)


########################################
# コマンドから実行時
########################################
if __name__ == '__main__':
    """コマンドから実行時"""
    main()
