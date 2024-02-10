# Assistente de Navegação com Análise de Imagem

## Descrição:


Descrição Detalhada do Sistema:
Objetivo:

Auxiliar pessoas com deficiência visual na navegação e compreensão do ambiente ao seu redor.

Funcionamento:

A câmera do dispositivo é utilizada para capturar imagens do ambiente em tempo real. As imagens capturadas são pré-processadas para otimizar a análise e extração de informações. O sistema utiliza um modelo de inteligência artificial de última geração para analisar as imagens e identificar objetos, pessoas, texto e outras características relevantes do ambiente. Uma descrição textual detalhada da cena é gerada com base na análise da imagem, utilizando linguagem natural e vocabulário adequado ao contexto. Desta forma a descrição textual é convertida em áudio falado, utilizando um motor de síntese de voz de alta qualidade, permitindo que o usuário ouça a descrição da cena em tempo real.

# Sistema de Auxílio para Deficientes Visuais

## Objetivo

Auxiliar pessoas com deficiência visual na navegação e compreensão do ambiente ao seu redor.

## Funcionamento

1. **Captura de Imagem:** A câmera do dispositivo é utilizada para capturar imagens do ambiente em tempo real.
2. **Processamento de Imagem:** As imagens capturadas são pré-processadas para otimizar a análise e extração de informações.
3. **Análise de Imagem:** Utiliza um modelo de inteligência artificial para identificar objetos, pessoas, texto e outras características relevantes do ambiente.
4. **Geração de Texto:** Uma descrição textual detalhada da cena é gerada com base na análise da imagem, utilizando linguagem natural.
5. **Síntese de Voz:** A descrição textual é convertida em áudio falado, permitindo que o usuário ouça a descrição da cena em tempo real.

## Funcionalidades

- **Análise em Tempo Real:** Opera continuamente, fornecendo feedback auditivo ao usuário.
- **Descrição Detalhada:** Inclui informações sobre objetos, pessoas, texto, cores, texturas, formas, localização espacial e outros elementos relevantes da cena.
- **Personalização:** Permite que o usuário ajuste a velocidade da fala, o volume, o idioma e outros parâmetros.
- **Interação Natural:** Oferece uma interface amigável e intuitiva para interação eficiente.

## Benefícios

- **Maior Independência:** Permite que pessoas com deficiência visual naveguem com mais autonomia e segurança.
- **Acesso à Informação:** Facilita o acesso à informação presente no ambiente.
- **Inclusão Social:** Promove a inclusão social e digital das pessoas com deficiência visual.

## Tecnologias Utilizadas

- **Visão Computacional:** Técnicas de processamento de imagem e inteligência artificial.
- **Generative AI:** Modelos de linguagem avançados para geração de texto natural.
- **Síntese de Voz:** Motores de conversão de texto em fala para reprodução de áudio de alta qualidade.
- **Interface Gráfica:** Interfaces amigáveis e intuitivas.

## Aplicações

- **Navegação Interna e Externa:** Auxilia na locomoção em casa, trabalho, ruas, parques e outros locais.
- **Identificação de Objetos e Pessoas:** Reconhece objetos, pessoas e outros elementos no ambiente.
- **Leitura de Texto:** Lê placas, anúncios, produtos, documentos e outros textos impressos.
- **Interação com Computadores:** Auxilia na utilização de computadores e dispositivos móveis.

## Público-Alvo

- Pessoas com deficiência visual total ou parcial.
- Pessoas com baixa visão.
- Pessoas com cegueira adquirida.
- Idosos com dificuldades de visão.

## Observações

- Este sistema é um protótipo funcional e pode ser aprimorado com o desenvolvimento de novas funcionalidades e a integração com outras tecnologias.
  
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
