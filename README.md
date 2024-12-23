# Análise de Dados do Vestibular ITA - 1ª Fase (2025)

## Introdução

Este projeto tem como objetivo realizar uma análise exploratória de dados (EDA) baseada nos resultados da 1ª fase do vestibular do ITA (Instituto Tecnológico de Aeronáutica) para identificar padrões de desempenho, relações entre notas e insights relevantes que possam ser utilizados para futuras estratégias de estudo e análise.

---

## Etapas do Projeto

### 1. Limpeza\*\* de Dados\*\*

Os dados utilizados foram obtidos a partir do site oficial do vestibular, contendo informações organizadas em colunas com dados dos candidatos. O processamento foi realizado utilizando Python e bibliotecas especializadas para manipulação e análise de dados.

#### Bibliotecas Utilizadas:

- **pandas**: Manipulação de estruturas de dados.
- **numpy**: Realização de cálculos matemáticos e estatísticos.
- **matplotlib** e **seaborn**: Visualização de dados com gráficos estatísticos.

#### Procedimentos:

1. Importação dos dados em formato tabular.
2. Limpeza e padronização dos dados para correção de valores ausentes ou inconsistentes.
3. Conversão de tipos de dados para formatos adequados, como `float` para colunas de notas.

---

### 2. **Análise Exploratória de Dados (EDA)**

A EDA foi conduzida para entender o comportamento dos dados, identificar relações e destacar padrões importantes. Foram realizadas as seguintes análises:

#### Estatísticas Descritivas:

- **Médias, medianas e desvios-padrão** das notas de cada matéria.
- Ordenação dos candidatos com base em cada matéria.
- Análise dos percentis de cada matéria.

#### Visualizações:

1. **Histogramas:** Mostram a distribuição das notas dos candidatos em diferentes categorias.
2. **Boxplots:** Evidenciam a dispersão e outliers em cada tipo de nota.
3. **Heatmaps de Correlação:** Destacam relações entre as notas de matérias e média final.

#### Resultados Identificados:

- As notas apresentaram distribuição assimétrica, com a maioria concentrada entre os valores 3,5 e 4,0.
- As correlações entre cada matéria e a média não foram tão distantes, mas seguiram a ordem: matemática -> física -> química.
- As médias também seguiram a mesma ordem, tendo sido a de matemática a mais baixa e a de química a mais alta, entre as exatas.
- Outliers foram identificados principalmente nas notas de inglês, indicando desempenhos excepcionalmente altos ou baixos.

---

### 3. **Insights Relevantes**

Os seguintes insights foram obtidos a partir das análises realizadas:

1. **Desempenho Geral:**

   - A maioria dos candidatos apresenta notas baixas, sugerindo dificuldades gerais na prova.
   - Um pequeno grupo de candidatos destaca-se com notas consistentemente altas, indicando um perfil de excelência acadêmica.

2. **Correlações Importantes:**

   - A dificuldade da prova de matemática parece ter feito-a se distanciar da distribuição de médias mais do que o normal, sugerindo que talvez a mesma não tenha servido tão bem para avaliar o perfil dos candidatos quanto a prova de química, por exemplo.

---

### 4. **Conclusões e Relevância**

Este projeto demonstrou como a análise de dados pode ser usada para entender melhor os resultados de uma prova competitiva como o vestibular do ITA.

#### Pontos de Destaque:

- **Estatísticas detalhadas**: Auxiliam na compreensão das características gerais dos candidatos.
- **Visualizações claras**: Facilitaram a comunicação dos resultados.
- **Insights práticos**: Possíveis aplicações incluem o ajuste de estratégias de estudo para candidatos futuros ou a **otimização da elaboração de provas**.

---

### 5. **Extensões Futuras**

- Ampliar a análise quando forem divulgados os resultados da segunda fase do vestibular.
- Investigar possíveis relações entre região de origem dos candidatos e desempenho, bem como fazer análises específicas para o segmento de candidatos cotistas.
- Criar dashboards interativos para visualização dinâmica dos dados.

Este projeto serve como uma peça importante para a minha formação como cientista de dados, destacando habilidades em manipulação de dados, visualização e análise estatística.

