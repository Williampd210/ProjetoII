function openPopup() {
    document.getElementById("popup").style.display = "flex";
    document.getElementById("login-error-message").style.display = "none";
  }
  function closePopup() {
    document.getElementById("popup").style.display = "none";
    clearFormFields();
  }
  function showForm(form) {
    if (form === 'login') {
      document.getElementById('login-form').style.display = 'block';
      document.getElementById('signup-form').style.display = 'none';
      document.querySelector('.tab-btn.active').classList.remove('active');
      document.querySelector('.tab-btn:nth-child(1)').classList.add('active');
    } else {
      document.getElementById('signup-form').style.display = 'block';
      document.getElementById('login-form').style.display = 'none';
      document.querySelector('.tab-btn.active').classList.remove('active');
      document.querySelector('.tab-btn:nth-child(2)').classList.add('active');
    }
  }
  function registerUser() {
    const name = document.getElementById('signup-name').value;
    const email = document.getElementById('signup-email').value.toLowerCase();
    const password = document.getElementById('signup-password').value;
    const confirmPassword = document.getElementById('signup-confirm-password').value;
    if (password !== confirmPassword) {
      alert('As senhas não coincidem!');
      return;
    }
    localStorage.setItem('user', JSON.stringify({ name, email, password }));
    alert('Cadastro realizado com sucesso!');
    clearFormFields();
    closePopup();
  }
  function loginUser() {
    const email = document.getElementById('login-email').value.toLowerCase();
    const password = document.getElementById('login-password').value;

    const user = JSON.parse(localStorage.getItem('user'));

    if (user && user.email === email && user.password === password) {
      alert('Login efetuado com sucesso!');
      clearFormFields();
      closePopup();
    } else {
      const errorMessage = document.getElementById('login-error-message');
      errorMessage.style.display = 'block';
    }
  }
  function clearFormFields() {
    document.getElementById('login-email').value = '';
    document.getElementById('login-password').value = '';
    document.getElementById('signup-name').value = '';
    document.getElementById('signup-email').value = '';
    document.getElementById('signup-password').value = '';
    document.getElementById('signup-confirm-password').value = '';
  }