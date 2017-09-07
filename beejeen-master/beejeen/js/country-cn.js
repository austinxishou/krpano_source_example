var html='';
var data_response='';
	
$(function(){

	request( encodeURIComponent( location.search.replace('?','') ) );
	
	$('body').on('click','#input-search',function(){
		search( encodeURIComponent( $('#input-text').val() ) );
	});
	
	$('body').on('keypress','#input-text',function(e){
        if(e.keyCode == 13){  
			search( encodeURIComponent( $('#input-text').val() ) );
        }
     });
     
    $('body').on('click','#language',function(){
    	localStorage.setItem('beejeen-language','en');
    	location.href=location.href.replace('country-cn.html','country-en.html');
    });

});

function request(request){
    $.ajax({
	    url:'http://www.beejeen.com/country?key=' + request,
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
	        data_response=data;
			if(!!data.link){
				location.href=data.link.replace('.html','-cn.html');
			}else{
				document.title = data.country.name ;
			 	apppend_data(data,'body');
			 	add_event();
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

function apppend_data(data,position){
	html=template('body_tpl', data);
	$(position).html(html);
}

function add_event(){
	
	$('.destination').on('click',function(){
    	$('#navigation').show();
    	zfx.showFullScreenMask();
//  	$('html').addClass('fixed');
    	$('#navigation>ul.nav-item>li').eq(0).addClass('current').siblings().removeClass('current');
    	$('#navigation>ul.nav-bar>li').eq(0).addClass('current').siblings().removeClass('current');
    });
    
    $('#navigation>ul.nav-bar>li').on('click',function(){
    	$(this).addClass('current').siblings().removeClass('current');
    	$('#navigation>ul.nav-item>li').eq( $(this).index() ).addClass('current')
    	.siblings().removeClass('current');
    });
    
    $('.nav-close').on('click',function(){
    	$('#navigation').hide();
    	zfx.hideFullScreenMask();
//  	$('html').removeClass('fixed');
    });
    
    $('#navigation span').on('click',function(){
    	search( encodeURIComponent( $(this).text() ) );
    });
    
    $('#navigation>input').on('click',function(){
    	search( encodeURIComponent( $(this).val() ) );
    });
    
    $('#navigation>input').on('keypress',function(e){
        if(e.keyCode == 13){  
			search( encodeURIComponent( $(this).val() ) );
        }
     });
    
}

//全屏、蒙版 封装模块
(function(){
	var zfx={

		//FullScreenMask
		hasFullScreenMask:false,
		maskId:'#full-screen-mask',
		
		showFullScreenMask:function(){
			var str='<div id="full-screen-mask" style="position:fixed;top:0;left:0;width: 100%;height: 100%;background: rgba(0,0,0,0.4);z-index: 1000;"></div>'
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

