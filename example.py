"""
例を実行します

py example.py all
"""

import datetime
import sys
import traceback


########################################
# コマンドから実行時
########################################
if __name__ == '__main__':
    """コマンドから実行時"""

    try:
        args = sys.argv

        if 1 < len(args):
            if args[1] == 'all':
                from examples.no1_render_empty import *
                from examples.no2_render_pillars import *
                from examples.no3_render_line_tapes import *
                from examples.no4_render_auto_shadow import *
                from examples.no5_render_auto_split_by_pillar import *

            else:
                raise ValueError(f'unsupported {args[1]=}')
        
        else:
            raise ValueError(f'unsupported {len(args)=}')

    except Exception as err:
        print(f"""\
[{datetime.datetime.now()}] おお、残念！　例外が投げられてしまった！
{type(err)=}  {err=}

以下はスタックトレース表示じゃ。
{traceback.format_exc()}
""")
