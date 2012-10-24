console.log("Hello");

$(function(ready){
	$("input[name='program']").change(function() {
		switch($("input[name='program']:checked").val())
		    {
		    case 'both':
			console.log("both selected");
			$('#hitting').show();
			$('#defense').show();
			$("input[name='price']").val(249);
			$('#price_field').html("Total: $249.00");
			break;
		    case 'def':
			$('#hitting').hide();
			$('#defense').show();
			$("input[name='price']").val(189);
			$('#price_field').html("Total: $189.00");
			console.log("def selected");
			break;
		    case 'hit':
			$('#hitting').show();
			$('#defense').hide();
			$("input[name='price']").val(189);
			$('#price_field').html("Total: $189.00");
			console.log("hit selected");
			break;
		    }
	    });
});