import argparse


def main(filename, lang):
    import whisper

    model = whisper.load_model("large")

    # Load audio
    audio = whisper.load_audio(f"content/{filename}")

    result = model.transcribe(audio, verbose=True, language=lang)

    # Write into a text file
    with open(f"download/{filename}.txt", "w") as f:
        f.write(f"▼ Transcription of {filename}\n")
        f.write(result["text"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f", "--filename", help="文字起こしするファイル名", required=True
    )  # noqa: E501
    parser.add_argument("-l", "--lang", help="言語コード デフォルトは`ja`")
    args = parser.parse_args()

    filename = args.filename
    lang = "ja" if args.lang is None else args.lang
    main(filename=filename, lang=lang)
