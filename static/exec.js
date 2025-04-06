function runCode(button) {
    const code = button.previousElementSibling.innerText;
    try {
      // Utilise un sandbox JS uniquement pour du JS généré
      const iframe = document.createElement('iframe');
      iframe.style.display = 'none';
      document.body.appendChild(iframe);
      const iframeWindow = iframe.contentWindow;
  
      iframeWindow.eval(code);
      alert("✅ Code exécuté (console ou résultat visible dans navigateur)");
    } catch (e) {
      alert("❌ Erreur : " + e.message);
    }
  }
  