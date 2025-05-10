document.addEventListener('DOMContentLoaded', function () {
    const csrfToken = document.querySelector('#csrf-form input[name=csrfmiddlewaretoken]').value;

    document.querySelectorAll('.btn-qty-plus, .btn-qty-minus').forEach(button => {
        button.addEventListener('click', function () {
            const row = this.closest('tr');
            const productId = row.dataset.productId;
            const input = row.querySelector('.qty-input');
            let qty = parseInt(input.value);

            if (this.classList.contains('btn-qty-plus')) {
                qty += 1;
            } else if (this.classList.contains('btn-qty-minus') && qty > 1) {
                qty -= 1;
            }

            input.value = qty;

            fetch('/cart/update/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify({ product_id: productId, quantity: qty })
            })
            .then(response => response.json())
            .then(data => {
                row.querySelector('.item-total').textContent = data.item_total + ' руб.';
                document.getElementById('cart-total').textContent = data.cart_total + ' руб.';
            });
        });
    });
});
