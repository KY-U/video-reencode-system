# video-reencode-system

Prova de Conceito de um Sistema de Reencode de Vídeo

## Descrição

O `video-reencode-system` é um sistema projetado para realizar reencode de vídeos usando `ffmpeg` para compressão, reduzindo espaço e custos sem sacrificar significativamente a qualidade. O sistema recebe o endereço de buckets da Google Cloud por requisições HTTP.

As opções de codec inicial são `h264`, `h264+` e `h265`, enquanto as opções de codec final são `vp8`, `vp9` e `av1`. Foram realizados testes com todas as combinações de codecs e parâmetros de encoding o mais similares possíveis. A métrica de qualidade de vídeo utilizada foi o PSNR. O resultado dos testes está disponível aqui: [Resultados dos Testes](https://docs.google.com/spreadsheets/d/1KBaI0MCrLNDGIszJqN0JJTRdKTZj6Jkiqy6kdszg2xM/edit?usp=sharing)

O código utilizado para os testes está presente na pasta `analise-exploratoria`.

Após decidir os codecs, foram testados os parâmetros de reencoding, que são:

- **Bitrate**: Tamanho em bits por segundo em uma gravação. Quanto menor o bitrate, maior a probabilidade de perda de qualidade da imagem.
- **Opção de Bitrate**: Configuração de como o bitrate é interpretado. Na configuração `unset`, o bitrate e a opção não são setados, deixando a configuração por conta do `ffmpeg`. Na configuração `variável`, a média de bitrate é mantida de acordo com o bitrate especificado. Na configuração `constante`, o bitrate é fixo em todos os frames.
- **CRF** (Constant Rate Factor): O significado desse fator depende do encoding, mas é basicamente o esforço do `ffmpeg` em manter a qualidade do encoding inicial, variando entre 0 e 63.
- **Speed** (Deadline): A rapidez com que o `ffmpeg` se esforça para manter a velocidade. A forma como isso é controlado varia entre os encodings, mas pode ser verificado na documentação.

Após decidir os parâmetros, foi implementado um sistema presente na pasta `servico-web`.

## Dependências

A lista completa de dependências está presente no arquivo `requirements.txt`. As principais tecnologias utilizadas foram:

- **Flask**: Para o serviço web.
- **Google Cloud Storage**: Para baixar os vídeos.
- **ffmpeg**: Para a compressão.

## Rodando o Projeto Localmente

1. Navegue até a pasta `servico-web`.

2. Crie um ambiente virtual com:

    ```bash
    python -m venv myenv
    ```

3. Ative o ambiente virtual:

   - No Windows:

     ```bash
     .\myenv\Scripts\activate
     ```

   - No macOS/Linux:

     ```bash
     source myenv/bin/activate
     ```

4. Instale as dependências:

    ```bash
    pip install --no-cache-dir -r requirements.txt
    ```

5. Execute a aplicação:

    ```bash
    python app.py
    ```

## Testando o Projeto

Para testar o projeto, você pode usar uma extensão de navegador para requisições HTTP, como [Yet Another REST Client](https://chromewebstore.google.com/detail/yet-another-rest-client/ehafadccdcdedbhcbddihehiodgcddpl), e enviar uma requisição POST com o corpo:

```json
{
    "video_source": "gs://psel_video_samples/h264.mp4"
}
```
Para o endpoint: http://127.0.0.1:5000/reencode

Ou execute o script de teste:
- No Windows:
    ```bash
    python .\tests\TestPostRequest.py
    ```

## Executando de Forma Containerizada

Para rodar o projeto de forma containerizada, basta ter o Docker instalado, disponível aqui: [Docker](https://www.docker.com) Em seguida, execute:

 ```bash
    docker compose up --build
    ```