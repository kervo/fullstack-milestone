var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();

var style = {
      base: {
        color: "##410D2F",
        fontFamily: 'Roboto, sans-serif',
        fontSmoothing: "antialiased",
        fontSize: "16px",
        "::placeholder": {
          color: "##410D2F"
        }
      },
      invalid: {
        fontFamily: 'Roboto, sans-serif',
        color: "#fa755a",
        iconColor: "#fa755a"
      }
    };
var card = elements.create('card', {style: style});
card.mount('#card-element');

