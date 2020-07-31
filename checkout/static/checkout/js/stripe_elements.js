var stripePublicKey = $("#id_stripe_public_key").text().slice(1, -1);
var clientSecret = $("#id_client_secret").text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

var style = {
  base: {
    color: "##410D2F",
    fontFamily: "Roboto, sans-serif",
    fontSmoothing: "antialiased",
    fontSize: "16px",
    "::placeholder": {
      color: "##410D2F",
    },
  },
  invalid: {
    fontFamily: "Roboto, sans-serif",
    color: "#fa755a",
    iconColor: "#fa755a",
  },
};
var card = elements.create("card", { style: style });
card.mount("#card-element");

// Handle card errors
card.addEventListener("change", function (event) {
  var errorDiv = document.getElementById("card-errors");
  if (event.error) {
    var cardError = `
        <span class="icon" role="alert">
        <i class="fas fa-exclamation-triangle"></i>
        </span>
        <span>${event.error.message}</span>`;
    $(errorDiv).html(cardError);
  } else {
    errorDiv.textContent = "";
  }
});

// Stripe submit payment
var form = document.getElementById("payment-form");

form.addEventListener("submit", function (ev) {
  ev.preventDefault();
  card.update({ disable: true });
  // Overwrites submit button
  $("#submit-button").attr("disable", true);
  stripe
    .confirmCardPayment(clientSecret, {
      payment_method: {
        card: card,
        billing_details: {
          
        },
      },
    })
    .then(function (result) {
      if (result.error) {
        var errorDiv = document.getElementById("card-errors");
        var cardError = `
        <span class="icon" role="alert">
        <i class="fas fa-exclamation-triangle"></i>
        </span>
        <span>${result.error.message}</span>`;
        $(errorDiv).html(cardError);
        ev.preventDefault();
        card.update({ disable: false });
        $("#submit-button").attr("disable", false);
      } else {
        if (result.paymentIntent.status === "succeeded") {
          form.submit();
        }
      }
    });
});
