$(document).ready(function(){

	$("#fort").click(function(event){
		$.ajax({
			data : {
				word : $('#mySelection').val(),
				del1 : $('#delsingdr').val(),
				add1 : $('#addsingdr').val(),
				del2 : $('#delpludr').val(),
				add2 : $('#addpludr').val(),
				del3 : $('#delsingob').val(),
				add3 : $('#addsingob').val(),
				del4 : $('#delpluob').val(),
				add4 : $('#addpluob').val()
			},
		type : 'POST' ,
		url : '/process'
		})
		.done(function(data) {
			document.getElementById('1').style.display = "none";
			document.getElementById('2').style.display = "none";
			document.getElementById('3').style.display = "none";
			document.getElementById('4').style.display = "none";
			document.getElementById('correctanswer').style.display = "none";
			document.getElementById('wronganswer').style.display = "none";
			if(data.ans1=="correct")
				document.getElementById('check0').innerHTML='<img src="../static/images/right.png" style="height:25px; width:25px" alt="Right" /> ';
			else
				document.getElementById('check0').innerHTML='<img src="../static/images/wrong.png" style="height:25px; width:25px" alt="Wrong" /> ';
			if(data.ans2=="correct")
				document.getElementById('check1').innerHTML='<img src="../static/images/right.png" style="height:25px; width:25px" alt="Right" /> ';
			else
				document.getElementById('check1').innerHTML='<img src="../static/images/wrong.png" style="height:25px; width:25px" alt="Wrong" /> ';

			if(data.ans3=="correct")
				document.getElementById('check2').innerHTML='<img src="../static/images/right.png" style="height:25px; width:25px" alt="Right" /> ';
			else
				document.getElementById('check2').innerHTML='<img src="../static/images/wrong.png" style="height:25px; width:25px" alt="Wrong" /> ';

			if(data.ans4=="correct")
				document.getElementById('check3').innerHTML='<img src="../static/images/right.png" style="height:25px; width:25px" alt="Right" /> ';
			else
				document.getElementById('check3').innerHTML='<img src="../static/images/wrong.png" style="height:25px; width:25px" alt="Wrong" /> ';
			if((data.ans1=="correct") && (data.ans2=="correct") && (data.ans3=="correct") && (data.ans4=="correct"))			
				document.getElementById('correctanswer').style.display = "inline";
			else
			{
				document.getElementById('wronganswer').style.display = "inline";
				if(data.count==1)
				document.getElementById('1').style.display = "inline";
				else if(data.count==2)
				document.getElementById('2').style.display = "inline";
				else if(data.count==3)
				document.getElementById('3').style.display = "inline";
				else if(data.count==4)
				document.getElementById('4').style.display = "inline";
			}
			});
		event.preventDefault();
	});

});
