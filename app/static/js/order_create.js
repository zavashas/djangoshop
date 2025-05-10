
document.getElementById('submit-btn').addEventListener('click', function () {
    Swal.fire({
        title: 'Подтвердите оформление',
        text: "Вы уверены, что хотите оформить заказ?",
        icon: 'question',
        showCancelButton: true,
        confirmButtonColor: '#28a745',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Да, оформить',
        cancelButtonText: 'Отмена'
    }).then((result) => {
        if (result.isConfirmed) {
            // Показываем загрузку
            Swal.fire({
                title: 'Оформляется...',
                text: 'Пожалуйста, подождите',
                allowOutsideClick: false,
                didOpen: () => {
                    Swal.showLoading();
                    // Отправляем форму
                    document.getElementById('order-form').submit();
                }
            });
        }
    });
});
 
