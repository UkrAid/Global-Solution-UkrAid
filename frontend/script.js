document
  .getElementById("feedbackForm")
  .addEventListener("submit", function (e) {
    e.preventDefault();

    const name = document.getElementById("feedName");
    const email = document.getElementById("feedEmail");
    const msg = document.getElementById("feedMsg");
    let valid = true;

    if (!name.value.trim() || name.value.trim().length < 2) {
      name.classList.add("error");
      document.getElementById("nameErr").textContent =
        "Por favor insira seu nome (mín. 2 caracteres).";
      valid = false;
    } else {
      name.classList.remove("error");
      document.getElementById("nameErr").textContent = "";
    }

    const emailRx = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRx.test(email.value.trim())) {
      email.classList.add("error");
      document.getElementById("emailErr").textContent =
        "Por favor insira um email válido.";
      valid = false;
    } else {
      email.classList.remove("error");
      document.getElementById("emailErr").textContent = "";
    }

    if (!msg.value.trim() || msg.value.trim().length < 10) {
      msg.classList.add("error");
      document.getElementById("msgErr").textContent =
        "Mensagem deve ter pelo menos 10 caracteres.";
      valid = false;
    } else {
      msg.classList.remove("error");
      document.getElementById("msgErr").textContent = "";
    }

    if (valid) {
      this.reset();
      const card = document.querySelector(".contact-form-wrapper");
      card.style.borderColor = "#16a34a";
      card.style.boxShadow = "0 0 24px rgba(22,163,74,0.2)";
      setTimeout(() => {
        card.style.borderColor = "";
        card.style.boxShadow = "";
      }, 4000);
    }
  });

["feedName", "feedEmail", "feedMsg"].forEach((id) => {
  document.getElementById(id).addEventListener("input", function () {
    this.classList.remove("error");
  });
});

// Slideshow
(function () {
  const track = document.querySelector(".slideshow-track");
  const dots = document.querySelectorAll(".dot");
  const total = document.querySelectorAll(".slide").length;
  let current = 0;
  let timer;

  function goTo(idx) {
    current = (idx + total) % total;
    track.style.transform = "translateX(-" + current * 100 + "%)";
    dots.forEach(function (d, i) {
      d.classList.toggle("active", i === current);
    });
  }

  function next() { goTo(current + 1); }
  function prev() { goTo(current - 1); }

  function startAuto() {
    timer = setInterval(next, 4500);
  }

  function resetAuto() {
    clearInterval(timer);
    startAuto();
  }

  document.querySelector(".slideshow-btn.next").addEventListener("click", function () { next(); resetAuto(); });
  document.querySelector(".slideshow-btn.prev").addEventListener("click", function () { prev(); resetAuto(); });
  dots.forEach(function (d, i) {
    d.addEventListener("click", function () { goTo(i); resetAuto(); });
  });

  goTo(0);
  startAuto();
})();

