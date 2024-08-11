# md-to-pdf

[md-to-pdf](https://github.com/simonhaenisch/md-to-pdf)を使って PDF を作成します。

[Markdown PDF](https://github.com/yzane/vscode-markdown-pdf)を使って PDF を作成することもできます。ほとんど同じフォーマットにしていますが、微妙に差異があります。

## Environtment

Visual Studio Code から devcontainer で起動します。必要なものがすべてそろいます。

## Generate PDF

```shell
npm run pdf article.md
```

md ファイルと同じディレクトリに PDF が作成されます。

[Markdown PDF](https://github.com/yzane/vscode-markdown-pdf)で PDF を作成した場合は `outputs` ディレクトリに作成されます。
