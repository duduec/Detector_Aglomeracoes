# Detector de Aglomerações em Eventos

Este projeto utiliza inteligência artificial com modelos pré-treinados YOLOv8 para identificar e alertar sobre aglomerações excessivas em vídeos de eventos públicos, como shows, feiras e manifestações. A ferramenta pode ser usada como apoio para equipes de segurança ou análise pós-evento.

## 🎯 Objetivo

Detectar automaticamente, por meio de visão computacional, áreas onde há uma concentração excessiva de pessoas em um vídeo. Quando a quantidade de pessoas em uma região excede um limite configurável, o sistema emite um alerta no console.

## 🚀 Tecnologias e Bibliotecas

- Python 3.10+
- [YOLOv8](https://github.com/ultralytics/ultralytics) (via `ultralytics`)
- OpenCV
- Numpy
- `uv` para gerenciamento de dependências
- Pytest para testes automatizados

## 📁 Estrutura do Projeto

```
Projeto_Aglomeracoes/
├── main.py
├── projeto.toml
├── yolov8n.pt
├── src/
│   └── aglomeracao/
│       └── logica_detector.py
├── tests/
│   └── test_logica_detector.py
└── README.md
```

## ▶️ Como Executar

1. Clone o repositório:

```bash
git https://github.com/duduec/Detector_Aglomeracoes.git
cd Projeto_Aglomeracoes
```

2. Instale as dependências com `uv`:

```bash
uv venv
uv pip install -r requirements.txt
```

3. Rode o script principal:

```bash
python main.py exemplo_video.mp4
```

## 🧪 Testes

Para executar os testes automatizados:

```bash
test_logica_detector.py
```

## ⚙️ Configurações

Você pode ajustar o limite de pessoas por frame no arquivo `logica_detector.py`, alterando a variável `LIMITE_PESSOAS`.

## 📌 Observações

- O modelo usado por padrão é o `yolov8n.pt`, mais leve e rápido. Para mais precisão, troque por `yolov8l.pt`.
- O projeto funciona com vídeos em formato `.mp4`.

## 📸 Exemplo de uso

> Ao processar o vídeo, o sistema imprime no terminal alertas como:

```
Frame 342: Aglomeração detectada! Pessoas: 57
```

## 🧠 Créditos

Baseado na estrutura e ideia original de projeto de detecção com YOLOv8, adaptado para o contexto de segurança em eventos.

## 👩‍💻 Autoria

Projeto desenvolvido por Isadora Machado e Eduardo Castanho, como parte da disciplina de Desenvolvimento de Aplicações com Inteligência Artificial do curso de Análise e Desenvolvimento de Sistemas da Faculdade Senac Pelotas – 2025.