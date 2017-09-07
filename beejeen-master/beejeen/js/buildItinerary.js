var html='';
var data_response='';

$(function(){
	
	$('main>.first>button').on('click',function(){
		$('main>.first').hide().siblings().show();
	});
	
	$('main>.second>.text>div').on('click',function(){
		$(this).addClass('current')
		.siblings('div').removeClass('current');
		$('main>.second>.text>section').removeClass('current').eq( $(this).index() ).addClass('current');
	});
	
	$(".datePicker").flatpickr({
		mode: "range",
		minDate: "today",
		dateFormat: "Y/m/d",
		locale:"zh"
	});
	
	$('main>.first>div>div').on('click',function(){
		$('#imgUpload').click();
	});
	
	$('#imgUpload').on('change', function(){
		var file = this.files[0];
		var URL = window.URL || window.webkitURL;
		var imgURL = URL.createObjectURL(file);
		$('main>.first>div>div>img').attr('src',imgURL);
		var fileName = $("#imgUpload").val();
        if( !checkFile( fileName ) ){
            alert("您上传的不是图片");
            $("#j_checkBox").val(null);
            return;
        }
        
	});  
	
	$("#submit").on('click',function () {
		var data = new FormData();
        data.append("title", "行程标题");
        data.append("author", 'zfx');
        data.append("data", $('.datePicker')[0].value);
        data.append("backgroundImage", $('#imgUpload')[0].files[0]);
        
        $.ajax({
            type: "POST",
            enctype: 'multipart/form-data',
            url: "http://www.beejeen.com/travel",
            data: data,
            processData: false,
            contentType: false,
            cache: false,
            timeout: 5000,
            success: function(data){
                console.log(data);
            },
            error: function(e){
                alert("无法连接服务器");
            }
        });
   });
	
});

function checkFile(name){
    if(name.match("png") ||
        name.match("jpg") ||
        name.match("JPG") ||
        name.match("PNG") ||
        name.match("jpeg") ||
        name.match("JPEG")){
        return true;
    }
    return false;
}