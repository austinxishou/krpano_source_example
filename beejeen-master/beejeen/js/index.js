var language='cn';

$(function(){
	
	language_choice();
	
	$('.href-box>a').attr('href','html/look-'+language+'.html');
	
	$('#input-search').click(function(){
		request( encodeURIComponent( $('#input-text').val() ) );
	});
	
	$('#input-text').on('keypress',function(e){ 
        if(e.keyCode == 13){  
        	console.log($(this).val());
			request( encodeURIComponent( $('#input-text').val() ) );
        }
     });
    
    $('.language').click(function(){
    	if( $(this).text()==('ENGLISH') ){
    		$(this).text('中文');
			displayLanguage('EN');
    	}else{
    		$(this).text('ENGLISH');
			displayLanguage('中');
    	}
    });
    
    $('.destination').on('click',function(){
    	$('#navigation').show();
    });
    
    $('#navigation span').on('click',function(){
    	request( encodeURIComponent( $(this).text() ) );
    });
    
    $('#navigation>div>div>input').on('click',function(){
    	request( encodeURIComponent( $(this).val() ) );
    });
    
});


//请求函数
function request(request){
//	var request_json={'key':request};
    $.ajax({
	    url:'http://www.beejeen.com/index?key=' + request,
	    type:'get', 
	    async:true, 
//	    data:JSON.stringify(request_json),
	    timeout:5000,
	    dataType:'json',
	    beforeSend:function(xhr){
	        console.log(xhr)
	        console.log('发送前')
	    },
	    success:function(data,textStatus,jqXHR){
	        console.log('成功')
	        console.log(data)
	        console.log(textStatus)
	        console.log(jqXHR)
	        window.location.href=data.link.replace('.html','-'+localStorage.getItem('beejeen-language')+'.html');
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
		$('#input-search').val('Beejeen Search');
		$('#input-text').attr('placeholder','country／city, Currently supports search for Croatia, Bosnia and Herzegovina, Thailand, Bali, Sri Lanka, South Korea, Laos etc');
		$('.href-box>a').text('Walk Around');
		$('.href-box>a').attr('href','html/look-en.html?0content');
	}else{
		localStorage.setItem('beejeen-language','cn');
		$('#input-search').val('百见一下');
		$('#input-text').attr('placeholder','国家／城市，目前支持搜索：斯里兰卡、泰国、巴厘岛、克罗地亚、波黑、韩国、老挝等');
		$('.href-box>a').text('逛一逛');
		$('.href-box>a').attr('href','html/look-cn.html?0content');
	}
}

//语言分析
function language_choice(){
	if ( localStorage.getItem('beejeen-language') ) {
		language=localStorage.getItem('beejeen-language')
	} else{
		var lang = navigator.language||navigator.userLanguage;
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
		$('#language').text('中文');
		$('#input-search').val('Beejeen Search');
		$('#input-text').attr('placeholder','country／city, Currently supports search for Croatia, Bosnia and Herzegovina, Thailand, Bali, Sri Lanka, South Korea, Laos etc');
		$('.href-box>a').text('Walk Around');
	}else{
		$('#language').text('ENGLISH');
		$('#input-search').val('百见一下');
		$('#input-text').attr('placeholder','国家／城市，目前支持搜索：斯里兰卡、泰国、巴厘岛、克罗地亚、波黑、韩国、老挝等');
		$('.href-box>a').text('逛一逛');
	}
}
