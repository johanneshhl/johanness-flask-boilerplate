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


function validatePassword(string) {
	if (string.length <= 6) {
		return false
	}else {
		return true
	}
}

function validateUser(string) {
	var newResponse = getUser(string);

	if (newResponse != 'ok'){
		return false
	}else {
		return true
	}
}


function validateForm(formElement, functionVar) {
		
		
		var parentNode = formElement.parent('div');
		
		if (functionVar != true) {
			var glyphicon = 'glyphicon-remove';
			var code = '(error)';
			var codeClass = 'has-error';
			var oppositeClass = 'has-success';
			formElement.closest('form').children('button').attr('disabled','');
		}else {
			var glyphicon = 'glyphicon-ok';
			var code = '(success)';
			var codeClass = 'has-success';
			var oppositeClass = 'has-error';
			formElement.closest('form').children('button').removeAttr('disabled');
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
		formElement.nextAll().remove()
		parentNode.append(nodes);

};


$("#createUserForm input[type*='password']").keyup(function(event) {

	validateForm($(this), validatePassword(this.value));


	
});


$("#createUserForm #username").keyup(function(event) {

	validateForm($(this), validateUser(this.value));

});






$(document).ready(function($) {

});