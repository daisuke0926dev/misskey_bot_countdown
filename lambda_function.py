from datetime import datetime
from misskey import Misskey
import os

def lambda_handler(event, context):
  # インスタンス(サーバー)とアクセストークンを環境変数から取得
  mk = Misskey(os.environ['MISSKEY_INSTANCE'])
  mk.token = os.environ['MISSKEY_TOKEN']
  today = datetime.now()

  # 指定された日付+1を入力
  target_date = datetime(2024, 1, 21)

  # 日数の差を計算
  delta = target_date - today

  # 日数の差を返す
  mk.notes_create(text="2024年1月20日まであと" + str(delta.days) + " 日")
