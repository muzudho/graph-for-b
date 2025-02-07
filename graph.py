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
            tl.Trellis.build(
                    config=args.config,    # json path
                    content=args.source,  # json path
                    workbook=args.output,
                    temp_dir=args.temp)

        else:
            raise ValueError(f'unsupported command: {args.command}')


    except Exception as err:
        print(f"""\
[{datetime.datetime.now()}] おお、残念！　例外が投げられてしまった！
{type(err)=}  {err=}

以下はスタックトレース表示じゃ。
{traceback.format_exc()}
""")


########################################
# コマンドから実行時
########################################
if __name__ == '__main__':
    """コマンドから実行時"""
    main()
