# 🎥 Roteiro para Gravação do Vídeo

## ⏱️ Duração Máxima
15 minutos (aproximadamente 2 a 3 minutos por integrante).

---

## 🗣️ Estrutura das Falas

### 1. Abertura e Contextualização (Integrante 1)
- Saudação inicial.
- Apresentação da equipe.
- Explicar o objetivo do trabalho:
  - Reproduzir experimento de um artigo científico.
  - Tema 6: *"Edge Detection of Agricultural Products Based on Morphologically Improved Canny Algorithm"*.
- Destacar brevemente o problema do Canny tradicional:
  - Filtro Gaussiano fixo.
  - Dificuldade em ruídos e iluminação.
  - Limiar fixo e perda de bordas.

⏱️ Tempo: ~2 minutos

---

### 2. Explicação da Metodologia (Integrante 2)
- Mostrar pipeline do algoritmo:
  1. Filtro morfológico composto (substitui o Gaussiano).
  2. Gradiente em 4 direções (0°, 45°, 90°, 135°).
  3. Otsu adaptativo para segmentação.
  4. Duplo limiar dinâmico.
- Explicar como cada etapa melhora o Canny original.
- Ressaltar a importância da morfologia para preservar detalhes de frutas e vegetais.

⏱️ Tempo: ~3 minutos

---

### 3. Implementação em Python (Integrante 3)
- Mostrar a organização do repositório:
  - `src/` → código modular (pré-processamento, gradiente, thresholds, pipeline).
  - `data/` → imagens originais, com ruído e resultados.
  - `docs/` → documentação.
- Explicar brevemente um trecho de código:
  - Como aplicar o filtro morfológico.
  - Como calcular o gradiente em 4 direções.
- Destacar que usamos **OpenCV**, **NumPy** e **Scikit-image**.

⏱️ Tempo: ~3 minutos

---

### 4. Resultados Experimentais (Integrante 4)
- Mostrar imagens de comparação:
  - Canny tradicional vs. algoritmo melhorado.
  - Sem ruído e com ruído (sal e pimenta).
- Explicar métricas utilizadas:
  - **B/A** → conectividade das bordas.
  - **PSNR** → qualidade sob ruído.
- Ressaltar que o algoritmo proposto:
  - Reduziu bordas falsas.
  - Aumentou conectividade real.
  - Melhorou desempenho sob ruído.

⏱️ Tempo: ~3 minutos

---

### 5. Conclusão e Encerramento (Todos)
- Cada integrante pode falar uma frase curta:
  - Importância do método em visão computacional.
  - Possíveis aplicações (robôs de colheita, inspeção de qualidade).
  - Limitações atuais e melhorias futuras.
- Agradecimentos finais.

⏱️ Tempo: ~3 minutos

---

## 📌 Dicas para o Vídeo
- Usar slides simples com imagens do artigo e resultados do código.
- Alternar fala entre integrantes de forma natural.
- Não ultrapassar 15 minutos.
- Mostrar resultados práticos (antes/depois) no vídeo para reforçar o impacto.

---