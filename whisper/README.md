# openai whisper sample

[OpenAI Whisper](https://github.com/openai/whisper.git)を使って音声ファイルから文字起こしをします。

## 環境

- Python
- Rye（パッケージ管理）

## 使い方

1. パッケージをインストールします。
   ```
   rye sync
   ```
2. content ディレクトリに音声ファイルを格納します。
3. プログラムを実行します。downloadディレクトリにテキストファイルが作成されます。
   ```
   ryu run src/whisper-sample/main.py -f {ファイル名}
   ```

---

## 自分メモ

### 初期設定

```
rye add --dev black mypy ruff
rye sync
```

.vscode/settings.json と pyproject.toml の設定
