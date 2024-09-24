let but = document.getElementById('but1')
let elements = document.getElementsByClassName('tovar-text');

function openForm() {
    document.getElementById("myForm").style.display = "block";
}
function closeForm() {
    document.getElementById("myForm").style.display = "none";
}
$(but).click(function(event) {
  event.preventDefault();
  let name = $(".classInputName").val();
  let email = $(".classInputEmail").val();
  let adress = $(".classInputAdress").val();
  let tovar = []
  for (let i = 0; i < elements.length; i++) {
  tovar.push(elements[i].textContent);
}

  $.ajax({
    url: "https://api.telegram.org/bot"+"токен заменить"+"/sendMessage?chat_id="+chatId,
    method: "POST",
    data: {
      chat_id: chatId,
      text: ('Имя: '+name + '\n' + 'Email: ' + email + '\n' + 'Адрес: ' + adress + '\n' + 'Товары: ' + tovar)
    },
    success: function(response) {
      alert("Заказ оформлен!");
    },
    error: function(xhr, status, error) {
      console.log(xhr.responseText);
    }
  });
});
