$(function(){
	//$(".content").css("display","none");
	// $(".spinner").delay(10000).hide(function () {
	// 	$(".content").fadeIn(3000);
    // });




	var firstListLink = $("#list1").find("a").first();

	firstListLink.css("background","#CCE5FF").css("border-bottom","3px solid #188FFF");

	var allListLink = $("#list1").find("a");

	$(".div-for-list1").slideDown(1000);

	allListLink.click(function(){
		var id = $(this).attr("id");

		switch(id){
			case "a1":
			listLinkClickEvent($("#a1"),$("#a2"),$("#a3"),$("#a4"),$("#a5"),$("#a6"),$("#a7"),$("#a8"));
			$(".div-for-list1").slideDown(1000);
			$(".div-for-list2").hide();
			$(".div-for-list3").hide();
			$(".div-for-list4").hide();
			$(".div-for-list5").hide();
			$(".div-for-list6").hide();
			$(".div-for-list7").hide();
			$(".div-for-list8").hide();
			break;
			case "a2":
			listLinkClickEvent($("#a2"),$("#a1"),$("#a3"),$("#a4"),$("#a5"),$("#a6"),$("#a7"),$("#a8"));
			$(".div-for-list2").slideDown(1000);
			$(".div-for-list1").hide();
			$(".div-for-list3").hide();
			$(".div-for-list4").hide();
			$(".div-for-list5").hide();
			$(".div-for-list6").hide();
			$(".div-for-list7").hide();
			$(".div-for-list8").hide();
			break;
			case "a3":
			listLinkClickEvent($("#a3"),$("#a1"),$("#a2"),$("#a4"),$("#a5"),$("#a6"),$("#a7"),$("#a8"));
			$(".div-for-list3").slideDown(1000);
			$(".div-for-list1").hide();
			$(".div-for-list2").hide();
			$(".div-for-list4").hide();
			$(".div-for-list5").hide();
			$(".div-for-list6").hide();
			$(".div-for-list7").hide();
			$(".div-for-list8").hide();
			break;
			case "a4":
			listLinkClickEvent($("#a4"),$("#a1"),$("#a2"),$("#a3"),$("#a5"),$("#a6"),$("#a7"),$("#a8"));
			$(".div-for-list4").slideDown(1000);
			$(".div-for-list1").hide();
			$(".div-for-list2").hide();
			$(".div-for-list3").hide();
			$(".div-for-list5").hide();
			$(".div-for-list6").hide();
			$(".div-for-list7").hide();
			$(".div-for-list8").hide();
			break;
			case "a5":
			listLinkClickEvent($("#a5"),$("#a1"),$("#a2"),$("#a3"),$("#a4"),$("#a6"),$("#a7"),$("#a8"));
			$(".div-for-list5").slideDown(1000);
			$(".div-for-list1").hide();
			$(".div-for-list2").hide();
			$(".div-for-list3").hide();
			$(".div-for-list4").hide();
			$(".div-for-list6").hide();
			$(".div-for-list7").hide();
			$(".div-for-list8").hide();
			break;
			case "a6":
			listLinkClickEvent($("#a6"),$("#a1"),$("#a2"),$("#a3"),$("#a4"),$("#a5"),$("#a7"),$("#a8"));
			$(".div-for-list6").slideDown(1000);
			$(".div-for-list1").hide();
			$(".div-for-list2").hide();
			$(".div-for-list3").hide();
			$(".div-for-list4").hide();
			$(".div-for-list5").hide();
			$(".div-for-list7").hide();
			$(".div-for-list8").hide();
			break;
			case "a7":
			listLinkClickEvent($("#a7"),$("#a1"),$("#a2"),$("#a3"),$("#a4"),$("#a5"),$("#a6"),$("#a8"));
			$(".div-for-list7").slideDown(1000);
			$(".div-for-list1").hide();
			$(".div-for-list2").hide();
			$(".div-for-list3").hide();
			$(".div-for-list4").hide();
			$(".div-for-list5").hide();
			$(".div-for-list6").hide();
			$(".div-for-list8").hide();
			break;
			case "a8":
			listLinkClickEvent($("#a8"),$("#a1"),$("#a2"),$("#a3"),$("#a4"),$("#a5"),$("#a6"),$("#a7"));
			$(".div-for-list8").slideDown(1000);
			$(".div-for-list1").hide();
			$(".div-for-list2").hide();
			$(".div-for-list3").hide();
			$(".div-for-list4").hide();
			$(".div-for-list5").hide();
			$(".div-for-list6").hide();
			$(".div-for-list7").hide();
			break;


		}
	});





});

function listLinkClickEvent(activeLink,link1,link2,link3,link4,link5,link6,link7){
	activeLink.css("background","#CCE5FF").
	css("border-bottom","3px solid #188FFF").
	css("color","black").
	css("padding","20px");

	link1.css("background","none").
	css("border-bottom","none").
	css("color","blue").
	css("padding","20px");

	link2.css("background","none").
	css("border-bottom","none").
	css("color","blue").
	css("padding","20px");

	link3.css("background","none").
	css("border-bottom","none").
	css("color","blue").
	css("padding","20px");

	link4.css("background","none").
	css("border-bottom","none").
	css("color","blue").
	css("padding","20px");

	link5.css("background","none").
	css("border-bottom","none").
	css("color","blue").
	css("padding","20px");

	link6.css("background","none").
	css("border-bottom","none").
	css("color","blue").
	css("padding","20px");

	link7.css("background","none").
	css("border-bottom","none").
	css("color","blue").
	css("padding","20px");
}