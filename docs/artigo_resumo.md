# 📄 Resumo do Artigo
**Título:** Edge Detection of Agricultural Products Based on Morphologically Improved Canny Algorithm  
**Autores:** Xiaokang Yu, Zhiwen Wang, Yuhang Wang, Canlong Zhang  
**Publicado em:** Mathematical Problems in Engineering, 2021  
**DOI:** [10.1155/2021/6664970](https://doi.org/10.1155/2021/6664970)  

---

## 🎯 Objetivo
Propor uma **versão melhorada do operador de Canny** para detecção de bordas em produtos agrícolas.  
A ideia é **reduzir falsos contornos** causados por iluminação/ruído e **preservar detalhes reais das bordas** dos objetos.

---

## 🔑 Problemas do Canny Tradicional
- Usa **filtro Gaussiano** fixo → pouco adaptável e pode apagar detalhes importantes.  
- Sofre com **ruído e variações de iluminação**, gerando bordas falsas.  
- Apenas considera **duas direções de gradiente** (0° e 90°).  
- **Limiar duplo fixo** → difícil escolher valores adequados para diferentes imagens.

---

## 🛠 Melhorias Propostas
1. **Filtro Morfológico Composto**  
   - Substitui o Gaussiano.  
   - Combina operações de abertura e fechamento com diferentes elementos estruturantes (pequenos e grandes).  
   - Fórmula final do filtro:
     ```
     A3 = 0.1 * (F ∘ B1) · B2 + 0.9 * (F · B2) ∘ B1
     ```
   - Preserva detalhes finos e remove ruídos (ex.: sal e pimenta).

2. **Cálculo do Gradiente em 4 Direções**  
   - Considera 0°, 45°, 90° e 135°.  
   - Melhora o posicionamento das bordas, evitando perda de contornos sutis.  

3. **Limiar Adaptativo (Otsu + Limiar Duplo)**  
   - Usa Otsu para segmentação inicial.  
   - Aplica **duplo limiar dinâmico** (alto e baixo) para decidir bordas reais.  
   - Elimina subjetividade na escolha manual.

---

## 📊 Resultados
- **Comparação com Canny tradicional e outro algoritmo de referência:**  
  - O método proposto gera bordas **mais conectadas** e com **menos falsos contornos**.  
  - Preserva bordas reais de frutas/vegetais (mesmo sob iluminação variável).  
  - Melhor desempenho em imagens com **ruído de sal e pimenta**.  

- **Métrica utilizada:**  
  - Razão **B/A** (bordas desconectadas sobre número total de pixels de borda).  
  - Valores **menores** no algoritmo proposto → melhor conectividade.  
  - **PSNR** mais alto em imagens ruidosas → melhor qualidade de reconstrução.  

---

## 🧩 Conclusões
- O algoritmo melhora a **robustez contra ruído** e a **detecção de contornos reais**.  
- Mais adequado para aplicações agrícolas (classificação, inspeção de qualidade, robôs de colheita).  
- Pode ser aplicado também em imagens típicas (ex.: Lena, objetos do cotidiano).  

---

## 🚀 Trabalhos Futuros
- Melhorar ainda mais a remoção de bordas falsas.  
- Validar em **aplicações práticas** (ex.: robôs agrícolas).  
- Explorar diferentes elementos estruturantes adaptados a formatos específicos de frutas e vegetais.

---