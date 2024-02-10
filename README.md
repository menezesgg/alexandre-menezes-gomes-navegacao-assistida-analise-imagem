# alexandre-menezes-gomes-navegacao-assistida-analise-imagem
Sistema é um assistente de navegação que utiliza análise de imagem para descrever o ambiente ao usuário através de voz. Ele captura imagens da webcam, analisa-as usando o modelo de linguagem Gemini Pro Vision da Google AI, e descreve o conteúdo da imagem em linguagem natural.
Descrição do Sistema para GitHub: Assistente de Navegação com Análise de Imagem
Desenvolvido por: Alexandre Menezes (ADS)

Linguagens de programação: Python, Javascript

Bibliotecas utilizadas:

OpenCV
Tkinter
PIL
Google GenerativeAI
pyttsx3

Funcionalidades:

Captura imagens da webcam em tempo real.
Analisa as imagens usando o modelo Gemini Pro Vision.
Gera uma descrição textual da imagem em linguagem natural.
Exibe a descrição na interface gráfica.
Lê a descrição em voz alta utilizando o motor de síntese de voz.
Arquitetura:

O sistema é composto por três camadas principais:

Camada de captura e processamento de imagem: Utiliza OpenCV para capturar imagens da webcam e as prepara para análise.
Camada de análise de imagem: Utiliza o modelo Gemini Pro Vision para gerar uma descrição textual da imagem.
Camada de interface e síntese de voz: Utiliza Tkinter para exibir a descrição na interface gráfica e pyttsx3 para lê-la em voz alta.
Benefícios:

Auxilia pessoas com deficiência visual a navegar em ambientes desconhecidos.
Fornece uma descrição objetiva e precisa do ambiente.
Interface intuitiva e fácil de usar.
Instruções para uso:

Instale as bibliotecas necessárias (OpenCV, Tkinter, PIL, Google GenerativeAI, pyttsx3).
Execute o script app.py.
Permita o acesso à webcam.
Clique no botão "Analisar" para capturar e analisar a imagem.
A descrição da imagem será exibida na interface e lida em voz alta.
Observações:

Este projeto utiliza o modelo Gemini Pro Vision da Google AI, que requer uma chave de API.
O modelo pode ser trocado por outros modelos de análise de imagem, desde que sejam compatíveis com a interface.
