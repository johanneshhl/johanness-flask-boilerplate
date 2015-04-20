'use strict';





function getUser(input) {
    var msg = $.ajax({
        type: "POST",
        url: '/session/checkuser',
        data: ({ username: input }),
        dataType: "text/html", async: false
    });

    return msg.responseText;
}


$('#username').keyup(function(event) {
	
	if ($(this).closest('form').attr('id') === 'createUserForm' != true) { }
	
	else {
	

	var newResponse = getUser(this.value);

	var parentNode = $(this).parent('div');
	
	
	
		if (newResponse != 'ok'){
			var glyphicon = 'glyphicon-remove';
			var code = '(error)'
			var codeClass = 'has-error'
			var oppositeClass = 'has-success'
			$(this).closest('form').children('button').attr('disabled','');
		}
		else {
			var glyphicon = 'glyphicon-ok';
			var code = '(success)';
			var codeClass = 'has-success'
			var oppositeClass = 'has-error'
			$(this).closest('form').children('button').removeAttr('disabled');
		}
		var nodes = '<span class="glyphicon '+ glyphicon +' form-control-feedback" aria-hidden="true"></span><span id="'+ this.id +'" class="sr-only">'+ code +'</span>';
		if (parentNode.hasClass('has-feedback') != true){
			parentNode.addClass('has-feedback');
		}
		if (parentNode.hasClass(codeClass) != true){
			parentNode.addClass(codeClass);
		}
		if (parentNode.hasClass(oppositeClass) == true){
			parentNode.removeClass(oppositeClass);
		}
		$(this).nextAll().remove()
		parentNode.append(nodes);
	}
	
});






$(document).ready(function($) {

});