// this identifies your website in the createToken call below
Stripe.setPublishableKey('pk_ucMA8KFJiCz0JLnk728nkTSQjzJYr');

function stripeResponseHandler(status, response) {
    if (response.error) {
	// re-enable the submit button
	$('.submit-button').removeAttr("disabled");
	// show the errors on the form
	$(".payment-error-title").show();
	$(".payment-error").html("<li>" + response.error.message + "</li></br>");
    } else {
	var form$ = $("#payment-form");
	// token contains id, last4, and card type
	var token = response['id'];
	// insert the token into the form so it gets submitted to the server
	form$.append("<input type='hidden' name='stripeToken' value='" + token + "' />");
	// and submit
	form$.get(0).submit();
    }
}

$(document).ready(function() {
	$("#payment-form").submit(function(event) {
		// disable the submit button to prevent repeated clicks
		$('.submit-button').attr("disabled", "disabled");
		// createToken returns immediately - the supplied callback submits the form if there are no errors
		Stripe.createToken({
                        number: $('.card-number').val(),
			    cvc: $('.card-cvc').val(),
			    exp_month: $('.card-expiry-month').val(),
			    exp_year: $('.card-expiry-year').val(),
			    name: $('.card-name').val()
			    }, stripeResponseHandler);
		return false; // submit from callback
	    });
    });

if (window.location.protocol === 'file:') {
    alert("stripe.js does not work when included in pages served over file:// URLs. Try serving this page over a webserver. Contact s\
upport@stripe.com if you need assistance.");
}
