# Assistente de Navegação com Análise de Imagem

**Linguagens de programação:** Python, Javascript

**Bibliotecas utilizadas:**
- OpenCV
- Tkinter
- PIL
- Google GenerativeAI
- pyttsx3

## Funcionalidades:
1. Captura imagens da webcam em tempo real.
2. Analisa as imagens usando o modelo Gemini Pro Vision.
3. Gera uma descrição textual da imagem em linguagem natural.
4. Exibe a descrição na interface gráfica.
5. Lê a descrição em voz alta utilizando o motor de síntese de voz.

## Arquitetura:
O sistema é composto por três camadas principais:
1. **Camada de captura e processamento de imagem:** Utiliza OpenCV para capturar imagens da webcam e as prepara para análise.
2. **Camada de análise de imagem:** Utiliza o modelo Gemini Pro Vision para gerar uma descrição textual da imagem.
3. **Camada de interface e síntese de voz:** Utiliza Tkinter para exibir a descrição na interface gráfica e pyttsx3 para lê-la em voz alta.

## Benefícios:
- Auxilia pessoas com deficiência visual a navegar em ambientes desconhecidos.
- Fornece uma descrição objetiva e precisa do ambiente.
- Interface intuitiva e fácil de usar.

## Instruções para uso:
1. Instale as bibliotecas necessárias (OpenCV, Tkinter, PIL, Google GenerativeAI, pyttsx3).
2. Execute o script `app.py`.
3. Permita o acesso à webcam.
4. Clique no botão "Analisar" para capturar e analisar a imagem.
5. A descrição da imagem será exibida na interface e lida em voz alta.

## Observações:
- Este projeto utiliza o modelo Gemini Pro Vision da Google AI, que requer uma chave de API.
- O modelo pode ser trocado por outros modelos de análise de imagem, desde que sejam compatíveis com a interface.

**Desenvolvido por:** Alexandre Menezes Gomes, Analista e Desenvolvedor de Sistemas - Fanap (2018)
