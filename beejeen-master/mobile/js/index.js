var language = 'cn';

$(function(){

	language_choice();
	
	$('.input-search').on('click',function(){
		request( encodeURIComponent( $(this).siblings('.input-text').val() ) );
	});
	
	$('.input-text').on('search',function(){ 
		request( encodeURIComponent( $(this).val() ) );
    });
    
    $('.language').click(function(){
    	if( $(this).text()==('EN') ){
			displayLanguage('EN');
    	}else{
			displayLanguage('中');
    	}
    });
});


//请求函数
function request(request){
	// var request_json={'key':request};
    $.ajax({
	    url:'http://m.beejeen.com/index?key=' + request,
	    //type:'post', //GET
	    type:'get', //post
	    async:true,    //或false,是否异步
	//    data:JSON.stringify(request_json),
	    timeout:5000,    //超时时间
	    dataType:'json',    //返回的数据格式：json/xml/html/script/jsonp/text
	    // jsonp: "callback",
	    beforeSend:function(xhr){
	        console.log(xhr)
	        console.log('发送前')
	    },
	    success:function(data,textStatus,jqXHR){
	        console.log('成功')
	        console.log(data)
	        console.log(textStatus)
	        console.log(jqXHR)
	        location.href=data.link.replace('.html','-'+localStorage.getItem('beejeen-language')+'.html');
	    },
	    error:function(xhr,textStatus){
	        console.log('错误')
	        console.log(xhr)
	        console.log(textStatus)
	    },
	    complete:function(){
	        console.log('结束')
	    }
  	});
}

function displayLanguage(language){
	if(language=='EN'){
		localStorage.setItem('beejeen-language','en');
		$('#main_cn').hide();
		$('#main_en').show();
	}else{
		localStorage.setItem('beejeen-language','cn');
		$('#main_en').hide();
		$('#main_cn').show();
	}
}

//语言分析
function language_choice(){
	
	if ( localStorage.getItem('beejeen-language') ) {
		language=localStorage.getItem('beejeen-language');
	} else{
		var type=navigator.appName;
		if (type=="Netscape"){
			var lang = navigator.language;
		}else{
			var lang = navigator.userLanguage;
		}
		if ( lang.substr(0,2) != "zh"){
			language='en';
			localStorage.setItem('beejeen-language','en');
		}else{
			language='cn';
			localStorage.setItem('beejeen-language','cn');
		}
	}

	init();
	
}

function init(){
	if(language=='en'){
		$('#main_en').show();
	}else{
		$('#main_cn').show();
	}
}
