$(document).ready(function (){
	$(document).on("scroll", function () {
		s_top = $("body").scrollTop();
		yes = $("#main").offset().top;
		if (s_top > yes) {
			$("#scroll").fadeIn(400);
		} else {
			$("#scroll").fadeOut(400);
		}
	});
	$("#scroll").click( function() {
		$("body, html").animate({
			scrollTop: 0
		}, 500);
		return false;
	});
});