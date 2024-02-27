document.querySelector('form').addEventListener('submit', function(event) {
    const password = document.querySelector('#password').value;
    const confirmPassword = document.querySelector('#confirm_password').value;

    if (password !== confirmPassword) {
        alert('Пароли не совпадают!');
        event.preventDefault();
    }
});