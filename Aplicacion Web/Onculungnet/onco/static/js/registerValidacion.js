document.getElementById('registerForm').addEventListener('submit', function(event) {
    let isValid = true;
    let errorMessages = '';

    // Validar el nombre de usuario (no vacío y sin espacios en blanco)
    const username = document.getElementById('id_username').value;
    if (username.trim() === '') {
        errorMessages += 'El nombre de usuario es obligatorio.\n';
        isValid = false;
    }
    if (username.includes(' ')) {
        errorMessages += 'El nombre de usuario no puede contener espacios en blanco.\n';
        isValid = false;
    }

    // Validar el correo electrónico (no vacío y formato válido)
    const email = document.getElementById('id_email').value;
    const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    if (!emailPattern.test(email)) {
        errorMessages += 'Por favor, ingresa un correo electrónico válido.\n';
        isValid = false;
    }

    // Validar la contraseña (mínimo 8 caracteres, máximo 20, al menos una mayúscula, una minúscula, un número, un carácter especial, sin espacios en blanco)
    const password1 = document.getElementById('id_password1').value;
    const password2 = document.getElementById('id_password2').value;

    const minLength = 8;
    const maxLength = 20;
    const upperCasePattern = /[A-Z]/;
    const lowerCasePattern = /[a-z]/;
    const numberPattern = /[0-9]/;
    const specialCharPattern = /[!@#$%^&*]/;

    if (password1.length < minLength) {
        errorMessages += 'La contraseña debe tener al menos ' + minLength + ' caracteres.\n';
        isValid = false;
    }
    if (password1.length > maxLength) {
        errorMessages += 'La contraseña no debe exceder ' + maxLength + ' caracteres.\n';
        isValid = false;
    }
    if (!upperCasePattern.test(password1)) {
        errorMessages += 'La contraseña debe contener al menos una letra mayúscula.\n';
        isValid = false;
    }
    if (!lowerCasePattern.test(password1)) {
        errorMessages += 'La contraseña debe contener al menos una letra minúscula.\n';
        isValid = false;
    }
    if (!numberPattern.test(password1)) {
        errorMessages += 'La contraseña debe contener al menos un número.\n';
        isValid = false;
    }
    if (!specialCharPattern.test(password1)) {
        errorMessages += 'La contraseña debe contener al menos un carácter especial (por ejemplo, !@#$%^&*).\n';
        isValid = false;
    }
    if (password1.includes(' ')) {
        errorMessages += 'La contraseña no puede contener espacios en blanco.\n';
        isValid = false;
    }

    // Validar que las contraseñas coinciden
    if (password1 !== password2) {
        errorMessages += 'Las contraseñas no coinciden.\n';
        isValid = false;
    }

    // Si hay errores, evitar el envío del formulario
    if (!isValid) {
        alert(errorMessages);
        event.preventDefault(); // Prevenir el envío del formulario
    }
});