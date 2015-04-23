'use strict';




var dropCookie = true;                      
var cookieDuration = 14;                    
var cookieName = 'cookiebanner-accepted';
var cookieValue = 'on';     

function setCookieAlert() {
	if (document.cookie != 'cookiebanner-accepted=true'){

		var theBodyTag = document.getElementsByTagName('body')[0];
		var theCookieElement = document.createElement('div');
		theCookieElement.setAttribute('id','cookieAlert');
		theCookieElement.setAttribute('class', 'cookie-notice alert-warning alert-dismissible');
		theCookieElement.setAttribute('role', 'alert');
		var siteName = 'Johannes\' Flask Boilerplate'
		var cookieTekst = 'Denne side anvender cookies til indsamling af indstillinger og statistikker. Læs mere <strong><a class="alert-link" href="/cookies" title="' + siteName +'\'s cookieside"> om vores cookies.</a></strong>'
		theCookieElement.innerHTML = '<a type="button" onclick="removeMe();" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></a>'+cookieTekst;

		$(theBodyTag).append(theCookieElement);
	}
};
function createCookie(){
	document.cookie = 'cookiebanner-accepted=true'
}
function removeMe() {
	createCookie()
	var element = document.getElementById('cookieAlert');
	element.parentNode.removeChild(element);
};

