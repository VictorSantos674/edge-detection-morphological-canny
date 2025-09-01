# 🧪 Metodologia de Implementação

Este documento descreve como será feita a implementação do algoritmo proposto no artigo  
**"Edge Detection of Agricultural Products Based on Morphologically Improved Canny Algorithm"**.

---

## 🔄 Pipeline do Algoritmo

1. **Carregar a Imagem**
   - Entrada: imagem em escala de cinza ou RGB (convertida para cinza).
   - Pasta: `data/originals/`.

2. **Pré-processamento com Filtro Morfológico Composto**
   - Substitui o filtro Gaussiano.
   - Operações de morfologia:
     - **Abertura (∘)** → remove ruído claro (picos).
     - **Fechamento (·)** → remove ruído escuro (fendas).
   - Filtros básicos:
     ```
     A1 = (F ∘ B) · B
     A2 = (F · B) ∘ B
     ```
   - Filtro composto:
     ```
     A3 = 0.1 * A1 + 0.9 * A2
     ```
   - Elementos estruturantes:  
     - `B1` = cruz 3x3  
     - `B2` = losango 5x5  

3. **Cálculo do Gradiente**
   - Tradicionalmente: apenas 0° e 90°.
   - Neste trabalho: **4 direções** (0°, 45°, 90°, 135°).
   - Fórmulas:
     ```
     M(x, y) = sqrt(gx² + gy² + g45² + g135²)
     θ(x, y) = arctan(gy / gx)
     ```
   - Implementado em `gradient.py`.

4. **Supressão de Não-Máximos**
   - Mantém apenas os pontos com maior intensidade ao longo da direção do gradiente.
   - Implementado em `improved_canny.py`.

5. **Segmentação por Limiar Adaptativo**
   - Método de Otsu → encontra um limiar inicial automaticamente.
   - Resultado = **segmentação bruta** da imagem.

6. **Duplo Limiar Dinâmico**
   - Aplica thresholds **alto (Th)** e **baixo (Tl)**.
   - Regras:
     - `M(x,y) < Tl` → não é borda.
     - `M(x,y) > Th` → é borda forte.
     - `Tl <= M(x,y) <= Th` → borda fraca → só vira borda se conectada a uma forte.

7. **Resultado Final**
   - Imagem binária de bordas refinadas.
   - Exportada para `data/results/`.

---

## 📂 Organização dos Módulos

- `preprocessing.py` → operações morfológicas (A1, A2, A3).
- `gradient.py` → cálculo do gradiente em 4 direções.
- `thresholding.py` → Otsu adaptativo + duplo limiar.
- `improved_canny.py` → pipeline completo (main).
- `utils.py` → carregamento, visualização e funções auxiliares.

---

## 📊 Avaliação dos Resultados

- **Visual** → comparar bordas detectadas com Canny tradicional.  
- **Métrica Quantitativa**:
  - **B/A** (conectividade das bordas).  
  - **PSNR** em imagens com ruído.

---

## 👥 Divisão de Tarefas (sugestão para equipe)

- **Integrante 1:** Implementação dos filtros morfológicos.  
- **Integrante 2:** Cálculo do gradiente em 4 direções.  
- **Integrante 3:** Segmentação adaptativa (Otsu + thresholds).  
- **Integrante 4:** Integração e execução do pipeline (`improved_canny.py`).  
- **Todos:** Preparação do vídeo, apresentação e análise dos resultados.

---