$(function(){
//	根据规则选择语言
	language_choice();
	
//根据选择的语言初始化界面
    language_init();
    
//  请求数据
	request( location.search.replace('?','') );
    
//  语言按钮点击
    $('#language').click(function(){
    	if( $(this).children('i').hasClass('icon-en') ){
    		$(this).children('i').removeClass('icon-en').addClass('icon-cn');
			displayLanguage('EN');
    	}else{
    		$(this).children('i').removeClass('icon-cn').addClass('icon-en');
			displayLanguage('中');
    	}
    });
    
//  介绍按钮点击
    $('#introduction-icon').click(function(){
    	$(this).toggleClass('clicked').parent().toggleClass('clicked');
//  	zfx.showFullScreenMask();
//  	$('#introduction-dialog').slideToggle(700);
    });
    
//  全屏按钮点击
    $('#full-screen').click(function(){
    	zfx.toggleFullScreen();
    	$(this).children('i').toggleClass('icon-fullScreen').toggleClass('icon-exitFullScreen');
    });
    
//  点击蒙版关闭蒙版
    $(document).on('click',zfx.maskId,function(){
    	zfx.hideFullScreenMask();
    	$('#introduction-dialog').slideUp(700);
    	$("#share-content").hide();
    });
    
//  音乐切换
    $('#music').click(function(){
    	$(this).toggleClass('clicked');
    	var audio=$('#mp3')[0];
    	if ( audio.paused ) {
	 		audio.play();
	 	} else{
	 		audio.pause();
	 	};
    });
	
//	分享二维码
	$('#share-content-qrcode').qrcode({
		width: 256,
		height: 256,
		text: location.href.replace('http://www','http://m')
	});
	
//	分享点击
	$('#share').on('click',function(){
		$("#share-content").toggle();
		zfx.showFullScreenMask();
	});
	
//	分享关闭按钮
	$('#share-content-close').on('click',function(){
		$('#share-content').hide();
		zfx.hideFullScreenMask();
	});

});

//定义全局变量
var data_introduction=''
var introduction_cn='';
var introduction_en='';
var title_cn='';
var title_en='';
var str='';

//请求数据
function request(request){
//function request(key,request){
//	var request_json={ key:request };
    $.ajax({
	    url:'http://www.beejeen.com/tour?type=' + request,
	    type:'get', 
	    async:true,    
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
	        if(!!data.link){
				window.location.href=data.link;
			 }else{
			 	analysis_data(data);
			 }
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

//根据规则选择语言
function language_choice(){
	if ( localStorage.getItem('beejeen-language') ) {
		language=localStorage.getItem('beejeen-language')
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
}

//语言切换
function displayLanguage(language){
	if(language=='EN'){
		localStorage.setItem('beejeen-language','en');
		$('#introduction-detail').html(introduction_en);
		document.title=title_en;
	}else{
		localStorage.setItem('beejeen-language','cn');
		$('#introduction-detail').html(introduction_cn);
		document.title=title_cn;
	}
}

//根据选择的语言初始化界面
function language_init(){
	if(language=='en'){
		$('#language').children('i').removeClass('icon-en').addClass('icon-cn');
		$('#introduction-detail').html(introduction_en);
	}else{
		$('#language').children('i').removeClass('icon-cn').addClass('icon-en');
		$('#introduction-detail').html(introduction_cn);
	}
}

//分析数据
function analysis_data(data){
	$('#iframe').attr('src',data.iframe_link);
	$('#like-text').text(data.like);
	$('#mp3').attr('src',data.music);
	data_introduction=data.introduction;
	title_cn=data_introduction.cn.name;
	title_en=data_introduction.en.name;
	like();
	document.title=eval( 'title_'+language);
	introduction_cn=join_data( data_introduction.cn , data.like );
	introduction_en=join_data( data_introduction.en , data.like );
	$('#introduction-detail').html( eval( 'introduction_'+language ) );
}

//介绍弹窗
function join_data(data,like){
	
	str='';
	str+='<div class="top">';
	str+='<h1 class="title">'+data.name+'</h1>';
	str+='<p class="likes-num">'+like+'</p><div class="likes"></div>';
	str+='<p class="views-num">'+data.view+'</p><div class="views"></div>';
	str+='<p class="address">'+data.address+'</p>';	
	str+='</div><div class="middle">';
	for(var i=0;i<data.middle.length;i++){
		str+='<div><div class="'+data.middle[i].icon+'"></div><p>'+data.middle[i].text+'</p></div>';
	}
	str+='</div>';
	str+='<div class="bottom">';
	for(var i=0;i<data.content.length;i++){
		str+='<h2>'+data.content[i].title+'</h2><h3>'+data.content[i].text+'</h3>';
	}
	for(var i=0;i<data.bottom.length;i++){
		str+='<p>'+data.bottom[i]+'</p>';
	}
	str+='</div>';
	
	return str;	
}

//点赞
function like(){
	if( localStorage.getItem( title_en ) ){
    	$('#like').find('i').removeClass('icon-like-click').addClass('icon-like-clicked');
    }else{
		
		$('#like').one('click',function(){
			$('#like').find('i').removeClass('icon-like-click').addClass('icon-like-clicked');
	    	
			$.post("http://www.beejeen.com/like",{
				key:title_en,
				type: location.search.replace('?','').split('&')[0]
			},function(data,status){
	    		console.log("数据：" + data + "\n状态：" + status);
	    		if( status == 'success' ){
	    			localStorage.setItem(title_en,title_en);
	    		}
	  		});
	    });
   }
}

//全屏、蒙版 封装模块
(function(){
	var zfx={
		isFullScreen : false,
		
		toggleFullScreen : function(){
			this.isFullScreen ? this.exitFullScreen() : this.requestFullScreen();
		},
		
		requestFullScreen : function(){
		    var docElm = document.documentElement;
		    	//W3C
		    if (docElm.requestFullscreen) {
		        docElm.requestFullscreen();
		    }
		        //FireFox
		    else if (docElm.mozRequestFullScreen) {
		        docElm.mozRequestFullScreen();
		    }
		        //Chrome等
		    else if (docElm.webkitRequestFullScreen) {
		        docElm.webkitRequestFullScreen();
		    }
		        //IE11
		    else if (elem.msRequestFullscreen) {
		        elem.msRequestFullscreen();
		    }
		    
		    this.isFullScreen=true;
		},
		
		exitFullScreen : function(){
		    if (document.exitFullscreen) {  
		    	document.exitFullscreen();  
			}  
			else if (document.mozCancelFullScreen) {  
			    document.mozCancelFullScreen();  
			}  
			else if (document.webkitCancelFullScreen) {  
			    document.webkitCancelFullScreen();  
			}
			else if (document.msExitFullscreen) {
			      document.msExitFullscreen();
			}
			
			this.isFullScreen=false;
		},
		
		//FullScreenMask
		hasFullScreenMask:false,
		maskId:'#full-screen-mask',
		
		showFullScreenMask:function(){
			var str='<div id="full-screen-mask" style="position:absolute;top:0;left:0;width: 100%;height: 100%;background: rgba(0,0,0,0.4);z-index: 1000;"></div>'
			$('body').append(str);
			this.hasFullScreenMask=true;
		},
		
		hideFullScreenMask:function(){
			$('#full-screen-mask').remove();
			this.hasFullScreenMask=false;
		},
		
		toggleFullScreenMask:function(){
			this.hasFullScreenMask ? this.hideFullScreenMask() : this.showFullScreenMask();
			
		}
	};
	
	//export api
	window.zfx=zfx;
})();

