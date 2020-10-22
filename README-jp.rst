sundir
======

*sundir* は、指定された、緯度、経度、高度、そして時刻における太陽の方向を方位、仰角で表示するアプリケーションです。


インストール、使用方法
----------------------

インストール
^^^^^^^^^^^^

``pip install sundir``


使用方法
^^^^^^^^

::

    sundir {緯度(Lat)} {経度(Lon)}
    
        緯度, 経度: {度}d{分}m{秒}s or {度}d

実行例
~~~~~~

::

    sundir 35d37m0s 139d47m3s --date "2020/09/18 13:00:00" --repeat 10
    
    latitude    : 35d37m0s
    longitude   : 139d47m3s
    altitude(m) : 0.0
    
             Date            AZ(deg)   EL(deg)
    2020/09/18 13:00:00     214.9717   50.7684
    2020/09/18 13:00:10     215.0299   50.7489
    2020/09/18 13:00:20     215.0881   50.7294
    2020/09/18 13:00:30     215.1462   50.7099
    2020/09/18 13:00:40     215.2043   50.6904
    2020/09/18 13:00:50     215.2623   50.6708
    2020/09/18 13:01:00     215.3203   50.6512
    2020/09/18 13:01:10     215.3782   50.6315
    2020/09/18 13:01:20     215.4361   50.6118
    2020/09/18 13:01:30     215.4940   50.5921

コマンドラインオプション
~~~~~~~~~~~~~~~~~~~~~~~~

``sundir --help`` を実行することでヘルプメッセージを表示します。:

::

    Usage: sundir [OPTIONS] [緯度(lat)] [経度(lon)]

    Options:

        --altitude FLOAT            算出する位置の高度(m)を設定する。
                                    [default: 0.0]

        --date "2020/8/11 13:45:10" 
                                    日付、時刻を設定する。
                                    [default: 現在時刻。秒単位で切り捨て]

        --interval INTEGER          複数回算出する場合の時間間隔を設定する。
                                    [default: 10]

        --repeat INTEGER            算出回数を設定する。
                                    [default: 1]

        --csv FILE                  FILE で指定されたパスへ CSV 形式で書き込む。

        --version                   バージョンを表示する。

        -h, --help                  ヘルプメッセージを表示する。

ライセンス
----------

`Apache License, Version 2.0 <http://www.apache.org/licenses/LICENSE-2.0>`__

変更履歴
--------

0.3.0
^^^^^

- first published version

0.3.1
^^^^^

- corrected the readme file.


作成者
------

`Takayuki Matsuda <mailto:taka.matsuda@simgics.co.jp>`__

