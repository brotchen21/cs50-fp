function removeItems(productId) {
    console.log(productId);
    fetch(`/remove_items/${productId}`, {
      method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
          location.reload();
        } else {
          alert(data.message);
        }
    });
  }
  function completeOrder() {
    if (confirm("Do you want to confirm your order?")) {
        alert("Order is registered");
    }
}