// Quiz
(function () {
  var perguntas = [
    {
      texto: "Qual API a UkrAid utiliza para monitorar alertas aéreos na Ucrânia?",
      opcoes: ["ACLED", "UkraineAlarm", "OpenStreetMap", "Nominatim"],
      correta: 1,
    },
    {
      texto: "Quantas APIs estão integradas na plataforma UkrAid?",
      opcoes: ["2", "3", "4", "5"],
      correta: 2,
    },
    {
      texto: "Para que serve a API ACLED na UkrAid?",
      opcoes: [
        "Localizar hospitais próximos",
        "Monitorar alertas aéreos",
        "Registrar eventos de conflito geolocalizados",
        "Geocodificar endereços",
      ],
      correta: 2,
    },
    {
      texto: "Qual ferramenta a UkrAid usa para encontrar abrigos e hospitais próximos?",
      opcoes: ["ACLED", "UkraineAlarm", "OpenStreetMap", "Google Maps"],
      correta: 2,
    },
    {
      texto: "A UkrAid exige cadastro ou autenticação para acessar dados de risco?",
      opcoes: [
        "Sim, sempre",
        "Sim, para funcionalidades avançadas",
        "Não — acesso aberto por design",
        "Depende da região",
      ],
      correta: 2,
    },
  ];

  var atual = 0;
  var pontos = 0;
  var respondida = false;

  var counter = document.querySelector(".quiz-counter");
  var barFill = document.querySelector(".quiz-bar-fill");
  var questionEl = document.querySelector(".quiz-question");
  var optionsEl = document.querySelector(".quiz-options");
  var feedbackEl = document.querySelector(".quiz-feedback");
  var navBtn = document.getElementById("quizNavBtn");
  var resultEl = document.querySelector(".quiz-result");
  var quizBody = document.querySelector(".quiz-body");

  function renderPergunta() {
    respondida = false;
    var p = perguntas[atual];
    var prog = (atual / perguntas.length) * 100;

    counter.textContent = "Pergunta " + (atual + 1) + " de " + perguntas.length;
    barFill.style.width = prog + "%";
    questionEl.textContent = p.texto;
    feedbackEl.textContent = "";
    feedbackEl.className = "quiz-feedback";
    navBtn.textContent = atual < perguntas.length - 1 ? "Próxima →" : "Ver Resultado";
    navBtn.disabled = true;

    optionsEl.innerHTML = "";
    p.opcoes.forEach(function (op, i) {
      var btn = document.createElement("button");
      btn.className = "quiz-option";
      btn.textContent = op;
      btn.addEventListener("click", function () { responder(i); });
      optionsEl.appendChild(btn);
    });
  }

  function responder(idx) {
    if (respondida) return;
    respondida = true;
    var p = perguntas[atual];
    var btns = optionsEl.querySelectorAll(".quiz-option");

    btns.forEach(function (btn, i) {
      btn.disabled = true;
      if (i === p.correta && idx !== p.correta) {
        btn.classList.add("reveal");
      }
    });

    if (idx === p.correta) {
      btns[idx].classList.add("correct");
      feedbackEl.textContent = "✓ Correto!";
      feedbackEl.className = "quiz-feedback acerto";
      pontos++;
    } else {
      btns[idx].classList.add("wrong");
      feedbackEl.textContent = "✗ Incorreto. A resposta certa está destacada.";
      feedbackEl.className = "quiz-feedback erro";
    }

    navBtn.disabled = false;
  }

  function mostrarResultado() {
    var pct = Math.round((pontos / perguntas.length) * 100);
    var msg;
    if (pct === 100) {
      msg = "Perfeito! Você é um especialista em UkrAid.";
    } else if (pct >= 60) {
      msg = "Bom trabalho! Você conhece bem a plataforma.";
    } else {
      msg = "Continue explorando — cada detalhe pode salvar vidas.";
    }

    quizBody.style.display = "none";
    resultEl.style.display = "block";
    resultEl.querySelector(".quiz-score").textContent = pontos + "/" + perguntas.length;
    resultEl.querySelector(".quiz-result-msg").textContent = msg;
    barFill.style.width = "100%";
    counter.textContent = "Concluído";
  }

  navBtn.addEventListener("click", function () {
    if (!respondida) return;
    if (atual < perguntas.length - 1) {
      atual++;
      renderPergunta();
    } else {
      mostrarResultado();
    }
  });

  document.getElementById("quizReiniciar").addEventListener("click", function () {
    atual = 0;
    pontos = 0;
    quizBody.style.display = "block";
    resultEl.style.display = "none";
    renderPergunta();
  });

  renderPergunta();
})();

// Seletor de Tema
(function () {
  var btns = document.querySelectorAll(".theme-btn");
  var html = document.documentElement;

  btns.forEach(function (btn) {
    btn.addEventListener("click", function () {
      var tema = btn.dataset.themeVal;
      if (tema === "padrao") {
        delete html.dataset.theme;
      } else {
        html.dataset.theme = tema;
      }
      btns.forEach(function (b) {
        b.classList.toggle("active", b === btn);
      });
    });
  });
})();
