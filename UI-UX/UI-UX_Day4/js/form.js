document.addEventListener('DOMContentLoaded', function () {
    const submit = document.querySelector('#submit');

    if (submit) {
        submit.addEventListener('click', function (even) {
            even.preventDefault();

            window.location.href = 'billing.html';
        });
    }
});