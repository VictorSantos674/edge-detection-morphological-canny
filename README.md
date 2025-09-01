# 🌾 Edge Detection of Agricultural Products Based on Morphologically Improved Canny Algorithm

Este projeto reproduz o experimento descrito no artigo:
**"Edge Detection of Agricultural Products Based on Morphologically Improved Canny Algorithm"** (Xiaokang Yu et al., 2021).

## 📌 Objetivo
Implementar uma versão melhorada do operador de Canny para detecção de bordas em produtos agrícolas, utilizando:
- Filtros morfológicos compostos (A1, A2, A3);
- Gradiente em 4 direções (0°, 45°, 90°, 135°);
- Segmentação adaptativa baseada em Otsu;
- Duplo limiar para detecção de bordas.

## 📂 Estrutura do Repositório
- `docs/`: documentação e roteiro do vídeo;
- `data/`: imagens de teste (originais, com ruído e resultados);
- `src/`: código do algoritmo e módulos auxiliares;
- `notebooks/`: experimentos e análises;
- `tests/`: testes unitários.

## ▶️ Execução
Instale as dependências:
```bash
pip install -r requirements.txt

Execute o algoritmo em uma imagem:

python src/improved_canny.py --input data/originals/tomato.jpg --output data/results/tomato_edges.png


Ou use o notebook:

jupyter notebook notebooks/experiment.ipynb
```

## 🎥 Entrega

Cada integrante da equipe terá um momento de fala no vídeo (máx. 15 min), explicando:

O artigo e as melhorias propostas;

A implementação em Python;

Os resultados obtidos;

Comparação com o Canny tradicional.


---

## 🚀 Próximos Passos

1. **Resumo do artigo** → criar `docs/artigo_resumo.md` (já posso gerar isso para você).  
2. **Implementação modular** → separar em `preprocessing`, `gradient`, `thresholding`, `improved_canny`.  
3. **Dataset pequeno** → usar imagens de frutas/vegetais (ex.: tomates, maçãs, bananas) + adicionar ruído (sal e pimenta).  
4. **Vídeo** → preparar `docs/roteiro_video.md` para dividir as falas da equipe.  