# AI.md — Documentação das Implementações com IA

Este documento descreve as três funcionalidades adicionadas à landing page da UkrAid por meio de assistência de IA, incluindo a lógica por trás de cada recurso e orientações de manutenção.

---

## 1. Slideshow de Imagens (Galeria)

### O que foi implementado

Uma seção `#galeria` com carrossel responsivo que exibe as três imagens do diretório `frontend/Images/`:

- `Kyiv.jpeg` — Vista de satélite de Kyiv
- `Ukraine-War.jpg` — Zona de conflito ativo
- `ACLED - Img.png` — Visualização de dados ACLED

### Lógica

- O carrossel usa `flexbox` com `translateX` para deslizar entre os slides sem remover elementos do DOM, garantindo transições suaves.
- Avanço automático a cada 4,5 segundos via `setInterval`.
- Navegação manual pelos botões `prev`/`next` e pelos indicadores de ponto (`.dot`). Qualquer interação manual reinicia o temporizador automático.
- Acessibilidade: todos os botões possuem `aria-label` e as imagens possuem `alt` descritivos.

### Como manter

- Para adicionar novas imagens: coloque o arquivo em `frontend/Images/`, adicione um novo `<div class="slide">` no HTML e um novo `<button class="dot">` na `.slideshow-dots`. O JavaScript detecta o total de slides automaticamente via `querySelectorAll(".slide").length`.
- Para alterar o intervalo automático: modifique o valor `4500` (ms) na chamada `setInterval` em `script.js`.

---

## 2. Quiz Interativo

### O que foi implementado

Uma seção `#quiz` com cinco perguntas de múltipla escolha sobre a plataforma UkrAid e segurança civil. O quiz fornece feedback imediato a cada resposta e exibe uma pontuação final com mensagem personalizada.

### Lógica

- As perguntas são definidas como um array de objetos (`perguntas`) em `script.js`, cada um com `texto`, `opcoes[]` e o índice da `correta`.
- A barra de progresso (`.quiz-bar-fill`) avança proporcionalmente após cada pergunta.
- Ao responder: opções corretas recebem a classe `.correct` (verde), incorretas recebem `.wrong` (vermelho) e a resposta certa é revelada com `.reveal` caso o usuário erre.
- O botão "Próxima →" fica desabilitado até que o usuário responda, evitando pulos acidentais.
- Ao concluir, o quiz exibe o placar final e uma mensagem de acordo com o desempenho (100% → "Perfeito", ≥60% → "Bom trabalho", <60% → mensagem de encorajamento).
- O botão "Reiniciar Quiz" restaura todas as variáveis ao estado inicial sem recarregar a página.

### Como manter

- Para adicionar ou editar perguntas: modifique o array `perguntas` em `script.js`. Cada objeto deve seguir a estrutura `{ texto, opcoes[], correta }` onde `correta` é o índice (base 0) da opção correta.
- Para alterar o número de perguntas: basta adicionar ou remover objetos do array. O contador e a barra de progresso se ajustam automaticamente.

---

## 3. Seletor de Tema

### O que foi implementado

Três botões circulares coloridos na barra de navegação que permitem alternar entre três temas visuais distintos, sem recarregar a página:

| Tema           | Atributo `data-theme` | Paleta                                |
| -------------- | --------------------- | ------------------------------------- |
| Padrão         | _(nenhum)_            | Roxo profundo / preto — tema original |
| Naval          | `naval`               | Azul marinho escuro / ciano gelo      |
| Alto Contraste | `alto-contraste`      | Verde-escuro / teal vibrante          |

### Lógica

- Os temas são implementados com **CSS Custom Properties** sobrepostos via seletores `[data-theme="naval"]` e `[data-theme="alto-contraste"]` aplicados ao elemento `<html>`.
- O JavaScript adiciona ou remove o atributo `data-theme` do `document.documentElement` ao clicar em cada botão. Para o tema padrão, o atributo é deletado.
- Como todas as cores do site já usam variáveis CSS (`var(--bg)`, `var(--glow)`, etc.), a troca de tema é instantânea e não quebra nenhum layout existente.
- O `.nav-aid` foi atualizado para usar `var(--glow)` no `text-shadow` em vez de `#a855f7` fixo, garantindo que o efeito de brilho reaja corretamente à mudança de tema.

### Como manter

- Para criar um novo tema: adicione um bloco `[data-theme="nome-do-tema"] { ... }` em `style.css` sobrescrevendo as variáveis desejadas. Depois adicione um novo `<button class="theme-btn">` no HTML e atualize a cor do botão com `.theme-btn[data-theme-val="nome-do-tema"] { background: #cor; }`.
- A preferência de tema não é persistida entre sessões. Para persistir, armazene o valor do tema em `localStorage` e aplique-o no carregamento da página.

---

## Estrutura de Arquivos Modificados

```
frontend/
├── index.html   — Adicionados: nav links (Galeria, Quiz), theme switcher, seção #galeria, seção #quiz
├── style.css    — Adicionados: temas naval/alto-contraste, estilos do slideshow, estilos do quiz, keyframes pulseGlow
├── script.js    — Adicionados: IIFE slideshow, IIFE quiz, IIFE seletor de tema
└── webdev.ai/
    └── AI.md    — Este arquivo
```

## Prompt Utilizado

You are an expert frontend developer. I need you to read all the existing files in my project to understand its current architecture, structure, and CSS styling. Your goal is to implement three new features and create a documentation file, strictly adhering to the established design system, classes, and code patterns.

Here are the specific tasks:

1. **Image Slideshow:**
   - Create a responsive slideshow/carousel section.
   - It must automatically cycle through (and allow manual navigation of) the three images located in the `frontend/images` directory.
   - Match the layout and container styles of the existing sections.

2. **Dynamic Quiz:**
   - Add a dynamic, interactive quiz section related to the theme of this project.
   - It should feature multiple-choice questions, provide immediate feedback upon submission, and display a final score.
   - Ensure the UI components (buttons, cards, text) match the existing site theme.

3. **Theme/Background Switcher:**
   - Implement a theme-switching functionality (e.g., a button, dropdown, or toggle group).
   - Provide 3 distinct theme options:
     - **Option 1:** The original page theme/background.
     - **Option 2:** A custom theme created by you (e.g., Dark Mode if original is light, or a sleek minimal variant).
     - **Option 3:** A second custom theme created by you (e.g., a vibrant or high-contrast variant).
   - Ensure this seamlessly updates the background and relevant text colors without breaking existing layout styles.

4. **Documentation File:**
   - After successfully implementing and testing all the features above, create a new file named `AI.md`.
   - Save this file inside the `frontend/webdev.ai` directory.
   - Inside `AI.md`, briefly document the changes you made, the logic behind the quiz/theme features, and how to maintain them.

**Strict Guidelines:**

- Do not rewrite existing working logic unless necessary to integrate the new features.
- Match the exact CSS/Tailwind/SASS styling, naming conventions, and formatting found in the source code.
- Write clean, commented, and modular code.

Please review the codebase first, then present the updated code or file structures.
