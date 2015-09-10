$(document).ready(function(){

	$.fn.api.settings.api = {
		'add to changelog': '/user/add-to-changelog/{commit}'
	};
	
	$('.add-to-changelog').api({
		action : 'add to changelog',
	})
});
