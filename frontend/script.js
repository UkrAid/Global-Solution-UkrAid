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
