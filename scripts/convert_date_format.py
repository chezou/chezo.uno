#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "python-frontmatter",
#   "python-dateutil",
#   "pytz",
# ]
# ///

import os
import frontmatter
from dateutil.parser import parse
import pytz
from datetime import datetime

# --- 設定 ---

# 1. 処理対象のMarkdownファイルが含まれるルートディレクトリを指定してください
TARGET_DIR = "./content/post"  # 例: "./content/posts"

# 2. 基準となるタイムゾーンを指定してください
# タイムゾーン情報がない日付は、ここで指定したタイムゾーンとして解釈されます。
# カナダ・ブリティッシュコロンビア州（DST考慮）の場合は "America/Vancouver" です。
# 日本の場合は "Asia/Tokyo" です。
DEFAULT_TIMEZONE = "America/Vancouver"

# --- 設定ここまで ---


def format_datetime_with_colon_in_offset(dt):
    """
    datetimeオブジェクトを 'YYYY-MM-DD HH:MM:SS±HH:MM' 形式の文字列に変換します。
    """
    # タイムゾーンオフセットを +HHMM または -HHMM の形式で取得
    offset = dt.strftime('%z')
    if not offset:
        return dt.strftime('%Y-%m-%d %H:%M:%S')

    # オフセットにコロンを挿入 (+HH:MM or -HH:MM)
    offset_with_colon = f"{offset[:-2]}:{offset[-2:]}"

    # 日付と時刻を指定のフォーマットで取得
    datetime_str = dt.strftime('%Y-%m-%d %H:%M:%S')

    return f"{datetime_str}{offset_with_colon}"

def process_markdown_file(file_path, default_tz):
    """
    単一のMarkdownファイルを処理し、dateとlastmodのフォーマットを更新します。
    """
    try:
        # ファイルをUTF-8で読み込み
        with open(file_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)

        # メタデータがない場合は処理をスキップ
        if not post.metadata:
            return

        metadata_updated = False

        # 'date'と'lastmod'フィールドをチェック
        for field in ['date', 'lastmod']:
            if field in post.metadata and post.metadata[field]:
                original_date_value = post.metadata[field]

                try:
                    # 文字列やdatetimeオブジェクトなど、様々な型に対応
                    dt_object = parse(str(original_date_value))
                except (ValueError, TypeError) as e:
                    print(f"⚠️  警告: 日付の解析に失敗しました。 スキップします。\n    ファイル: {file_path}\n    フィールド: '{field}', 値: '{original_date_value}'\n    エラー: {e}")
                    continue

                # タイムゾーン情報がない(naive)場合、デフォルトのタイムゾーンを適用
                if dt_object.tzinfo is None or dt_object.tzinfo.utcoffset(dt_object) is None:
                    localized_dt = default_tz.localize(dt_object)
                # タイムゾーン情報がある(aware)場合、対象のタイムゾーンに変換
                else:
                    localized_dt = dt_object.astimezone(default_tz)

                # 新しいフォーマットの文字列に変換
                new_date_str = format_datetime_with_colon_in_offset(localized_dt)

                # 値が変更された場合のみ更新フラグを立てる
                if str(original_date_value) != new_date_str:
                    post.metadata[field] = new_date_str
                    metadata_updated = True

        # メタデータが1つでも更新された場合、ファイルに書き戻す
        if metadata_updated:
            with open(file_path, 'wb') as f:
                frontmatter.dump(post, f)
            print(f"✅ 更新しました: {file_path}")

    except Exception as e:
        print(f"❌ エラー: ファイル処理中に予期せぬ問題が発生しました。\n    ファイル: {file_path}\n    エラー: {e}")


def main():
    """
    メイン処理。ディレクトリを探索し、各Markdownファイルを処理します。
    """
    # タイムゾーンオブジェクトの初期化
    try:
        default_tz = pytz.timezone(DEFAULT_TIMEZONE)
    except pytz.UnknownTimeZoneError:
        print(f"❌ エラー: 設定されたタイムゾーン '{DEFAULT_TIMEZONE}' が無効です。")
        print("利用可能なタイムゾーンのリストは pytz.all_timezones で確認できます。")
        return

    if not os.path.isdir(TARGET_DIR):
        print(f"❌ エラー: 指定されたディレクトリ '{TARGET_DIR}' が見つかりません。")
        return

    print(f"🔍 '{TARGET_DIR}' 内のMarkdownファイルを検索・処理します...")
    print(f"🕒 基準タイムゾーン: {DEFAULT_TIMEZONE}")
    print("-" * 30)

    # 指定されたディレクトリを再帰的に探索
    for root, _, files in os.walk(TARGET_DIR):
        for file in files:
            # 拡張子が .md または .markdown のファイルを対象
            if file.endswith((".md", ".markdown")) and not file == "_index.md":
                file_path = os.path.join(root, file)
                process_markdown_file(file_path, default_tz)

    print("-" * 30)
    print("🎉 処理が完了しました。")

if __name__ == "__main__":
    main()
