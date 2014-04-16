$(document).ready(function(){
	$('div').click(function(){
		$(this)
			.animate({top: "0",left: "0",width: "100%",height: "100%"}, 1500)
			.animate({top: "40%",left: "40%",width: "20%",height: "20%"}, 1500);
	});
});