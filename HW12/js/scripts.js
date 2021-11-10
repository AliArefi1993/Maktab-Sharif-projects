// $(document).ready(function () {
//     $("btn").click(function () {
//         console.log("here")
//         $("#btn").hide();
//     });
// });

$(document).ready(function () {
    $('.btn.btn-outline-dark.mt-auto').on('click', function () {
        quantity = $("#cart").text()
        productName = $(this).parentsUntil()[2].children[2].children[0].children[0].textContent
        productPrice = $(this).parentsUntil()[2].children[2].children[0].children[2].nextSibling.textContent
        quantity = parseInt(quantity) + 1
        $("#cart").text(quantity);

        $('.modal-body-list').append(`<li>
        ${quantity}-  </span>  <span> ${productName}    </span>${productPrice}</P>
    </li>`)
    });
});